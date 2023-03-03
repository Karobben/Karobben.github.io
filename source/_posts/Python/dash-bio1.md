---
toc: true
url: dash_bio1
covercopy: © Karobben
priority: 10000
date: 2022-10-01 17:32:35
title: "Dash-bio, powered by plotly, python"
ytitle: "Dash-bio, powered by plotly, python"
description: "Dash-bio, powered by plotly, python"
excerpt: "Dash-bio is a library that enables the creation of interactive, dynamic dashboards for exploring and analyzing biological data using Plotly Dash. With its customizable components and support for various data formats, dash-bio is a convenient tool for bioinformatics professionals and researchers <a title='ChatGPT'>Who sad this?</a>"
tags: [Python, dash]
category: [Python, Data]
cover: "https://s1.ax1x.com/2022/10/02/xKI759.png"
thumbnail: "https://s1.ax1x.com/2022/10/02/xKI759.png"
---

## What is dash and how wants dash

>  Dash is the original low-code framework for rapidly building data apps in Python, R, Julia, and F# (experimental). Written on top of Plotly.js and React.js, Dash is ideal for **building and deploying data apps** with customized **user interfaces**. It's particularly suited for anyone who works with data. Through a couple of simple patterns, Dash abstracts away all of the technologies and protocols that are required to build a full-stack web app with interactive data visualization. ==Dash is simple enough that you can bind a user interface to your code in less than 10 minutes.==
> Dash apps are rendered in the **web browser**. You can deploy your apps to VMs or Kubernetes clusters and then **share them through URLs**. Since Dash apps are viewed in the web browser, Dash is inherently cross-platform and mobile ready. There is a lot behind the framework. Plotly develops Dash and also offers a platform for writing and deploying Dash apps in an enterprise environment. If you're interested, please get in touch.
> From: [dash.plotly.com](https://dash.plotly.com/introduction)

Examples: [Dash Galleries](https://dash.gallery/Portal/)

## Installation

```bash
pip install dash
pip install jupyter-dash
pip install pandas
pip install dash_bio dash_auth
pip install matplotlib
pip install openpyxl
```

## Hello Word for Dash

```python
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

|![](https://s1.ax1x.com/2022/10/02/xK4pUs.png)|
|:-:|



!!! note How Dash Works
    For the example above, main layouts information was stored in `app.layout`. It is a list. Each part is arranged horizontally from top to bottom. We can add `tags` for html one by one. For example, the `h1` tag, `div` tag.

### Customize Hello Dash

![](https://s1.ax1x.com/2022/10/02/xKI759.png)


<details>
<summary>Codes for Dashboard</summary>

```python
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

markdown_text = '''
### Dash and Markdown

One of the greatist feature from Dash is the markdown rendering. It may can only redenring the basic features but it could be very helpful. unfortunately, it not support html tags in the markdown. **But it accepts code highlight!!  Chears!!!**<br>
<pre>
code test, this is a code block
</pre>
\```bash
echo hello world
\```
'''

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash',
            style={
            'textAlign': 'center',
            'color': colors['text']
        }),

    html.Div(children='''
        Dash: A web application framework for your data.
    ''',
            style={
            'textAlign': 'center',
            'color': colors['text'],
        }),

    html.Div(children=[
        html.Div(children=[dcc.Graph(
            id='example-graph',
            figure=fig, style={"height": 720})], style={'width':"60%",'height': "100%"}),
        html.Div(children=[
            dcc.Markdown(children=markdown_text),
            dcc.Graph(figure=fig, style={'width':"100%", "height": "100%"})
            ],
            style={'width':"40%", "height": "100%"})] ,
    style={'display': 'flex', "height": "100%"}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```


</details>



## Styles

### Height auto-size by the window

50% of the height of the current window
```python
style={'width':"100%", "height": "50vh"}
```

### Window overflow-show

```python
style={'width':"100%", "max-height": "50%", "overflow": "scroll"}
style={'width':"100%", "max-height": "50%", "overflow-x": "scroll"}
style={'width':"100%", "max-height": "50%", "overflow-y": "scroll"}
```

## Call back


<!--<details>-->
<details><summary>Codes for Call back example</summary>

```python
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)
```
</details>
<!--</details>-->

Example shw: [dash.plotly.com](https://dash.plotly.com/basic-callbacks)

!!! note Explain

Input widgets is from `dash.dcc.Input`. By giving an id as `my-input`, it could be called back. After we added it in a thread `@app.callback`, it can update automatically whenever you made a change.
For adding more callback widgets, we can add, Dropdown widgets for instance, and show the result on a new line. We can't add the Input&Output in the old thread directly. But we can add it in a new thread.

Two things for `callback` functions:
1. A threads is paired with function behind.
2. The parameters in the function following the order of the `Input` from the `@` threads.

When you paired a thread and function, the like below:

```python
@app.callback(
    Output("id1", 'data')
    Input("id2", 'value')
    Input("id3", 'data')
)
def update(P1, P2):
    P3 = P1 + P2
    return P3
```

In this result, it would accepts the data from widget 'id3' and 'id2'. New variable `P3` is returned and be assigned into the widget 'id1'. You can use it to make a sample calculator.

<!--<details>-->
<details><summary>Codes for Call back example</summary>

```python
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text'),
        dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], value='Montréal', id='my-input2'),
    ]),
    html.Br(),
    html.Div(id='my-output'),
    html.Div(id='my-output2'),

])

