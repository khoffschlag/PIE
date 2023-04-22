import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.ticker as ticker


def plot_equations_3D(equations, domain=(0, 15), resolution=1, plot_intersection_only=False, save_fig=None):

    """
    Plot approximations of (multiple) equations

    Args:
        equations (list): A list of functions that take three arguments (x, y, z) and return a boolean value.
                          If you want to connect multiple conditions in one equation - use & instead of 'and' and
                          | instead of 'or'. This is needed, because x,y and z are going to be numpy matrices!
        domain (tuple): A tuple specifying a range [a,b] of the x, y, and z values to evaluate the functions on.
                        CAUTION: a and b have to be greater than 0!!!
        resolution (int): With the default resolution of 1 and a domain range of [a,b] (b-a)+1 values will be calculated
                          and plotted. If you want to have k times the amount, set resolution to k.
                          Example: If you specify a domain of (0,10) this method with resolution=1 would calculate
                          11 evenly spaced values for x, y and z. These values would be
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
                          With resolution=2 we would double the amount of evenly spaced calculated values
                          in the range [a,b].
        plot_intersection_only (bool): Whether to only plot the intersecting region. Otherwise, plot all inequalities.
        save_fig (str): If you want to save the generated plot, specify a path to the location where it should be saved
    """

    # For the case that a user just wanted to plot one equation and forgot to put it into a list
    if not isinstance(equations, list):
        equations = [equations]

    if domain[0] < 0 or domain[1] < 0:
        raise ValueError('The domain specifies a range [a,b] where a and b has to be greater than 0!'
                         + 'You have specified a domain with also negative value(s)')

    # Create a meshgrid that covers the specified domain.
    # The meshgrid is used to create a grid of points in the three-dimensional space that will be used to evaluate
    # the equations.
    x, y, z = np.meshgrid(
        np.linspace(domain[0], domain[1], resolution*((domain[1]-domain[0])+1)),
        np.linspace(domain[0], domain[1], resolution*((domain[1]-domain[0])+1)),
        np.linspace(domain[0], domain[1], resolution*((domain[1]-domain[0])+1)),
        indexing='ij'
    )

    colors = np.empty(x.shape, dtype=object)  # this matrix is going to say which equation will be which color
    possible_colors = mcolors.TABLEAU_COLORS  # We could specify other color palettes but these look alright
    # The list possible_colors_key is useful because I want to use the first color of the list for the first equation,
    # the second color for the second equation and so on
    possible_colors_keys = list(possible_colors.keys())
    if 'tab:red' in possible_colors:
        del possible_colors['tab:red']  # red should only be used for the intersection

    # iteratively the intersection matrix will get ones at the locations where several equations overlap
    intersection = np.ones_like(x)
    # iteratively we add the regions of the equations to the union matrix
    union = np.zeros_like(x)

    for i, func in enumerate(equations):
        # func_result is a matrix containing the results for all the possible defined combinations of x, y and z
        func_result = func(x, y, z)

        # The matrix intersection is used to calculate the set of points that satisfy all equations.
        intersection = np.logical_and(intersection, func_result)

        # The matrix union is used to calculate the set of points that satisfy any of the equations .
        union = np.logical_or(union, func_result)

        # Let's color the equation with color number i
        colors[func_result] = possible_colors[possible_colors_keys[i]]

    # Now we color the intersection with the color red!
    colors[intersection] = 'tab:red'

    # Plotting stuff
    ax = plt.figure().add_subplot(projection='3d')
    ax.set_aspect('equal')

    if plot_intersection_only:
        ax.voxels(intersection, facecolors=colors)
    else:
        ax.voxels(union, facecolors=colors)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ticks = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x / resolution))
    ax.xaxis.set_major_formatter(ticks)
    ax.yaxis.set_major_formatter(ticks)
    ax.zaxis.set_major_formatter(ticks)

    if save_fig is not None:
        plt.savefig(save_fig)

    plt.show()
