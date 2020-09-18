import pydenticon
import random
from io import BytesIO
from typing import Union, Optional

import discord
from redbot.core import checks, commands
from redbot.core.utils import chat_formatting as chat


class Identicon(commands.Cog):
    """
    Generate an unique avatar using your Discord ID
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["idicon"])
    @checks.bot_has_permissions(attach_files=True)
    async def identicon(
        self,
        ctx: commands.Context,
        user: Union[discord.Member, discord.User, int] = None,
    ):
        """
        Generate an unique pydenticon with an user's Discord ID

        Parameters
        ----------
        `[user]` - any valid user that shares a server with this bot (ID|tag#1234|tag)
        """

        msg = ""
        DEFAULT_SCALE = 9
        DEFAULT_SIZE = 120

        scale = DEFAULT_SCALE
        size = DEFAULT_SIZE - DEFAULT_SIZE % scale

        if isinstance(user, int):
            try:
                user = await ctx.bot.fetch_user(user)
            except discord.NotFound:
                await ctx.send(
                    chat.error("Discord user with ID `{}` not found").format(user)
                )
                return
            except discord.HTTPException:
                await ctx.send(
                    chat.warning(
                        "I was unable to get data about user with ID `{}`. Try again later"
                    ).format(user)
                )
                return
        if user is None:
            user = ctx.author

        random.seed(user.id)
        color_white = "#000000"
        color_black = "#ffffff"
        fg: [str]
        bg: str
        # these approaches generate same results
        fg = ["#{:06x}".format(random.randint(0x0, 0xFFFFFF))]
        bg = "#{:06x}".format(random.randint(0x0, 0xFFFFFF))
        if fg[0] == bg:
            # squashing an edge case for some users...
            bg = color_black if fg != color_black else color_white

        f = BytesIO()
        # pydenticon.Generator(rows, columns, digest=<built-in function openssl_md5>, foreground=['#000000'], background='#ffffff')
        # NOTE: max scale supported with md5 is 15
        generator = pydenticon.Generator(scale, scale, foreground=fg, background=bg)
        icon = generator.generate(str(user.id), size, size)
        f.write(icon)
        f.seek(0)
        f.name = "identicon.png"
        await ctx.send(msg + f"{user.name}'s identicon:", file=discord.File(f))
