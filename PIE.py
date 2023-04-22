import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def plot_equations_3D(equations, domain=(0, 15), plot_intersection_only=False, save_fig=None):

    """
    Plot (multiple) equations

    Args:
        equations (list): A list of functions that take three arguments (x, y, z) and return a boolean value.
                          If you want to connect multiple conditions in one equation - use & instead of 'and' and
                          | instead of 'or'. This is needed, because x,y and z are going to be numpy matrices!
        domain (tuple): A tuple specifying a range [a,b] of the x, y, and z values to evaluate the inequalities on.
                        The stepsize is 1.
                        CAUTION: The specified range has to be in R+ (no negative numbers)
        plot_intersection_only (bool): Whether to only plot the intersecting region. Otherwise, plot all inequalities.
        save_fig (str): If you want to save the generated plot, specify a path to the location where it should be saved
    """

    # Create a meshgrid that covers the specified domain.
    # The meshgrid is used to create a grid of points in the three-dimensional space that will be used to evaluate
    # the equations.
    x, y, z = np.meshgrid(
        np.linspace(domain[0], domain[1], domain[1]-domain[0]),
        np.linspace(domain[0], domain[1], domain[1]-domain[0]),
        np.linspace(domain[0], domain[1], domain[1]-domain[0]),
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
    ax.set_aspect('auto')

    if plot_intersection_only:
        ax.voxels(intersection, facecolors=colors)
    else:
        ax.voxels(union, facecolors=colors)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([domain[0], domain[1]])
    ax.set_ylim([domain[0], domain[1]])
    ax.set_zlim([domain[0], domain[1]])
    plt.show()
    if save_fig is not None:
        plt.savefig(save_fig)
