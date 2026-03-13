import demucs.separate
from pathlib import Path

import os
os.environ["TORCHAUDIO_USE_SOUNDFILE_LEGACY_INTERFACE"] = "1"

CURRENT_DIR = Path(__file__).parent
INPUT = CURRENT_DIR / "input.wav"

# Step 1: separate stems
demucs.separate.main(["--out", str(CURRENT_DIR / "separated"), str(INPUT)])

# Step 2: predict MIDI from the guitar stem (ends up in 'other')
guitar_stem = CURRENT_DIR / "separated" / "htdemucs" / "input" / "other.wav"