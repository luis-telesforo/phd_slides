import numpy as np
from manim import *
from manim import TexTemplate
from manim_slides.slide import Slide

my_template = TexTemplate()
my_template.add_to_preamble(r"\usepackage[svgnames]{xcolor}")
my_template.add_to_preamble(r"\usepackage{amsthm}"
                            r"\usepackage{amsmath}"
                            r"\usepackage{amsfonts}"
                            r"\usepackage{amssymb}")
my_template.add_to_preamble(r"\usepackage{tikz}")
my_template.add_to_preamble(r"\usetikzlibrary{calc}")

my_template.add_to_preamble(
    r"\tikzstyle{zero}=[circle,draw=black,fill=white,inner sep=0pt,minimum size=2.5mm]	\tikzstyle{one}=[circle,"
    r"draw=black,fill=black,inner sep=0pt,minimum size=2.5mm]	\tikzstyle{two}=[circle,draw=black,fill=gray,"
    r"inner sep=0pt,minimum size=2.5mm] ")

config.background_color = WHITE

# colors
ROSA = "#CC79A7"
NARANJA = "#E69F00"
AZUL = "#56B4E9"
VERDOSO = "#0072B2"


class BlackSlide(Slide, Scene):
    def construct(self):
        Text.set_default(color='BLACK', font_size=30)
        Mobject.set_default(color='BLACK')

    def create_title(self, title):
        self.wait_time_between_slides = .1
        self.wipe(None, title, direction=RIGHT)
        self.next_slide()
        self.wait_time_between_slides = 0

    def finish(self):
        all_mobjects = VGroup()
        for x in self.mobjects:
            if isinstance(x, VMobject):
                all_mobjects.add(x)
        # for x in triangle_tex:
        #     if not isinstance(x, VMobject):
        #         print(type(x))
        self.wipe(all_mobjects, None)


def fade_text(slide, text):
    slide.play(FadeIn(text))
    slide.next_slide()
    slide.play(FadeOut(text))


