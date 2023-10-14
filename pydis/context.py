class Context:

  def __init__(self, bot, message):
    self.bot = bot
    self.message = message
    self.valid = message.content.startswith(bot.prefix)
    self.command = message.content.split()[0][len(bot.prefix):]
