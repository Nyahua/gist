import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd
import numpy as np

def minmax_scale(X, min, max):
    X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
    X_scaled = X_std * (max - min) + min
    return X_scaled

def plotly_scatter(df, x, y, s=None, c=None, alpha=0.35):
    x = df[x].values
    y = df[y].values
    text = [f'{c}: {v:,.0f}<br>' for v in df[c].values]
    if s is None:
        s  = 16
    else:
        text = [t + f'{s}: {v:,.0f}' for t, v in zip(text, df[s].values)]
        s = minmax_scale(np.sqrt(df[s].values), 5, 35)
        
    if c is not None:
        c = minmax_scale(df[c].values, 0, 255)
        
    data = [go.Scatter(
        x = x, y = y, 
        text = text,
        hoverinfo = 'x+y+text',
        mode = 'markers',
        marker=dict(
            size = s, color = c, colorscale = 'Jet',
            showscale = True, opacity = alpha
        )
    )]
    layout = go.Layout(
        hovermode = 'closest'
    )
    return go.Figure(data, layout)

if __name__ == "__main__":

    housing = pd.read_csv('data/housing.csv')
    fig = plotly_scatter(housing, x="longitude", y="latitude", c='median_house_value', s='population')
    plot(fig)