#import ipywidgets
import ipywidgets as ipw

from IPython.display import display

#make the parent folder visible
from os.path import abspath,dirname
import sys
sys.path.insert(0, dirname( dirname( abspath(__file__) ) ) )

#import calculatePi.archimedes
from calculatePi.archimedes import  returnPiUpToN,plotTheApproximationPolygon,returnPointsUpToN

def returnArchimedesWidget(maxN):
    points = returnPointsUpToN(maxN)
    values_of_pi = returnPiUpToN(maxN)

    def plot_approximation(n):
        display( plotTheApproximationPolygon(points[n]) )

    def return_piapproximation(n):
        htmlString = '<h3>The approximate value of pi is {}</h3>'.format(values_of_pi[n])
        display(ipw.HTML(htmlString))

    slider = ipw.IntSlider(
        min=0,
        step=1,
        max=maxN,
        description = 'n'
    )

    circle = ipw.interactive_output(plot_approximation, {'n':slider})
    pivalue_widget = ipw.interactive_output(return_piapproximation, {'n':slider})

    return ipw.VBox(
        children= [
            ipw.HBox(children=[slider,pivalue_widget]),
            circle
        ]
    )
