import re
import unittest
import os


TASK_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../task.py'))

with open(TASK_PATH) as file:
    lines = file.readlines()


class TestCase(unittest.TestCase):
    def _get_boolean_function(self, name):
        line = next(line for line in lines if line.startswith('%s'%name))
        match = re.match(r'%s = (?P<expr>.*)'%name, line)
        if not match: self.fail("%s not found"%name)
        expr = match.group('expr')

        def func(**globals_):
            return eval(expr, globals_)

        return func

    def test_boolean1(self):
        func = self._get_boolean_function('boolean1')

        for obj in ([], "xaxa", [1, 2, 3], 'x'):
            self.assertTrue(func(obj=obj),
                            f"Incorrect expression for boolean1: returned False for {obj=}")
        for obj in ((), "ax", ('x',)):
            self.assertFalse(func(obj=obj),
                             f"Incorrect expression for boolean1: returned True for {obj=}")

    def test_boolean2(self):
        func = self._get_boolean_function('boolean2')

        for num in (0., 1., 0.5, 0, 1, 10, 100):
            self.assertTrue(func(num=num),
                            f"Incorrect expression for boolean2: returned False for {num=}")
        for num in (75., 2., 100., -1., -1, 101):
            self.assertFalse(func(num=num),
                             f"Incorrect expression for boolean2: returned True for {num=}")

    def test_boolean3(self):
        func = self._get_boolean_function('boolean3')
        class CustomList(list): pass

        for obj in ((), '', None, {}):
            self.assertTrue(func(obj=obj),
                            f"Incorrect expression for boolean3: returned False for {obj=}")
        for obj in ([], CustomList()):
            self.assertFalse(func(obj=obj),
                             f"Incorrect expression for boolean3: returned True for {obj=}")

    def test_boolean4(self):
        func = self._get_boolean_function('boolean4')

        for num in (0., 1., 0.5, 0, 1, 10, 100):
            self.assertTrue(func(num=num),
                            f"Incorrect expression for boolean4: returned False for {num=}")
        for num in (float('inf'),):
            self.assertFalse(func(num=num),
                             f"Incorrect expression for boolean4: returned True for {num=}")
