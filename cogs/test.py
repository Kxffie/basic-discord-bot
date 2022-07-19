from nextcord.ext import commands
import nextcord


class Basic(commands.Cog):
    def __init__(self, client):
        super().__init__()

    @commands.command()
    async def test(self, ctx):
        await ctx.send(f'Test Command!')


def setup(client):
    client.add_cog(Basic(client))
