import numpy as np
import matplotlib.pyplot as plt

def width_and_orientation(figwidth=4, aspect_ratio=0.7):
    """
    Generate a Matplotlib plot with dynamic height scaling to maintain aspect ratio.

    Parameters:
        figwidth (float): Desired figure width.
        aspect_ratio (float): Height-to-width ratio (default 0.7 for 4:3 proportions).

    Returns:
        plt: Matplotlib plot.
    """
    plt.style.use('default')
    plt.rcParams.update({
        'figure.dpi': 150,
        'axes.grid': True,
        'grid.alpha': 0.3,
        'lines.linewidth': 0.8,
        'axes.linewidth': 0.5,
        'axes.axisbelow': True,
        'axes.labelsize': 10,
        'axes.titlesize': 12,
        'xtick.labelsize': 6,
        'ytick.labelsize': 6,
        'legend.fontsize': 5
    })

    figheight = figwidth * aspect_ratio  # Automatically calculate height
    x = np.linspace(-10, 10, 200)
    plt.figure(figsize=(figwidth, figheight))  # Dynamically scale height
    plt.axhline(y=0, color='k', linewidth=0.8)
    plt.axvline(x=0, color='k', linewidth=0.8)
    plt.plot(x, x**2, 'b-', linewidth=0.8, label='y = x²: Base parabola')
    plt.plot(x, 2*x**2, 'r-', linewidth=0.8, label='y = 2x²: Narrower (|a| > 1)')
    plt.plot(x, -0.5*x**2, 'g-', linewidth=0.8, label='y = -0.5x²: Wider (|a| < 1), flipped (a < 0)')
    plt.grid(True)
    plt.legend(loc='lower left')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Width and Orientation')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xticks(np.arange(-10, 11, 2))
    plt.yticks(np.arange(-10, 11, 2))
    plt.gca().set_aspect(1.0)  # Enforce equal aspect ratio
    plt.tight_layout()
    for spine in plt.gca().spines.values():
        spine.set_linewidth(0.5)
    return plt


def vertical_shifts(figwidth=4, aspect_ratio=0.7):
    """
    Generate a Matplotlib plot with dynamic height scaling to maintain aspect ratio.

    Parameters:
        figwidth (float): Desired figure width.
        aspect_ratio (float): Height-to-width ratio (default 0.7 for 4:3 proportions).

    Returns:
        plt: Matplotlib plot.
    """
    figheight = figwidth * aspect_ratio  # Automatically calculate height
    x = np.linspace(-10, 10, 200)

    plt.style.use('default')
    plt.rcParams.update({
        'figure.dpi': 150,
        'axes.grid': True,
        'grid.alpha': 0.3,
        'lines.linewidth': 0.8,
        'axes.linewidth': 0.5,
        'axes.axisbelow': True,
        'axes.labelsize': 10,
        'axes.titlesize': 12,
        'xtick.labelsize': 6,
        'ytick.labelsize': 6,
        'legend.fontsize': 5
    })

    plt.figure(figsize=(figwidth, figheight))  # Set figure size dynamically
    plt.axhline(y=0, color='k', linewidth=0.8)
    plt.axvline(x=0, color='k', linewidth=0.8)
    plt.plot(x, x**2, 'b-', linewidth=0.8, label='y = x²: Base parabola')
    plt.plot(x, x**2 + 2, 'r-', linewidth=0.8, label='y = x² + 2: Shift up')
    plt.plot(x, x**2 - 2, 'g-', linewidth=0.8, label='y = x² - 2: Shift down')
    plt.grid(True)
    plt.legend(loc='lower left')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Vertical Shifts')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xticks(np.arange(-10, 11, 2))
    plt.yticks(np.arange(-10, 11, 2))
    plt.tight_layout()
    for spine in plt.gca().spines.values():
        spine.set_linewidth(0.5)

    return plt


