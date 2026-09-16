from openai import OpenAI

from app.core.config import (
    AZURE_OPEN_AI_ENDPOINT,
    AZURE_OPEN_AI_API_KEY,
    AZURE_OPENAI_MODEL,
)

client = OpenAI(               #creates connection
    api_key=AZURE_OPEN_AI_API_KEY,
    base_url=AZURE_OPEN_AI_ENDPOINT.rstrip("/")+"/openai/v1",
)

def ask_llm(            #client can communicate with Azure OpenAI.
    question_type,
    patient_data,
    transcript_data
):

    prompt = f"""
You are a clinical documentation and medical decision support assistant.

Your responsibility is to analyze the provided patient record and encounter transcript and complete the requested task accurately.

Important Instructions:

- Use only the information contained in the patient record and transcript.
- Do not invent symptoms, diagnoses, medications, laboratory results, procedures, or treatment plans.
- If required information is unavailable, state "Not Documented".
- Maintain professional clinical language.
- Prioritize accuracy over completeness.
- Avoid repeating information unnecessarily.
- Use the transcript as the primary source for today's encounter details.
- Use the patient record as supporting clinical history and background information.
PATIENT RECORD
--------------
{patient_data}

ENCOUNTER TRANSCRIPT
--------------------
{transcript_data}

TASK
----
{question_type}

Generate the requested output only.
"""

    # print("Endpoint:", AZURE_OPEN_AI_ENDPOINT)
    # print("Model:", AZURE_OPENAI_MODEL)
    # print("API Version:", AZURE_OPEN_AI_API_KEY_VERSION)

    response = client.chat.completions.create(
        model=AZURE_OPENAI_MODEL,
        messages=[
            {
                "role": "system",
                "content": """
                   You are an experienced clinical documentation specialist.

                   Use only documented information.
                   Never hallucinate.
                   Maintain professional medical language.
                   If information is missing, state Not Documented.
                """
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=800
    )

    return response.choices[0].message.content