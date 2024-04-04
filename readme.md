# IPython + GPT-4

A quick toy implementation of a random idea: what if `ipython` had a magic function that sent the current session to
gpt-4 along with a prompt, and automatically evaluated the result in the current session?

Disclaimer: this is terribly unsafe and should not be used with any sensitive data.

```
Python 3.9.14 (main, Oct 19 2022, 22:42:39)
Type 'copyright', 'credits' or 'license' for more information
IPython 8.18.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: %load_ext ipython_gpt

In [2]: names = ["jordan", "octavia", "cyrelle"]

In [3]: gpt write a random greeter, run it with `names`
import random

def random_greeter(names):
    if names:
        name = random.choice(names)
        print(f"Hello, {name}!")
    else:
        print("Hello there!")

# Running the greeter with the provided names
names = ["jordan", "octavia", "cyrelle"]
random_greeter(names)

Hello, jordan!

In [4]: gpt make the greeting more formal
import random

def formal_greeter(names):
    greetings = ["Good day", "Greetings", "Salutations", "Hello"]
    title = "Mx."
    for name in names:
        greeting_selected = random.choice(greetings)
        print(f"{greeting_selected}, {title} {name.capitalize()}!")

formal_greeter(names)

Greetings, Mx. Jordan!
Salutations, Mx. Octavia!
Hello, Mx. Cyrelle!
```