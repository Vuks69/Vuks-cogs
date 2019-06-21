from redbot.core import commands
from random import randint


# noinspection PyMissingConstructor
class Phonetics(commands.Cog):
    """Description of the cog visible with [p]help MyFirstCog.
    Also if you didn't notice, *not there yet*."""

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
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @commands.command()
    async def codeword(self, ctx, letter=None):
        """Not there yet, dumbo."""
        if letter is None:
            letter = self.alphabet[randint(0, 26)]
        letter = letter.upper()
        await ctx.send(letter + " " + self.ph[letter][0])

    @commands.command()
    async def phonetic(self, ctx, letter=None):
        """Not there yet, dumbo."""
        if letter is None:
            letter = self.alphabet[randint(0, 26)]
        letter = letter.upper()
        await ctx.send(letter + " " + self.ph[letter][1])
