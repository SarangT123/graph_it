## Commands of graph it

#### The prefix for the bot is `;`


The commands can be catogorized to two parts

- Single graph commands
- Multi graph commands

--------------------------------------------------

### Single graph commands 
----------------------------
<table>
<thead>
<tr>
<th>Command</th>
<th>ARGS</th>
</tr>
</thead>
<tbody>
<tr>
<td>bar</td>
<td>&lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;</td>
</tr>
<tr>
<td>pie</td>
<td>&lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;</td>
</tr>
<tr>
<td>linear</td>
<td>&lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;</td>
</tr>
<tr>
<td>area</td>
<td>&lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;</td>
</tr>
<tr>
<td>scatter</td>
<td>&lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;</td>
</tr>
<tr>
<td>hist</td>
<td>&lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;</td>
</tr>
</tbody>
</table>

What does they refer to?
<table>
<thead>
<tr>
<th>ARG</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>title</td>
<td>Title of the graph</td>
</tr>
<tr>
<td>xl</td>
<td>main label on the x axis</td>
</tr>
<tr>
<td>yl</td>
<td>main label on the y axis</td>
</tr>
<tr>
<td>data</td>
<td>the data for the graph</td>
</tr>
</tbody>
</table>



### Multi graph commands
---------------------------
<table>
<thead>
<tr>
<th>Command</th>
<th>ARGS</th>
</tr>
</thead>
<tbody>
<tr>
<td>bar_multi</td>
<td>&lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;</td>
</tr>
<tr>
<td>linear_multi</td>
<td>&lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;</td>
</tr>
<tr>
<td>pie_multi</td>
<td>&lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;</td>
</tr>
<tr>
<td>are_multi</td>
<td>&lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;</td>
</tr>
<tr>
<td>scatter_multi</td>
<td>&lt;title&gt; &lt;xl&gt; &lt;yl&gt; &lt;data&gt;</td>
</tr>
</tbody>
</table>


What does they refer to?
<table>
<thead>
<tr>
<th>ARG</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>title</td>
<td>Title of the graph</td>
</tr>
<tr>
<td>xl</td>
<td>main label on the x axis</td>
</tr>
<tr>
<td>yl</td>
<td>main label on the y axis</td>
</tr>
<tr>
<td>data</td>
<td>the data for the graph</td>
</tr>
</tbody>
</table>


---------------------------
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


But for multigraphs you would have 2 datasets to do that put a space after the first dataset

Eg: `;bar_multi temparature location-day temparature-in-degrees NYC-day1,10,NYC-day2,20 WDC-day1,30,WDC-day2,20`

Here the data is 
`NYC-day1,10,NYC-day2,20 WDC-day1,30,WDC-day2,20`

And the first set would be `NYC-day1,10,NYC-day2,20`

The second set is spearated from the first set through a space so the second set is `WDC-day1,30,WDC-day2,20`