import importlib.util
import os
import re
import unittest
from io import StringIO
from unittest.mock import patch


TASK_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../task.py'))
spec = importlib.util.spec_from_file_location("task", TASK_PATH)
task = importlib.util.module_from_spec(spec)


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_output(self, mock_output: StringIO):
        spec.loader.exec_module(task)
        output = mock_output.getvalue().strip()
        self.assertEqual(r'2 + 1e-05 == 2.00001', output, "Incorrect output")

    def test_approach(self):
        with open(TASK_PATH) as file:
            for line in file:
                if match := re.match(r'^print\((.*)\)$', line):
                    self.assertRegex(match.group(1), r'((str\(.*?\)|["\'].*?["\'])\s*\+?\s*)+',
                                     "str function or string concatenation not used")
                    return
            else:
                self.fail("No print call found")
