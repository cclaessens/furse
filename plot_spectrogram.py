# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:28:35 2016

@author: claessen
"""

import matplotlib.pyplot as plt

def plot_spectrogram(X, Y, Z, gidno, clabel):
    
    plt.figure(figno)
    plt.contourf(X, Y, Z, 20)
    cbar = plt.colorbar()
    cbar.ax.set_ylabel(clabel)

    plt.title("spectrogam")
    plt.xlabel("time /s")
    plt.ylabel("frequency /Hz")
    plt.show()
    
    return