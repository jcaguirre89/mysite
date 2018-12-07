# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 14:04:23 2017

@author: crist

create plotly charts
"""

import numpy as np

import plotly.graph_objs as go
import plotly


def chart_line_base100(df, title='', formatchart='.3%', size=(800, 600)):

    #turn prices into base 100 ts
    returns = df.pct_change(periods=1).fillna(0)
    df_100 = 100*(returns+1).cumprod()
    
    data=[]
    for col in df.columns:    
        trace=go.Scatter(x=df_100.index,
                         y=df_100[col],
                         name=col,
                         mode='lines',
                         )
    
        data.append(trace)

    layout=go.Layout(
        title=title,
        height=size[1],
        width=size[0],
        showlegend=True,
        margin=go.layout.Margin(l=75),
        legend=dict(x=-0.3, y=1),
        xaxis=dict(
                showgrid=False
                ),
        yaxis=dict(
                showgrid=False,
                showticklabels=False,
                hoverformat=formatchart,
                
                ),
            )
    
    fig = go.Figure(data=data, layout=layout)

    
    s=plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    s=s.replace('"showLink": true','"showLink": false')
    
    return s


def chart_line(df, name='', formatchart='.3%', size=(800, 600)):
    """
    creates a line chart for each column in the dataframe, using the index as X axis. 
    inputs:
    df: a dataframe of each series you want to plot, with the index as your desired X axis.
    formatchart: the formatting you want the series to have. default is 3 decimal place percentage.
    size: the chart's size, in pixels. [width, height]
    
    output:
    s: the plotly chart html code, as a string.
    """
    
    data = []
    for col in df.columns:    
        trace = go.Scatter(x=df.index,
                         y=df[col],
                         name=col,
                         mode='lines',
                         )
    
        data.append(trace)

    layout=go.Layout(
        title=name,
        height=size[1],
        width=size[0],
        #legend=dict(orientation='h'),
        margin=go.layout.Margin(l=75),
        xaxis=dict(
                showgrid=False
                ),
        yaxis=dict(
                showgrid=False,
                hoverformat=formatchart,
                ),
            )
    
    fig = go.Figure(data=data, layout=layout)

    s = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    s = s.replace('"showLink": true', '"showLink": false')
    
    return s


def chart_bar(y, title='', categories=None, formatchart='.3%', size=(800, 600)):

    if categories is None:
        categories = np.arange(y.shape[0])
    
    trace1 = go.Bar(
            x=categories,
            y=y,
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )
                
    data = [trace1]

    layout = go.Layout(
        title=title,
        height=size[1],
        width=size[0],
        showlegend=False,
        xaxis=dict(
            autorange=True,
            showgrid=False,
            #zeroline=False,
            #showline=False,
            ticks='',
            showticklabels=False,
        ),
        yaxis=dict(
            autorange=True,
            showgrid=False,
            #zeroline=False,
            #showline=False,
            ticks='',
            showticklabels=False,
            hoverformat=formatchart,
            )   
            )
    
    fig = go.Figure(data=data, layout=layout)

    s = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    s = s.replace('"showLink": true','"showLink": false')
    
    return s


def chart_bar_cum(y, y_cum, title='', categories=False, formatchart='.3%', size=(800, 600)):

    if categories:
        categories = y.index
    else:
        categories = np.arange(y.shape[0])
    
    trace1 = go.Bar(
            x=categories,
            y=y,
            name='Current Capital',
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )

    trace2 = go.Scatter(
            x=categories,
            y=y_cum,
            name='Cumulate Return',
            mode='lines',
            yaxis='y2',
        )
                
    data = [trace1, trace2]


    layout=go.Layout(
        title=title,
        height=size[1],
        width=size[0],
        showlegend=False,
        xaxis=dict(
            autorange=True,
            showgrid=False,
            #zeroline=False,
            #showline=False,
            ticks='',
            showticklabels=False,
        ),
        yaxis=dict(
            autorange=True,
            showgrid=False,
            #zeroline=False,
            #showline=False,
            ticks='',
            showticklabels=False,
            hoverformat=formatchart,
            ),
        yaxis2=dict(
            autorange=True,
            showgrid=False,
            #zeroline=False,
            #showline=False,
            ticks='',
            showticklabels=False,
            hoverformat='.1%',
            overlaying='y',
            side='right',
            ),        
            )
    fig = go.Figure(data=data, layout=layout)

    
    s=plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    s=s.replace('"showLink": true','"showLink": false')
    
    return s