def examples_pseudospheres(slide, indicate):
    # EJEMPLO K_3_4
    # k_3
    k_3_blue = (r"\begin{tikzpicture}\foreach\t in {1,2,3,4}{\node (\t) at  (1,\t) {};}\foreach \t/\l in {1/A,"
                r"2/B,3/C}{\node (\l) at  (4,\t+.5) [zero] {};}\end{tikzpicture}")
    k_3 = SingleStringMathTex(k_3_blue, tex_template=my_template, stroke_width=3, fill_opacity=1,
                              should_center=True, color=AZUL)
    slide.play(Write(k_3.shift(RIGHT * 2.1)))
    slide.next_slide()
    # k_4
    k_4_red = (r"\begin{tikzpicture}\foreach \t in {1,2,3,4}{\node (\t) at  (1,\t)[zero] {};}\foreach \t/\l in {"
               r"1/A,2/B,3/C}{\node (\l) at  (4,\t+.5) {};}\end{tikzpicture}")
    k_4 = SingleStringMathTex(k_4_red, tex_template=my_template, stroke_width=3, fill_opacity=1,
                              should_center=True, color=ROSA)
    slide.play(Write(k_4.shift(LEFT * 2.1)))
    slide.next_slide()
    # k_3_4
    k_3_4_lines = (r"\begin{tikzpicture}\foreach \t in {1,2,3,4}	{\node  (\t) at  (1,\t) {};}\foreach \t/\l in {"
                   r"1/A,2/B,3/C} {\node (\l) at  (4,\t+.5) {};}\foreach \x in {1,2,3,4}\foreach \l in {A,B,"
                   r"C} \filldraw(\x)--(\l);\end{tikzpicture}")
    k_3_4 = SingleStringMathTex(k_3_4_lines, tex_template=my_template, stroke_width=3, fill_opacity=0, color=GREY)
    k_3_4.set_z_index(-1)
    slide.play(Write(k_3_4))
    slide.next_slide()
    slide.play(FadeOut(k_3_4), FadeOut(k_3), FadeOut(k_4))
    # EJMPLO K_2_2_3
    # lineas
    k_2_2_3_lineas_1 = (r"\begin{tikzpicture}[scale=3]\node (1) at (2,3) {};\node [white] (a) at (2.5,3.2) {};\node ("
                        r"x) at (1,3) {};\node (0) at (2.2,2.5)  {};	\node [white] (b) at (1.5,2)  {};	\node (y) "
                        r"at (2.1,2.7)  {};	\node (z) at (3,2)  {};	\draw[dotted](a) -- (0); \draw [dotted](b) -- ("
                        r"0);	\draw[dotted](1)-- (a);		\draw[dotted](b)-- (1);	\end{tikzpicture}")
    k_2_2_3_lineas_2 = (r"\begin{tikzpicture}[scale=3]\node (1) at (2,3) {};\node [white] (a) at (2.5,3.2) {};\node ("
                        r"x) at (1,3) {};\node (0) at (2.2,2.5)  {};	\node [white] (b) at (1.5,2)  {};	\node (y) "
                        r"at (2.1,2.7)  {};	\node (z) at (3,2)  {};	\draw[opacity=0.2](x)--(b);	\draw[dotted]("
                        r"0)--(x);	\draw[opacity=0.2](x)--(a);	\draw ("
                        r"x)--(1);	\draw (x)--(1);	\draw (z)--(1);	\draw ("
                        r"z)--(a);	\draw[opacity=0.2](z)--(b);	\draw [dotted](0)--(z);	\draw[dotted](y)-- (a);"
                        r"\draw[dotted](y)-- (1);	\draw[dotted](y)-- (0);	\draw["
                        r"dotted](y)-- (b);	\end{tikzpicture}")
    lines = SingleStringMathTex(k_2_2_3_lineas_1, tex_template=my_template, stroke_width=3, fill_opacity=1,
                                should_center=True, color=GREY)
    lines.set_z_index(-1)
    lines2 = SingleStringMathTex(k_2_2_3_lineas_2, tex_template=my_template, stroke_width=3, fill_opacity=1,
                                 should_center=True, color=GREY)
    lines2.set_z_index(-1)
    # triangulos
    triangle1_tex = (r"\begin{tikzpicture}[scale=3]\node (1) at (2,3) {};\node [white] (a) at (2.5,3.2) {};\node ("
                     r"x) at (1,3) {};	\node (0) at (2.2,2.5)  {};	\node [white] (b) at (1.5,2)  {};	\node (y) "
                     r"at (2.1,2.7)  {};	\node (z) at (3,2)  {};    \draw (1)-- (a)--(x)--(1);	\draw (1) -- ("
                     r"b)--(x)--(1);	\draw(1)-- (a)--(z)--(1);	\draw(1) -- (b)--(z)--(1);	\fill[gray,"
                     r"opacity=0.2](2,3)--(2.5,3.2)--(1,3)--(2,3);\end{tikzpicture}")
    triangle1 = SingleStringMathTex(triangle1_tex, tex_template=my_template, stroke_width=3, fill_opacity=.5,
                                    should_center=True, color=GREY_A)
    triangle1.set_z_index(0)
    triangle1_r = triangle1.copy()
    triangle2_tex = (r"\begin{tikzpicture}[scale=3]    \node (1) at (2,3) {};	\node [white] (a) at (2.5,"
                     r"3.2) {};	\node (x) at (1,3) {};	\node (0) at (2.2,2.5)  {};	\node [white] (b) at (1.5,"
                     r"2)  {};	\node (y) at (2.1,2.7)  {};	\node (z) at (3,2)  {};    \draw (1)-- (a)--(x)--("
                     r"1);	\draw (1) -- (b)--(x)--(1);	\draw(1)-- (a)--(z)--(1);	\draw(1) -- (b)--(z)--(1);	"
                     r"\fill[black,opacity=0.2](2,3)--(1.5,2)--(1,3)--(2,3);	\end{tikzpicture}")
    triangle2 = SingleStringMathTex(triangle2_tex, tex_template=my_template, stroke_width=3, fill_opacity=.5,
                                    should_center=True, color=GREY)
    triangle2.set_z_index(0)
    triangle2_r = triangle2.copy()
    triangle3_tex = (r"\begin{tikzpicture}[scale=3]    \node (1) at (2,3) {};	\node [white] (a) at (2.5,"
                     r"3.2) {};	\node (x) at (1,3) {};	\node (0) at (2.2,2.5)  {};	\node [white] (b) at (1.5,"
                     r"2)  {};	\node (y) at (2.1,2.7)  {};	\node (z) at (3,2)  {};    \draw (1)-- (a)--(x)--("
                     r"1);	\draw (1) -- (b)--(x)--(1);	\draw(1)-- (a)--(z)--(1);	\draw(1) -- (b)--(z)--(1);	"
                     r"\fill[black,opacity=0.2](2,3)--(2.5,3.2)--(3,2)--(2,3); \end{tikzpicture}")
    triangle3 = SingleStringMathTex(triangle3_tex, tex_template=my_template, stroke_width=3, fill_opacity=.5,
                                    should_center=True, color=GREY)
    triangle3.set_z_index(0)
    triangle3_r = triangle3.copy()
    triangle4_tex = (r"\begin{tikzpicture}[scale=3]   \node (1) at (2,3) {};	\node [white] (a) at (2.5,3.2) {};	"
                     r"\node (x) at (1,3) {};	\node (0) at (2.2,2.5)  {};	\node [white] (b) at (1.5,"
                     r"2)  {};	\node (y) at (2.1,2.7)  {};	\node (z) at (3,2)  {};    \draw (1)-- (a)--(x)--("
                     r"1);	\draw (1) -- (b)--(x)--(1);	\draw(1)-- (a)--(z)--(1);	\draw(1) -- (b)--(z)--(1);	"
                     r"\fill[gray,opacity=0.2](2,3)--(1.5,2)--(3,2)--(2,3);	\end{tikzpicture}")
    triangle4 = SingleStringMathTex(triangle4_tex, tex_template=my_template, stroke_width=3, fill_opacity=.5,
                                    should_center=True, color=GREY_A)
    triangle4.set_z_index(1)
    triangle4_r = triangle4.copy()
    # Vertices
    zero0_tex = (r"\begin{tikzpicture}[scale=3]	\node (1) at (2,3) {};	\node [white] (a) at (2.5,3.2) {};	\node "
                 r"(x) at (1,3)  {};	\node (0) at (2.2,2.5) [zero] {};	\node [white] (b) at (1.5,"
                 r"2)  {};	\node (y) at (2.1,2.7)  {};	\node (z) at (3,2) {};	\end{tikzpicture}")
    zero0 = SingleStringMathTex(zero0_tex, tex_template=my_template, stroke_width=3, fill_opacity=1,
                                should_center=True, color=BLACK)
    zero0.set_z_index(0)
    zero0_r = zero0.copy()
    zero1_tex = (r"\begin{tikzpicture}[scale=3]	\node (1) at (2,3) [zero] {};	\node [white] (a) at (2.5,"
                 r"3.2) {};	\node (x) at (1,3)  {};	\node (0) at (2.2,2.5) {};	\node [white] (b) at (1.5,"
                 r"2)  {};	\node (y) at (2.1,2.7)  {};	\node (z) at (3,2) {};\end{tikzpicture}")
    zero1 = SingleStringMathTex(zero1_tex, tex_template=my_template, stroke_width=3, fill_opacity=1,
                                should_center=True, color=BLACK)
    zero1.set_z_index(2)
    zero1_r = zero1.copy()
    twoy_tex = (r"\begin{tikzpicture}[scale=3]	\node (1) at (2,3)  {};	\node [white] (a) at (2.5,3.2)  {};	\node "
                r"(x) at (1,3)  {};	\node (0) at (2.2,2.5) {};	\node [white] (b) at (1.5,2)  {};	\node (y) at ("
                r"2.1,2.7) [two] {};	\node (z) at (3,2)  {};	\end{tikzpicture}")
    twoy = SingleStringMathTex(twoy_tex, tex_template=my_template, stroke_width=3, fill_opacity=1,
                               should_center=True, color=AZUL)
    twoy.set_z_index(0)
    twoy_r = twoy.copy()
    twoxz_tex = (r"\begin{tikzpicture}[scale=3]	\node (1) at (2,3)  {};	\node [white] (a) at (2.5,3.2)  {};	\node "
                 r"(x) at (1,3) [two] {};	\node (0) at (2.2,2.5) {};	\node [white] (b) at (1.5,2)  {};	\node "
                 r"(y) at (2.1,2.7)  {};	\node (z) at (3,2) [two] {};	\end{tikzpicture}")
    twoxz = SingleStringMathTex(twoxz_tex, tex_template=my_template, stroke_width=3, fill_opacity=1,
                                should_center=True, color=AZUL)
    twoxz.set_z_index(2)
    twoxz_r = twoxz.copy()
    one_tex = (r"\begin{tikzpicture}[scale=3]	\node (1) at (2,3)  {};	\node [white] (a) at (2.5,3.2) [one] {"
               r"};	\node (x) at (1,3)  {};	\node (0) at (2.2,2.5)  {};	\node [white] (b) at (1.5,2) [one] {};	"
               r"\node (y) at (2.1,2.7)  {};	\node (z) at (3,2)  {};	\end{tikzpicture}")
    one = SingleStringMathTex(one_tex, tex_template=my_template, stroke_width=3, fill_opacity=1,
                              should_center=True, color=ROSA)
    one.set_z_index(2)
    one_r = one.copy()
    # creacion
    slide.play(Write(zero0.set_opacity(1).shift(RIGHT * .82 + DOWN * .4)))
    slide.play(Write(zero1.shift(UP * 1.65)))
    slide.next_slide()
    slide.play(Write(one))
    slide.next_slide()
    slide.play(Write(twoxz.shift(DOWN * .4)))
    slide.play(Write(twoy.shift(UP * .45 + RIGHT * .4)))
    slide.next_slide()
    slide.play(Write(lines.set_opacity(1).set_fill(opacity=0)))
    slide.next_slide()
    slide.play(Write(lines2.set_opacity(1).set_fill(opacity=0)))
    slide.next_slide()
    if indicate:
        slide.play(Indicate(triangle1.set_opacity(0).set_fill(opacity=.5), color=YELLOW))
        slide.next_slide()
        slide.play(Indicate(triangle2.set_opacity(0).set_fill(opacity=.5), color=YELLOW))
        slide.next_slide()
        slide.play(Indicate(triangle3.set_opacity(0).set_fill(opacity=.5), color=YELLOW))
        slide.next_slide()
        slide.play(Indicate(triangle4.set_opacity(0).set_fill(opacity=.5), color=YELLOW))
        slide.next_slide()
    else:
        slide.play(Create(triangle1.set_opacity(0).set_fill(opacity=.5)))
        slide.play(Create(triangle2.set_opacity(0).set_fill(opacity=.5)))
        slide.play(Create(triangle3.set_opacity(0).set_fill(opacity=.5)))
        slide.play(Create(triangle4.set_opacity(0).set_fill(opacity=.5)))
        slide.next_slide()
    slide.play(Unwrite(one),
               Unwrite(zero1),
               Unwrite(zero0),
               Unwrite(twoy),
               Unwrite(twoxz),
               Unwrite(lines),
               Unwrite(lines2),
               Unwrite(triangle1),
               Unwrite(triangle2),
               Unwrite(triangle3),
               Unwrite(triangle4))


