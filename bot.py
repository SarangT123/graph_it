from discord.ext import commands
import config
bot = commands.Bot(command_prefix=";")
bot.remove_command('help')
bot.load_extension("cogs.graph_single")
bot.load_extension("cogs.graph_multi")
bot.load_extension("cogs.basic_commands")
bot.load_extension("cogs.graph_single_quick")

import keepalive
keepalive.keep_alive()

bot.run(config.TOKEN)

