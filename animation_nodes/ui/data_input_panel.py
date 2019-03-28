import bpy
from bpy.props import *
from .. utils.layout import writeText
from .. tree_info import getNodesByType, getNodeByIdentifier

class ViewportInputPanel(bpy.types.Panel):
    bl_idname = "AN_PT_viewport_input_panel"
    bl_label = "Viewport Input"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AN"

    def draw(self, context):
        layout = self.layout
        nodes = getNodesByType("an_ViewportInputNode")
        for node in nodes:
            box = layout.box()

            row = box.row()
            row.label(text = node.label + ":")
            row.operator("an.toogle_viewport_input_box", text="",
                icon='TRIA_DOWN' if node.hidden else 'TRIA_RIGHT',
                emboss = False).identifier = node.identifier

            if not node.hidden:
                for socket in node.outputs[:-1]:
                    socket.drawSocket(box, text = socket.text, node = node, drawType = "TEXT_PROPERTY_OR_NONE")

class ToogleViewportInputBox(bpy.types.Operator):
    bl_idname = "an.toogle_viewport_input_box"
    bl_label = "Toogle Viewport Input Box"

    identifier: StringProperty(name = "Node Identifier")

    def execute(self, context):
        node = getNodeByIdentifier(self.identifier)
        node.hidden = not node.hidden
        return {"FINISHED"}
