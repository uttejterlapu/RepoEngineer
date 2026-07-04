# from google import genai
# from openai import OpenAI
# from app.config.settings import settings

from abc import ABC, abstractmethod
from typing import Type
from pydantic import BaseModel

class LLMClient(ABC):
    @abstractmethod
    def generate(
        self,
        system_prompt : str,
        user_prompt : str,
        response_model : Type[BaseModel],
    ):
        pass
    
    # def __init__(self):
    #     self.googleClient = genai.Client(api_key=settings.GOOGLE_VERTEX_API)
    #     self.gitClient = OpenAI(
    #         base_url = settings.ENDPOINT,
    #         api_key = settings.GITAI_API_KEY,
    #     )
    
    # def askVertexAI(self, question:str):
    #     response = self.client.models.generate_content(
    #         model='gemini-2.5-flash',
    #         contents=question,
    #     )
    #     return response.text
    
    # def askGitAI(self, question:str):
    #     response = self.gitClient.chat.completions.create(
    #         model=settings.MODEL_NAME,
    #         messages=[                    
    #             {"role": "system", "content": "SYSTEM_PROMPT"},
    #             {"role": "user", "content": question}
    #         ],
    #         temperature=settings.TEMPERATURE,
    #         max_tokens=settings.MAX_OUTPUT_TOKENS,
    #     )
        
    #     return response.choices[0].message.content