# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 14:04:23 2017

@author: crist

create plotly charts
"""

import numpy as np
import plotly.graph_objs as go
import plotly
import os
import string
import pandas as pd

def chart_line(df, name='', formatchart='.3%', size=[800,600]):

    data=[]
    for col in df.columns:    
        trace=go.Scatter(x=df.index,
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
        margin=go.Margin(l=75),
        xaxis=dict(
                showgrid=False
                ),
        yaxis=dict(
                showgrid=False,
                hoverformat=formatchart,
                ),
            )
    
    fig = go.Figure(data=data, layout=layout)

    
    s=plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    s=s.replace('"showLink": true','"showLink": false')
    
    return s



def chart_line_dropdown(df, name='', formatchart='.3%', size=[800,600]):

    cols=df.columns
    generic_meta_list={}
    aux_list=[]
    for freq in cols:
        aux_list=list(np.array(cols)==freq)
        generic_meta_list[freq]=[val for val in aux_list]
    
    simple_list=list(np.array(cols)==cols[0])
    
    

    
    data=[]
    for idx, col in enumerate(cols):    
        trace=go.Scatter(x=df.index,
                         y=df[col],
                         mode='lines',
                         visible=simple_list[idx]
                         )
    
        data.append(trace)
    
    menus=[]
    for col in cols:
        menu_aux=dict(label = col,
                       method = 'update',
                       args = [{'visible': generic_meta_list[col]}, {'title':name}])
        menus.append(menu_aux)
    
    
    
    updatemenus =[dict(active=0, buttons=menus, x=-0.2, y=1)]
    
    layout=go.Layout(
        title=name,
        height=size[1],
        width=size[0],
        #legend=dict(orientation='h'),
        margin=go.Margin(l=75),
        xaxis=dict(
                showgrid=False
                ),
        yaxis=dict(
                showgrid=False,
                hoverformat=formatchart,
                ),
        updatemenus=updatemenus
            )
    
    fig = go.Figure(data=data, layout=layout)
    
    
    s=plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    s=s.replace('"showLink": true','"showLink": false')
    
    return s

def chart_bar(y, title='', categories=None, formatchart='.3%', size=[800,600]):

    if categories==None:
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
            autotick=True,
            ticks='',
            showticklabels=False,
        ),
        yaxis=dict(
            autorange=True,
            showgrid=False,
            #zeroline=False,
            #showline=False,
            autotick=True,
            ticks='',
            showticklabels=False,
            hoverformat=formatchart,
            )   
            )
    
    fig = go.Figure(data=data, layout=layout)

    
    s=plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    s=s.replace('"showLink": true','"showLink": false')
    
    return s

def chart_bar_cum(y, y_cum, title='', categories=False, formatchart='.3%', size=[800,600]):

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
            autotick=True,
            ticks='',
            showticklabels=False,
        ),
        yaxis=dict(
            autorange=True,
            showgrid=False,
            #zeroline=False,
            #showline=False,
            autotick=True,
            ticks='',
            showticklabels=False,
            hoverformat=formatchart,
            ),
        yaxis2=dict(
            autorange=True,
            showgrid=False,
            #zeroline=False,
            #showline=False,
            autotick=True,
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




#if __name__=='__main__':

    