def TEST():
    print("123")

@app.callback(
    Output(component_id='my-output2', component_property='children'),
    Input(component_id='my-input2', component_property='value'),
)

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value'),

)

def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)
```
</details>
<!--</details>-->


## Use local picture

The easiest and lightest way to using local picture is cite a picture in Markdown. But before doing that, you should make a directory `assets` and then, put the picture in it.

```md
![Picture](/assets/1.png)
```



## Plots


```python
import plotly.express as px

# All settings

fig = px.scatter(
    # Colors for each elements
    color = ['A', 'B', 'C'],
)

## map axis text
fig.update_layout(
    xaxis=dict(title='',
        tickvals= [1, 2, 3, 4, 5], # raw text in axis
        ticktext = ['a', 'b', 'c', 'd'] # alternative text
    )
)

# Other layout informations
fig.update_layout(
    # stringent size
    autosize=False,
    width=500,
    height=500,
    xaxis_title= "X Axis",
    yaxis_title= "Y Axis",
    title_font_color="salmon",
    #more details for title
    title={
        'y':0.9, 'x':0.5,
        'font': {'size': 30},
        'xanchor': 'center',
        'yanchor': 'top'}

)


# Bar plot
fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
```


### Blank Background for plot

```python
fig.update_layout(
    autosize=False,
    width=300,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    title={
        'y':0.9, 'x':0.5,
        'font': {'size': 30},
        'xanchor': 'center',
        'yanchor': 'top'}
)
```

### Pileup example


This function if for make a igv like graph.
The basic example is in this [link](https://dash.plotly.com/dash-bio/pileup). There is a few things worth to mention:
- The reference genome is '2bit' format, which [is a binary file format designed for storing a genome consists of multiple chromosomal sequences.](https://biojulia.net/BioSequences.jl/v1.0/io/twobit.html)
- To create a 2bi genome, you can follow the instruction from [UCSC](https://genome.ucsc.edu/goldenPath/help/twoBit.html)










```python
import pysam
import collections
import pandas as pd
import matplotlib.pyplot as plt

samfile = pysam.AlignmentFile("WD-wts+wts149+wts149_3.s.bam", "rb")


Depth = []
for read in samfile.fetch('X', 3134870, 3172221):
    Depth += [i[1] for i in read.aligned_pairs]

frequency = collections.Counter(Depth)
Dep_TB = pd.DataFrame(dict(frequency), index=['Freq']).T
Dep_TB['Loc'] = Dep_TB.index
Dep_TB.Loc = pd.to_numeric(Dep_TB.Loc)


plt.plot(Dep_TB.Loc,  Dep_TB.Freq)
```










<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
