"""
Code
"""

def test_fn(x:int):
    "Test function"
    return x * 4 / 3

def say_hello(x):
    "Test procedure"
    return "<i>Hello %s</i>" % x

def define_env(env):
    "Declare environment for jinja2 templates for markdown"

    for fn in [test_fn, say_hello]:
        env.macro(fn)