import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
from IPython.display import display

def cuadratica(a,b,c,x):
    return a*x**2 + b*x + c

def indirecta(a,b,c):
    return - b**2/(4*a) + c

def plot(a,b):
    c=1
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    xo=-b/(2*a)
    yo=- b**2/(4*a) + c
    x = np.arange(-10,10,0.001)
    
    def ploti(a,b,z):
        c=1
        xo=-b/(2*a)
        yo=- b**2/(4*a) + c
        x = np.arange(-1,20,0.01)
        axs[z].plot(x, cuadratica(x, b, c, xo),c='black',lw=0.5,alpha=.2)

    y=np.arange(0,10,0.25)

    for i in range(len(y)):
        ploti(y[i],b,1)
        
    def plotii(a,b,z):
        c=1
        xo=-b/(2*a)
        yo=- b**2/(4*a) + c
        x = np.arange(-1,20,0.01)
        axs[z].plot(x, cuadratica(a, x, c, xo),c='black',lw=0.5,alpha=.2)
        
    for i in range(len(y)):
        plotii(a,y[i],2)
    
    axs[1].plot(x, indirecta(x, b, c),lw=2,c='red')
    axs[2].plot(x, indirecta(a, x, c),lw=2,c='red')
    
    axs[0].plot(x, cuadratica(a, b, c, x))
    axs[0].plot(xo, yo,'ro')
    axs[0].set_xlabel(r'$x$')
    axs[0].set_ylabel(r'$f(x)$')
    axs[0].set_xlim(-10,10)
    axs[0].set_ylim(-10,10)
    axs[0].set_xticks([])
    axs[0].set_yticks([])

    axs[1].plot(x, cuadratica(x, b, c, xo))
    axs[1].plot(a, yo,'ro')
    axs[1].set_xlim(0,10)
    axs[1].set_ylim(-10,10)
    axs[1].set_xlabel(r'$a$')
    axs[1].set_ylabel(r'$f^*(a)$')
    axs[1].set_xticks([])
    axs[1].set_yticks([])

    axs[2].plot(x, cuadratica(a, x, c, xo))
    axs[2].plot(b, yo,'ro')
    axs[2].set_xlim(0,10)
    axs[2].set_ylim(-10,10)
    axs[2].set_xlabel(r'$b$')
    axs[2].set_ylabel(r'$f^*(b)$')
    axs[2].set_xticks([])
    axs[2].set_yticks([])

    plt.show()

a_slider = widgets.FloatSlider(value=5, min=1, max=10, step=1, description='a:')
b_slider = widgets.FloatSlider(value=5, min=1, max=10, step=1, description='b:')

widgets.interactive(plot, a=a_slider, b=b_slider)
