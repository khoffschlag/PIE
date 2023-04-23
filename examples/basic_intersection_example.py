from PIE import plot_algebraic_problem_3D

if __name__ == '__main__':
    def expr_1(x, y, z):
        return (x >= 10) & (y <= 20)

    def expr_2(x, y, z):
        return z <= 30


    plot_algebraic_problem_3D(expressions=[expr_1, expr_2], domain=(0, 50), plot_intersection_only=True)