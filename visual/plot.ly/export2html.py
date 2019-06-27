import plotly.graph_objs as go
import plotly.plotly as py
import plotly

import numpy as np

colorscale = [[0, '#FAEE1C'], [0.33, '#F3558E'], [0.66, '#9C1DE7'], [1, '#581B98']]
trace1 = go.Scatter(
    y = np.random.randn(500),
    mode='markers',
    marker=dict(
        size='16',
        color = np.random.randn(500),
        colorscale=colorscale,
        showscale=True
    )
)
layout = go.Layout()
data = [trace1]
fig = go.Figure(data=data, layout=layout)

config={'displayModeBar': False, 'showLink': False}
plotly.offline.plot(fig, filename="scatter.html", include_plotlyjs=True, config=config, auto_open=False)

# include_plotlyjs="directory" for many html files in same directory
