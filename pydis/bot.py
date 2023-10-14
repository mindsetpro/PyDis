from pydis.client import Client
from pydis.context import Context

class Bot(Client):

  def __init__(self, token):
    super().__init__(token)
    self.prefix = '!'
    self.commands = {}
    self.cogs = {}
    self.events = {}

  def command(self, name=None):
    
    def decorator(func):
      if not name:
        name = func.__name__
        
      desc = func.__doc__ or 'No description provided.'
      
      self.commands[name] = {
        'func': func,
        'name': name,
        'desc': desc
      }
      
      return func

    return decorator

  cmd = command

  async def on_message(self, msg):
    ctx = Context(self, msg)
    if ctx.valid:
      await self.handle_commands(ctx)

  async def handle_commands(self, ctx):
    if ctx.command in self.commands:
      await self.commands[ctx.command](ctx)
    else:
      for cog in self.cogs.values():
        if ctx.command in cog.commands:
          await cog.commands[ctx.command](ctx)
