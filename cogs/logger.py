from nextcord.ext import commands
import nextcord
from config import alertsChannel


class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client
        super().__init__()

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        embed = nextcord.Embed(title=f"{message.author.name} deleted a message | User ID: <{message.author.id}>",
                               description=f"{message.content}", color=nextcord.Color.blue())
        channel = self.client.get_channel(alertsChannel)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        embed = nextcord.Embed(
            title=f"{message_before.author.name} edited a message. | User ID: <{message_before.author.id}>", color=nextcord.Color.blue())
        embed.add_field(name="Before edit:",
                        value=f"{message_before.content}", inline=False)
        embed.add_field(name="After edit:",
                        value=f"{message_after.content}", inline=False)
        channel = self.client.get_channel(alertsChannel)
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(Logs(client))
