# calculate-pi-app

This is app is a didactical example that uses ipywidgets and voila to create an interactive lecture that illustrates how to calculate the value of π with the Archimedes method and with a Montecarlo method.

## Usage

Download or clone the repository running the following line of code in the terminal

    $ git clone https://github.com/Miguel-ASM/calculate-pi-app.git

Create a virtual environment with ```conda```

    $ conda create --prefix ./venv python=3.8

activate the virtual environment and install the dependencies

    $ conda activate venv/
    $ cd calculate-pi-app
    $ pip install -r requirements.txt

In the same folder as ```app.ipynb``` run

    $ voila app.ipynb

a new tab will open in the browser running the app.

## Deployment in Heroku

The app is also deployed in Heroku [here](https://pi-calculation.herokuapp.com/).

## Built with

- [python](https://www.python.org/)
- [jupyter notebook](https://jupyter.org/)
- [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/#)
- [voila](https://voila.readthedocs.io/en/stable/)
