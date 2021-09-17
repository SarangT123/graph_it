from discord.ext import commands
import discord


import matplotlib.pyplot as plt


class graph():
    def ___init__(self):
        pass

    def barGraph(self, datax, datay, title, xl, yl, ng):
        x = datax
        y = datay
        fig = plt.figure(figsize=(10, 5))
        plt.rcParams['axes.facecolor'] = '#fcb86a'
        plt.rcParams['text.color'] = 'black'
        plt.rcParams['axes.labelcolor'] = 'black'
        fig.patch.set_facecolor('#fcb86a')
        for i in range(ng):
            print(x[i], y[i])
            plt.bar(x[i], y[i],
                    width=0.4,)
        plt.xlabel(xl)
        plt.ylabel(yl)
        plt.title(title)
        plt.savefig('mygraph.png')

    def linearGraph(self, datax, datay, title, xl, yl, ng):
        x = datax
        y = datay
        fig = plt.figure(figsize=(10, 5))
        plt.rcParams['axes.facecolor'] = '#fcb86a'
        plt.rcParams['text.color'] = 'black'
        plt.rcParams['axes.labelcolor'] = 'black'
        fig.patch.set_facecolor('#fcb86a')
        for i in range(ng):
            print(x[i], y[i])
            plt.bar(x[i], y[i])
        plt.xlabel(xl)
        plt.ylabel(yl)
        plt.title(title)
        plt.savefig('mygraph.png')

    def pieGraph(self, datax, datay, title, xl, yl, ng):
        x = datax
        y = datay
        fig = plt.figure(figsize=(10, 5))
        plt.rcParams['axes.facecolor'] = '#fcb86a'
        plt.rcParams['text.color'] = 'black'
        plt.rcParams['axes.labelcolor'] = 'black'
        fig.patch.set_facecolor('#fcb86a')
        for i in range(ng):
            plt.pie(y[i], labels=x[i])
        plt.title(title)
        plt.savefig('mygraph.png')

    def scatterGraph(self, datax, datay, title, xl, yl, ng):
        x = datax
        y = datay
        fig = plt.figure(figsize=(10, 5))
        plt.rcParams['axes.facecolor'] = '#fcb86a'
        plt.rcParams['text.color'] = 'black'
        plt.rcParams['axes.labelcolor'] = 'black'
        fig.patch.set_facecolor('#fcb86a')
        for i in range(ng):
            plt.scatter(x[i], y[i])
        plt.xlabel(xl)
        plt.ylabel(yl)
        plt.title(title)
        plt.savefig('mygraph.png')

    def histGraph(self, datax, datay, title, xl, yl, ng):
        x = datax
        y = datay
        fig = plt.figure(figsize=(10, 5))
        plt.rcParams['axes.facecolor'] = '#fcb86a'
        plt.rcParams['text.color'] = 'black'
        plt.rcParams['axes.labelcolor'] = 'black'
        fig.patch.set_facecolor('#fcb86a')
        for i in range(ng):
            plt.hist(x[i], y[i], histtype="bar", rwidth=0.8)
        plt.xlabel(xl)
        plt.ylabel(yl)
        plt.title(title)
        plt.savefig('mygraph.png')

    def areaGraph(self, datax, datay, title, xl, yl, ng):
        x = datax
        y = datay
        fig = plt.figure(figsize=(10, 5))
        plt.rcParams['axes.facecolor'] = '#fcb86a'
        plt.rcParams['text.color'] = 'black'
        plt.rcParams['axes.labelcolor'] = 'black'
        fig.patch.set_facecolor('#fcb86a')
        for i in range(ng):
            plt.stackplot(x[i], y[i])
        plt.xlabel(xl)
        plt.ylabel(yl)
        plt.title(title)
        plt.savefig('mygraph.png')


class graph_multi(commands.Cog):
    """The description for Bargraph goes here."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command("bar_multi")
    async def bar_multi(self, ctx, title: str, xl: str, yl: str, *, data: str):
        dbg = graph()
        print(data)
        data = data.split(" ")
        for i in range(len(data)):
            data[i] = data[i].split(",")
        ng = len(data)
        print(data, ng)
        keys = []
        values = []
        for i in range(len(data)):
            keys.append([])
            values.append([])
            print(i)

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
            dbg.barGraph(keys, values, title, xl, yl, ng)
            await ctx.send(file=discord.File('mygraph.png'))

    @commands.command("linear_multi")
    async def linear_multi(self, ctx, title: str, xl: str, yl: str, *, data: str):
        dbg = graph()
        print(data)
        data = data.split(" ")
        for i in range(len(data)):
            data[i] = data[i].split(",")
        ng = len(data)
        print(data, ng)
        keys = []
        values = []
        for i in range(len(data)):
            keys.append([])
            values.append([])
            print(i)

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
            dbg.barGraph(keys, values, title, xl, yl, ng)
            await ctx.send(file=discord.File('mygraph.png'))

    @commands.command("scatter_multi")
    async def scatter_multi(self, ctx, title: str, xl: str, yl: str, *, data: str):
        dbg = graph()
        print(data)
        data = data.split(" ")
        for i in range(len(data)):
            data[i] = data[i].split(",")
        ng = len(data)
        print(data, ng)
        keys = []
        values = []
        for i in range(len(data)):
            keys.append([])
            values.append([])
            print(i)

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
            dbg.barGraph(keys, values, title, xl, yl, ng)
            await ctx.send(file=discord.File('mygraph.png'))

    @commands.command("area_multi")
    async def area_multi(self, ctx, title: str, xl: str, yl: str, *, data: str):
        dbg = graph()
        print(data)
        data = data.split(" ")
        for i in range(len(data)):
            data[i] = data[i].split(",")
        ng = len(data)
        print(data, ng)
        keys = []
        values = []
        for i in range(len(data)):
            keys.append([])
            values.append([])
            print(i)

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
            dbg.barGraph(keys, values, title, xl, yl, ng)
            await ctx.send(file=discord.File('mygraph.png'))

    @commands.command("pie_multi")
    async def pie_multi(self, ctx, title: str, xl: str, yl: str, *, data: str):
        dbg = graph()
        print(data)
        data = data.split(" ")
        for i in range(len(data)):
            data[i] = data[i].split(",")
        ng = len(data)
        print(data, ng)
        keys = []
        values = []
        for i in range(len(data)):
            keys.append([])
            values.append([])
            print(i)

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
            dbg.barGraph(keys, values, title, xl, yl, ng)
            await ctx.send(file=discord.File('mygraph.png'))


def setup(bot):
    bot.add_cog(graph_multi(bot))
