import unreal

def FoliageToActor(actor):
    foliage_components = actor.get_components_by_class(unreal.HierarchicalInstancedStaticMeshComponent)
    for comp in foliage_components:
        foliage_sm = comp.static_mesh
        if foliage_sm is not None:
            instances = comp.get_instance_count()
            for i in range(instances):
                transform = comp.get_instance_transform(i, True)
                #print (transform, foliage_sm.get_name())
                new_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor, transform.translation, transform.rotation.rotator())
                new_actor.set_actor_scale3d(transform.scale3d)
                
                sm_comp = new_actor.static_mesh_component
                sm_comp.set_static_mesh (foliage_sm)
                

unrealEditorSubSystem = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem)
currentWorld = unrealEditorSubSystem.get_editor_world()

foliage_actors = unreal.GameplayStatics.get_all_actors_of_class(currentWorld, unreal.InstancedFoliageActor)
for actor in foliage_actors:
    FoliageToActor(actor)