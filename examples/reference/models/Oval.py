import numpy as np

from bokeh.io import curdoc, show
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Oval, Plot

N = 9
x = np.linspace(-2, 2, N)
y = x**2

source = ColumnDataSource(dict(x=x, y=y))

plot = Plot(
    title=None, width=300, height=300,
    min_border=0, toolbar_location=None)

glyph = Oval(x="x", y="y", width=0.4, height=0.6, angle=-0.7, fill_color="#1d91d0")
plot.add_glyph(source, glyph)

xaxis = LinearAxis()
plot.add_layout(xaxis, 'below')

yaxis = LinearAxis()
plot.add_layout(yaxis, 'left')

plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

curdoc().add_root(plot)

show(plot)
