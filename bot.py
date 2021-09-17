from flask import Flask
from discord.ext import commands
import config
bot = commands.Bot(command_prefix="!")
bot.load_extension("cogs.graph_single")
bot.load_extension("cogs.graph_multi")
bot.load_extension("cogs.basic_commands")


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


bot.run(config.TOKEN)
app.run(host="0.0.0.0")
