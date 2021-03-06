import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, save

template = """
{% block preamble %}
<style>
    .grid {
        display: inline-grid;
        grid-template-columns: auto auto;
        grid-gap: 10px;
        padding: 10px;
        background-color: gray;
    }
    .item {
        background-color: black;
    }
</style>
{% endblock %}
{% block contents %}
<div class="grid">
    {{ super() }}
</div>
{% endblock %}
{% block root %}
<div class="item">{{ super() }}</div>
{% endblock %}
"""

items = []

for location in ["above", "right", "left", "below"]:
    coeffs = [10**3, 10**6]
    V = np.arange(10)

    figs = []

    for ycoeff in coeffs:
        row = []
        for xcoeff in coeffs:
            fig = figure(height=200, width=200)
            fig.xaxis.formatter.use_scientific = False
            fig.yaxis.formatter.use_scientific = False
            fig.xaxis.major_label_orientation = "vertical"
            fig.yaxis.major_label_orientation = "horizontal"
            fig.scatter(V*xcoeff, V*ycoeff)
            row.append(fig)
        figs.append(row)

    items.append(gridplot(figs, toolbar_location=location))

save(items, template=template)
