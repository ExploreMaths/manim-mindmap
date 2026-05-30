from manim import *
from manim_mindmap import *

class Scene_Name(MovingCameraScene):
    def construct(self):
        self.camera.frame.set_width(50).move_to(10*RIGHT)
        node_style = NodeStyle()
        root = Node(Tex('球体积').to_edge(LEFT,buff = 0).shift(0.5*LEFT))

        A1 = Node(Tex('公元前3世纪'))
        A2 = Node(Tex('公元3世纪'))
        A3 = Node(Tex('公元5世纪'))
        A4 = Node(Tex('公元17世纪'))
        A5 = Node(Tex('公元18世纪'))

        for A in [A1, A2, A3, A4, A5]:
            root.add_child(A)

        A11 = Node(Tex('阿基米德平衡法'))
        A1.add_child(A11)

        A21 = Node(Tex('《九章算术》'))
        A22 = Node(Tex('刘徽：牟合方盖'))
        A2.add_child(A21)
        A2.add_child(A22)

        A221 = Node(Tex('球与牟合方盖的关系'))
        A222 = Node(Tex('牟合方盖体积？'))
        A22.add_child(A221)
        A22.add_child(A222)

        A31 = Node(Tex('祖暅：开立圆术'))
        A32 = Node(Tex('祖冲之：球体积'))
        A3.add_child(A31)
        A3.add_child(A32)

        A41 = Node(Tex('开普勒'))
        A42 = Node(Tex('卡瓦列里原理'))
        A4.add_child(A41)
        A4.add_child(A42)

        A51 = Node(Tex('松永良弼：会玉术'))
        A5.add_child(A51)

        self.play(
            LayoutAnimation(self,root,layout_type = LayoutType.TimeLine,node_style = node_style)
        )
        self.wait()

        A22.scale(1.5)
        A31.scale(1.5)
        A32.scale(1.5)
        A51.scale(0.8)

        self.play(
            LayoutAnimation(self,root,layout_type = LayoutType.TimeLine,node_style = node_style)
        )
        self.wait()

        root.alter_content(Tex(r'球\\体\\积'))
        
        self.play(
            LayoutAnimation(self,root,layout_type = LayoutType.TimeLine,node_style = node_style)
        )
        self.wait()

with tempconfig(
    {
        "quality": "low_quality", # low_quality   medium_quality   high_quality
        "preview": True,
        "tex_template":TexTemplateLibrary.ctex,
        # "renderer": "opengl"
    }
):
    Scene_Name().render()