import unittest
import os
import re

TASK_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../task.py'))


class TestCase(unittest.TestCase):
    def test_comments(self):
        with open(TASK_PATH) as file:
            lines = file.readlines()

        statements = [
            'print("Hello, world!")',
            'print(math.sqrt(2))',
            'print(datetime.datetime.now())',
        ]

        patterns = [re.compile(re.escape(stmt) + r'\s*(?P<comment>#.*)?')
                    for stmt in statements]

        for i, line in enumerate(lines):
            for pattern in patterns:
                if match := pattern.match(line):
                    self.assertIsNotNone(match.group('comment'),
                                         msg=f"missing comment in line {i + 1}")
