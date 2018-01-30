# -*- coding: utf-8 -*-
"""
CPEM 2018 paper figure 3
"""
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt

def exp_matplotlib_cpem2018_fig3_run():
    ####### input data ######
    #S21 measured by HP8530A
    d8530A = """-7.96
    -11.59
    -14.94
    -17.89
    -17.72
    -20.50
    -24.55
    -27.18
    -28.34
    -29.96
    -33.00
    -33.99
    -35.86
    -38.78
    -34.12
    -31.56
    -39.85
    -50.89"""
    d8530A=np.loadtxt(StringIO(d8530A))
    #S21 measured by DLOMS PNA
    dPNA = """-1.08
    0.73
    -1.77
    -3.82
    -5.68
    -7.57
    -10.69
    -11.90
    -12.26
    -14.47
    -16.19
    -16.63
    -17.23
    -19.40
    -11.95
    -8.18
    -16.63
    -27.11"""
    dPNA=np.loadtxt(StringIO(dPNA))
    freq = np.linspace(1,18,18) # Frequency GHz
    diff = dPNA - d8530A
    ################### end input###############

    fig1, ax1 = plt.subplots()
    ax1.plot(freq, d8530A, 'k--', label='Distributed mixer')
    ax1.plot(freq, dPNA, 'b-', label='Distributed LO and mixer')
    ax1.set_xlabel('Frequency [GHz]')
    ax1.set_ylabel(r'Insertion Loss - $S_{21}$ [dB]')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(freq, diff, 'r-.', label='Difference')
    ax2.set_ylabel('Difference [dB]', color='k')
    ax2.tick_params('y', colors='k')

    ax1.set_xlim(xmin=1, xmax=18)

    fig1.tight_layout()
    ax1.legend(loc='upper center', frameon=False)
    ax2.legend(loc='lower center', frameon=False)
    plt.show()
    #fig1.savefig('Fig3.eps',format='eps')
    #fig1.savefig('Fig3_wsl.png',dpi=1200)