def esfera(slide, full):
    escala = 2.3
    origen = np.array((2, 2.6, 1)) * escala
    azul1 = LabeledDot(Tex("1"), point=np.array((2, 3, 1)) * escala - origen, color=AZUL)
    azul_1 = LabeledDot(Tex("-1"), point=np.array((2.2, 2.5, 1)) * escala - origen, color=AZUL)
    rosa1 = LabeledDot(Tex("1"), point=np.array((2.5, 3.2, 1)) * escala - origen, color=ROSA)
    rosa_1 = LabeledDot(Tex("-1"), point=np.array((1.5, 2, 1)) * escala - origen, color=ROSA)
    naranja1 = LabeledDot(Tex("1"), point=np.array((1, 3, 1)) * escala - origen, color=NARANJA)
    naranja_1 = LabeledDot(Tex("-1"), point=np.array((3, 2, 1)) * escala - origen, color=NARANJA)
    azules = VGroup(azul1, azul_1)
    rosas = VGroup(rosa1, rosa_1)
    naranjas = VGroup(naranja1, naranja_1)
    if full:
        puntos_toda = VGroup(azules, rosas, naranjas)
        lineas_toda = VGroup()
        total_colors = len(puntos_toda)
        for d in range(total_colors):
            c = d
            if c + 1 == total_colors:
                c = -1
            for p in puntos_toda[d]:
                for q in puntos_toda[c + 1]:
                    lineas_toda.add(Line(p.get_center(), q.get_center(), color=GREY, z_index=-1))
        triangulos_total = VGroup()
        for p in rosas:
            for q in naranjas:
                triangulos_total.add(
                    Polygon(p.get_center(),
                            q.get_center(),
                            azul1.get_center(),
                            z_index=-2,
                            color=GREY,
                            fill_color=GREY,
                            fill_opacity=.5))

        slide.play(Create(puntos_toda), Create(lineas_toda), Create(triangulos_total))
        slide.next_slide()
    else:
        puntos_1 = VGroup(azules, rosas, naranja1)
        lineas_1 = VGroup()
        cuadro = VGroup()
        for d in azules:
            for p in rosas:
                cuadro.add(Line(d.get_center(), p.get_center(), color=GREY, z_index=-1))
        lineas_1.add(cuadro)
        triangulos_1 = VGroup()

        one_side(naranja1, lineas_1, triangulos_1, True, blues_set=azules, pinks_set=rosas)

        slide.play(Create(puntos_1), Create(lineas_1), Create(triangulos_1))
        slide.next_slide()
        x = LabeledDot(MathTex(r"x"), point=triangulos_1[1].get_center(), color=WHITE)
        slide.play(Create(x))
        slide.next_slide()
        extension = MathTex(r"f(gx)=gf(x)")
        slide.play(Write(extension.shift(UP * 2 +RIGHT*3.5)))
        slide.next_slide()
        slide.play(Indicate(cuadro, color=VERDOSO), Indicate(azules, color=VERDOSO), Indicate(rosas, color=VERDOSO))
        slide.next_slide()

        lineas_2 = VGroup()
        triangulos_2 = VGroup()

        one_side(naranja_1, lineas_2, triangulos_2, False, azules, pinks_set=rosas)
        lineas_2.set_z_index(-1)
        triangulos_2.set_z_index(-2)
        slide.play(Create(naranja_1), Create(lineas_2), Create(triangulos_2))
        extension2 = MathTex(r"f(gx)=g\hat{f}(x)", color=AZUL).shift(UP * 2 + RIGHT * 3.5)
        slide.play(TransformMatchingShapes(extension, extension2))
        slide.next_slide()


def one_side(vertex, lines_set, triangle_set, inside, blues_set, pinks_set):
    for d, p in zip(blues_set, pinks_set):
        lines_set.add(Line(d.get_center(), vertex.get_center(), color=GREY, z_index=-1))
        lines_set.add(Line(p.get_center(), vertex.get_center(), color=GREY, z_index=-1))
    if inside:
        grises = [GREY, GREY_A]
        zindex = [-2, -3]
        blues_to_use = blues_set
    else:
        grises = [GREY]
        zindex = [-2]
        blues_to_use = blues_set[0]
    for p, c, z in zip(blues_to_use, grises, zindex):
        for q in pinks_set:
            triangle_set.add(
                Polygon(p.get_center(),
                        q.get_center(),
                        vertex.get_center(),
                        z_index=z,
                        color=c,
                        fill_color=c,
                        fill_opacity=.5))
    blues_set.set_z_index(0)
    pinks_set.set_z_index(0)


class SimplicialComplexes(BlackSlide):
    def construct(self):
        super().construct()
        title = Title("Common language")
        self.create_title(title)
        simplicial_complex = (
            VGroup(
                VGroup(Text("A simplicial complex over "),
                       MathTex(r"V"),
                       Text(" is a subset ")).arrange(RIGHT),
                VGroup(MathTex(r"\Delta\subseteq\mathcal{P}(V)"),
                       Text("closed under contentions")).arrange(RIGHT)).arrange(DOWN))
        fade_text(self, simplicial_complex)
        vertex_text = Text(" A vertex.")
        vertex_pic = Dot(radius=.1, color=BLACK).set_z_index(1)
        vertex_tex = VGroup(MathTex(r"\{"), vertex_pic.copy(), MathTex(r"\}")).arrange(RIGHT)
        vertex = VGroup(vertex_text, vertex_pic, vertex_tex).arrange(DOWN, buff=1.9)
        self.play(Write(vertex))
        self.next_slide()
        edge_text = Text(" An edge.")
        vertex_pic_2 = Dot(radius=.1, color=ROSA).set_z_index(1)
        edge_tex = VGroup(MathTex(r"\{"),
                          vertex_pic.copy(),
                          MathTex(r","),
                          vertex_pic_2.copy(),
                          MathTex(r"\}")).arrange(RIGHT)
        VGroup(edge_text,
               vertex_pic_2,
               edge_tex).arrange(DOWN, buff=1.9)
        edge_pic = Line(vertex_pic.get_center() + LEFT, vertex_pic_2.get_center() + RIGHT,
                        color=GREY)
        self.play(TransformMatchingShapes(vertex_text, edge_text),
                  TransformMatchingShapes(vertex_tex, edge_tex),
                  # TransformMatchingTex(vertex_tex[0], edge_tex[0]),
                  vertex_pic.animate.shift(LEFT),
                  Write(vertex_pic_2.shift(RIGHT)))
        self.next_slide()
        self.play(Create(edge_pic))
        self.next_slide()
        triangle_text = Text(" A triangle.")
        vertex_pic_3 = Dot(radius=.1, color=AZUL).set_z_index(1)
        triangle_tex = VGroup(MathTex(r"\{"),
                              vertex_pic.copy(),
                              MathTex(r","),
                              vertex_pic_2.copy(),
                              MathTex(r","),
                              vertex_pic_3.copy(),
                              MathTex(r"\}")).arrange(RIGHT)
        VGroup(triangle_text,
               vertex_pic_3,
               triangle_tex).arrange(DOWN, buff=1.9)
        # edge_pic_2 = Line(vertex_pic.get_center(), vertex_pic_3.get_center() + UP*1.5,
        #                 color=GREY)
        # edge_pic_3 = Line(vertex_pic_2.get_center(), vertex_pic_3.get_center() + UP*1.5,
        #                 color=GREY)
        triangle_pic = Polygon(vertex_pic.get_center(),
                               vertex_pic_2.get_center(),
                               vertex_pic_3.get_center() + UP * 1.5,
                               z_index=-1,
                               color=GREY,
                               fill_color=GREY,
                               fill_opacity=1)
        triangle = VGroup(triangle_pic)
        self.wait_time_between_slides = .1
        self.play(TransformMatchingShapes(edge_text, triangle_text),
                  TransformMatchingShapes(edge_tex, triangle_tex),
                  # Write(edge_pic_2),
                  # Write(edge_pic_3),
                  Write(vertex_pic_3.shift(UP * 1.5)),
                  Create(triangle))
        self.next_slide()
        self.wait_time_between_slides = 0
        self.finish()


