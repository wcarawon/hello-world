import plotly.graph_objects as go

fig = go.Figure(data=go.Bar(x=['h', 'e', 'l', 'o', 'w', 'r', 'd'], y=[1, 1, 3, 2, 1, 1, 1]))
fig.update_layout(title='Letter Frequency in "Hello World"')
fig.write_html('first_figure.html', auto_open=True)
