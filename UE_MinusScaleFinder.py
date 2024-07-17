import unreal

def MinusScaleFinder () :
    unrealEditorSubsystem = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem)
    editorActorSubsytem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    world = unrealEditorSubsystem.get_editor_world()
    actorArr = unreal.GameplayStatics.get_all_actors_of_class(world, unreal.StaticMeshActor)
    
    selectableActor= []
    for actor in actorArr :
        scale : unreal.Vector = actor.get_actor_scale3d()
        if scale.x <= 0 or scale.y <= 0 or scale.z <= 0 :
            selectableActor.append(actor)
            
    editorActorSubsytem.select_nothing()
    if len(selectableActor) != 0 :
        for actor in selectableActor :
            editorActorSubsytem.set_actor_selection_state(actor, True)
        print ("I gotcha!")
    else : print("There's nothing minus scale.")

MinusScaleFinder()