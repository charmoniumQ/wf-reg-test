import os
from pathlib import Path

import parsl

from wf_reg_test.util import expect_type

exec(Path(os.environ["PARSL_CONFIG"]).read_text(), globals(), locals())

@parsl.python_app
def foo(x: int) -> int:
    return x**2

print(foo(3).result())

def bar():
    @parsl.python_app
    def foo2(x: int) -> int:
        return x**2

    print(foo2(3).result())

bar()

def foo3(x: int) -> int:
    return x**2

def bar2():
    @parsl.python_app
    def foo4(x: int) -> int:
        return foo3(expect_type(int, x))

    print(foo(3).result())

bar2()
