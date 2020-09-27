from .commands import Todo

__red_end_user_data_statement__ = (
    "This cog stores data manually created by users (todo's) "
    "and user IDs for the purpose of identifying owners of the todo lists."
)


def setup(bot):
    cog = Todo(bot)
    bot.add_cog(cog)
