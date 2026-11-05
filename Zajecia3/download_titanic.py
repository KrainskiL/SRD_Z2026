"""
Download the Titanic CSV used in Class 3 into the current folder.

Why this script exists:
pd.read_csv(url) may fail with SSLCertVerificationError on some student machines
(corporate proxy / incomplete CA store). This script saves a local titanic.csv
so the notebook can read from disk.

Usage (from this folder, in Anaconda Prompt / terminal):
    python download_titanic.py
"""

from __future__ import annotations

import ssl
import urllib.request
from pathlib import Path

# Same URL as in the Class 3 notebook
URL = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
OUT_PATH = Path(__file__).resolve().parent / "titanic.csv"


def download_titanic(force: bool = False) -> Path:
    """Download Titanic CSV next to this script. Skip if the file already exists."""
    if OUT_PATH.exists() and not force:
        print(f"Already present: {OUT_PATH} ({OUT_PATH.stat().st_size} bytes)")
        return OUT_PATH

    print(f"Downloading:\n  {URL}")
    # unverified context: workaround for CERTIFICATE_VERIFY_FAILED on some setups
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(URL, context=context) as response:
        OUT_PATH.write_bytes(response.read())

    print(f"Saved: {OUT_PATH} ({OUT_PATH.stat().st_size} bytes)")
    return OUT_PATH


if __name__ == "__main__":
    download_titanic()
