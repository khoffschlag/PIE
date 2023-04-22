from PIE import plot_equations_3D

if __name__ == '__main__':
    def eq_1(x, y, z):
        return (x >= 10) & (y <= 20)

    def eq_2(x, y, z):
        return z <= 30

    plot_equations_3D(
        equations=[eq_1, eq_2],
        domain=(0, 10),
        plot_intersection_only=False
    )