class PseudoesferaDefinicion(BlackSlide):
    def construct(self):
        super().construct()
        # inicio
        title = Title("What is a pseudosphere?")
        self.create_title(title)
        # definicion pseudoesfera
        V = VGroup(MathTex(r"V_{p}:"),
                   Text(" finite for each"),
                   MathTex(r"p\in\mathbb{P}")).arrange(RIGHT)
        P = VGroup(MathTex(r"\mathbb{P}:"),
                   Text(" finite")).arrange(RIGHT)
        self.play(Write(P))
        self.next_slide()
        self.play(P.animate.shift(UP))
        self.play(Write(V))
        self.next_slide()
        self.play(V.animate.shift(UP), P.animate.shift(UP))
        def_psi = VGroup(MathTex(r"\Psi"),
                         Text(" simplicial complex")).arrange(RIGHT)
        self.play(Write(def_psi))
        self.next_slide()
        self.play(Unwrite(P + V))
        # definicion pseudoesfera vertices, simplejos
        self.play(def_psi.animate.shift(UP))
        vertex = VGroup(Text("Vertices: "),
                        MathTex(r"(p,v)"), Text(" where "),
                        MathTex(r"v\in V_{p}, p\in\mathbb{P}")).arrange(RIGHT)
        self.play(Write(vertex))
        self.next_slide()
        self.play(def_psi.animate.shift(UP), vertex.animate.shift(UP))
        simplices = VGroup(Text("Simplices: "),
                           MathTex(r"(p,v),(p,w)\in \sigma\implies v=w")).arrange(RIGHT)
        self.play(Write(simplices))
        self.next_slide()
        claro = Text("Clear, right?")
        self.wait_time_between_slides = .1
        self.play(Unwrite(def_psi + vertex + simplices))
        super_afirmacion = Text("It is the biggest chromatic complex on those vertices.")
        self.play(FadeIn(super_afirmacion))
        self.next_slide()
        self.play(FadeOut(super_afirmacion), FadeIn(claro))
        self.next_slide()
        self.wait_time_between_slides = 0
        self.finish()


class Ejemplos(BlackSlide):
    def construct(self):
        super().construct()
        title = Title("Some examples")
        self.create_title(title)
        examples_pseudospheres(self, True)
        ready = Text("Ready to study applications...")
        fade_text(self, ready)
        or_no = Text("...maybe not!")
        fade_text(self, or_no)
        # estado del arte
        state_art = VGroup(Text("The knowledge of pseudospheres consisted"),
                           Text("of 3 pages of"), Text("Distributed Computing", t2s={'[0:-2]': ITALIC}),
                           Text("Through Combinatorial Topology!", t2s={'[0:-2]': ITALIC})).arrange(DOWN)
        self.play(Write(state_art))
        self.next_slide(loop=True)
        self.play(Circumscribe(state_art))
        self.next_slide(loop=False)
        self.finish()


class Matroides(BlackSlide):
    def construct(self):
        super().construct()
        # title = Title("My path begins!")
        title = Title("The first discovery")
        self.create_title(title)
        pseudospheres = Text("Pseudospheres")
        fam_pseudospheres = Circle().surround(pseudospheres)
        subset = VGroup(pseudospheres, fam_pseudospheres)
        self.wait_time_between_slides = .1
        self.play(Write(pseudospheres))
        self.play(Create(fam_pseudospheres))
        self.next_slide()
        self.play(ScaleInPlace(subset, .3))
        self.play(subset.animate.shift(RIGHT * 1.4))
        # matroides
        matr = Text("Matroids", font_size=15)
        self.play(FadeIn(matr.shift(LEFT * 1.2)))
        matroids = VGroup(matr, subset)
        fam_matroids = Circle().surround(matroids)
        self.play(Create(fam_matroids))
        self.next_slide()
        self.play(Uncreate(fam_matroids))
        self.play(Uncreate(fam_pseudospheres))
        self.play(Uncreate(pseudospheres))
        self.play(Uncreate(matr))
        title2 = Title("Matroids")
        self.play(Transform(title, title2))
        self.next_slide()
        matroid_complex = VGroup(
            MathTex(r"\sigma,\tau\in\Delta",
                    tex_template=my_template),
            MathTex(r"\dim (\sigma)>\dim (\tau) \implies"
                    r" \exists x\in\sigma\setminus\tau \colon \tau\cup\{x\}\in\Delta",
                    tex_template=my_template)).arrange(DOWN)
        self.play(Write(matroid_complex))
        self.next_slide()
        self.play(matroid_complex.animate.shift(UP * 2))
        triangle = Triangle(color=GREY, fill_color=GREY, fill_opacity=1).shift(LEFT * 2 + DOWN)
        triangle.set_z_index(-1)
        p1 = Dot(point=triangle.points[0], radius=.1, color=BLACK)
        p2 = Dot(point=triangle.points[3], radius=.1, color=NARANJA)
        p3 = Dot(point=triangle.points[7], radius=.1, color=AZUL)
        edge = Line(p2.get_center(), p3.get_center(), color=GREY, z_index=-1)
        tres = VGroup(p1, p2, p3, triangle, edge)
        triangle2 = Triangle(color=GREY, fill_color=GREY, fill_opacity=1).shift(RIGHT * 2 + DOWN)
        triangle2.set_z_index(-1)
        q2 = Dot(point=triangle2.points[3], radius=.1, color=ROSA)
        q3 = Dot(point=triangle2.points[7], radius=.1, color=AZUL)
        line = Line(q2.get_center(),q3.get_center(),color=GREY).set_z_index(-1)
        dos = VGroup(q2, q3, line)
        self.play(Create(dos + tres))
        self.next_slide()
        self.play(Uncreate(triangle), p1.animate.move_to(triangle2.points[0]), Create(triangle2))
        self.next_slide()
        self.play(Uncreate(tres), Uncreate(dos), Uncreate(triangle2), Unwrite(matroid_complex), Unwrite(matr))
        self.next_slide()
        consequences = (VGroup(Text("Pseudospheres"),
                               Text("are shellable (Theorem 13.3.6 of Herlihy, M., et.al. 2013)."))
                        .arrange(DOWN))
        self.play(Write(consequences))
        self.next_slide()
        self.wait_time_between_slides = 0
        homotopy = Text("are shellable because they are matroids.").move_to(consequences[1])
        self.play(Transform(consequences[1], homotopy))
        self.next_slide()
        self.finish()
        # morse = Text("With no shellings I proved that")
        # self.play(FadeIn(morse.shift(UP * 2)))
        # self.next_slide()
        # self.play(Unwrite(consequences), Unwrite(morse))


