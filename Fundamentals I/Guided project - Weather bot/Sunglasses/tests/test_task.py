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
    @patch('sys.stdout', new_callable=StringIO)
    def _test_sunglasses(self, uvi: int, should_print: bool, mock_stdout):
        patch_source = f"def get_current_values(*args): return False, None, None, {uvi}"
        with patch('builtins.input', new=testutils.MockInput("Barcelona")), \
             testutils.SourcePatch(testutils.HIDDEN_PATH, patch_source):
            testutils.load_module_from_path(TASK_PATH)

        self.assertEqual("Wear some sunglasses!" if should_print else "",
                         mock_stdout.getvalue().strip(),
                         f"Failed for UVI={uvi} (it should{'' if should_print else ' not'} print "
                         f"a message)")

    def test_sunglasses(self):
        for value in [5, 10, 12.5]:
            self._test_sunglasses(value, True)

    def test_no_sunglasses(self):
        for value in [4.9, 2, 0]:
            self._test_sunglasses(value, False)
