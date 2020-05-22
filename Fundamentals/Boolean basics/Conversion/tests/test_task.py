import unittest

from .. import task


class TestCase(unittest.TestCase):
    def _test_answer(self, name: str, expected):
        ans = getattr(task, name)
        self.assertEqual(expected, ans, f"Answer to {name}) is incorrect")

    def test_answers(self):
        expected = {
            'a': False,
            'b': True,
            'c': False,
            'd': "foo",
            'e': "bar",
            'f': True,
        }

        for name, exp in expected.items():
            self._test_answer(name, exp)
