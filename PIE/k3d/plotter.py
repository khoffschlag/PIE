import numpy as np
import k3d
import random


def plot_algebraic_problem_3D(expressions, domain=(0, 15), resolution=1, plot_intersection_only=False,
                              colors=None, intersection_color=None, outlines=False, only_random_colors=False):

    """
    Plot approximations of (multiple) equations using k3d library.

    Args:
        expressions (list): A list of functions that take three arguments (x, y, z) and return a boolean value.
        domain (tuple): A tuple specifying a range [a,b] of the x, y, and z values to evaluate the functions on.
        resolution (int): Resolution factor for calculating the meshgrid.
        plot_intersection_only (bool): Whether to only plot the intersecting region. Otherwise, plot all inequalities.
        colors (list): Hex-colors that are used to color the areas.
                       Use first color for first area, second color for second area etc.
                       If None, use default colors.
                       If colors list contain fewer colors than there are expressions, random colors will be generated.
        intersection_color (int): Hex-color that is used for the intersection.
                                  Do not include this color in possible_colors!
                                  If None, use default red for intersection.
        only_random_colors (bool): If set to True, use random colors (except for intersection)
        outlines (bool): Set to True if you want to see the outlines per default.
    """

    if not isinstance(expressions, list):
        expressions = [expressions]

    if domain[0] < 0 or domain[1] < 0:
        raise ValueError('The domain specifies a range [a,b] where a and b has to be greater than 0!'
                         + 'You have specified a domain with also negative value(s)')

    x, y, z = np.meshgrid(
        np.linspace(domain[0], domain[1], resolution * ((domain[1] - domain[0]) + 1)),
        np.linspace(domain[0], domain[1], resolution * ((domain[1] - domain[0]) + 1)),
        np.linspace(domain[0], domain[1], resolution * ((domain[1] - domain[0]) + 1)),
        indexing='ij'
    )

    if colors is None:
        colors = [
            0x6A8A82,  # (Sage Green)
            0x3E4095,  # (Royal Blue)
            0xFFD700,  # (Gold)
            0x7D3C98,  # (Purple)
            0x008080,  # (Teal)
            0xC73866,  # (Berry)
            0xFF5733,  # (Vivid Orange)
            0x00A86B,  # (Emerald Green)
            0xF4A460,  # (Sandy Brown)
        ]

    if only_random_colors:
        colors = []

    delta_c = len(colors) - len(expressions) # if negative -> need to add more colors
    while delta_c < 0:
        colors.append(int(hex(random.randrange(0, 2**24)), 16))
        delta_c += 1

    if intersection_color is None:
        intersection_color = 0xA93C3E  # (Deep Red)

    intersection = np.ones_like(x, dtype=bool)
    union = np.zeros_like(x, dtype=bool)

    plot = k3d.plot(grid_auto_fit=True)
    distinct_areas = []
    for i, func in enumerate(expressions):
        func_result = func(x, y, z)

        distinct_area = func_result.copy()
        distinct_area[union] = False
        distinct_areas.append(distinct_area)

        intersection &= func_result
        union |= func_result

    if not plot_intersection_only:
        # Now we have distinct plots but the original intersection still needs to be deleted
        for i in range(len(distinct_areas)):
            mat = distinct_areas[i]
            mat[intersection] = False
            plot_name = 'Expr #' + str(i+1)
            plot += k3d.voxels(mat.astype(np.uint8), color_map=colors[i], outlines=outlines, name=plot_name)

    plot += k3d.voxels(intersection.astype(np.uint8), color_map=intersection_color, outlines=outlines, name='Intersection')
    plot.display()
