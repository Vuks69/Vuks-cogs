from redbot.core import checks, commands


class JoinTriggers(commands.Cog):
    """TODO"""

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_member_join(self, mem):
    #     if mem.guild.id not in (133049272517001216, 240154543684321280):
    #         return
    #     words = ('red', 'admin', 'sinbad', 'r3d', 's1nb@d', 's1nbad', 'sinb@d', 'adm1n')
    #     name = mem.name.lower().replace(' ', '')
    #     if not any(x in name for x in words):
    #         return
    #     c = self.bot.get_channel(171665724262055936)
    #     await c.send(
    #         f'A new member with a tracked word in their name has joined {mem.guild}!\n'
    #         f'Name: {mem}\n'
    #         f'ID: {mem.id}\n'
    #         f'Discord join timestamp: {mem.created_at}\n'
    #     )
