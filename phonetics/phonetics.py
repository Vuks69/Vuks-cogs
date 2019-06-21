from redbot.core import commands


class Phonetics(commands.Cog):
    """Description of the cog visible with [p]help MyFirstCog"""

    def __init__(self, bot):
        self.bot = bot
        self.ph = {
            'A': ('Alfa', '__AL__ FAH'),
            'B': ('Bravo', '__BRAH__ VOH'),
            'C': ('Charlie', '__CHAR__ LEE or __SHAR__ LEE'),
            'D': ('Delta', '__DELL__ TAH')
        }

    @commands.command()
    async def phonetics(self, ctx):
        """Not there yet, dumbo."""

        await ctx.send("Great success!")