class PosetChrom(BlackSlide):
    def construct(self):
        super().construct()
        title = Title("Which matroids are pseudospheres?")
        self.create_title(title)
        pseudospheres = Text("Pseudospheres")
        fam_pseudospheres = Circle().surround(pseudospheres)
        subset = VGroup(pseudospheres, fam_pseudospheres).scale(.4)
        # matroides
        matr = Text("Matroids", font_size=20).next_to(pseudospheres, LEFT * 3.5)
        matroids = VGroup(matr, subset)
        fam_matroids = Circle().surround(matroids, buffer_factor=1)
        superset = VGroup(matroids, fam_matroids)
        self.play(Create(fam_matroids), Create(fam_pseudospheres), Write(pseudospheres), Write(matr))
        # poset
        poset = Text("Posets", font_size=20)
        self.play(Create(poset.next_to(pseudospheres, RIGHT * 4.8)))
        poset_subset = VGroup(subset, poset)
        fam_poset = Circle().surround(poset_subset, buffer_factor=1)
        self.wait_time_between_slides = .1
        self.play(Create(fam_poset))
        caract = Intersection(fam_poset, fam_matroids, color=BLACK)
        self.next_slide()
        self.play(FadeTransform(fam_pseudospheres, caract, replace_mobject_with_target_in_scene=False))
        self.next_slide()
        self.wait_time_between_slides = 0
        c_simpl = Text("Chromatic", font_size=20).next_to(poset, buff=-1.3).shift(UP * .3)
        balanced = Text("complexes", font_size=20).next_to(c_simpl, DOWN)
        c_balanced = VGroup(c_simpl, balanced)
        self.play(Transform(poset, c_balanced))
        self.next_slide()
        whole = VGroup(c_balanced, pseudospheres, fam_matroids, matr, fam_poset, caract, poset)
        # self.play(Uncreate(whole))
        # self.next_slide()
        # dem = Text("Proof")
        # self.play(FadeIn(dem.shift(UP * 2)))
        # self.next_slide()
        # black = Dot(point=LEFT, radius=.1, color=BLACK).set_z_index(1)
        # pink = Dot(black.get_center() + RIGHT, radius=.1, color=ROSA).set_z_index(1)
        # blue = Dot(pink.get_center() + RIGHT, radius=.1, color=AZUL).set_z_index(1)
        # menor1 = MathTex(r"<", font_size=40).next_to(black, RIGHT)
        # menor2 = MathTex(r"<").next_to(pink, RIGHT)
        # self.play(Create(black))
        # self.next_slide()
        # self.play(Write(menor1))
        # self.next_slide()
        # self.play(Create(pink))
        # self.next_slide()
        # self.play(Write(menor2))
        # self.next_slide()
        # self.play(Create(blue))
        # self.next_slide()
        # black1 = Dot(black.get_center() + DOWN, color=BLACK)
        # black2 = Dot(black.get_center() + UP, color=BLACK)
        # pink1 = Dot(pink.get_center() + DOWN, radius=.1, color=ROSA)
        # pink2 = Dot(pink.get_center() + UP, radius=.1, color=ROSA)
        # blue2 = Dot(blue.get_center() + UP, radius=.1, color=AZUL)
        # blue3 = Dot(blue.get_center() + DOWN, radius=.1, color=AZUL)
        # blacks = VGroup(black1, black2)
        # pinks = VGroup(pink1, pink2)
        # blues = VGroup(blue, blue2, blue3)
        # lines_black_pink = VGroup().set_z_index(-1)
        # lines_pink_blue = VGroup().set_z_index(-1)
        # for i in blacks:
        #     for j in pinks:
        #         lines_black_pink.add(Line(i.get_center(), j.get_center(), color=GREY))
        # for i in pinks:
        #     for j in blues:
        #         lines_pink_blue.add(Line(i.get_center(), j.get_center(), color=GREY))
        # self.play(Transform(black, blacks),
        #           Transform(pink, pinks),
        #           Transform(blue, blues),
        #           Transform(menor1, lines_black_pink),
        #           Transform(menor2, lines_pink_blue))
        # self.next_slide()
        # self.play(Uncreate(pink), Uncreate(black), Uncreate(blue), Uncreate(menor1), Uncreate(menor2))
        self.finish()


class Join(BlackSlide):
    def construct(self):
        super().construct()
        title = Title("The last characterization")
        self.create_title(title)
        # join
        ensamble1 = Text("Join ")
        ensamble2 = MathTex(r"\Delta\ast\Gamma=\{\sigma\cup\tau\mid\sigma\in\Delta,\tau\in\Gamma\}")
        ensamble = VGroup(ensamble1, ensamble2).arrange(DOWN)
        fade_text(self, ensamble)
        examples_pseudospheres(self, False)
        # join caracter
        ensamble_caract = Text("Pseudospheres are precisely\n finite joins of finite sets.")
        self.play(AddTextLetterByLetter(ensamble_caract))
        self.next_slide()
        self.play(RemoveTextLetterByLetter(ensamble_caract))
        self.finish()


class GEspacios(BlackSlide):
    def construct(self):
        super().construct()
        title = Title("Groups acting on pseudospheres")
        self.create_title(title)
        g_0 = VGroup(MathTex("G:"), Text(" a finite discrete group.")).arrange(RIGHT)
        g_ast = VGroup(MathTex(r"\underbrace{G\ast \cdots\ast G}_{n+1}"),
                       Text(" is a pseudosphere.")).arrange(RIGHT)
        g_psi = VGroup(g_0, g_ast).arrange(DOWN)
        self.play(Write(g_0))
        self.next_slide()
        self.play(Write(g_ast))
        self.next_slide()
        # E_n spaces
        g_acts = VGroup(MathTex("G"), Text(" acts on ")).arrange(RIGHT)
        g_ast2 = VGroup(MathTex(r"\underbrace{G\ast \cdots\ast G}_{n+1}"),
                        MathTex(r"=\Psi_{n}(G).")).arrange(RIGHT)
        g_psi2 = VGroup(g_acts, g_ast2).arrange(DOWN)
        self.play(ReplacementTransform(g_psi, g_psi2))
        self.next_slide()
        # esferas
        z_2_acts = VGroup(MathTex(r"\mathbb{Z}_{2}"), Text(" acts on ")).arrange(RIGHT)
        z_2_ast2 = VGroup(MathTex(r"\underbrace{\mathbb{Z}_{2}\ast \cdots\ast \mathbb{Z}_{2}}_{n+1}"),
                          MathTex(r"=\Psi_{n}(\mathbb{Z}_{2}).")).arrange(RIGHT)
        sphere = VGroup(MathTex(r"\underbrace{\mathbb{Z}_{2}\ast \cdots\ast \mathbb{Z}_{2}}_{n+1}"),
                        MathTex(r"=S^{n}.")).arrange(RIGHT)
        # grupo z_2
        g_psi3 = VGroup(z_2_acts, z_2_ast2).arrange(DOWN)
        # grupo esfera
        g_psi4 = VGroup(z_2_acts, sphere).arrange(DOWN)
        self.play(ReplacementTransform(g_psi2, g_psi3))
        self.next_slide()
        self.play(ReplacementTransform(g_psi3, g_psi4))
        self.next_slide()
        self.play(FadeOut(g_psi4))
        # octaedro
        esfera(self, True)
        self.next_slide()
        self.finish()


