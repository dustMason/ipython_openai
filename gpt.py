import openai
from IPython.core.magic import (Magics, magics_class, line_magic)


@magics_class
class GPT(Magics):

    @line_magic
    def gpt(self, line):
        sys_message = {
            "role": "system",
            "content": "You are a python codebot. Respond ONLY in python source code. Do not use markdown."
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
        for chunk in response:
            if chunk.choices:
                c = chunk.choices[0].delta.content
                if c:
                    full_response += c
                    print(c or "", end="")
        code = delete_prefix("python", delete_prefix("```", delete_suffix("```", full_response.strip().rstrip())))
        self.shell.run_cell(code)


def delete_prefix(prefix, text):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def delete_suffix(suffix, text):
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text
