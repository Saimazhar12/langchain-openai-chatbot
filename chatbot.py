from langchain_openai import ChatOpenAI
import os
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

class ChatBot:
    def __init__(self):
        self.model_name = "gpt-3.5-turbo"
        self.temperature = 0
        self.load_model()

    def load_model(self):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY not found. Please set it in .env file.")

        self.llm = ChatOpenAI(
            model_name=self.model_name,
            temperature=self.temperature,
            openai_api_key=api_key
        )

    def chat_bot(self, message, history):
        return self.llm.invoke(message).content


if __name__ == "__main__":
    chatbot = ChatBot()
    gr.ChatInterface(chatbot.chat_bot).launch(share=True)