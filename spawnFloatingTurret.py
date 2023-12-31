import unreal

# Get Editor World
editor_world = unreal.EditorLevelLibrary.get_editor_world()

#Get the editor viewport client
levelSubSys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
viewport = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_level_viewport_camera_info()

cameraLocation = viewport[0]
cameraRotation = viewport[1]

#Converts the rotation to a direction vector
cameraDirection = cameraRotation.get_forward_vector()

#Specifies distance from camera at which to spawn turret
distance = 500

#Calculates spawn location
spawnLocation = cameraLocation + cameraDirection * distance

# Get Blueprint class
blueprint = unreal.EditorAssetLibrary.load_asset('/Game/Blueprints/Turret/BP_FloatingTurret')
blueprint_class = unreal.load_class(None, blueprint.get_path_name())

#Spawn the floating turret blueprint
new_floating_turret = unreal.EditorLevelLibrary.spawn_actor_from_object(blueprint, spawnLocation)

# Output the name of the spawned actor (Optional)
print(f'Spawned actor with name: {new_floating_turret.get_name()}')