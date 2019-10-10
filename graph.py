import pickle
import plotly.figure_factory as ff
import numpy
import plotly.graph_objects as go

heights = pickle.load(open("heights.p", "rb"))
average_heights = numpy.random.normal(70.590551,1.59, 3020)
weights = pickle.load(open("weights.p", "rb"))
average_weights = numpy.random.normal(189.818, 30.8647, 3020)

# https://www.cdc.gov/nchs/data/nhsr/nhsr122-508.pdf

group_labels = ['Top 25', 'US Male Average']
heights = [heights, average_heights]
fig = ff.create_distplot(heights, group_labels, show_rug=False, bin_size=1)
fig.update_layout(
    title=go.layout.Title(
        text="Heights of Top 25 Football Players vs. Average American Males",
        
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Height (Inches)",
            font=dict(
                size=18,
                color="#7f7f7f"
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Frequency",
            font=dict(
                size=18,
                color="#7f7f7f"
            )
        )
    )
)
fig.show()

group_labels = ['Top 25', 'US Male Average']
weights = [weights, average_weights]
fig = ff.create_distplot(weights, group_labels, show_rug=False, bin_size=6)
fig.update_layout(
    title=go.layout.Title(
        text="Weights of Top 25 Football Players vs. Average American Males",
        
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Weight (Inches)",
            font=dict(
                size=18,
                color="#7f7f7f"
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Frequency",
            font=dict(
                size=18,
                color="#7f7f7f"
            )
        )
    )
)
fig.show()
