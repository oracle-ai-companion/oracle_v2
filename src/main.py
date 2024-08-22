from src.bot import DiscordBot
from src.config import DISCORD_TOKEN

def main():
    bot = DiscordBot()
    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()