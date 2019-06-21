from .phonetics import Phonetics


def setup(bot):
    cog = Phonetics(bot)
    bot.add_cog(cog)
