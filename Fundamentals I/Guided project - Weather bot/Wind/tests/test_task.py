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
    def _test_wind(self, wind: int, should_print: bool):
        patch_source = f"def get_current_values(*args): return True, 10, {wind}, 5"
        with patch('builtins.input', new=testutils.MockInput("Barcelona")), \
                testutils.SourcePatch(testutils.HIDDEN_PATH, patch_source), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            testutils.load_module_from_path(TASK_PATH)

        printed = mock_stdout.getvalue().strip() == "Very strong winds, don't go outside!"
        self.assertFalse(printed ^ should_print,
                         f"Should{'' if should_print else ' not'} print a message for {wind=}")

    def test_wind(self):
        for wind in [21, 30, 50]:
            self._test_wind(wind, True)

    def test_not_wind(self):
        for wind in [20, 15, 0]:
            self._test_wind(wind, False)
