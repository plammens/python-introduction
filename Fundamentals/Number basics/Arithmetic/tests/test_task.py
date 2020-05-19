import importlib.util
import os
import re
import unittest

from ..task import number, remainder


TASK_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../task.py'))


class TestCase(unittest.TestCase):
    def test_values(self):
        self.assertEqual(10668, number)
        self.assertEqual(8, remainder)

    def test_expressions(self):
        with open(TASK_PATH) as file:
            for line in file:
                if m := re.match(r'^number *= *(.*)$', line):
                    self.assertRegex(m.group(1), r'^1532\*7\s*-\s*56$',
                                     "The operation should be entered as an expression without "
                                     "pre-computing")
                    break
            else:
                self.fail("No print call found")

            for line in file:
                if m := re.match(r'^remainder *= *(.*)$', line):
                    self.assertRegex(m.group(1), r'^(number|\(\s*1532\*7\s*-\s*56\s*\))\s*%\s*13$',
                                     "The remainder operation should be entered as an expression "
                                     "without pre-computing")
                    break
            else:
                self.fail("No print call found")
