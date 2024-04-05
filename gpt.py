import openai
from IPython.core.magic import (Magics, magics_class, line_magic)
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import PygmentsTokens
from pygments.lexers.python import PythonLexer
from pygments import lex

from prompt_toolkit.shortcuts import confirm


@magics_class
class GPT(Magics):

    @line_magic
    def gpt(self, line):
        lexer = PythonLexer()

        sys_message = {
            "role": "system",
            "content": "You are a python codebot, running in an ipython session. Respond ONLY in python source code. Do not use markdown."
        }
        history = self.shell.history_manager.get_range()
        concatenated_history = '\n'.join([item[2] for item in history])
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                sys_message,
                {"role": "user", "content": concatenated_history},
                {"role": "user", "content": line},
            ],
            max_tokens=2000,
            stream=True,
        )
        full_response = ""
        current_line = ""
        for chunk in response:
            if chunk.choices:
                c = chunk.choices[0].delta.content
                if c:
                    full_response += c
                    current_line += c
                    if "\n" in current_line:
                        print_highlighted_line(current_line, lexer)
                        current_line = ""
        if current_line:
            print_highlighted_line(current_line, lexer)
        print("\n---")
        if confirm("Run it?"):
            code = trim_markdown(full_response)
            self.shell.run_cell(code)


def print_highlighted_line(line: str, lexer: PythonLexer) -> None:
    tokens = list(lex(line, lexer))
    print_formatted_text(PygmentsTokens(tokens), end="")


def trim_markdown(input: str) -> str:
    def delete_prefix(prefix, text):
        if text.startswith(prefix):
            return text[len(prefix):]
        return text

    def delete_suffix(suffix, text):
        if text.endswith(suffix):
            return text[:-len(suffix)]
        return text

    return delete_prefix("python", delete_prefix("```", delete_suffix("```", input.strip().rstrip())))
