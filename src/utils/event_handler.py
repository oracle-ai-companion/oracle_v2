import discord
from src.utils.message_processor import MessageProcessor
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class EventHandler:
    def __init__(self, bot):
        self.bot = bot
        self.message_processor = MessageProcessor(bot)

    async def setup(self):
        @self.bot.event
        async def on_ready():
            logger.info(f"Logged in as {self.bot.user}")
            await self.bot.change_presence(activity=discord.Game(name="Analyzing data"))

        @self.bot.event
        async def on_message(message):
            if message.author == self.bot.user:
                return

            if isinstance(message.channel, discord.DMChannel) or self.bot.user in message.mentions or message.reference and message.reference.resolved.author == self.bot.user:
                await self.message_processor.process_message(message)
            else:
                await self.bot.process_commands(message)

        @self.bot.event
        async def on_reaction_add(reaction, user):
            # Implement reaction handling logic
            pass

        # Add more event handlers as needed