from manim import *

class DerivateAnimation(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 2, 1],
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        axes.to_edge(RIGHT)

        # Create graph of the function log(x)
        graph = axes.plot(lambda x: np.log(x), x_range=[0.1, 5])
        graph.to_edge(RIGHT)

        # Create area under the curve
        secant = axes.get_secant_slope_group(x=1.5, graph=graph, dx=2, dx_label=MathTex(r"\Delta x"), dy_label=r"f(x+\Delta x)-f(x)")
        tangent = axes.get_secant_slope_group(x=1.5, graph=graph, dx=0.0001)
        # Create integral_formula
        funcion_formula = MathTex(r"f(x)=ln(x)")
        derivate_formula = MathTex(r"f'(x) = \lim_{\Delta x \to 0} \frac{f(x+\Delta x) - f(x)}{\Delta x}")
        derivate_formula2 = MathTex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}")

        # Position objects on the screen
        funcion_formula.to_edge(LEFT)
        #suma_riemann_formula.to_edge(DOWN)
        derivate_formula.to_corner(RIGHT + DOWN)
        derivate_formula2.to_corner(RIGHT + DOWN)

        # Animation
        self.wait(1)
        self.play(Create(axes))
        self.play(Write(axes_labels))
        self.wait(1)
        self.play(Write(funcion_formula))
        self.play(Create(graph))
        self.wait(1)
        self.play(Create(secant))
        self.wait(1)
        self.play(Write(derivate_formula))
        
        dx = 1.50
        for _ in range(3):
            secant2 = axes.get_secant_slope_group(x=1.5, graph=graph, dx=dx, dx_label=MathTex(r"\Delta x"), dy_label=r"f(x+\Delta x)-f(x)")
            self.play(Transform(secant, secant2))
            self.wait(1)
            dx = dx - 0.5
        self.play(Transform(secant, tangent))
        self.play(Transform(derivate_formula, derivate_formula2))
        self.wait(2)

class IntegralAnimation(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 2, 1],
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        axes.to_edge(RIGHT)

        # Create graph of the function log(x)
        graph = axes.plot(lambda x: np.log(x), x_range=[0.1, 5])
        graph.to_edge(RIGHT)

        # Create area under the curve
        area = axes.get_area(graph, [1, 4])
        riemann_rect = axes.get_riemann_rectangles(graph, x_range=[1,4], dx=1, input_sample_type='right', fill_opacity=0.4)

        # Create integral_formula
        funcion_formula = MathTex(r"f(x)=ln(x)")
        integral_formula = MathTex(r"\int f(x) \, dx")
        suma_riemann_formula = MathTex(r"\sum_{i=1}^{n} \ f(xi) \Delta x")
        lim_suma_riemann_formula = MathTex(r"\lim_{\Delta x \to 0} \sum_{i=1}^{n} \ f(xi) \Delta x")

        # Position objects on the screen
        funcion_formula.to_edge(LEFT)
        suma_riemann_formula.to_edge(DOWN)
        integral_formula.to_edge(DOWN)
        lim_suma_riemann_formula.to_edge(DOWN)

        # Animation
        self.wait(1)
        self.play(Create(axes))
        self.play(Write(axes_labels))
        self.wait(1)
        self.play(Write(funcion_formula))
        self.play(Create(graph))
        self.wait(1)
        self.play(Write(suma_riemann_formula))
        self.wait(1)
        self.play(Create(riemann_rect))
        self.wait(1)
        
        dx = 0.5
        for i in range(5):
            riemann_rect2 = axes.get_riemann_rectangles(graph, x_range=[1,4], dx=dx, input_sample_type='right', fill_opacity=0.4)
            self.play(Transform(riemann_rect, riemann_rect2))
            self.wait(1)
            if i > 3:
                self.play(Transform(suma_riemann_formula, lim_suma_riemann_formula))
            dx = dx / 2
        self.play(Transform(riemann_rect, area))
        self.wait(1)
        self.play(Transform(suma_riemann_formula, integral_formula))
        self.wait(2)



