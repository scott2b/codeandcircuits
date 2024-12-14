import numpy as np
import matplotlib.pyplot as plt

def create_response_plot(zeta, wn, static=True):
    t = np.linspace(0, 10, 1000)
    response = np.exp(-zeta * wn * t) * np.cos(wn * np.sqrt(np.maximum(0, 1 - zeta**2)) * t)
    
    plt.figure(figsize=(8, 4) if static else (6, 4))
    plt.plot(t, response, 'b-')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(f'Response (ζ = {zeta}, ωn = {wn})')
    plt.ylim(-1, 1)
    return plt
