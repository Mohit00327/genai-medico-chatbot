from dotenv import load_dotenv
load_dotenv()

import os
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.environ.get("ELEVEN_API_KEY")


# -----------------------------
# gTTS (Legacy)
# -----------------------------
def text_to_speech_with_gtts_old(input_text, output_filepath):
    try:
        audio = gTTS(
            text=input_text,
            lang="en",
            slow=False
        )
        audio.save(output_filepath)

    except Exception as e:
        print(f"gTTS Error: {e}")


# -----------------------------
# ElevenLabs (Legacy)
# -----------------------------
def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    try:
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

        audio = client.generate(
            text=input_text,
            voice="Rachel",
            output_format="mp3_22050_32",
            model="eleven_turbo_v2"
        )

        elevenlabs.save(audio, output_filepath)

    except Exception as e:
        print(f"ElevenLabs Error: {e}")


# -----------------------------
# gTTS
# -----------------------------
def text_to_speech_with_gtts(input_text, output_filepath):
    try:
        audio = gTTS(
            text=input_text,
            lang="en",
            slow=False
        )

        audio.save(output_filepath)

        return output_filepath

    except Exception as e:
        print(f"gTTS Error: {e}")
        return None


# -----------------------------
# ElevenLabs
# -----------------------------
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    try:

        if not ELEVENLABS_API_KEY:
            raise ValueError("ELEVEN_API_KEY not found.")

        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

        audio = client.generate(
            text=input_text,
            voice="21m00Tcm4TlvDq8ikWAM",
            output_format="mp3_22050_32",
            model="eleven_turbo_v2"
        )

        elevenlabs.save(audio, output_filepath)

        return output_filepath

    except Exception as e:
        print(f"ElevenLabs Error: {e}")
        return None