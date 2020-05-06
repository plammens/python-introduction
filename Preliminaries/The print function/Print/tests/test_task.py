import importlib.util
import os
import unittest
from io import StringIO
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("task", os.path.normpath(
    os.path.join(os.path.dirname(__file__), '../task.py')))
task = importlib.util.module_from_spec(spec)


class TestCase(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_output(self, mock_output):
        spec.loader.exec_module(task)
        self.assertEqual("This program\nprints two lines.\n", mock_output.getvalue())
