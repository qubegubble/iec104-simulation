from pathlib import Path
import sys

# Ensure `src` is on sys.path so tests can import project modules directly.
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))
