import importlib.util
import os
import re
import unittest
from io import StringIO
from unittest.mock import patch

from ..task import num1, num2

TASK_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../task.py'))
spec = importlib.util.spec_from_file_location("task", TASK_PATH)
task = importlib.util.module_from_spec(spec)


class TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_output(self, mock_output):
        spec.loader.exec_module(task)
        stdout = mock_output.getvalue()
        self.assertEqual((float(num1) - int(num2))*3, float(stdout.strip()),
                         "Incorrect output")

    def test_conversion_used(self):
        with open(TASK_PATH) as file:
            for line in file:
                if match := re.match(r'^print\((.*)\)$', line):
                    self.assertRegex(match.group(1).strip(),
                                     r'\(float\(num1\)\s*-\s*(int|float)\(num2\)\)\s*\*\s*3',
                                     "float or int function not used")
                    return
            else:
                self.fail("No print call found")
