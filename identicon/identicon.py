import pydenticon
import random
from io import BytesIO
from typing import Union, Optional

import discord
from redbot.core import checks, commands
from redbot.core.utils import chat_formatting as chat


class Identicon(commands.Cog):
    """
    Generates an unique avatar using your Discord ID

    Many thanks to Fixator10#7133 for the idea and help on this.
	Unfortunately there are a few bugs that need to be ironed out.
	For example, calling `[p]identicon` with user ID will only work
	if you provide the `scale` and `size` params.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["idi"])
    @checks.bot_has_permissions(attach_files=True)
    async def identicon(
        self,
        ctx: commands.Context,
        scale: Optional[int],
        size: Optional[int],
        colorful: Optional[bool],
        *,
        user: Union[discord.Member, discord.User, int] = None,
    ):
        """
        Generate an unique avatar using your Discord ID

        Parameters
        ----------
        `scale` (int)
        - amount of squares per row
        - default is 10
        `size` (int)
        - size of the image (size x size)
        - cannot be set without the `scale` parameter
        - default is 240, may be altered slightly to prevent artifacts
        `colorful` (bool)
        - set the identicon to use colors, or black & white
        - default is True
        `user`
        - user for whom the identicon is to be generated
        - may be an ID, a mention or their username
        - - (varied results if there are multiple users with an identical name)
        - defaults to command invoker
        """

        msg = ""
        DEFAULT_SCALE = 10
		DEFAULT_SIZE = 240
        scale = scale if scale else DEFAULT_SCALE
        if scale < 5 or scale > 15:
            msg += (
                f"Scale is out of bounds <5, 15> and has been set to {DEFAULT_SCALE}.\n"
            )
            scale = DEFAULT_SCALE
        size = size - size % scale if size else DEFAULT_SIZE - DEFAULT_SIZE % scale
		if size < 10 or size > 2000 :
			msg += (
				f"Size is out of bounds <10, 2000> and has been set to {DEFAULT_SIZE}.\n"
			)
			size = DEFAULT_SIZE - DEFAULT_SIZE % scale
        colorful = colorful if isinstance(colorful, bool) else True

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
        if colorful:
            # these approaches generate same results
            fg = ["#{:06x}".format(random.randint(0x0, 0xFFFFFF))]
            bg = "#{:06x}".format(random.randint(0x0, 0xFFFFFF))
            # fg = ['#' + hex(random.randint(0x0, 0xFFFFFF))[2:].zfill(6)]
            # bg = '#' + hex(random.randint(0x0, 0xFFFFFF))[2:].zfill(6)
            if fg[0] == bg:
                # squashing an edge case for some users...
                bg = color_black if fg != color_black else color_white
        else:  # black & white
            fg = [color_white]
            bg = color_black

        f = BytesIO()
        # pydenticon.Generator(rows, columns, digest=<built-in function openssl_md5>, foreground=['#000000'], background='#ffffff')
        # NOTE: max scale supported with md5 is 15
        generator = pydenticon.Generator(scale, scale, foreground=fg, background=bg)
        icon = generator.generate(str(user.id), size, size)
        f.write(icon)
        f.seek(0)
        f.name = "identicon.png"
        await ctx.send(msg + f"{user.name}'s identicon:", file=discord.File(f))
