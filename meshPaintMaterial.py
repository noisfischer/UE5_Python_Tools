import unreal

# Retrieve an instance of the AssetTools class. Provides functions for asset creation, duplication, etc.
AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
# Access the MaterialEditingLibrary. Provides functions to edit materials and material instances.
MaterialEditLibrary = unreal.MaterialEditingLibrary
# Access the EditorAssetLibrary. Provides functions like loading, saving and modifying assets.
EditorAssetLibrary = unreal.EditorAssetLibrary

# Create new material
MeshPaintMaterial = AssetTools.create_asset("M_MeshPaint", "/Game/Materials/MasterMaterials", unreal.Material, unreal.MaterialFactoryNew())

# Add Texture Parameters for each Surface
base_colors = []
normals = []
orm = []

# Create constant variables for easy node placement
NodePositionX = -500
NodePositionY = -300

# Create Vertex Color Nodes
VertexColorNode_Color = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY * 10)
VertexColorNode_Color.set_editor_property('Desc', 'Base_Color')

VertexColorNode_Normal = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY * 8)
VertexColorNode_Normal.set_editor_property('Desc', 'Normal')

VertexColorNode_R = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY * 6)
VertexColorNode_R.set_editor_property('Desc', 'Occlusion')

VertexColorNode_G = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY * 4)
VertexColorNode_G.set_editor_property('Desc', 'Roughness')

VertexColorNode_B = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY * 2)
VertexColorNode_B.set_editor_property('Desc', 'Metallic')

# Create One Minus Nodes
OneMinusNode_Color = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 2, NodePositionY * 10)
OneMinusNode_Normal = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 2, NodePositionY * 8)
OneMinusNode_R = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 2, NodePositionY * 6)
OneMinusNode_G = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 2, NodePositionY * 4)
OneMinusNode_B = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 2, NodePositionY * 2)

# Create Base Color, Normal, and ORM Texture Parameters
for i in range(5):
    # Create Texture Parameters
    BaseColorParameter = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), NodePositionX, NodePositionY + i * 150)
    NormalParameter = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), NodePositionX, NodePositionY + i * 150)
    ORMParameter = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), NodePositionX, NodePositionY + i * 150)

    # Set names and sample types
    BaseColorParameter.set_editor_property("ParameterName", unreal.Name("BaseColor_{}".format(i)))
    BaseColorParameter.set_editor_property('sampler_source', unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)

    NormalParameter.set_editor_property("ParameterName", unreal.Name("Normal_{}".format(i)))
    NormalParameter.set_editor_property('sampler_source', unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
    NormalParameter.set_editor_property('sampler_type', unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)

    ORMParameter.set_editor_property("ParameterName", unreal.Name("ORM_{}".format(i)))
    ORMParameter.set_editor_property('sampler_source', unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
    ORMParameter.set_editor_property('sampler_type', unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)

    # Add the above to the arrays we previously defined
    base_colors.append(BaseColorParameter)
    normals.append(NormalParameter)
    orm.append(ORMParameter)

# Define lerp arrays
base_color_lerps = []
normal_lerps = []
orm_r_lerps = []
orm_g_lerps = []
orm_b_lerps = []

for i in range(5):
    base_color_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)
    normal_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)
    orm_r_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)
    orm_g_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)
    orm_b_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)

    # Add lerp node to corresponding arrays
    base_color_lerps.append(base_color_lerp)
    normal_lerps.append(normal_lerp)
    orm_r_lerps.append(orm_r_lerp)
    orm_g_lerps.append(orm_g_lerp)
    orm_b_lerps.append(orm_b_lerp)

# Connect Base Color Connections

# Connect Base Color Parameters to Lerps
MaterialEditLibrary.connect_material_expressions(base_colors[0], '', base_color_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[1], '', base_color_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[2], '', base_color_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[3], '', base_color_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[4], '', base_color_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[4], '', base_color_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_Color, '', base_color_lerps[0], 'Alpha')

# Connect Vertex Color Node to Base Color Lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'A', OneMinusNode_Color, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'R', base_color_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'G', base_color_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'B', base_color_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'A', base_color_lerps[4], 'Alpha')

