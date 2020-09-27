import hashlib
import discord

from typing import Literal

from redbot.core import commands, Config


class Todo(commands.Cog):
    __author__ = "Vuks#5767"

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        unique_id = int(hashlib.sha512((self.__author__ + "@" + self.__class__.__name__).encode()).hexdigest(), 16)
        self.config = Config.get_conf(self, identifier=unique_id, force_registration=True)
        self.config.register_user(todos=[])

    async def red_delete_data_for_user(
            self, *, requester: Literal["discord", "owner", "user", "user_strict"], user_id: int,
    ):
        await self.config.user_from_id(user_id).clear()

    @commands.group()
    async def todo(self, ctx: commands.Context):
        """TODO"""

    @todo.command(aliases=["new", "create"])
    async def add(self, ctx: commands.Context, new_todo: str):
        async with self.config.user(ctx.author).todos() as user_todos:
            user_todos.append(new_todo)
        await ctx.tick()

    @todo.command(name="clear")
    async def remove_all(self, ctx: commands.Context):
        async with self.config.user(ctx.author).todos() as user_todos:
            user_todos.clear()
        await ctx.tick()

    @todo.command()
    async def list(self, ctx: commands.Context):
        # https://github.com/aikaterna/gobcog/blob/7721dbfb96622d84ceb3e0dc8c7b60e13a592423/adventure/adventure.py#L3611
        NotImplementedError()

    @todo.command(name="todo")
    async def _easter_egg(self, ctx: commands.Context):
        """Say hi to the Pink Panther!"""
        await ctx.send("Todo, todo, todo todo todo todooooo~")
