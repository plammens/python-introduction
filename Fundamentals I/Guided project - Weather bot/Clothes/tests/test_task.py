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
    def _test_clothes(self, rain: bool, temp: int, clothes: str):
        patch_source = f"def get_current_values(*args): return {rain}, {temp}, None, 0"
        with patch('builtins.input', new=testutils.MockInput("Barcelona")), \
             testutils.SourcePatch(testutils.HIDDEN_PATH, patch_source), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            testutils.load_module_from_path(TASK_PATH)

        last_line = mock_stdout.getvalue().strip().split('\n')[-1]
        if clothes:
            self.assertEqual(f"Wear {clothes}!", last_line,
                             f"Failed for {rain=} {temp=} (it should print a message)")
        else:
            self.assertNotRegex(last_line, r'Wear (?!sunglasses).*!',
                                f"Should not print a message for {rain=} and {temp=}")

    def test_winter_coat(self):
        for temp in (-20, 0, 4.9):
            self._test_clothes(True, temp, "a winter coat")
        for temp in (5, 10, 12):
            self._test_clothes(False, temp, "a winter coat")

    def test_raincoat(self):
        for temp in (5, 10, 12):
            self._test_clothes(True, temp, "a raincoat")

    def test_light_clothes(self):
        for temp in (20, 25, 30):
            self._test_clothes(False, temp, "light clothes")
            self._test_clothes(True, temp, "light clothes")

    def test_nothing(self):
        for temp in (12.1, 15, 19.9):
            self._test_clothes(True, temp, "")
            self._test_clothes(False, temp, "")