# Make Lerp Connections
MaterialEditLibrary.connect_material_expressions(base_color_lerps[0], '', base_color_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(base_color_lerps[1], '', base_color_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(base_color_lerps[2], '', base_color_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(base_color_lerps[3], '', base_color_lerps[4], 'A')

# Connect Last Lerp to the Base Color Channel
MaterialEditLibrary.connect_material_property(base_color_lerps[4], '', unreal.MaterialProperty.MP_BASE_COLOR)

# Make Normal Map Connections

# Connect Normal Parameters to Lerps
MaterialEditLibrary.connect_material_expressions(normals[0], '', normal_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(normals[1], '', normal_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(normals[2], '', normal_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(normals[3], '', normal_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(normals[4], '', normal_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(normals[4], '', normal_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_Normal, '', normal_lerps[0], 'Alpha')

# Connect Vertex Color Node to Normal Lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'A', OneMinusNode_Normal, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'R', normal_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'G', normal_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'B', normal_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'A', normal_lerps[4], 'Alpha')

# Make Lerp Connections
MaterialEditLibrary.connect_material_expressions(normal_lerps[0], '', normal_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(normal_lerps[1], '', normal_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(normal_lerps[2], '', normal_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(normal_lerps[3], '', normal_lerps[4], 'A')

# Connect Last Lerp to the Normal Channel
MaterialEditLibrary.connect_material_property(normal_lerps[4], '', unreal.MaterialProperty.MP_NORMAL)

# Connect ORM Red Channel Parameters to Lerps (AMBIENT OCCLUSION)
MaterialEditLibrary.connect_material_expressions(orm[0], '', orm_r_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(orm[1], '', orm_r_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(orm[2], '', orm_r_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(orm[3], '', orm_r_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], '', orm_r_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], '', orm_r_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_R, '', orm_r_lerps[0], 'Alpha')

# Connect Vertex Color Node to ORM Red Channel Lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'A', OneMinusNode_R, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'R', orm_r_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'G', orm_r_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'B', orm_r_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'A', orm_r_lerps[4], 'Alpha')

# Make Lerp Connections
MaterialEditLibrary.connect_material_expressions(orm_r_lerps[0], '', orm_r_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(orm_r_lerps[1], '', orm_r_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(orm_r_lerps[2], '', orm_r_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(orm_r_lerps[3], '', orm_r_lerps[4], 'A')

# Connect Last Lerp to the Ambient Occlusion Channel
MaterialEditLibrary.connect_material_property(orm_r_lerps[4], '', unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)

# Connect ORM Green Channel Parameters to Lerps (ROUGHNESS)
MaterialEditLibrary.connect_material_expressions(orm[0], '', orm_g_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(orm[1], '', orm_g_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(orm[2], '', orm_g_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(orm[3], '', orm_g_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], '', orm_g_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], '', orm_g_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_G, '', orm_g_lerps[0], 'Alpha')

# Connect Vertex Color Node to ORM Green Channel Lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'A', OneMinusNode_G, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'R', orm_g_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'G', orm_g_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'B', orm_g_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'A', orm_g_lerps[4], 'Alpha')

# Make Lerp Connections
MaterialEditLibrary.connect_material_expressions(orm_g_lerps[0], '', orm_g_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(orm_g_lerps[1], '', orm_g_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(orm_g_lerps[2], '', orm_g_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(orm_g_lerps[3], '', orm_g_lerps[4], 'A')

# Connect Last Lerp to the Roughness Channel
MaterialEditLibrary.connect_material_property(orm_g_lerps[4], '', unreal.MaterialProperty.MP_ROUGHNESS)

# Connect ORM Blue Channel Parameters to Lerps (Metallic)
MaterialEditLibrary.connect_material_expressions(orm[0], '', orm_b_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(orm[1], '', orm_b_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(orm[2], '', orm_b_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(orm[3], '', orm_b_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], '', orm_b_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], '', orm_b_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_B, '', orm_b_lerps[0], 'Alpha')

# Connect Vertex Color Node to ORM Blue Channel Lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'A', OneMinusNode_B, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'R', orm_b_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'G', orm_b_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'B', orm_b_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'A', orm_b_lerps[4], 'Alpha')

# Make Lerp Connections
MaterialEditLibrary.connect_material_expressions(orm_b_lerps[0], '', orm_b_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(orm_b_lerps[1], '', orm_b_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(orm_b_lerps[2], '', orm_b_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(orm_b_lerps[3], '', orm_b_lerps[4], 'A')

# Connect Last Lerp to the Metallic Channel
MaterialEditLibrary.connect_material_property(orm_b_lerps[4], '', unreal.MaterialProperty.MP_METALLIC)

# Create Material Instance
MeshPaintInstance = AssetTools.create_asset("MeshPaintInstance", "/Game/Materials/MasterMaterials", unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())
MaterialEditLibrary.set_material_instance_parent(MeshPaintInstance, MeshPaintMaterial)
MeshPaintInstance.set_editor_property("Parent", MeshPaintMaterial)
MaterialEditLibrary.update_material_instance(MeshPaintInstance)

# Save Material and Instance
EditorAssetLibrary.save_asset("/Game/Materials/MasterMaterials/M_MeshPaint", True)
EditorAssetLibrary.save_asset("/Game/Materials/MasterMaterials/MeshPaintInstance", True)