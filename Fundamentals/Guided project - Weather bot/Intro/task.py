# ----- Don't edit this part -----
import importlib.util
import os

HIDDEN_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../hidden.py'))
spec = importlib.util.spec_from_file_location("hidden", HIDDEN_PATH)
hidden = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hidden)

# ----- Your solution goes here -----
