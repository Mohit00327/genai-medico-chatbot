import os
import gradio as gr

from brain_of_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_elevenlabs


SYSTEM_PROMPT = """
You are an experienced medical doctor.

Analyze the uploaded medical image together with the patient's spoken complaint.

Instructions:
- Give a short medical opinion.
- Mention what you observe.
- Suggest possible causes.
- Suggest basic remedies.
- Recommend consulting a healthcare professional if necessary.
- Do NOT use markdown.
- Do NOT use bullet points.
- Keep the response under 3 sentences.
- Speak naturally like a real doctor.
"""


def process_inputs(audio_filepath, image_filepath):

    try:

        # -----------------------------
        # Speech → Text
        # -----------------------------
        speech_to_text_output = transcribe_with_groq(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
            audio_filepath=audio_filepath,
            stt_model="whisper-large-v3"
        )

        # -----------------------------
        # Vision + LLM
        # -----------------------------
        if image_filepath:

            doctor_response = analyze_image_with_query(
                query=SYSTEM_PROMPT + "\n\nPatient: " + speech_to_text_output,
                encoded_image=encode_image(image_filepath),
                model="meta-llama/llama-4-scout-17b-16e-instruct"
            )

        else:

            doctor_response = "Please upload an image for medical analysis."

        # -----------------------------
        # Text → Speech
        # -----------------------------
        audio_output_path = text_to_speech_with_elevenlabs(
            input_text=doctor_response,
            output_filepath="doctor_response.mp3"
        )

        return (
            speech_to_text_output,
            doctor_response,
            audio_output_path
        )

    except Exception as e:

        return (
            "Error",
            str(e),
            None
        )


iface = gr.Interface(
    fn=process_inputs,

    inputs=[

        gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="🎤 Speak your symptoms"
        ),

        gr.Image(
            type="filepath",
            label="🖼 Upload Medical Image"
        ),
    ],

    outputs=[

        gr.Textbox(
            label="Speech to Text"
        ),

        gr.Textbox(
            label="Doctor's Response",
            lines=6
        ),

        gr.Audio(
            label="Doctor Voice Response",
            type="filepath",
            autoplay=True
        ),
    ],

    title="🩺 AI Medical Assistant (Voice + Vision)",

    description="""
Upload a medical image and describe your symptoms using your voice.
The AI analyzes both the image and your speech to generate a medical response with voice output.
""",

    allow_flagging="never"
)

iface.launch(
    debug=True
)