from typing import Type

from openai import OpenAI
from pydantic import BaseModel

from app.config.settings import settings
from app.llm.base import LLMClient

class OpenAIClient(LLMClient):
    def __init__(self):
        self.client = OpenAI(
            base_url = settings.ENDPOINT,
            api_key = settings.GITAI_API_KEY,
        )
        self.model = settings.MODEL_NAME
        self.temperature = settings.TEMPERATURE
        self.max_output_tokens = settings.MAX_OUTPUT_TOKENS

    def generate(
        self,
        system_prompt : str,
        user_prompt : str,
        response_model : Type[BaseModel]
    ) -> BaseModel:
        response = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[                    
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format=response_model,
            temperature=self.temperature,
            max_tokens=self.max_output_tokens,
        )
        
        return response.choices[0].message.parsed
        