class BorsukUlam(BlackSlide):
    def construct(self):
        super().construct()
        title = Title("The Borsuk-Ulam theorem is a theorem about pseudospheres")
        self.create_title(title)
        # Borsuk-Ulam
        bu = Text("Borsuk-Ulam")
        bu0 = Text("There is no continuous function ")
        bu1 = MathTex(r"f\colon S^{n+1}\rightarrow S^{n}")
        bu2 = Text(" preserving the action of ")
        bu3 = MathTex(r"\mathbb{Z}_{2}")
        # orden del texto y titulo
        buthm0 = VGroup(bu0, bu1).arrange(DOWN)
        buthm1 = VGroup(bu2, bu3).arrange(RIGHT)
        buttl = VGroup(bu, buthm0, buthm1).arrange(DOWN)
        # creacion
        self.play(Write(buttl))
        self.next_slide()
        # bu_psi
        bu1_psi = MathTex(r"f\colon |\Psi_{n+1}(\mathbb{Z}_{2})|\rightarrow |\Psi_{n}(\mathbb{Z}_{2})|").move_to(bu1)
        self.play(TransformMatchingShapes(bu1, bu1_psi))
        self.next_slide()
        # matousek
        mt = Text("Matousek").move_to(bu)
        mt1 = MathTex(r"f\colon |\Psi_{n+1}(G)|\rightarrow |\Psi_{n}(G)|").move_to(bu1_psi)
        mt3 = MathTex("G").move_to(bu3)
        self.play(TransformMatchingShapes(bu, mt),
                  TransformMatchingShapes(bu1_psi, mt1),
                  TransformMatchingShapes(bu3, mt3))
        self.next_slide()
        self.play(FadeOut(mt),
                  FadeOut(mt1),
                  FadeOut(mt3),
                  FadeOut(bu2),
                  FadeOut(bu0))
        # tucker
        # tucker enunciado
        tk = Text("Tucker").move_to(bu)
        tk0 = VGroup(Text("If "), MathTex(r"\Delta"),
                     Text(" is a triangulation which is antipodally symmetric")).arrange(RIGHT)
        tk1 = VGroup(Text(" on the boundary of  "), MathTex(r"B^{n}"),
                     Text(", there is no simplicial map ")).arrange(RIGHT)
        tk2 = MathTex(r"f\colon\Delta\rightarrow\Psi_{n-1}(\mathbb{Z}_{2})").arrange(RIGHT)
        tk3 = VGroup(Text("preserving the action of "),
                     MathTex(r"\mathbb{Z}_{2}"),
                     Text("on the boundary of "),
                     MathTex(r"B^{n}")).arrange(RIGHT)
        tucker = VGroup(tk, tk0, tk1, tk2, tk3).arrange(DOWN)
        self.play(Write(tucker))
        self.next_slide()
        self.play(FadeOut(tk, tk1, tk2, tk3),
                  FadeOut(tk0[0], tk0[1], tk0[2][0:3]))
        # antipodalmente simetricas
        sym = Text("Antipodally symmetric triangulations", font_size=40).move_to(title)
        prueba = tk0[2][3:]
        self.play(Transform(prueba, sym), FadeOut(title))
        self.next_slide()
        # Definición original
        circle = Circle(radius=2, color=GREY)
        circle.set_z_index(-1)
        p1 = Dot(point=circle.point_at_angle(225 * DEGREES), radius=.2, color=AZUL)
        p1_t = Text("1", font_size=20, color=BLACK).move_to(p1)
        p0 = Dot(point=circle.point_at_angle(45 * DEGREES), radius=.2, color=AZUL)
        p0_t = Text("-1", font_size=20, color=BLACK).move_to(p0)
        q1 = Dot(point=circle.point_at_angle(315 * DEGREES), radius=.2, color=ROSA)
        q1_t = Text("1", font_size=20, color=BLACK).move_to(q1)
        q0 = Dot(point=circle.point_at_angle(135 * DEGREES), radius=.2, color=ROSA)
        q0_t = Text("-1", font_size=20, color=BLACK).move_to(q0)
        points = VGroup(p1, p1_t, p0, p0_t, q1, q1_t, q0, q0_t)
        self.play(Write(circle))
        self.next_slide()
        x1 = Dot(point=circle.point_at_angle(240 * DEGREES), radius=.2, color=NARANJA)
        x1.set_z_index(0)
        x1_t = Text("-1", font_size=20, color=BLACK).move_to(x1)
        x1_t.set_z_index(2)
        x2 = Dot(point=circle.point_at_angle(60 * DEGREES), radius=.2, color=NARANJA)
        x2.set_z_index(0)
        x2_t = Text("1", font_size=20, color=BLACK).move_to(x2)
        x2_t.set_z_index(2)
        linea_antip = Arrow(x1, x2, color=BLACK)
        points2 = VGroup(x1, x2, x1_t, x2_t)
        # animacion
        self.play(Write(x1))
        self.next_slide()
        self.play(Write(x1_t))
        self.next_slide()
        self.play(Write(linea_antip))
        self.next_slide()
        self.play(Write(x2))
        self.play(Write(x2_t))
        self.play(Unwrite(linea_antip))
        self.next_slide()
        self.play(Write(points))
        self.next_slide()
        # dimension 1
        square = Square(side_length=4, color=BLACK)
        square.set_z_index(-1)
        # cuadrado
        self.add(points)
        self.play(Transform(circle, square),
                  p1.animate.move_to(square.get_corner(DOWN + LEFT)),
                  p0.animate.move_to(square.get_corner(UP + RIGHT)),
                  q1.animate.move_to(square.get_corner(DOWN + RIGHT)),
                  q0.animate.move_to(square.get_corner(UP + LEFT)),
                  p1_t.animate.move_to(square.get_corner(DOWN + LEFT)),
                  p0_t.animate.move_to(square.get_corner(UP + RIGHT)),
                  q1_t.animate.move_to(square.get_corner(DOWN + RIGHT)),
                  q0_t.animate.move_to(square.get_corner(UP + LEFT)),
                  x2.animate.move_to(np.array([1.3, 2, 1])),
                  x1.animate.move_to(np.array([-1.3, -2, 1])),
                  x2_t.animate.move_to(np.array([1.3, 2, 1])),
                  x1_t.animate.move_to(np.array([-1.3, -2, 1])))
        self.next_slide()
        self.finish()


