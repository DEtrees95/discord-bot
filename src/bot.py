"""Main entry point for the Discord bot."""

import os
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")


def create_bot() -> commands.Bot:
    """Create and configure the Discord bot instance.

    Returns:
        commands.Bot: Configured bot instance.
    """
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(
        command_prefix="!",
        intents=intents,
    )
    return bot


bot = create_bot()


@bot.event
async def on_ready() -> None:
    """Handle bot ready event."""
    print(f"Logged in as {bot.user}")


if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise ValueError("DISCORD_TOKEN not found in .env file")
    bot.run(token)
