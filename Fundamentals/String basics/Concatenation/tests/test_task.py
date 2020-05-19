import importlib.util
import os
import re
import unittest
from io import StringIO
from unittest.mock import patch

from ..task import age, name


TASK_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../task.py'))
spec = importlib.util.spec_from_file_location("task", TASK_PATH)
task = importlib.util.module_from_spec(spec)


class TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_output(self, mock_output):
        spec.loader.exec_module(task)
        stdout = mock_output.getvalue()
        self.assertEqual(f"My name is {name} and I'm {age} years old\n", stdout,
                         "Output is not in requested format")

    def test_concat_used(self):
        with open(TASK_PATH) as file:
            lines = file.readlines()

        for line in lines:
            if match := re.match(r'^print\((.*)\)$', line):
                self.assertRegex(match.group(1), r'^(.*\s*\+\s*).*$',
                                 "String concatenation not used")
                break
        else:
            self.fail("No print call found")
