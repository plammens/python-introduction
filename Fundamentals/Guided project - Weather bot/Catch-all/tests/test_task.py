import importlib.util
import itertools
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
    def _test_perfect_weather(self, rain: bool, temp: float, wind: int, uvi: int,
                              should_print: bool):
        patch_source = f"def get_current_values(*args): return {rain}, {temp}, {wind}, {uvi}"
        with patch('builtins.input', new=testutils.MockInput("Barcelona")), \
             testutils.SourcePatch(testutils.HIDDEN_PATH, patch_source), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            testutils.load_module_from_path(TASK_PATH)

        printed = mock_stdout.getvalue().strip() == "Perfect weather. Enjoy the outdoors!"
        self.assertFalse(printed ^ should_print,
                         f"Should{'' if should_print else ' not'} print the message for "
                         f"{rain=}, {temp=}, {wind=}, {uvi=}")

    def test_perfect_weather(self):
        for rain, temp, wind, uvi in itertools.product([False], [12.1, 19.9], [5], [0, 4.9]):
            self._test_perfect_weather(rain, temp, wind, uvi, True)

    def test_not_perfect_weather(self):
        for rain, temp, wind, uvi in itertools.product([True], [12.1, 19.9], [5], [0, 4.9]):
            self._test_perfect_weather(rain, temp, wind, uvi, False)
        for rain, temp, wind, uvi in itertools.product([False], [6, 25], [5], [0, 4.9]):
            self._test_perfect_weather(rain, temp, wind, uvi, False)
        for rain, temp, wind, uvi in itertools.product([False], [12.1, 19.9], [25], [0, 4.9]):
            self._test_perfect_weather(rain, temp, wind, uvi, False)
        for rain, temp, wind, uvi in itertools.product([False], [12.1, 19.9], [5], [5, 6]):
            self._test_perfect_weather(rain, temp, wind, uvi, False)
