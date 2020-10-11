import asyncio
import functools

import aiohttp
import discord

from redbot.core import commands
from PIL import Image
from io import BytesIO

MAX_SIZE = 8 * 1000 * 1000


class ImageFindError(Exception):
    """Generic error for the _get_image function."""
    pass


class ImageCorruption(commands.Cog):
    """
    Corrupt images through raw data manipulation.
    """

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.imagetypes = ['png']

    @staticmethod
    def _corrupt_image(img):
        pass

    async def _get_image(self, ctx, link):
        """Helper function to find an image.

        Originally written by Flame442, edited to fit this cog."""
        if ctx.guild:
            file_size_limit = ctx.guild.filesize_limit
        else:
            file_size_limit = MAX_SIZE
        if not ctx.message.attachments and not link:
            async for msg in ctx.channel.history(limit=10):
                for a in msg.attachments:
                    if a.url.split('.')[-1].lower() in self.imagetypes:
                        link = a.url
                        break
                if link:
                    break
            if not link:
                raise ImageFindError('Please provide an attachment.')
        if link:  # linked image
            ext = link.split('.')[-1]
            if ext.lower() not in self.imagetypes:
                raise ImageFindError(
                    f'"{ext}" is not a supported filetype. Make sure you provide a direct link.'
                )
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get(link) as response:
                        r = await response.read()
                        img = Image.open(BytesIO(r))
                except (OSError, aiohttp.ClientError):
                    raise ImageFindError(
                        'An image could not be found. Make sure you provide a direct link.'
                    )
        else:  # attached image
            ext = ctx.message.attachments[0].url.split('.')[-1]
            if ext.lower() not in self.imagetypes:
                raise ImageFindError(f'"{ext}" is not a supported filetype.')
            if ctx.message.attachments[0].size > file_size_limit:
                raise ImageFindError('That image is too large.')
            temp_orig = BytesIO()
            await ctx.message.attachments[0].save(temp_orig)
            temp_orig.seek(0)
            img = Image.open(temp_orig)
        if max(img.size) > 3840:
            raise ImageFindError('That image is too large.')
        img = img.convert('RGB')

        return img

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def corrupt(self, ctx: commands.context, link: str = None):
        """
        Attempt to corrupt an image file.

        Use the optional parameter "link" to use a **direct link** as the target.
        """
        async with ctx.typing():
            try:
                img = await self._get_image(ctx, link)
            except ImageFindError as e:
                return await ctx.send(e)

            task = functools.partial(self._corrupt_image, img)

            try:
                image = await asyncio.wait_for(task, timeout=60)
            except asyncio.TimeoutError:
                return await ctx.send('The image took too long to process.')
            try:
                await ctx.send(file=discord.File(image))
            except discord.errors.HTTPException:
                return await ctx.send('That image is too large.')
