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
        html_message_template ="""<div class="jumbotron">
        <h3>
        π ≈ {pi_value:.8f}
        </h3>
        </div>
        """
        htmlString = html_message_template.format(pi_value = values_of_pi[n])
        display(ipw.HTML(htmlString))

    slider = ipw.IntSlider(
        min=0,
        step=1,
        max=maxN,
        description = 'n'
    )

    circle = ipw.interactive_output(plot_approximation, {'n':slider})
    pivalue_widget = ipw.interactive_output(return_piapproximation, {'n':slider})

    return ipw.HBox(
        children= [
            circle,
            ipw.VBox(
                children = [
                    slider,
                    pivalue_widget
                ],
                layout = ipw.Layout(align_items = 'flex-end')
            )
        ],
        layout = ipw.Layout(justify_content = 'center')
    )
