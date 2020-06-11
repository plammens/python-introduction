import importlib.util
import os
import unittest
from unittest.mock import patch

TESTUTILS_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../../testutils.py'))
spec = importlib.util.spec_from_file_location("testutils", TESTUTILS_PATH)
testutils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(testutils)

TASK_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../task.py'))


class TestCase(unittest.TestCase):
    @patch('builtins.input', new_callable=testutils.MockInput)
    def test_city(self, mock_input):
        task = testutils.load_module_from_path(TASK_PATH)
        try:
            self.assertEqual(mock_input.text, task.city, "input() not used")
            self.assertEqual(mock_input.prompt_used, "Enter a city: ",
                             "Incorrect prompt for input()")
        except AttributeError:
            self.fail('Variable `city` not found')
