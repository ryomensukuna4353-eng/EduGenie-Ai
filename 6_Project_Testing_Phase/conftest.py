"""Lets the tests in this folder import the app code from Phase 5."""
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent / "5_Project_Development_Phase"
sys.path.insert(0, str(APP_DIR))
