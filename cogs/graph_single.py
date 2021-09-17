from discord.ext import commands
import discord


import matplotlib.pyplot as plt


class graph():
    def ___init__(self):
        pass

    def barGraph(self, datax, datay, title, xl, yl):
        x = datax
        y = datay
        fig = plt.figure(figsize=(10, 5))
        plt.rcParams['axes.facecolor'] = '#fcb86a'
        plt.rcParams['text.color'] = 'black'
        plt.rcParams['axes.labelcolor'] = 'black'
        fig.patch.set_facecolor('#fcb86a')
        plt.bar(x, y, color='#6a9bfc',
                width=0.4,)
        plt.xlabel(xl)
        plt.ylabel(yl)
        plt.title(title)
        plt.savefig('mygraph.png')

    def linearGraph(self, datax, datay, title, xl, yl):
        x = datax
        y = datay
        fig = plt.figure(figsize=(10, 5))
        plt.rcParams['axes.facecolor'] = '#fcb86a'
        plt.rcParams['text.color'] = 'black'
        plt.rcParams['axes.labelcolor'] = 'black'
        fig.patch.set_facecolor('#fcb86a')
        plt.plot(x, y, color='#6a9bfc')
        plt.xlabel(xl)
        plt.ylabel(yl)
        plt.title(title)
        plt.savefig('mygraph.png')

    def pieGraph(self, datax, datay, title, xl, yl):
        x = datax
        y = datay
        fig = plt.figure(figsize=(10, 5))
        plt.rcParams['axes.facecolor'] = '#fcb86a'
        plt.rcParams['text.color'] = 'black'
        plt.rcParams['axes.labelcolor'] = 'black'
        fig.patch.set_facecolor('#fcb86a')
        plt.pie(y, labels=x)
        plt.title(title)
        plt.savefig('mygraph.png')

    def scatterGraph(self, datax, datay, title, xl, yl):
        x = datax
        y = datay
        fig = plt.figure(figsize=(10, 5))
        plt.rcParams['axes.facecolor'] = '#fcb86a'
        plt.rcParams['text.color'] = 'black'
        plt.rcParams['axes.labelcolor'] = 'black'
        fig.patch.set_facecolor('#fcb86a')
        plt.scatter(x, y, color='#6a9bfc')
        plt.xlabel(xl)
        plt.ylabel(yl)
        plt.title(title)
        plt.savefig('mygraph.png')

    def histGraph(self, datax, datay, title, xl, yl):
        x = datax
        y = datay
        fig = plt.figure(figsize=(10, 5))
        plt.rcParams['axes.facecolor'] = '#fcb86a'
        plt.rcParams['text.color'] = 'black'
        plt.rcParams['axes.labelcolor'] = 'black'
        fig.patch.set_facecolor('#fcb86a')
        plt.hist(x, y, histtype="bar", rwidth=0.8)
        plt.xlabel(xl)
        plt.ylabel(yl)
        plt.title(title)
        plt.savefig('mygraph.png')

    def areaGraph(self, datax, datay, title, xl, yl):
        x = datax
        y = datay
        fig = plt.figure(figsize=(10, 5))
        plt.rcParams['axes.facecolor'] = '#fcb86a'
        plt.rcParams['text.color'] = 'black'
        plt.rcParams['axes.labelcolor'] = 'black'
        fig.patch.set_facecolor('#fcb86a')
        plt.stackplot(x, y, color='#6a9bfc')
        plt.xlabel(xl)
        plt.ylabel(yl)
        plt.title(title)
        plt.savefig('mygraph.png')


