using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;

public class Unity_CustomUtils : EditorWindow
{
    [MenuItem("Custom/Select Same Mesh &a")]
    static void SelectSameMesh() {
        List<GameObject> foundObjects = new List<GameObject>();

        GameObject selectedObject = Selection.activeGameObject;
        Mesh targetMesh = selectedObject.GetComponent<MeshFilter>().sharedMesh;
        if (targetMesh == null) {
            return;
        }
        foreach(MeshFilter meshFilter in FindObjectsOfType<MeshFilter>()) {
            if (meshFilter.sharedMesh != null) {
                if (targetMesh == meshFilter.sharedMesh) {
                    foundObjects.Add(meshFilter.gameObject);
                }
            }
        }
        Selection.objects = foundObjects.ToArray();
    }

    [MenuItem("Custom/Select Parent Object &s")]
    static void SelectParent() {
        GameObject[] selectedObjects = Selection.gameObjects;
        List<GameObject> tempList = new List<GameObject> ();
        foreach (GameObject obj in selectedObjects) {
            tempList.Add(obj.transform.parent.gameObject);
        }
        GameObject[] tempArr = tempList.ToArray();
        Selection.objects = tempArr;
    }

    [MenuItem("Custom/Clear Lightmap &d")]
    static void ClearLightmap () {
        MeshRenderer[] gameObjects = FindObjectsOfType<MeshRenderer>();
        foreach (MeshRenderer meshRenderer in gameObjects) {
            meshRenderer.lightmapIndex = -1;
            meshRenderer.lightmapScaleOffset = new Vector4 (0, 0, 0, 0);
        }

    }

}

