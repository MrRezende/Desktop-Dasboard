from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from firebase.data_access import get_data

def create_graph():
    # Obter dados do Firebase
    data = get_data()

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Simular dados para um gráfico de barras
    categories = data.keys()
    values = data.values()

    ax.bar(categories, values)
    ax.set_title('Gráfico de Barras')
    ax.set_xlabel('Categorias')
    ax.set_ylabel('Valores')

    canvas = FigureCanvas(fig)
    return canvas
