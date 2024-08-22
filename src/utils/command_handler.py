from discord.ext import commands
from src.services.langchain.wrapper import LangChainWrapper
from src.services.langchain.tools import get_tools
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class CommandHandler:
    def __init__(self, bot):
        self.bot = bot
        self.langchain_wrapper = LangChainWrapper()
        self.tools = get_tools()

    async def setup(self):
        @self.bot.command(name="search")
        async def search_command(ctx, *, query):
            try:
                response = await self.langchain_wrapper.process_command("search", query, self.tools)
                await ctx.send(response)
            except Exception as e:
                logger.error(f"Error processing search command: {str(e)}")
                await ctx.send("Sorry, I encountered an error while processing your request.")

        @self.bot.command(name="help")
        async def help_command(ctx):
            # Implement help command logic
            pass

        @self.bot.command(name="analyze")
        async def analyze_command(ctx, *, query):
            # Implement analysis command using LangChain
            pass

        # Add more commands as needed

    async def process_command(self, ctx, command_name, *args):
        command = self.bot.get_command(command_name)
        if command:
            await command(ctx, *args)
        else:
            try:
                response = await self.langchain_wrapper.process_command(command_name, *args, self.tools)
                await ctx.send(response)
            except Exception as e:
                logger.error(f"Error processing command {command_name}: {str(e)}")
                await ctx.send("Sorry, I encountered an error while processing your request.")