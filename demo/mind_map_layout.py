from manim import *
from manim_mindmap import *

class Scene_Name(MovingCameraScene):
    def construct(self):
        self.camera.frame.set_width(25).move_to(RIGHT)
        root = Node(Tex('球体积').to_edge(LEFT))

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

        # 首次创建
        self.play(
            LayoutAnimation(self,root)
        )

        A221 = Node(Tex('球与牟合方盖的关系'))
        A222 = Node(Tex('牟合方盖体积？'))
        A22.add_child(A221)
        A22.add_child(A222)
        # 插入节点
        self.play(
            LayoutAnimation(self,root)
        )
        self.wait()

        A31 = Node(Tex('祖暅：开立圆术'))
        A32 = Node(Tex('祖冲之：球体积'))
        A3.add_child(A31)
        A3.add_child(A32)
        # 插入节点
        self.play(
            LayoutAnimation(self,root)
        )
        self.wait()

        A41 = Node(Tex('开普勒'))
        A42 = Node(Tex('卡瓦列里原理'))
        A4.add_child(A41)
        A4.add_child(A42)

        A51 = Node(Tex('松永良弼：会玉术'))
        A5.add_child(A51)
        # 插入节点
        self.play(
            LayoutAnimation(self,root)
        )
        self.wait()

        # 放缩节点
        A31.scale(1.5)
        A51.scale(0.8)
        self.play(
            LayoutAnimation(self,root)
        )
        self.wait()

        # 修改节点内容
        root.alter_content(Tex(r'球\\体\\积',color = RED,font_size = 60))
        self.play(
            LayoutAnimation(self,root)
        )
        self.wait()

        # 修改节点、连线样式
        node_style = NodeStyle(
            node_style=[
                {'color':RED,'stroke_width':20,'stroke_opacity':0.5},
                {'color':YELLOW,'stroke_width':12,'stroke_opacity':0.5},
                {'color':BLUE,'stroke_width':6,'stroke_opacity':0.5},
                {'color':GREEN,'stroke_width':3,'stroke_opacity':0.5},
            ],
            line_style=[
                {'color':RED,'stroke_width':20,'stroke_opacity':0.5},
                {'color':YELLOW,'stroke_width':12,'stroke_opacity':0.5},
                {'color':BLUE,'stroke_width':6,'stroke_opacity':0.5},
                {'color':GREEN,'stroke_width':3,'stroke_opacity':0.5},
            ]
        )
        self.play(
            LayoutAnimation(self,root,node_style = node_style)
        )
        self.wait()

        # 修改布局
        layout_config = LayoutConfig(
            direction = LEFT
        )
        self.play(
            LayoutAnimation(self,root,layout_config = layout_config,node_style = node_style),
            self.camera.frame.animate.shift(12*LEFT)
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