from typing import TYPE_CHECKING

from discord.ext import commands

if TYPE_CHECKING:
    from discord.ext.commands import Bot


class Example(commands.Cog):
    """Eine Beispiel-Klasse für einen Discord-Bot-Cog."""

    def __init__(self, bot: "Bot"):
        """Initialisiert die Example-Klasse.

        Args:
            bot (Bot): Die Bot-Instanz.
        """
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context) -> None:
        """Antwortet auf den Befehl 'ping' mit 'Pong!'.

        Args:
            ctx (Context): Der Kontext des Befehlsaufrufs.
        """
        await ctx.send("Pong!")


async def setup(bot: "Bot") -> None:
    """Fügt den Example-Cog dem Bot hinzu.

    Args:
        bot (Bot): Die Bot-Instanz.
    """
    await bot.add_cog(Example(bot))
