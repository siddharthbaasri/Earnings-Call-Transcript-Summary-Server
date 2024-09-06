import os
from groq import Groq
from prompt import system_message, user_message


class Groq_llm():
    def __init__(self):
        self.model = "llama3-8b-8192"        
        self.client = Groq(
            api_key = os.getenv('GROQ_API_KEY'),
        )
    
    def getSummary(self, context):
        response = self.client.chat.completions.create(
            messages = [
                {
                    "role": "system", 
                    "content": system_message
                },
                {
                    "role": "user", 
                    "content": user_message.format(context = context)
                },
            ],             
            model= self.model,
            stream = False,
        )
        return response.choices[0].message.content