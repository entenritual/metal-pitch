# metal-pitch

Converts a guitar audio stem into MIDI and MusicXML using Spotify's [Basic Pitch](https://github.com/spotify/basic-pitch) model for transcription and [music21](https://web.mit.edu/music21/) for score export. Audio separation is handled by [Demucs](https://github.com/facebookresearch/demucs) (htdemucs).

## How it works

Each stage is a separate script:

1. **`separate.py`** — Demucs splits a full mix into stems (vocals, bass, drums, guitar, etc.)
2. **`transcribe.py`** — Basic Pitch transcribes the guitar stem to MIDI using the ICASSP 2022 model
3. **`export.py`** — music21 converts the MIDI to a MusicXML score

## Project structure

```
metal-pitch/
├── separated/
│   └── htdemucs/
│       └── input/
│           └── guitar.wav      # Guitar stem from Demucs
├── output.mid                  # Generated MIDI
├── output.xml                  # Generated MusicXML score
├── separate.py                 # Step 1 — stem separation
├── transcribe.py               # Step 2 — MIDI transcription
├── export.py                   # Step 3 — MusicXML export
└── pyproject.toml
```

## Setup

### 1. Install uv

**Linux / macOS**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Then restart your shell or run `source $HOME/.local/bin/env`.

**Windows (PowerShell)**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Then restart your terminal — uv will be on your PATH automatically.

### 2. Clone the repo

```bash
git clone https://github.com/jtamas0705/metal-pitch.git
cd metal-pitch
```

### 3. Create the virtual environment

**Linux / macOS**
```bash
uv venv --python 3.11
source .venv/bin/activate
```

**Windows**
```powershell
uv venv --python 3.11
.venv\Scripts\activate
```

> Python 3.11 is recommended. Any version between 3.10 and 3.12 will work.

### 4. Install dependencies

```bash
uv pip install -r pyproject.toml
```

Or if you want uv to resolve and lock everything from `pyproject.toml`:

```bash
uv sync
```

> `uv sync` is preferred — it installs exactly the versions locked in `uv.lock`, keeping your environment reproducible across machines.

### 5. Verify the install

```bash
uv run python -c "import basic_pitch; import demucs; import music21; print('all good')"
```

## Usage

### Step 1 — Separate stems

```bash
uv run python separate.py
```

Runs Demucs (htdemucs) on your input file and outputs the guitar stem to `separated/htdemucs/input/guitar.wav`.

### Step 2 — Transcribe to MIDI

```bash
uv run python transcribe.py
```

Runs Basic Pitch on the guitar stem and writes `output.mid`.

### Step 3 — Export to MusicXML

```bash
uv run python export.py
```

Parses `output.mid` with music21 and writes `output.xml`.

## Output

- `output.mid` — standard MIDI, importable into any DAW (Ableton, Logic, GarageBand, etc.)
- `output.xml` — MusicXML score, openable in MuseScore, Sibelius, Finale, etc.

## Dependencies

Managed via `pyproject.toml`. Key packages:

- `basic-pitch[onnx,tf]` — audio-to-MIDI transcription
- `demucs` — source separation
- `music21` — MIDI to MusicXML conversion
- `torch` + `torchaudio` — required by Demucs
- `onnxruntime` — ONNX backend for Basic Pitch

## Notes

- Requires Python `>=3.10,<3.13`
- On Jetson / ARM, make sure your `torch` and `onnxruntime` builds match your CUDA/hardware setup
- Basic Pitch works best on monophonic or lightly polyphonic guitar parts — cleaner stem separation leads to better MIDI output
- music21 only needs a notation backend (e.g. MuseScore) if you want to render the score visually; XML export works standalone