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


class graph_multi(commands.Cog):
    """The description for Bargraph goes here."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command("bar")
    async def bar(self, ctx, title: str, xl: str, yl: str, data: str):
        dbg = graph()
        data = data.split("#")
        ng = len(data)
        for i in range(len(data)):
            data[i] = data[i].split(",")
        keys = []
        values = []
        for i in range(len(data)):
            keys.append([])
            values.append([])

        for i in range(len(data)):
            for n in range(len(data[i])):
                if n % 2 == 0:
                    keys[i].append(data[i][n])
                else:
                    values[i].append(int(data[i][n]))
        if len(values) != len(keys):
            await ctx.send("The amount of keys and values are not the same")
        else:
            print(keys, values)
            dbg.barGraph(keys, values, title, xl, yl)
            await ctx.send(file=discord.File('mygraph.png'))


def setup(bot):
    bot.add_cog(graph_multi(bot))
