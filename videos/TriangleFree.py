        
from manim import *
from manim.animation.transform_matching_parts import TransformMatchingAbstractBase
from manim_revealjs import *


class FixedEndsLine(Line):
    def __init__(self, start=LEFT, end=RIGHT, buff=0, path_arc=None, **kwargs):
        super().__init__(start, end, buff, path_arc, **kwargs)
        self.add_updater(lambda e:         e.put_start_and_end_on(start.get_center(), end.get_center()))

class Triangle2(PresentationScene):
    # CONFIG={
	# 	"camera_config":{"background_color":"#475147"}
	# }
    def construct(self):

        self.camera.background_color = "#111"
        # self.add(ScreenRectangle(fill_color=RED))

        # useColors = TexTemplate()
        # useColors.add_to_preamble(r"\usepackage{xcolor}")


        # title = Tex("How many edges can there be in a triangle free graph?").shift(UP*2)

        waits = 1

        # self.add(title)
        # if waits == 1: self.wait()

        # self.end_fragment()


        v11 = Dot(LEFT + np.sqrt(2)*DOWN)
        v12 = Dot(RIGHT + np.sqrt(2)*DOWN)
        v21 = Dot()

        e1112 = FixedEndsLine(v11, v12)
        e1221 = FixedEndsLine(v12, v21)
        e2111 = FixedEndsLine(v21, v11)

        g3 = VGroup(VGroup(v11,v12,v21), VGroup(e1112, e1221, e2111))

        self.play(Create(g3, lag_ratio=0.4), run_time=2)

        # if waits == 1:
            # self.wait()

        self.end_fragment()

        self.play(e1112.animate.set_color(RED))

        x = Cross(scale_factor=0.3).move_to(e1112.get_center())

        self.play(Create(x))
        if waits == 1: self.wait(0.5)
        # self.end_fragment()
        self.play(FadeOut(x), FadeOut(e1112))
        # if waits == 1: self.wait()
        self.end_fragment()

        v22 = Dot(2*np.sqrt(2)*DOWN)
        e1122 = FixedEndsLine(v11, v22)
        e1222 = FixedEndsLine(v12, v22)

        g4 = VGroup(v22, VGroup(e1122, e1222))
        self.play(Create(g4, lag_ratio=0.5))

        # if waits == 1: self.wait()
        self.end_fragment()
        e2122 = FixedEndsLine(v21, v22).set_color(RED)
        
        self.play(FadeIn(e1112, e2122))
        if waits == 1: self.wait(0.5)
        self.play(FadeOut(e1112), FadeOut(e2122))

        # if waits == 1: self.wait()
        self.end_fragment()
        e1112.set_opacity(0)

        v13 = Dot(np.sqrt(2)*DOWN-0.001*LEFT)
        e1321 = FixedEndsLine(v13, v21)
        e1322 = FixedEndsLine(v13, v22)
        g5 = VGroup(v13, e1321, e1322)
        self.play(Create(g5, lag_ratio=0.5))
        # if waits == 1: self.wait()
        self.end_fragment()
        
        v23 = Dot(0.5*np.sqrt(2)*DOWN + RIGHT)
        e1123 = FixedEndsLine(v11,v23)
        e1223 = FixedEndsLine(v12, v23)
        e1323 = FixedEndsLine(v13,v23)
        g6 = VGroup(v23,e1123, e1223, e1323)
        self.play(Create(g6, lag_ratio=0.5))
        # if waits == 1: self.wait()
        self.end_fragment()
        
        v14 = Dot(0.5*np.sqrt(2)*DOWN + LEFT)
        e1421 = FixedEndsLine(v14, v21)
        e1422 = FixedEndsLine(v14, v22)
        e1423 = FixedEndsLine(v14,v23)
        g7 = VGroup(v14, e1421, e1422, e1423)
        self.play(Create(g7, lag_ratio=0.5))
        # if waits == 1: self.wait()
        self.end_fragment()


        v24 = Dot(1.25*np.sqrt(2)*DOWN + 0.25*LEFT)
        e1124 = FixedEndsLine(v11, v24)
        e1224 = FixedEndsLine(v12, v24)
        e1324 = FixedEndsLine(v13, v24)
        e1424 = FixedEndsLine(v14, v24)
        g8 = VGroup(v24, e1124, e1224, e1324, e1424)
        self.play(Create(g8, lag_ratio=0.5))
        # if waits == 1: self.wait()
        self.end_fragment()

        gLeft = VGroup(v11, v12, v13, v14)
        gRight = VGroup(v21, v22, v23, v24)
        self.play(gLeft.animate.set_color(RED), gRight.animate.set_color(BLUE))
        if waits == 1: self.wait()
        self.play(v11.animate.move_to(LEFT+UP),
            v12.animate.move_to(LEFT),
            v13.animate.move_to(LEFT-UP),
            v14.animate.move_to(LEFT-2*UP),
            v21.animate.move_to(RIGHT+UP),
            v22.animate.move_to(RIGHT),
            v23.animate.move_to(RIGHT-UP),
            v24.animate.move_to(RIGHT-2*UP),
            run_time=2)
        if waits == 1: self.wait()

        v15 = Dot(LEFT - 3.5*UP).set_color(RED)
        v25 = Dot(RIGHT - 3.5*UP).set_color(BLUE)
        e1415 = DashedLine(v14, v15).set_color(RED)
        e2425 = DashedLine(v24,v25).set_color(BLUE)
        e152 = VGroup(*[FixedEndsLine(v15,v) for v in [v21,v22,v23,v24, v25]])
        e251 = VGroup(*[FixedEndsLine(v25,v) for v in [v11,v12,v13,v14]])
        g10 = VGroup(e1415, v15, e2425, v25) + e152 + e251
        self.play(Create(g10, lag_ratio=0.1), run_time = 3)
        if waits == 1: self.wait(2)

        self.end_fragment()

        bipGraph = g3+g4+g5+g6+g7+g8+g10
        self.play(bipGraph.animate.shift(LEFT*3))
        # if waits == 1: self.wait(2)


        leftSide = MathTex(r"\text{Edge density          }").move_to(DOWN*0.1+RIGHT*2)
        right1 = MathTex(r"=\frac{\text{Number of edges in the graph}}{\text{Number of possible edges}}").next_to(leftSide, DOWN)
        self.play(Write(leftSide))
        self.play( Write(right1))
        # self.wait()
        self.end_fragment()

        right2 = MathTex(r"=\frac{\frac{n}{2}\cdot\frac{n}{2}}{\binom{n}{2}}").move_to(right1)
        self.play(Transform(right1, right2))
        # self.wait()
        self.end_fragment()

        # right3 = MathTex(r"=\frac{2n^2}{4n(n-1)}").move_to(right2)
        # self.play(Transform(right1, right3))
        # self.wait()

        right4 = MathTex(r"=\frac{1}{2}\frac{n^2}{n^2-n}").move_to(right2)
        self.play(Transform(right1, right4))
        # self.wait()      
        self.end_fragment()

        limit = MathTex(r"\to \frac{1}{2}\text{ as } n\to\infty").next_to(right4, DOWN).set_color(ORANGE)
        self.play(Write(limit))
        # self.wait()
        # self.wait()
        self.end_fragment()
