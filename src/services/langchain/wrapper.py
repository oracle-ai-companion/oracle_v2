from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.messages import HumanMessage
from src.config import OPENAI_API_KEY

class LangChainWrapper:
    def __init__(self):
        self.chat_model = ChatOpenAI(model_name="gpt-4o-mini", api_key=OPENAI_API_KEY)
        self.embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

    def get_chat_model(self):
        return self.chat_model

    def get_embeddings(self):
        return self.embeddings

    async def process_message(self, message: HumanMessage):
        response = await self.chat_model.agenerate([[message]])
        return response.generations[0][0].text

    async def process_command(self, command_name, *args):
        command_input = f"{command_name} {' '.join(args)}"
        message = HumanMessage(content=command_input)
        return await self.process_message(message)

    async def analyze_image(self, image_url):
        # Implement image analysis logic here
        return f"Image analysis for {image_url} is not implemented yet."

    async def analyze_video(self, video_url):
        # Implement video analysis logic here
        return f"Video analysis for {video_url} is not implemented yet."