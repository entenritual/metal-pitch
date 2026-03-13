
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
guitar_stem = CURRENT_DIR / "separated" / "htdemucs" / "input" / "guitar.wav"

model_output, midi_data, note_events = predict(guitar_stem)
midi_data.write(str(CURRENT_DIR / "output.mid"))
