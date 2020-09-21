import ipywidgets as ipw
from IPython.display import display,clear_output

from matplotlib.pyplot import close as close_fig

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

    # Set an output widget to display the plot, an HTML widget
    # to display the value of pi and buttons widget to update everything
    plot_output = ipw.Output()
    html_output = ipw.HTML()
    update_button = ipw.Button(description="Add points!")

    # A dropdown widget to choose how many new points are added when
    # update_button is clicked
    dropdown_newpoints = ipw.Dropdown(
        options=[1, 10, 100],
        value=1,
        description='New Points:',
        disabled=False,
    )

    # Add Initial plot to the plot_output
    with plot_output:
        fig = plotTheMonteCarloExperiment( [] )
        display( fig )
        close_fig( fig ) #close figs to liberate memory

    # define initial value for the html_output
    html_message_template ="""<div class="jumbotron">
    <h3>
    π ≈ {pi_value}
    </h3>
    </div>
    """
    html_output.value = html_message_template.format(pi_value = str(monte) )

    # Add a call back to the button that will update the Montecarlo Approx with a new point
    # and update the scatter plot.
    # Using a decorator
    @update_button.on_click
    def on_button_clicked(b):
        # add new point to the Montecarlo experiment
        monte.addNewPoint(dropdown_newpoints.value)
        # Update the plot
        with plot_output:
            clear_output(wait=True)
            fig = plotTheMonteCarloExperiment(monte.points)
            display( fig )
            close_fig( fig ) #close figs to liberate memory
        # Update the widget printing the value of pi
        html_output.value = html_message_template.format(pi_value = str(monte) )

    add_points_widget = ipw.VBox(
        children = [
            dropdown_newpoints,
            update_button
        ],
        layout = ipw.Layout(align_items = 'flex-end')
    )

    return ipw.HBox(
        children= [
            plot_output,
            ipw.VBox(
                children = [
                    add_points_widget,
                    html_output
                ]
            )
        ],
        layout = ipw.Layout(justify_content = 'center')
    )
