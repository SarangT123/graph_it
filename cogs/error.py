from discord.ext import commands
import discord
from discord.ext.commands.core import command


class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.CommandError):
            pass
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send("Command on cooldown :clock:")
        elif isinstance(commands.MissingRequiredArgument):
            print("horror")
            embed = discord.Embed(
                title="Ooops", description="Seems you havent given all the values or have messed up the command. We have provided some help below", color=0xff4747)
            await ctx.send(embed=embed)
            embed = discord.Embed(
                title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description=" ", color=0xffd642)
            embed.set_author(
                name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
            embed.add_field(
                name="Bar graph", value="You can use `;bar <title> <X axis label> <Y axis label> <data>` to make a bar chart  For help on how to write data please do `;help data`", inline=True)
            embed.add_field(
                name="Pie chart", value="You can use `;pieg <title> <X axis label> <Y axis label> <data>` to make a pie chart  For help on how to write data please do `;help data`", inline=True)
            embed.set_footer(text="Thanks for using us")
            embed.add_field(name="scatter chart", value="You can use `;scatter <title> <X axis label> <Y axis label> <data>` to make a scatter chart  For help on how to write data please do `;help data`", inline=True)
            embed.add_field(
                name="Area chart", value="You can use `;Area <title> <X axis label> <Y axis label> <data>` to make an Area chart  For help on how to write data please do `;help data`", inline=True)
            embed.add_field(
                name="Linear chart", value="You can use `;linear <title> <X axis label> <Y axis label> <data>` to make a Linear chart  For help on how to write data please do `;help data`", inline=True)
            embed.add_field(name="Histogram", value="You can use `py  ;hist <title> <X axis label> <Y axis label> <data&bin>` to make a histogram chart  For help on how to write data please do `;help data`", inline=True)
            embed.set_footer(text="Thanks for using us")
            await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
