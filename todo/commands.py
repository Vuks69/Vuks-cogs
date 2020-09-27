from redbot.core import commands


class Todo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def red_delete_data_for_user(*, requester, user_id):
        NotImplementedError()

    @commands.group()
    async def todo(self, ctx: commands.Context):
        NotImplementedError()

    @todo.command(aliases=["new", "create"])
    async def add(self, ctx: commands.Context):
        NotImplementedError()

    @todo.command(aliases=["delete", "del"])
    async def remove(self, ctx: commands.Context):
        NotImplementedError()

    @todo.command()
    async def list(self, ctx: commands.Context):
        NotImplementedError()

    @todo.command(name="todo")
    async def _easter_egg(self, ctx: commands.Context):
        await ctx.send("Todo, todo, todo todo todo todooooo~")
