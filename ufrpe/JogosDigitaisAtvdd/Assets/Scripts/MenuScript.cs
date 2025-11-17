using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MenuScript : MonoBehaviour
{
    private GUISkin newSkin;

	void Start()
	{
		newSkin = Resources.Load ("Menu Skin") as GUISkin;
	}

	void OnGUI()
	{
		const int buttonWidth = 84;
		const int buttonHeight = 60;

		GUI.skin = newSkin;

		if (GUI.Button (
			new Rect (Screen.width / 2 - (buttonWidth / 2), 
		         	(2 * Screen.height / 2.5f) - (buttonWidth / 2),
	         		buttonWidth, buttonHeight),
			"Start!")) 
		{
			Application.LoadLevel("Level1");
		}
	}
}
