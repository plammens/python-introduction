import importlib.util
import os
import unittest
from io import StringIO
from unittest.mock import patch

TESTUTILS_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../../testutils.py'))
spec = importlib.util.spec_from_file_location("testutils", TESTUTILS_PATH)
testutils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(testutils)

TASK_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../task.py'))


class TestCase(unittest.TestCase):
    def _test_name(self, place: str, valid: bool):
        with patch('builtins.input', new=testutils.MockInput(place)), \
             patch('sys.stdout', new_callable=StringIO) as stdout:
            testutils.load_module_from_path(TASK_PATH)
            self.assertEqual("Invalid city name" if not valid else "", stdout.getvalue().strip())

    def test_valid_city(self):
        for city in ["London", "Barcelona", "Birmingham"]:
            self._test_name(city, True)

    def test_invalid_city(self):
        for name in ["zzzz", "cacac"]:
            self._test_name(name, False)