class Generaliza(BlackSlide):
    def construct(self):
        super().construct()
        title = Title("Tucker's lemma is a theorem about pseudospheres!")
        self.create_title(title)
        # gsym = VGroup(MathTex(r"G-", font_size=40),
        #               Text("symmetric subdivisions ", font_size=40)).arrange(RIGHT)
        # self.play(Write(gsym.shift(UP * 3)))
        hexagono = RegularPolygon(8, radius=2.5)
        vertices = hexagono.get_vertices()
        pares = VGroup()
        nones = VGroup()
        lineas = VGroup()
        etiquetas = VGroup()
        subdiv1 = VGroup()
        subdiv2 = VGroup()
        for v in range(len(vertices)):
            if v % 2 == 0:
                pares.add(Dot(vertices[v], radius=.15, color=AZUL, z_index=1))
                etiquetas.add(Text(str(v // 2), font_size=20, color=BLACK).move_to(vertices[v]).set_z_index(2))
            else:
                nones.add(Dot(vertices[v], radius=.15, color=NARANJA, z_index=1))
                etiquetas.add(Text(str(v // 2), font_size=20, color=BLACK).move_to(vertices[v]).set_z_index(2))
        for x in range(len(pares)):
            for y in range(len(nones)):
                linea = Line(pares[x].get_center(), nones[y].get_center(), z_index=-1, color=GREY)
                lineas.add(linea)
                if x == y:
                    subdiv1.add(Dot(linea.get_center(), radius=.15, color=ROSA, z_index=1))
                elif (x + y) % 2 == 0:
                    subdiv2.add(Dot(linea.point_from_proportion(.8), radius=.15, color=BLACK, z_index=1))
        self.play(Create(pares), Create(nones), Create(lineas), Create(etiquetas))
        self.next_slide()
        for i in range(len(subdiv1)):
            self.play(Create(subdiv1[i]))
            self.next_slide()
        for i in range(len(subdiv2)):
            self.play(Create(subdiv2[i]))
            self.next_slide()
        self.wait_time_between_slides = .1
        self.play(Uncreate(pares + nones + lineas + etiquetas + subdiv1 + subdiv2))
        self.next_slide()
        self.wait_time_between_slides = 0
        #tk = Text("Tucker").move_to(gsym)
        tk0 = VGroup(Text("If "), MathTex(r"\Delta"),
                     Text(" is a triangulation which is antipodally symmetric")).arrange(RIGHT)
        tk1 = VGroup(Text(" on the boundary of  "), MathTex(r"B^{n}"),
                     Text(", there is no simplicial map ")).arrange(RIGHT, buff=1.2)
        tk2 = MathTex(r"f\colon\Delta\rightarrow\Psi_{n-1}(\mathbb{Z}_{2})").arrange(RIGHT)
        tk3 = VGroup(Text(" preserving the action of ",
                          font_size=30), MathTex(r"\mathbb{Z}_{2}"),
                     VGroup(Text("on the boundary of "),
                     MathTex(r"B^{n}")).arrange(RIGHT, buff = 1.2)).arrange(RIGHT)
        tucker = VGroup(tk0, tk1, tk2, tk3).arrange(DOWN)
        tk1_cone = MathTex(r"S^{n-1}\ast x").move_to(tk1[1])
        tk1_cone_2 = tk1_cone.copy()
        tk1_cone_2 = tk1_cone_2.move_to(tk3[-1][-1])
        self.play(Write(tucker))
        self.next_slide()
        self.play(Transform(tk1[1], tk1_cone),Transform(tk3[-1][-1], tk1_cone_2))
        self.next_slide()
        # luis alberto
        # la = Text("Luis Alberto").move_to(tk)
        la0 = VGroup(Text("If "), MathTex(r"\Delta"),
                     Text(" is a subdivision which is"), MathTex(r"G-"),
                     Text("symmetric")).arrange(RIGHT).move_to(tk0)
        la1 = VGroup(Text(" on the boundary of  "),
                     MathTex(r"\Psi_{n-1}(G)\ast x"),
                     Text(r", there is no simplicial map ")).arrange(RIGHT).move_to(tk1)
        la2 = MathTex(r"f\colon\Delta\rightarrow\Psi_{n-1}(G)").arrange(RIGHT).move_to(tk2)
        la3 = VGroup(Text("preserving the action of "),
                     MathTex(r"G"), Text("on "),
                     MathTex(r"\Psi_{n-1}(G)")).arrange(RIGHT).move_to(tk3)
        self.play(TransformMatchingShapes(tk0, la0),
                  TransformMatchingShapes(tk1[1], la1[1]),
                  TransformMatchingShapes(tk2, la2),
                  TransformMatchingShapes(tk3, la3))
        self.next_slide()
        self.play(FadeOut(la0),
                  FadeOut(la1[1]),
                  FadeOut(la2),
                  FadeOut(la3),
                  FadeOut(tk1[2:]),
                  FadeOut(tk1[0]))
        prueba = Text("Proof")
        fade_text(self, prueba)
        bu = Text("Matousek").shift(UP*2)
        self.play(FadeIn(bu))
        self.next_slide()
        bu0 = Text("There is no continuous function ").shift(UP )
        bu1 = MathTex(r"f\colon |\Psi_{n+1}(G)|\rightarrow |\Psi_{n}(G)|").move_to(bu0.get_center() + DOWN)
        bu2 = Text(" preserving the action of ")
        bu3 = MathTex(r"G")
        buthm1 = VGroup(bu2, bu3).arrange(RIGHT).move_to(bu1.get_center() + DOWN)
        self.play(FadeIn(bu0, bu1, buthm1))
        self.next_slide()
        self.play(FadeOut(bu0, bu, buthm1), bu1.animate.move_to(bu))
        self.next_slide()
        join = MathTex(r"\Psi_{n+1}(G) = \Psi_{n}(G)\ast G = \bigcup_{g\in G} \Psi_{n}(G)\ast g").move_to(bu0)
        self.play(Write(join))
        self.next_slide()
        iff = MathTex(r"\iff").move_to(join)
        self.play(Transform(join, iff))
        bu_version2 = MathTex(r"\hat{f}\colon |\Psi_{n}(G)\ast e|\rightarrow |\Psi_{n}(G)|").move_to(
            join.get_center() + DOWN)
        self.play(Write(bu_version2))
        self.next_slide()
        guarda = VGroup(bu1, join, bu_version2)
        self.play(guarda.animate.to_corner(LEFT + UP, buff=.5).scale(.4))
        esfera(self, False)
        self.finish()


class Portadores(BlackSlide):
    def construct(self):
        super().construct()
        title = Title("We are almost ready for applications")
        self.create_title(title)
        # mapas portadores
        carrier = VGroup(
            VGroup(Text("A carrier map sends, monotonously, each simplex in"),
                   MathTex(r"I")).arrange(RIGHT),
            VGroup(Text("to a subcomplex of"),
                   MathTex(r"O")).arrange(RIGHT)).arrange(DOWN)
        self.play(FadeIn(carrier))
        self.next_slide()
        carrier_2 = VGroup(
            VGroup(Text("A carrier map is an order preserving function from"),
                   MathTex(r"I")).arrange(RIGHT),
            VGroup(Text("into the lattice of subcomplexes of"),
                   MathTex(r"O")).arrange(RIGHT)).arrange(DOWN)
        self.play(Transform(carrier, carrier_2))
        self.next_slide()
        self.play(FadeOut(carrier),Uncreate(title))
        # consenso
        # input
        square_input = Square(side_length=2, color=GREY).shift(LEFT * 4)
        square_input.set_z_index(-1)
        # procesos
        p1 = LabeledDot(Tex("1", font_size=20),
                        point=square_input.get_corner(DOWN + LEFT),
                        radius=.2,
                        color=AZUL)
        p0 = LabeledDot(Tex("-1", font_size=20),
                        point=square_input.get_corner(UP + RIGHT),
                        radius=.2,
                        color=AZUL)
        q1 = LabeledDot(Tex("1", font_size=20),
                        point=square_input.get_corner(DOWN + RIGHT),
                        radius=.2,
                        color=NARANJA)
        q0 = LabeledDot(Tex("-1", font_size=20),
                        point=square_input.get_corner(UP + LEFT),
                        radius=.2,
                        color=NARANJA)
        points = VGroup(p1, p0, q1, q0)
        # output
        output = Square(side_length=2, color=BLACK).shift(RIGHT * 4)
        p1o = LabeledDot(Tex("1", font_size=20),
                         point=output.get_corner(DOWN + LEFT),
                         radius=.2,
                         color=AZUL)
        p0o = LabeledDot(Tex("-1", font_size=20),
                         point=output.get_corner(UP + RIGHT),
                         radius=.2,
                         color=AZUL)
        q1o = LabeledDot(Tex("1", font_size=20),
                         point=output.get_corner(DOWN + RIGHT),
                         radius=.2,
                         color=NARANJA)
        q0o = LabeledDot(Tex("-1", font_size=20),
                         point=output.get_corner(UP + LEFT),
                         radius=.2,
                         color=NARANJA)
        pointso = VGroup(p1o, p0o, q1o, q0o)
        up_line = Line(p1o.get_center(), q1o.get_center(), color=GREY)
        up_line.set_z_index(-1)
        bot_line = Line(p0o.get_center(), q0o.get_center(), color=GREY)
        bot_line.set_z_index(-1)
        # dibujar
        self.play(Create(square_input),
                  Create(points),
                  Create(pointso),
                  Create(bot_line),
                  Create(up_line))
        self.next_slide()
        # carrier
        start_point = Dot().next_to(p1, direction=np.array([1, -1, 0]), buff=.01).get_center()
        end_point = Dot().next_to(p1o, direction=np.array([-1, -1, 0]), buff=.01).get_center()
        cp1 = CurvedArrow(start_point=start_point, end_point=end_point, color=BLACK)

        start_point = Dot().next_to(p0, direction=np.array([1, 1, 0]), buff=.01).get_center()
        end_point = Dot().next_to(p0o, direction=np.array([-1, 1, 0]), buff=.01).get_center()
        cp0 = CurvedArrow(start_point=start_point, end_point=end_point, angle=-1.9, color=BLACK)

        start_point = Dot().next_to(q0, direction=np.array([1, 1, 0]), buff=.01).get_center()
        end_point = Dot().next_to(q0o, direction=np.array([-1, 1, 0]), buff=.01).get_center()
        cq0 = CurvedArrow(start_point=start_point, end_point=end_point, angle=-1.9, color=BLACK)

        start_point = Dot().next_to(q1, direction=np.array([1, -1, 0]), buff=.01).get_center()
        end_point = Dot().next_to(q1o, direction=np.array([-1, -1, 0]), buff=.01).get_center()
        cq1 = CurvedArrow(start_point=start_point, end_point=end_point, color=BLACK)
        carrier_v = VGroup(cp0, cp1, cq0, cq1)
        self.play(Create(cp1))
        self.next_slide()
        self.play(Create(cp0))
        self.next_slide()
        self.play(Create(cq0))
        self.next_slide()
        self.play(Create(cq1))
        self.next_slide()
        self.play(FadeOut(carrier_v))
        self.play(Create(cp0.next_to(ORIGIN, direction=np.array([0, 1, 0]), buff=1.1)))
        self.next_slide()
        self.play(Create(cq1.next_to(ORIGIN, direction=np.array([0, -1, 0]), buff=1.1)))
        self.next_slide()
        self.play(FadeOut(cp0), FadeOut(cq1))
        # carrier edges
        both = Circle(color=BLACK).surround(output)
        start_pt = Dot().next_to(square_input.get_left(), direction=np.array([1, 0, 0]), buff=.01)
        end_pt = Dot().next_to(both.point_at_angle(180 * DEGREES), direction=np.array([-1, 0, 0]), buff=.01)
        cleft = Arrow(start=start_pt, end=end_pt, color=BLACK)
        self.play(Create(cleft))
        self.next_slide()
        self.wait_time_between_slides = .1
        self.play(Create(both))
        self.next_slide()
        self.wait_time_between_slides = 0
        self.play(FadeOut(cleft))
        start_pt = Dot().next_to(square_input.get_right(), direction=np.array([1, 0, 0]), buff=.01)
        cright = Arrow(start=start_pt, end=end_pt, color=BLACK)
        self.play(Create(cright))
        self.next_slide()
        self.finish()


class DC(BlackSlide):
    def construct(self):
        super().construct()
        title = Title("An abstract theorem about distributed computing")
        self.create_title(title)
        I = MathTex(r"I").move_to(UL + LEFT)
        SO = (MathTex(r"SO", substrings_to_isolate="S")
              .move_to(UR + RIGHT)
              .save_state())
        SP = (MathTex(r"SP", substrings_to_isolate="S")
              .move_to(DOWN * 2)
              .save_state())

        task = Arrow(I.get_center(), SO.get_center(), color=BLACK, buff=.5, stroke_width=3)
        task_t = LabeledDot(MathTex(r"\mathcal{T}'"), point=task.get_center() + UP * .5)

        protocol = Arrow(I.get_center(), SP.get_center(), color=BLACK, buff=.5, stroke_width=3)
        protocol_t = LabeledDot(MathTex(r"\mathcal{E}"), point=protocol.get_center() + LEFT * .5)

        decision = Arrow(SP.get_center(), SO.get_center(), color=AZUL, buff=.5, stroke_width=3)
        decision_t = (MathTex(r"Sd", substrings_to_isolate="S")
                      .move_to(decision.get_center() + RIGHT * .5)
                      .save_state())
        self.play(AnimationGroup(Write(I), Write(SO), Write(task), Write(task_t)))
        self.next_slide()

        self.play(AnimationGroup(Write(SP), Write(protocol), Write(protocol_t)))
        self.next_slide()

        guarda = VGroup(I, task, task_t, protocol, protocol_t)
        self.play(FadeOut(guarda))
        self.play(AnimationGroup(Unwrite(SO[0]),
                                 Unwrite(SP[0])))
        self.next_slide()

        self.play(AnimationGroup(Write(decision), Write(decision_t[1])))
        self.next_slide()
        self.play(AnimationGroup(FadeIn(guarda),
                                 Write(decision_t[0]),
                                 Restore(SO),
                                 Restore(SP)))
        self.next_slide()
        leq = MathTex(r"\leq").move_to(ORIGIN)
        self.play(Write(leq))
        NewI = MathTex(r"\Psi_{n}G").move_to(I)
        Newprotocol_t = LabeledDot(MathTex(r"\operatorname{WF}"), point=protocol.get_center() + LEFT * 1)
        NewSP = (MathTex(r"S(\operatorname{WF}(\Psi_{n}G))")
                 .move_to(SP)
                 .save_state())
        NewT = LabeledDot(MathTex(r"\mathcal{T}"), point=task_t.get_center())
        self.next_slide()
        self.play(AnimationGroup(Transform(I, NewI),
                                 Transform(protocol_t, Newprotocol_t),
                                 Transform(SP, NewSP),
                                 Transform(task_t, NewT)))
        all = VGroup(NewI, SO, NewSP, decision, decision_t, protocol, task, task_t)
        IG = MathTex(r"I").move_to(NewI)
        SPG = MathTex(r"S(\operatorname{WF}(I))").move_to(NewSP)
        task_t_prime = LabeledDot(MathTex(r"\mathcal{T}'"), point=task.get_center() + UP * .5)
        I_must_be_G_free = VGroup(MathTex(r"G"), Text(" acts freely on "), MathTex(r"I")).arrange(RIGHT)
        I_must_be_G_free.scale(.6)
        I_must_be_G_free.move_to(IG.get_center()+LEFT*2+UP)
        self.next_slide()
        self.play(AnimationGroup(Transform(I, IG),
                                 Transform(SP, SPG),
                                 Transform(task_t, task_t_prime),
                                 FadeOut(leq, decision, decision_t)))
        self.next_slide()
        fade_text(self, I_must_be_G_free)
        self.play(FadeOut(I, SP, SO, task, protocol, protocol_t, task_t))
        self.play(Uncreate(title))
        self.next_slide()
        protocolG = Arrow(IG.get_center(), SPG.get_center(), color=BLACK, buff=.5, stroke_width=3)
        allG = VGroup(IG, SPG, protocolG).shift(UP + LEFT * 4)
        start_point = Dot().next_to(IG, direction=np.array([1, 1, 0]), buff=.1).get_center()
        end_point = Dot().next_to(SO, direction=np.array([50, -40, 0]), buff=.01).get_center()
        taskG = CurvedArrow(start_point, end_point, color=BLACK, stroke_width=3, angle=-1.9)
        taskG_t = LabeledDot(MathTex(r"\mathcal{T}'"), point=taskG.get_center() + UP)

        allG.add(taskG)
        allG.add(taskG_t)
        all.add(allG.shift(UL))
        all.shift(DOWN + RIGHT * 2.5)
        funcion = Arrow(start=IG.get_center(),
                        end=NewI.get_center() + (RIGHT * .5 + DOWN * .2),
                        color=BLACK,
                        buff=1,
                        stroke_width=3)
        funcion_t = LabeledDot(MathTex(r"f'"), point=funcion.get_center() + UP * .5)
        funcion_completa = VGroup(funcion_t, funcion).scale(.8)
        task_t_2 = LabeledDot(MathTex(r"\mathcal{T}"), point=task_t.get_center() + UP * .5)
        #Transform(task_t, task_t_2)
        all.remove(task_t)
        all.add(task_t_2)
        self.play(Write(all.scale(.8)))
        self.next_slide()

        self.play(Write(funcion_completa))
        self.next_slide()
        funcion2 = Arrow(start=SPG.get_center(),  # + (LEFT * .5),
                         end=NewSP.get_center(),  # + (RIGHT * .5 + DOWN * .2),
                         color=AZUL, buff=.5, stroke_width=3)
        funcion2_t = LabeledDot(MathTex(r"Sf'"), point=funcion2.get_center() + DOWN * .6 + LEFT * .5)
        funcion2_completa = VGroup(funcion2_t, funcion2).scale(.8)
        self.play(Write(funcion2_completa))
        self.next_slide()
        self.finish()


class Gracias(BlackSlide):
    def construct(self):
        super().construct()
        self.play(Create(Text("Thank you!")))
