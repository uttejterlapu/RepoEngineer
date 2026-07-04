import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_VERTEX_API = os.getenv("GOOGLE_VERTEX_API")
    GITAI_API_KEY = os.getenv("GITAI_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "openai/gpt-5")
    TEMPERATURE = float(
        os.getenv("TEMPERATURE", "0.2")
    )
    MAX_OUTPUT_TOKENS = int(
        os.getenv("MAX_OUTPUT_TOKENS",1000)
    )
    ENDPOINT = os.getenv("ENDPOINT")
    GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")

settings = Settings()