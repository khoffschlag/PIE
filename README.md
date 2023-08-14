# PIE: Plot Inequalities and Equations

PIE is a Python module that allows you to plot inequalities and equations as well as the intersections between them.

**To see PIE in action, see: https://github.com/khoffschlag/PIE/blob/main/examples/basic_examples_k3d.ipynb**

**Please note that PIE can currently only plot in the
first quadrant where the x/y/z-axis values are greater than or equal to zero.
Also are the generated plots are only approximations and maybe slightly misaligned.**

## Installation

Before installing PIE, ensure that you have Git, Python 3, and virtualenv for Python 3 installed on your computer.

To clone the repository, open your terminal and run the following command:

> git clone https://github.com/khoffschlag/PIE.git

Next, navigate to the cloned directory using the command:

> cd PIE


Create a virtual environment for your project using your preferred virtual environment manager.
For example, using venv:

> python3 -m venv env

Activate the virtual environment usin:

> source env/bin/activate


Install PIE using:

> pip install .


After installing the packages and activating the virtual environment, you can run the scripts or use the module,
as shown in the examples/basic_examples_k3d.ipynb file.

Please note that the created virtual environment needs to be activated in the terminal where you wish to run the scripts.
If you opened a new terminal, you may have to go into the PIE directory and run the source command from the installation
process again.
