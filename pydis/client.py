import discord

class Client(discord.Client):

  def __init__(self, token):
    super().__init__() 
    self.token = token

  async def start(self, *args, **kwargs):
    self.run(self.token, *args, **kwargs)
