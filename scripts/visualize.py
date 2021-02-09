import pandas as pd
import plotly.graph_objects as go

def return_figures():
    results = pd.read_csv('data/result.csv')
    results.timestamp = pd.to_datetime(results.timestamp * 1000000)

    fig = go.Figure()

    fig.add_trace(
        go.Bar(x=results['timestamp'], y=results['download'],
                name='Download',
                marker_color = 'green',
                opacity=0.4,
                marker_line_color='rgb(8,48,107)',
                marker_line_width=2)
    )

    fig.add_trace(
        go.Bar(x=results['timestamp'], y=results['upload'],
                name='Upload',
                marker_color = 'red',
                opacity=0.4,
                marker_line_color='rgb(8,48,107)',
                marker_line_width=2)
    )

    fig.add_trace(
        go.Scatter(x=results['timestamp'], y=results['ping'],
                name='Ping',
                mode='markers',
                marker_symbol='x',
                marker_color = 'blue',
                marker_size=15,
                opacity=0.4)
    )

    layout_fig = dict(title = 'Speedtest Overview',)

    return dict(data = fig, layout = layout_fig)