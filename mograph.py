bl_info = {
    "name": "Motion Graph",
    "author": "IvanB",
    "description": "Motion Graph",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Object > Motion Graph",
    "warning": "",
    "category": "User"
}

# Blender imports
import bpy
import bpy.types

class MOGRAPH_PT_main_panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Motion Graph"
    bl_context = "objectmode"
    bl_category = "Motion Graph"

    def draw(self, context):
        layout = self.layout
       
        row = layout.row()
        row.operator("mograph.exec", text="Make Scene")

class MOGRAPH_OT_exec(bpy.types.Operator):
    """Operator for my first addon..."""     

    bl_idname = "mograph.exec"     
    bl_label = "Create Basic Scene"         
    bl_options = {'REGISTER'}
        

    def execute(self, context):
        #cleansing
        bpy.data.objects['Cube'].select_set(True)
        bpy.ops.object.delete(use_global=False, confirm=False)
        bpy.data.objects['Light'].select_set(True)
        bpy.ops.object.delete(use_global=False)

        #cam
        bpy.data.objects['Camera'].select_set(True)
        bpy.ops.object.rotation_clear(clear_delta=False)
        bpy.ops.object.location_clear(clear_delta=False)
        bpy.ops.transform.rotate(value=-1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.translate(value=(-0, -44.44, -0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        #bpy.ops.transform.rotate(value=3.14159, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
        bpy.ops.transform.rotate(value=3.14159, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
        

        #plane
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.object.scale[0] = 16
        bpy.context.object.scale[1] = 9
        bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        return {"FINISHED"}   

classes = (MOGRAPH_OT_exec, 
           MOGRAPH_PT_main_panel)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
        

if __name__ == "__main__":
    register()

