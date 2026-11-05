# AI Video Production Pipeline

Python-based starter project for AI video automation.

## Features

- Script and scene planning
- ElevenLabs-compatible TTS integration (via environment variable)
- Subtitle generation
- FFmpeg video assembly (placeholder)
- Vertical 9:16 export presets
- Configurable output resolution

Use environment variables for API credentials. Do not commit keys.

## Installation

```bash
git clone https://github.com/demarco2016/ai-video-production-pipeline.git
cd ai-video-production-pipeline
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add ELEVENLABS_API_KEY
# Install FFmpeg separately on your system
```

## Usage

```bash
python pipeline.py
```

Extend the functions to call real TTS APIs and FFmpeg commands.

## Notes

This is a starter. Full video rendering requires FFmpeg and actual API integration.
