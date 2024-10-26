import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

CB_COLOR_CYCLE = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628', '#984ea3', '#999999', '#e41a1c', '#dede00',
                  '#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628', '#984ea3', '#999999', '#e41a1c', '#dede00']
HATCHINGS = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
MARKERS = ['D', 'o', '^', 'v', 's', 'X', '*', 'D', 'o', '^', 'v', 's', 'X', '*', 'D', 'o', '^', 'v', 's', 'X', '*']
STYLES = ['solid', 'dotted', 'dashed', 'dashdot', (0, (3, 1, 1, 1, 1, 1)), (0, (3, 1, 1, 1))]


def plotting_setup(font_size=12):
    """
    Sets global plot formatting settings
    """
    plt.style.use('seaborn-v0_8-colorblind')
    plt.rcParams['font.size'] = font_size
    rc('text', usetex=False)
    plt.rcParams['font.family'] = 'sans-serif'
    rc('font', **{'family': 'sans-serif', 'sans-serif': ['Arial']})
