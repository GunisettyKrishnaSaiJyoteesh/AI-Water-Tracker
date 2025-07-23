import os
from langchain_community.llms import Ollama
from langchain.schema import HumanMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama2-uncensored")  # fallback to llama2-uncensored

# Initialize Ollama LLM
llm = Ollama(
    model=OLLAMA_MODEL,
    temperature=0.5
)

class WaterIntakeAgent:
    def __init__(self):
        self.history = []

    def analyze_intake(self, intake_ml):
        prompt = f"""You are a hydration assistant. The user has consumed {intake_ml} ml of water today. Provide a hydration status and suggest if they need to drink more water."""
        response = llm.invoke(prompt)  # Ollama takes plain strings
        return response

if __name__ == "__main__":
    agent = WaterIntakeAgent()
    intake_ml = 1500
    feedback = agent.analyze_intake(intake_ml)
    print(f"Hydration Status: {feedback}")
