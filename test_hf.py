from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("HF_TOKEN")

print("Token loaded:", bool(token))

client = InferenceClient(api_key=token)

models = [
    "meta-llama/Llama-3.1-8B-Instruct",
    "mistralai/Mistral-7B-Instruct-v0.3",
    "HuggingFaceTB/SmolLM3-3B",
    "Qwen/Qwen2.5-3B-Instruct",
]

for model in models:
    print(f"\nTesting {model}")

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": "Hello"
                }
            ],
            max_tokens=20
        )

        print("SUCCESS")
        print(response.choices[0].message.content)

    except Exception as e:
        print("FAILED")
        print(e)