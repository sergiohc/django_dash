import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import random

from django_plotly_dash import DjangoDash

app = DjangoDash('dashboard')

df = px.data.iris()
fig = px.scatter(
    df, x="sepal_length", y="sepal_width", color="species", title="Updating Title Color"
)

# Define o layout da aplicação
app.layout = html.Div(
    style={'height': '100vh', 'width': '100vw', 'display': 'flex', 'flexDirection': 'column'},  # Estilos para ocupar 100% da tela
    children=[
        html.Button("Update Graph Color", id="update-color-button-2", style={'flex': '0 1 auto', 'margin': '10px'}),  # Botão com layout flexível
        dcc.Graph(
            figure=fig,
            id="my-fig",
            style={'flex': '1 1 auto', 'height': '100%', 'width': '100%'}  # Define o gráfico para preencher o restante da tela
        ),
    ]
)

@app.callback(
    Output("my-fig", "figure"),
    Input("update-color-button-2", "n_clicks")
)
def update_graph_color(n_clicks):
    if n_clicks is None:
        return fig

    # Definindo uma nova cor aleatória para o título
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    new_color = f"rgb({red}, {green}, {blue})"

    # Atualizando a cor do título no layout do gráfico
    updated_fig = fig
    updated_fig.update_layout(title_font_color=new_color)

    return updated_fig
