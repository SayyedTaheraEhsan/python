class LagrangeInterpolator:
    def __init__(self, x_values, y_values):
        if len(x_values) != len(y_values):
            raise ValueError("x and y values must have the same length.")
        self.x = x_values
        self.y = y_values
        self.n = len(x_values)

    def interpolate(self, x_point):
        """
        Interpolate the y value at a given x_point using Lagrange Polynomial.
        """
        total = 0
        for i in range(self.n):
            term = self.y[i]
            for j in range(self.n):
                if i != j:
                    term *= (x_point - self.x[j]) / (self.x[i] - self.x[j])
            total += term
        return total

    def get_polynomial(self):
        """
        Returns the symbolic Lagrange polynomial using sympy.
        """
        from sympy import symbols, simplify
        x = symbols('x')
        poly = 0
        for i in range(self.n):
            term = self.y[i]
            for j in range(self.n):
                if i != j:
                    term *= (x - self.x[j]) / (self.x[i] - self.x[j])
            poly += term
        return simplify(poly)
