import ipywidgets as ipw
from IPython.display import display,clear_output

# Make the parent folder visible to import my project packages
from os.path import abspath,dirname
import sys
sys.path.insert(0, dirname( dirname( abspath(__file__) ) ) )

# Import my project modules
from calculatePi.pebbles import  MontecarloApprox,plotTheMonteCarloExperiment

# This function returns the widget
def returnPebblessWidget():

    # Set an instance of the MontecarloApprox class
    monte = MontecarloApprox()

    # Set an output widget to display the plot and a button widget to update it
    plot_output = ipw.Output()
    update_button = ipw.Button(description="Click Me!")

    # Add Initial plot to the plot_output
    with plot_output:
        display( plotTheMonteCarloExperiment( [] ) )

    # Add a call back to the button that will update the Montecarlo Approx with a new point
    # and update the scatter plot.
    # Using a decorator
    @update_button.on_click
    def on_button_clicked(b):
        monte.addNewPoint()
        with plot_output:
            clear_output(wait=True)
            display( plotTheMonteCarloExperiment(monte.points) )

    return ipw.VBox(
        children= [
            update_button,
            plot_output
        ]
    )
