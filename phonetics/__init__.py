from .phonetics import Phonetics


def setup(bot):
    # Add the cog to the bot.
    cog = Phonetics(bot)
    bot.add_cog(cog)
