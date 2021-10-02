from discord.ext import commands
import discord
import time


class BasicCommands(commands.Cog):
    """The description for BasicCommands goes here."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command("help", aliases=["h,hlp"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def helpp(self, ctx, *, helpwith: str = ""):
        if helpwith == "bar":

            embed = discord.Embed(
                title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description=" ", color=0xffd642)
            embed.set_author(
                name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
            embed.add_field(
                name="Bar graph", value="You can use `;bar <title> <X axis label> <Y axis label> <data>` to make a bar chart  For help on how to write data please do `;help data`", inline=True)
            embed.set_footer(text="Thanks for using us")
            await ctx.send(embed=embed)
        elif helpwith == "pie":

            embed = discord.Embed(
                title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description="   ", color=0xffd642)
            embed.set_author(
                name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
            embed.add_field(
                name="Pie chart", value="You can use `;pieg <title> <X axis label> <Y axis label> <data>` to make a pie chart  For help on how to write data please do `;help data`", inline=True)
            embed.set_footer(text="Thanks for using us")
            await ctx.send(embed=embed)
        elif helpwith == "scatter":
            embed = discord.Embed(
                title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description="   ", color=0xffd642)
            embed.set_author(
                name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
            embed.add_field(name="scatter chart", value="You can use `;scatter <title> <X axis label> <Y axis label> <data>` to make a scatter chart  For help on how to write data please do `;help data`", inline=True)
            embed.set_footer(text="Thanks for using us")
            await ctx.send(embed=embed)
        elif helpwith == "area":
            embed = discord.Embed(
                title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description="   ", color=0xffd642)
            embed.set_author(
                name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
            embed.add_field(
                name="Area chart", value="You can use `;Area <title> <X axis label> <Y axis label> <data>` to make an Area chart  For help on how to write data please do `;help data`", inline=True)
            embed.set_footer(text="Thanks for using us")
            await ctx.send(embed=embed)
        elif helpwith == "linear":
            embed = discord.Embed(
                title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description="   ", color=0xffd642)
            embed.set_author(
                name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
            embed.add_field(
                name="Linear chart", value="You can use `;linear <title> <X axis label> <Y axis label> <data>` to make a Linear chart  For help on how to write data please do `;help data`", inline=True)
            embed.set_footer(text="Thanks for using us")
            await ctx.send(embed=embed)
        elif helpwith == "histogram":
            embed = discord.Embed(
                title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description="   ", color=0xffd642)
            embed.set_author(
                name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
            embed.add_field(name="Histogram", value="You can use `py  ;hist <title> <X axis label> <Y axis label> <data&bin>` to make a histogram chart  For help on how to write data please do `;help data`", inline=True)
            embed.set_footer(text="Thanks for using us")
            await ctx.send(embed=embed)
        elif helpwith == "data":
            embed = discord.Embed(
                title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description="   ", color=0xffd642)
            embed.set_author(
                name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
            embed.add_field(
                name="Syntax", value="**The data is a simple syntax provided by the bot** ", inline=False)
            embed.add_field(
                name=" Usage", value="For any graph other than histogram the syntax is the  `name,value,name,value......`", inline=False)
            embed.add_field(
                name="Example", value=";bar title xaxistitle yaxistitle `bar1,10,bar2,25,bar3,13`", inline=False)
            embed.add_field(
                name="In histogram", value="data,data,data... bin,bin,bin....", inline=False)
            embed.add_field(
                name="Example", value=" ;hist title titlex titley `10,13,27,32` `10,20,30`", inline=True)
            embed.set_footer(text="Thanks for using us")
            await ctx.send(embed=embed)
        elif helpwith == "quick":
            embed = discord.Embed(
                title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description=" ", color=0xffd642)
            embed.set_author(
                name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
            embed.add_field(name="Quick commands", value="Quick commands are used for quickly drawing some graphs. You can put 'Q' infront of any graph command to Use this mode. Eg: `;Qlinear 1sec,100,2sec,200 `", inline=False)
            embed.set_footer(text="Thanks for using us")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot",
                                  description="Choose which topic you need help with", color=0xffd642)
            embed.set_author(
                name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
            embed.add_field(
                name="help", value="`Select an option from below which you need help with`", inline=False)
            embed.add_field(
                name=";help graphname", value=";help `<graphname>`  to get help with graphs", inline=False)
            embed.add_field(name=";helpmulti graphname",
                            value=";helpmulti `<graphname>`  to get help with multigraphs", inline=False)
            embed.add_field(name=";help quick",
                            value=";help quick", inline=False)
            embed.set_footer(text="Thanks for using us")
            await ctx.send(embed=embed)

    @commands.command('tutorial')
    @commands.cooldown(2, 120, commands.BucketType.user)
    async def tutorial(self, ctx):
        await ctx.send("Welcome to the tutorial on how to use the bot bucke up your seats cuase we are going to have some fun \n ill show u the bare minimum on how to use the bot")
        time.sleep(4)
        await ctx.send("Lets learn how to draw a bar graph first. Should be pretty easy for someone as inteligent as you")
        time.sleep(3)
        await ctx.send("in order to draw a bar graph you can simply do `;bar title xtitle ytitle key,value,key,value....` Here ill show an example")
        time.sleep(2)
        await ctx.send(";bar supercoolgraph date temparture day1,34,day2,27,day3,25")
        time.sleep(1)
        await ctx.send(file=discord.File("mygraphtut.png"))
        time.sleep(1)
        await ctx.send("Thats it very simple. Now that you know the basics use our help command to get more info. Wait ill just put it here for you")
        embed = discord.Embed(title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot",
                              description="Choose which topic you need help with", color=0xffd642)
        embed.set_author(
            name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
        embed.add_field(
            name="help", value="`Select an option from below which you need help with`", inline=False)
        embed.add_field(
            name=";help graphname", value=";help `<graphname>`  to get help with graphs", inline=False)
        embed.add_field(name=";helpmulti graphname",
                        value=";helpmulti `<graphname>`  to get help with multigraphs", inline=False)
        embed.add_field(name=";help quick",
                        value=";help quick", inline=False)
        embed.set_footer(text="Thanks for using us")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BasicCommands(bot))
