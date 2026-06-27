import ai_helper
print(ai_helper.__file__)
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(api_key=HF_TOKEN)


def generate_health_remark(glucose, haemoglobin, cholesterol):
    prompt = f"""
You are a healthcare assistant.

Patient Details:
- Glucose: {glucose} mg/dL
- Haemoglobin: {haemoglobin} g/dL
- Cholesterol: {cholesterol} mg/dL

Provide:
1. Overall health status
2. Possible health risks
3. Diet suggestions
4. Lifestyle advice

Keep the answer under 100 words.

End with:
This is not a medical diagnosis.
"""

    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=180,
            temperature=0.3,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"AI Error:\n{str(e)}"


if __name__ == "__main__":
    print(generate_health_remark(130, 13.5, 210))
    