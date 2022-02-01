## Commands of graph it

#### The prefix for the bot is `;`

### Single graph commands 
----------------------------
Command  | ARGS
-------- | -------
bar      | &lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;
pie      | &lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;
linear   | &lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;
area     | &lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;
scatter  | &lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;
hist     | &lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;

What does they refer to?
ARG | Meaning
----|--------
title | Title of the graph
xl | main label on the x axis
yl| main label on the y axis
data | the data for the graph


### How to write the data?
---------------------------
The data format is quite simple 

The format is &lt;key&gt;,&lt;value&gt;

Lets do it with a command to get more info 

```py
;bar supercoolgraph date temparture day1,34,day2,27,day3,25
```

Lets take this command as an example

In this 
```day1,34,day2,27,day3,25``` is the data

The key for x label and value for y label

now lets run it 
<img src="https://media.discordapp.net/attachments/873944956358762606/938094215693467668/mygraph.png">

And it works like a charm