def vertex_vertical_shifts(figwidth=4, aspect_ratio=0.7):
    """
    Generate a Matplotlib plot with dynamic height scaling to maintain aspect ratio.

    Parameters:
        figwidth (float): Desired figure width.
        aspect_ratio (float): Height-to-width ratio (default 0.7 for 4:3 proportions).

    Returns:
        plt: Matplotlib plot.
    """
    figheight = figwidth * aspect_ratio  # Automatically calculate height
    x = np.linspace(-10, 10, 200)

    plt.style.use('default')
    plt.rcParams.update({
        'figure.dpi': 150,
        'axes.grid': True,
        'grid.alpha': 0.3,
        'lines.linewidth': 0.8,
        'axes.linewidth': 0.5,
        'axes.axisbelow': True,
        'axes.labelsize': 10,
        'axes.titlesize': 12,
        'xtick.labelsize': 6,
        'ytick.labelsize': 6,
        'legend.fontsize': 5
    })

    plt.figure(figsize=(figwidth, figheight))  # Dynamic figure size
    plt.axhline(y=0, color='k', linewidth=0.8)
    plt.axvline(x=0, color='k', linewidth=0.8)
    plt.plot(x, x**2, 'b-', linewidth=0.8, label='y = x²: Base parabola')
    plt.plot(x, x**2 + 2, 'r-', linewidth=0.8, label='y = x² + 2: Shift up')
    plt.plot(x, x**2 - 2, 'g-', linewidth=0.8, label='y = x² - 2: Shift down')
    plt.grid(True)
    plt.legend(loc='lower left')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Vertex Vertical Shifts')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xticks(np.arange(-10, 11, 2))
    plt.yticks(np.arange(-10, 11, 2))
    plt.tight_layout()
    for spine in plt.gca().spines.values():
        spine.set_linewidth(0.5)

    return plt


def vertex_horizontal_shifts(figwidth=4, aspect_ratio=0.7):
    """
    Generate a Matplotlib plot with dynamic height scaling to maintain aspect ratio.

    Parameters:
        figwidth (float): Desired figure width.
        aspect_ratio (float): Height-to-width ratio (default 0.7 for 4:3 proportions).

    Returns:
        plt: Matplotlib plot.
    """
    figheight = figwidth * aspect_ratio  # Automatically calculate height
    x = np.linspace(-10, 10, 200)

    plt.style.use('default')
    plt.rcParams.update({
        'figure.dpi': 150,
        'axes.grid': True,
        'grid.alpha': 0.3,
        'lines.linewidth': 0.8,
        'axes.linewidth': 0.5,
        'axes.axisbelow': True,
        'axes.labelsize': 10,
        'axes.titlesize': 12,
        'xtick.labelsize': 6,
        'ytick.labelsize': 6,
        'legend.fontsize': 5
    })

    plt.figure(figsize=(figwidth, figheight))  # Dynamic figure size
    plt.axhline(y=0, color='k', linewidth=0.8)
    plt.axvline(x=0, color='k', linewidth=0.8)
    plt.plot(x, x**2, 'b-', linewidth=0.8, label='y = x²: Base parabola')
    plt.plot(x, (x - 2)**2, 'r-', linewidth=0.8, label='y = (x-2)²: Shift right')
    plt.plot(x, (x + 2)**2, 'g-', linewidth=0.8, label='y = (x+2)²: Shift left')
    plt.grid(True)
    plt.legend(loc='lower left')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Vertex Horizontal Shifts')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xticks(np.arange(-10, 11, 2))
    plt.yticks(np.arange(-10, 11, 2))
    plt.tight_layout()
    for spine in plt.gca().spines.values():
        spine.set_linewidth(0.5)

    return plt

import plotly.graph_objects as go
import numpy as np


