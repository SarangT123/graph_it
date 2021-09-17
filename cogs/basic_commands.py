from discord.ext import commands
import discord

helpembed = discord.Embed(title="Hello, world!",
                          description=":D", colour=0x87CEEB)
helpembed.add_field(
    name="__help__", value="`Select an option from below which you need help with`", inline=False)
helpembed.add_field(name="!help <graphname>",
                    value="!help bar \n to get help with graphs", inline=False)
helpembed.add_field(name="!helpmulti <graphname>",
                    value="!helpmulti bar \n to get help with multigraphs", inline=False)
helpembed.set_footer(text="Thanks for using us",
                     icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")

helpembeddata = discord.Embed(title="Using data syntax",
                              description=":D", colour=0x87CEEB)
helpembeddata.add_field(
    name="Syntax", value="**The data is a simple syntax provided by the bot** \n *__Usage__* \n For any graph other than histogram the syntax is the \n `<name>,<value>,<name>,<value>......... ", inline=False)
helpembeddata.add_field(name="Example",
                        value="!bar title xaxistitle yaxistitle `bar1,10,bar2,25,bar3,13`", inline=False)
helpembeddata.add_field(name="In histogram",
                        value="<data>,<data>,<data>... <bin>,<bin>,<bin>.... \n __Example__ \n !hist title titlex titley `10,13,27,32` `10,20,30`", inline=False)
helpembeddata.add_field(name="In multigraphs",
                        value="<name>,<value>,<name>,<value>..... <nameofgraph2>,<value>,<nameofgraph2>,<value>....", inline=False)
helpembeddata.set_footer(text="Thanks for using us",
                         icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")


class BasicCommands(commands.Cog):
    """The description for BasicCommands goes here."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command("help")
    async def help(self, ctx, helpwith: str):
        if helpwith == "bar":
            await ctx.send("**How to use bar chart** \n You can use ```py \n !bar <title> <X axis label> <Y axis label> <data>``` to make a bar chart \n For help on how to write data please do `!help data`")
        if helpwith == "pie":
            await ctx.send("**How to use pie chart** \n You can use ```py \n !pieg <title> <X axis label> <Y axis label> <data>``` to make a pie chart \n For help on how to write data please do `!help data`")
        if helpwith == "scatter":
            await ctx.send("**How to use scatter chart** \n You can use ```py \n !scatter <title> <X axis label> <Y axis label> <data>``` to make a scatter chart \n For help on how to write data please do `!help data`")
        if helpwith == "area":
            await ctx.send("**How to use area chart** \n You can use ```py \n !area <title> <X axis label> <Y axis label> <data>``` to make an area chart \n For help on how to write data please do `!help data`")
        if helpwith == "linear":
            await ctx.send("**How to use linear chart** \n You can use ```py \n !linear <title> <X axis label> <Y axis label> <data>``` to make a linear chart \n For help on how to write data please do `!help data`")
        if helpwith == "histogram":
            await ctx.send("**How to use histogram chart** \n You can use ```py \n !hist <title> <X axis label> <Y axis label> <data>``` to make a histogram chart \n For help on how to write data please do `!help data`")
        if helpwith == "data":
            await ctx.send("")
        await ctx.send(embed=helpembed)


def setup(bot):
    bot.add_cog(BasicCommands(bot))
