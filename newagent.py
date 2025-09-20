import os
from huggingface_hub import InferenceClient

class Agent:
    def __init__(self, model="mistralai/Mistral-7B-Instruct-v0.2"):
        self.client = InferenceClient(
            provider="featherless-ai",
            api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN")
        )
        self.model = model

    def run(self, topic: str) -> str:
        prompt = f"""
        You are a helpful research assistant.
        Your task: Summarize research findings on the topic: {topic}.
        Create a concise report with bullet points and key takeaways.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message["content"]


# ✅ reusable agent
agent = Agent()