def x__plotly_width_and_orientation():
    # Generate a smooth x range
    x = np.linspace(-10, 10, 1000)
    # Create the plot
    fig = go.Figure()
    # Add the parabola traces
    fig.add_trace(go.Scatter(
        x=x, y=x**2, mode='lines',
        name='y = x²', line=dict(color='blue', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=x, y=2*x**2, mode='lines',
        name='y = 2x²', line=dict(color='red', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=x, y=-0.5*x**2, mode='lines',
        name='y = -0.5x²', line=dict(color='green', width=2)
    ))
    # Set the axis ranges, grid lines, and darker 0 axes
    fig.update_layout(
        title="Width and Orientation",
        xaxis=dict(
            title="x",
            range=[-10, 10],
            tickmode='linear',
            dtick=1,
            showgrid=True, gridcolor='lightgray',
            zeroline=True, zerolinecolor='black', zerolinewidth=2  # Darker 0 axis
        ),
        yaxis=dict(
            title="y",
            range=[-10, 10],
            tickmode='linear',
            dtick=1,
            showgrid=True, gridcolor='lightgray',
            zeroline=True, zerolinecolor='black', zerolinewidth=2  # Darker 0 axis
        ),
        template="plotly_white",
        showlegend=True
    )
    return fig


import plotly.graph_objects as go
import numpy as np

def plotly_width_and_orientation(export_path=None):
    """
    Generate a Plotly plot for 'Width and Orientation'.

    Parameters:
        export_path (str): Path to export the static image (e.g., 'output.png').
                           If None, the plot will be displayed interactively.
    """
    x = np.linspace(-10, 10, 1000)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=x**2, mode='lines',
        name='y = x²', line=dict(color='blue', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=x, y=2*x**2, mode='lines',
        name='y = 2x²', line=dict(color='red', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=x, y=-0.5*x**2, mode='lines',
        name='y = -0.5x²', line=dict(color='green', width=2)
    ))
    fig.update_layout(
        title="Width and Orientation",
        xaxis=dict(
            title="x",
            range=[-10, 10],
            tickmode='array',
            tickvals=list(range(-10, 11, 2)),  # Even-numbered ticks from -10 to 10
            showgrid=True, gridcolor='lightgray',
            zeroline=True, zerolinecolor='black', zerolinewidth=2
        ),
        yaxis=dict(
            title="y",
            range=[-10, 10],
            tickmode='array',
            tickvals=list(range(-10, 11, 2)),  # Even-numbered ticks from -10 to 10
            showgrid=True, gridcolor='lightgray',
            zeroline=True, zerolinecolor='black', zerolinewidth=2
        ),
        template="plotly_white",
        showlegend=True
    )
    if export_path:
        fig.write_image(export_path)
    else:
        fig.show()


def plotly_vertical_shifts(export_path=None):
    """
    Generate a Plotly plot for 'Width and Orientation'.

    Parameters:
        export_path (str): Path to export the static image (e.g., 'output.png').
                           If None, the plot will be displayed interactively.
    """
    x = np.linspace(-10, 10, 1000)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=x**2, mode='lines',
        name='y = x²', line=dict(color='blue', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=x, y=x**2+2, mode='lines',
        name='y = x² + 2', line=dict(color='red', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=x, y=x**2-2, mode='lines',
        name='y = x² - 2', line=dict(color='green', width=2)
    ))
    fig.update_layout(
        title="Vertical Shifts",
        xaxis=dict(
            title="x",
            range=[-10, 10],
            tickmode='array',
            tickvals=list(range(-10, 11, 2)),  # Even-numbered ticks from -10 to 10
            showgrid=True, gridcolor='lightgray',
            zeroline=True, zerolinecolor='black', zerolinewidth=2
        ),
        yaxis=dict(
            title="y",
            range=[-10, 10],
            tickmode='array',
            tickvals=list(range(-10, 11, 2)),  # Even-numbered ticks from -10 to 10
            showgrid=True, gridcolor='lightgray',
            zeroline=True, zerolinecolor='black', zerolinewidth=2
        ),
        template="plotly_white",
        showlegend=True
    )
    if export_path:
        fig.write_image(export_path)
    else:
        fig.show()

import plotly.graph_objects as go
import numpy as np

def interactive_width_and_orientation():
    """
    Generate an interactive Plotly plot with properly rendered sliders 
    for parameters a, b, and c, avoiding layout issues.
    """
    # Define the x range
    x = np.linspace(-10, 10, 500)

    # Function to calculate y values
    def parabola(a, b, c, x):
        return a * x**2 + b * x + c

    # Default parameters
    a_init, b_init, c_init = 1, 0, 0
    # Create figure with the initial parabola
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=parabola(a_init, b_init, c_init, x),
        mode="lines",
        line=dict(color="blue", width=2),
        name=f"y = {a_init}x² + {b_init}x + {c_init}"
    ))
    # Slider ranges
    a_values = np.linspace(-2, 2, 21)
    b_values = np.linspace(-5, 5, 21)
    c_values = np.linspace(-10, 10, 21)
    # Steps for each slider
    steps_a = [dict(
        method="restyle",
        args=[{"y": [parabola(a, b_init, c_init, x)]}],
        label=f"{a:.1f}"
    ) for a in a_values]
    steps_b = [dict(
        method="restyle",
        args=[{"y": [parabola(a_init, b, c_init, x)]}],
        label=f"{b:.1f}"
    ) for b in b_values]
    steps_c = [dict(
        method="restyle",
        args=[{"y": [parabola(a_init, b_init, c, x)]}],
        label=f"{c:.1f}"
    ) for c in c_values]
    # Combine sliders with independent control
    sliders = [
        dict(
            active=10,
            currentvalue={"prefix": "a = ", "font": {"size": 14}},
            pad={"t": 30},
            steps=steps_a
        ),
        dict(
            active=10,
            currentvalue={"prefix": "b = ", "font": {"size": 14}},
            pad={"t": 30},
            steps=steps_b
        ),
        dict(
            active=10,
            currentvalue={"prefix": "c = ", "font": {"size": 14}},
            pad={"t": 30},
            steps=steps_c
        )
    ]
    # Update layout with sliders and clean annotation
    fig.update_layout(
        title="Interactive Parabola: y = ax² + bx + c",
        sliders=sliders,
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(range=[-10, 10]),
        yaxis=dict(range=[-20, 20]),
        template="plotly_white"
    )
    return fig