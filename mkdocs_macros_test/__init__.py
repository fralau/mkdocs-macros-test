"""
Code
"""

def test_fn(x:float):
    "Test function"
    return x * 4 / 3

def say_hello(s:str):
    "Test procedure"
    return "<i>Hello %s</i>" % s

def define_env(env):
    "Declare environment for jinja2 templates for markdown"

    for fn in [test_fn, say_hello]:
        env.macro(fn)


    # you could, of course, also define a macro here:
    @env.macro
    def test_fn2(s:str):
        return "I am displaying this: %s" % s