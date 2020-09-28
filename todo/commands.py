import asyncio
import hashlib
import discord

from typing import Literal

from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import pagify, box
from redbot.core.utils.menus import start_adding_reactions
from redbot.core.utils.predicates import ReactionPredicate


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
    async def add(self, ctx: commands.Context, *, new_todo: str):
        """Add todos to your personal list."""
        async with self.config.user(ctx.author).todos() as user_todos:
            user_todos.append(new_todo)
        await ctx.tick()

    @todo.command(name="clear")
    async def remove_all(self, ctx: commands.Context):
        """Clear out your todos list"""
        msg = await ctx.send("Are you sure you want to clear your todo list? This cannot be undone!")
        # noinspection PyAsyncCall
        start_adding_reactions(msg, ReactionPredicate.YES_OR_NO_EMOJIS)
        pred = ReactionPredicate.yes_or_no(msg, ctx.author)
        try:
            await ctx.bot.wait_for("reaction_add", check=pred, timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("Timeout Error.")
            return

        if not pred.result:
            await ctx.send("Not clearing your todos.")
        else:
            async with self.config.user(ctx.author).todos() as user_todos:
                user_todos.clear()
            await ctx.send("Todos cleared.")

    @todo.command()
    async def list(self, ctx: commands.Context):
        """Show your personal todos."""
        msg = "Your todo list:\n"
        async with self.config.user(ctx.author).todos() as user_todos:
            for todo in user_todos:
                msg += "+ {}\n".format(todo)
        for page in pagify(msg, ["\n"], shorten_by=16):
            await ctx.send(box(page.lstrip(" "), lang="diff"))

    @todo.command(name="todo", hidden=True)
    async def _easter_egg(self, ctx: commands.Context):
        """Say hi to the Pink Panther!"""
        await ctx.send("Todo, todo, todo todo todo todooooo~")
