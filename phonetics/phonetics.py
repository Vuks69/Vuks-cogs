from redbot.core import commands


# noinspection PyMissingConstructor
class Phonetics(commands.Cog):
    """Description of the cog visible with [p]help MyFirstCog"""

    def __init__(self, bot):
        self.bot = bot
        self.ph = {
            'A': ('Alfa', '__AL__ FAH'),
            'B': ('Bravo', '__BRAH__ VOH'),
            'C': ('Charlie', '__CHAR__ LEE or __SHAR__ LEE'),
            'D': ('Delta', '__DELL__ TAH'),
            'E': ('Echo', '__ECK__ OH'),
            'F': ('Foxtrot', '__FOKS__ TROT'),
            'G': ('Golf', 'GOLF'),
            'H': ('Hotel', 'HO __TELL__'),
            'I': ('India', '__IN__ DEE AH'),
            'J': ('Juliett', '__JEW__ LEE ETT'),
            'K': ('Kilo', '__KEY__ LOH'),
            'L': ('Lima', '__LEE__ MAH'),
            'M': ('Mike', 'MIKE'),
            'N': ('November', 'NO __VEM__ BER'),
            'O': ('Oscar', '__OSS__ CAH'),
            'P': ('Papa', 'PAH __PAH__'),
            'Q': ('Quebec', 'KEH __BECK__'),
            'R': ('Romeo', '__ROW__ ME OH'),
            'S': ('Sierra', 'SEE __AIR__ RAH'),
            'T': ('Tango', '__TANG__ GO'),
            'U': ('Uniform', '__YOU__ NEE FORM or __OO__ NEE FORM'),
            'V': ('Victor', '__VIK__ TAH'),
            'W': ('Whiskey', '__WISS__ KEY'),
            'X': ('X-ray', '__ECKS__ RAY'),
            'Y': ('Yankee', '__YANG__ KEY'),
            'Z': ('Zulu', '__ZOO__ LOO')
        }

    @commands.command()
    async def phonetics(self, ctx):
        """Not there yet, dumbo."""

        await ctx.send(self.ph['A'])