class graph_single(commands.Cog):
    """The description for Bargraph goes here."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command("bar")
    async def bar(self, ctx, title: str, xl: str, yl: str, *, data: str):
        dbg = graph()
        data = data.split(",")
        keys = []
        values = []
        for i in range(len(data)):
            if i % 2 == 0:
                keys.append(data[i])
            else:
                values.append(int(data[i]))
        if len(values) != len(keys):
            await ctx.send("The amount of keys and values are not the same")
        else:
            print(keys, values)
            dbg.barGraph(keys, values, title, xl, yl)
            await ctx.send(file=discord.File('mygraph.png'))
        @bar.MissingRequiredArgument
        async def notenargs(self,ctx):
            embed=discord.Embed(title="Ooops", description="Seems you havent given all the values or have messed up the command. We have provided some help below", color=0xff4747)
            await ctx.send(embed=embed)
            embed=discord.Embed(title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description=" ", color=0xffd642)
            embed.set_author(name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
            embed.add_field(name="Bar graph", value="You can use `;bar <title> <X axis label> <Y axis label> <data>` to make a bar chart  For help on how to write data please do `;help data`", inline=True)
            embed.add_field(name="Pie chart", value="You can use `;pieg <title> <X axis label> <Y axis label> <data>` to make a pie chart  For help on how to write data please do `;help data`", inline=True)
            embed.set_footer(text="Thanks for using us")
            embed.add_field(name="scatter chart", value="You can use `;scatter <title> <X axis label> <Y axis label> <data>` to make a scatter chart  For help on how to write data please do `;help data`", inline=True)
            embed.add_field(name="Area chart", value="You can use `;Area <title> <X axis label> <Y axis label> <data>` to make an Area chart  For help on how to write data please do `;help data`", inline=True)
            embed.add_field(name="Linear chart", value="You can use `;linear <title> <X axis label> <Y axis label> <data>` to make a Linear chart  For help on how to write data please do `;help data`", inline=True)
            embed.add_field(name="Histogram", value="You can use `py  ;hist <title> <X axis label> <Y axis label> <data&bin>` to make a histogram chart  For help on how to write data please do `;help data`", inline=True)
            embed.set_footer(text="Thanks for using us")
            await ctx.send(embed=embed)

    @commands.command("linear")
    async def linear(self, ctx, title: str, xl: str, yl: str, *, data: str):
        dbg = graph()
        data = data.split(",")
        keys = []
        values = []
        for i in range(len(data)):
            if i % 2 == 0:
                keys.append(data[i])
            else:
                values.append(int(data[i]))
        if len(values) != len(keys):
            await ctx.send("The amount of keys and values are not the same")
        else:
            print(keys, values)
            dbg.linearGraph(keys, values, title, xl, yl)
            await ctx.send(file=discord.File('mygraph.png'))
    @linear.error
    async def notenargs2(self,ctx):
        embed=discord.Embed(title="Ooops", description="Seems you havent given all the values or have messed up the command. We have provided some help below", color=0xff4747)
        await ctx.send(embed=embed)
        embed=discord.Embed(title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description=" ", color=0xffd642)
        embed.set_author(name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
        embed.add_field(name="Bar graph", value="You can use `;bar <title> <X axis label> <Y axis label> <data>` to make a bar chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Pie chart", value="You can use `;pieg <title> <X axis label> <Y axis label> <data>` to make a pie chart  For help on how to write data please do `;help data`", inline=True)
        embed.set_footer(text="Thanks for using us")
        embed.add_field(name="scatter chart", value="You can use `;scatter <title> <X axis label> <Y axis label> <data>` to make a scatter chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Area chart", value="You can use `;Area <title> <X axis label> <Y axis label> <data>` to make an Area chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Linear chart", value="You can use `;linear <title> <X axis label> <Y axis label> <data>` to make a Linear chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Histogram", value="You can use `py  ;hist <title> <X axis label> <Y axis label> <data&bin>` to make a histogram chart  For help on how to write data please do `;help data`", inline=True)
        embed.set_footer(text="Thanks for using us")
        await ctx.send(embed=embed)

    @commands.command("area")
    async def area(self, ctx, title: str, xl: str, yl: str, *, data: str):
        dbg = graph()
        data = data.split(",")
        keys = []
        values = []
        for i in range(len(data)):
            if i % 2 == 0:
                keys.append(data[i])
            else:
                values.append(int(data[i]))
        if len(values) != len(keys):
            await ctx.send("The amount of keys and values are not the same")
        else:
            print(keys, values)
            dbg.areaGraph(keys, values, title, xl, yl)
            await ctx.send(file=discord.File('mygraph.png'))
    @area.error
    async def notenargs3(self,ctx):
        embed=discord.Embed(title="Ooops", description="Seems you havent given all the values or have messed up the command. We have provided some help below", color=0xff4747)
        await ctx.send(embed=embed)
        embed=discord.Embed(title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description=" ", color=0xffd642)
        embed.set_author(name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
        embed.add_field(name="Bar graph", value="You can use `;bar <title> <X axis label> <Y axis label> <data>` to make a bar chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Pie chart", value="You can use `;pieg <title> <X axis label> <Y axis label> <data>` to make a pie chart  For help on how to write data please do `;help data`", inline=True)
        embed.set_footer(text="Thanks for using us")
        embed.add_field(name="scatter chart", value="You can use `;scatter <title> <X axis label> <Y axis label> <data>` to make a scatter chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Area chart", value="You can use `;Area <title> <X axis label> <Y axis label> <data>` to make an Area chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Linear chart", value="You can use `;linear <title> <X axis label> <Y axis label> <data>` to make a Linear chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Histogram", value="You can use `py  ;hist <title> <X axis label> <Y axis label> <data&bin>` to make a histogram chart  For help on how to write data please do `;help data`", inline=True)
        embed.set_footer(text="Thanks for using us")
        await ctx.send(embed=embed)

    @commands.command("pie")
    async def pie(self, ctx, title: str, xl: str, yl: str, *, data: str):
        dbg = graph()
        data = data.split(",")
        keys = []
        values = []
        for i in range(len(data)):
            if i % 2 == 0:
                keys.append(data[i])
            else:
                values.append(int(data[i]))
        if len(values) != len(keys):
            await ctx.send("The amount of keys and values are not the same")
        else:
            print(keys, values)
            dbg.pieGraph(keys, values, title, xl, yl)
            await ctx.send(file=discord.File('mygraph.png'))
    @pie.error
    async def notenargs4(self,ctx):
        embed=discord.Embed(title="Ooops", description="Seems you havent given all the values or have messed up the command. We have provided some help below", color=0xff4747)
        await ctx.send(embed=embed)
        embed=discord.Embed(title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description=" ", color=0xffd642)
        embed.set_author(name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
        embed.add_field(name="Bar graph", value="You can use `;bar <title> <X axis label> <Y axis label> <data>` to make a bar chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Pie chart", value="You can use `;pieg <title> <X axis label> <Y axis label> <data>` to make a pie chart  For help on how to write data please do `;help data`", inline=True)
        embed.set_footer(text="Thanks for using us")
        embed.add_field(name="scatter chart", value="You can use `;scatter <title> <X axis label> <Y axis label> <data>` to make a scatter chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Area chart", value="You can use `;Area <title> <X axis label> <Y axis label> <data>` to make an Area chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Linear chart", value="You can use `;linear <title> <X axis label> <Y axis label> <data>` to make a Linear chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Histogram", value="You can use `py  ;hist <title> <X axis label> <Y axis label> <data&bin>` to make a histogram chart  For help on how to write data please do `;help data`", inline=True)
        embed.set_footer(text="Thanks for using us")
        await ctx.send(embed=embed)

    @commands.command("scatter")
    async def scatter(self, ctx, title: str, xl: str, yl: str, *, data: str):
        dbg = graph()
        data = data.split(",")
        keys = []
        values = []
        for i in range(len(data)):
            if i % 2 == 0:
                keys.append(data[i])
            else:
                values.append(int(data[i]))
        if len(values) != len(keys):
            await ctx.send("The amount of keys and values are not the same")
        else:
            print(keys, values)
            dbg.scatterGraph(keys, values, title, xl, yl)
            await ctx.send(file=discord.File('mygraph.png'))
    @scatter.error
    async def notenargs5(self,ctx):
        embed=discord.Embed(title="Ooops", description="Seems you havent given all the values or have messed up the command. We have provided some help below", color=0xff4747)
        await ctx.send(embed=embed)
        embed=discord.Embed(title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description=" ", color=0xffd642)
        embed.set_author(name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
        embed.add_field(name="Bar graph", value="You can use `;bar <title> <X axis label> <Y axis label> <data>` to make a bar chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Pie chart", value="You can use `;pieg <title> <X axis label> <Y axis label> <data>` to make a pie chart  For help on how to write data please do `;help data`", inline=True)
        embed.set_footer(text="Thanks for using us")
        embed.add_field(name="scatter chart", value="You can use `;scatter <title> <X axis label> <Y axis label> <data>` to make a scatter chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Area chart", value="You can use `;Area <title> <X axis label> <Y axis label> <data>` to make an Area chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Linear chart", value="You can use `;linear <title> <X axis label> <Y axis label> <data>` to make a Linear chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Histogram", value="You can use `py  ;hist <title> <X axis label> <Y axis label> <data&bin>` to make a histogram chart  For help on how to write data please do `;help data`", inline=True)
        embed.set_footer(text="Thanks for using us")
        await ctx.send(embed=embed)

    @commands.command("hist")
    async def hist(self, ctx, title: str, xl: str, yl: str, data: str, bins: str):
        dbg = graph()
        data = data.split(',')
        bins = bins.split(',')
        print(data, bins)
        data = [int(i) for i in data]
        bins = [int(i) for i in bins]
        print(data, bins)
        dbg.histGraph(data, bins, title, xl, yl)
        await ctx.send(file=discord.File('mygraph.png'))
    @hist.error
    async def notenargs6(self,ctx):
        embed=discord.Embed(title="Ooops", description="Seems you havent given all the values or have messed up the command. We have provided some help below", color=0xff4747)
        await ctx.send(embed=embed)
        embed=discord.Embed(title="Help is here", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot", description=" ", color=0xffd642)
        embed.set_author(name="Graph it", url="https://discord.com/api/oauth2/authorize?client_id=887213789081124914&permissions=412317190208&scope=bot")
        embed.add_field(name="Bar graph", value="You can use `;bar <title> <X axis label> <Y axis label> <data>` to make a bar chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Pie chart", value="You can use `;pieg <title> <X axis label> <Y axis label> <data>` to make a pie chart  For help on how to write data please do `;help data`", inline=True)
        embed.set_footer(text="Thanks for using us")
        embed.add_field(name="scatter chart", value="You can use `;scatter <title> <X axis label> <Y axis label> <data>` to make a scatter chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Area chart", value="You can use `;Area <title> <X axis label> <Y axis label> <data>` to make an Area chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Linear chart", value="You can use `;linear <title> <X axis label> <Y axis label> <data>` to make a Linear chart  For help on how to write data please do `;help data`", inline=True)
        embed.add_field(name="Histogram", value="You can use `py  ;hist <title> <X axis label> <Y axis label> <data&bin>` to make a histogram chart  For help on how to write data please do `;help data`", inline=True)
        embed.set_footer(text="Thanks for using us")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(graph_single(bot))
