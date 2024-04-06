# IPython + GPT-4

A quick implementation of a random idea: what if `ipython` had a magic function that sent the current session to
gpt-4 along with a prompt, and automatically evaluated the result in the current session?

## Installation

```
pip install ipython_openai
```

Then, you can either load the extension during an ipython session with `%load_ext ipython_openai` or add the following
to your ipython config.

```
c.InteractiveShellApp.extensions = ['ipython_openai']
```

## Configuration

Your OpenAI API key should be available in the `OPENAI_API_KEY` env var. You can configure the model used by adding an
entry to your ipython config: `c.GPT.model_name = 'gpt-4-turbo-preview'`.

## Usage

This extension adds two new "magic" functions

## `gen`

```
In [1]: gen a 5 line greeter function with randomness
import random
def greet():
    names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]
    greeting = ["Hello", "Hi", "Hey", "Greetings", "What's up"]
    print(f"{random.choice(greeting)}, {random.choice(names)}!")

Run it? (y/n) y

In [2]: greet()
Hello, Bob!
```

## `ask`

```
In [3]: ask what happened
When the `greet()` function was called, the following occurred:
1. The function selected a random name from the list `names`, which contains five different names: "Alice", "Bob", "Charlie", "Diana", and "Edward".
2. It also selected a random greeting from the list `greeting`, which includes five different greetings: "Hello", "Hi", "Hey", "Greetings", and "What's up".
3. It combined the selected greeting and name with a formatted string to create a message.
4. Finally, the function printed this message to the console.
Since the selections are random, the exact output can vary with each call to `greet()`, displaying a greeting and a name randomly chosen from the lists provided.
```
