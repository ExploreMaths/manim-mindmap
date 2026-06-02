from manim import *
from CustomTool.ManimObject.mindmap import *

class Scene_Name(MovingCameraScene):
    def construct(self):
        self.camera.frame.set_width(25).move_to(RIGHT)
        root = Node(Tex('球体积').shift(LEFT*1.5))

        A1 = Node(Tex('公元前3世纪'))
        A2 = Node(Tex('公元3世纪'))
        A3 = Node(Tex('公元5世纪'))
        A4 = Node(Tex('公元17世纪'))
        A5 = Node(Tex('公元18世纪'))
        # 首次创建
        self.play(
            InsertNode(self,{root:[A1,A2,A3,A4,A5]},layout_type = LayoutType.Standard),
            run_time = 2
        )
        self.wait()

        A11 = Node(Tex('阿基米德平衡法'))

        A21 = Node(Tex('《九章算术》'))
        A22 = Node(Tex('刘徽：牟合方盖'))

        A221 = Node(Tex('球与牟合方盖的关系'))
        A222 = Node(Tex('牟合方盖体积？'))

        A31 = Node(Tex('祖暅：开立圆术'))
        A32 = Node(Tex('祖冲之：球体积'))

        A41 = Node(Tex('开普勒'))
        A42 = Node(Tex('卡瓦列里原理'))

        A51 = Node(Tex('松永良弼：会玉术'))

        # 插入节点
        for dic in [{A2:[A21,A22]},{A22:[A221,A222]},{A3:[A31,A32]},{A4:[A41,A42]}]:
            self.play(
                InsertNode(self,dic,layout_type = LayoutType.Standard)
            )
        self.play(
            InsertNode(self,{A1:[A11],A5:[A51]},layout_type = LayoutType.Standard),
        )
        self.wait()

        # 调整节点大小 + 修改节点样式
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
            ScaleNode(self,{A31:1.5,A32:1.5,A51:0.8},layout_type = LayoutType.Standard,node_style = node_style),
            run_time = 2
        )
        self.wait()

        # 修改节点内容
        self.play(
            AlterNode(self,{root:Tex(r'球\\体\\积',color = RED,font_size = 60)},layout_type = LayoutType.Standard),
            run_time = 2
        )
        self.wait()

with tempconfig(
    {
        "quality": "high_quality", # low_quality   medium_quality   high_quality
        "preview": True,
        "tex_template":TexTemplateLibrary.ctex,
        # "renderer": "opengl"
    }
):
    Scene_Name().render()