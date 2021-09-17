from discord.ext import commands
import config

bot = commands.Bot(command_prefix="!")
bot.load_extension("cogs.graph_single")
bot.load_extension("cogs.graph_multi")


bot.run(config.TOKEN)
