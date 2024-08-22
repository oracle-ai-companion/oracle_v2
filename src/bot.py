import discord
from discord.ext import commands
from src.utils.logger import setup_logger
from src.utils.command_handler import CommandHandler
from src.utils.event_handler import EventHandler
from src.services.langchain.wrapper import LangChainWrapper
from src.services.vector_store.milvus_client import MilvusClient

logger = setup_logger(__name__)

class DiscordBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents, help_command=None)

        self.langchain_wrapper = LangChainWrapper()
        self.milvus_client = MilvusClient()
        self.command_handler = CommandHandler(self)
        self.event_handler = EventHandler(self)

    async def setup_hook(self):
        await self.command_handler.setup()
        await self.event_handler.setup()

    async def on_ready(self):
        logger.info(f"Logged in as {self.user}")
        self.milvus_client.connect()

    async def close(self):
        self.milvus_client.disconnect()
        await super().close()

    def run(self, token):
        super().run(token)