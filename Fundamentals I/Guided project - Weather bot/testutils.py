import importlib.util
import os

HIDDEN_PATH = os.path.join(os.path.dirname(__file__), 'hidden.py')


class MockInput:
    def __init__(self, text="Barcelona"):
        self.prompt_used = None
        self.text = text

    def __call__(self, prompt):
        self.prompt_used = prompt
        return self.text


class SourcePatch:
    def __init__(self, path, patch_source):
        self.path = path
        self.patch = patch_source
        with open(path) as file:
            self.original = file.read()

    def __enter__(self):
        with open(self.path, 'a') as file:
            file.write(self.patch)

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.path, 'w') as file:
            file.write(self.original)


def load_module_from_path(path: str):
    name = os.path.basename(path).rsplit('.', maxsplit=1)[0]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
