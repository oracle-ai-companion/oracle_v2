import discord
from langchain_core.messages import HumanMessage
from src.services.langchain.wrapper import LangChainWrapper
from src.utils.logger import setup_logger
import re

logger = setup_logger(__name__)

class MessageProcessor:
    def __init__(self, bot):
        self.bot = bot
        self.langchain_wrapper = LangChainWrapper()

    async def process_message(self, message):
        content = self.parse_mentions(message.content)
        attachments = message.attachments

        # Process text content
        human_message = HumanMessage(content=content)
        response = await self.langchain_wrapper.process_message(human_message)

        # Process attachments (images, videos)
        if attachments:
            for attachment in attachments:
                if attachment.content_type.startswith('image'):
                    image_analysis = await self.langchain_wrapper.analyze_image(attachment.url)
                    response += f"\n\nImage analysis: {image_analysis}"
                elif attachment.content_type.startswith('video'):
                    video_analysis = await self.langchain_wrapper.analyze_video(attachment.url)
                    response += f"\n\nVideo analysis: {video_analysis}"

        await message.channel.send(response)

    def parse_mentions(self, content):
        def replace_mention(match):
            id = match.group(2)
            if match.group(1) == '@&':
                role = discord.utils.get(self.bot.guilds[0].roles, id=int(id))
                return f"@{role.name}" if role else match.group(0)
            elif match.group(1) == '@':
                user = self.bot.get_user(int(id))
                return f"@{user.name}" if user else match.group(0)
            elif match.group(1) == '#':
                channel = self.bot.get_channel(int(id))
                return f"#{channel.name}" if channel else match.group(0)
            return match.group(0)

        return re.sub(r'<(@&?|#)!?(\d+)>', replace_mention, content)