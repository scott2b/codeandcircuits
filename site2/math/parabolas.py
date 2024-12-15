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