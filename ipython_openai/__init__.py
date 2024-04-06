__version__ = '0.0.1'

from .gpt import GPT


def load_ipython_extension(ipython):
    ipython.register_magics(GPT)
