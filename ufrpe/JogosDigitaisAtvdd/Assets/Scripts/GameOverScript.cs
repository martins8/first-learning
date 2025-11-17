using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameOverScript : MonoBehaviour
{
    private GUISkin newSkin;

	void Start()
	{
		newSkin = Resources.Load ("Menu Skin") as GUISkin;
	}

	void OnGUI()
	{
		const int buttonWidth = 120;
		const int buttonHeight = 60;

		GUI.skin = newSkin;

        // tentar novamente
		if (GUI.Button (
			new Rect (Screen.width / 2 - (buttonWidth / 2), 
		         	(2 * Screen.height / 4) - (buttonWidth / 2),
	         		buttonWidth, buttonHeight),
			"Restart")) 
		{
			Application.LoadLevel("Level1");
		}

        // menu principal
        if (GUI.Button (
			new Rect (Screen.width / 2 - (buttonWidth / 2), 
		         	(2 * Screen.height / 2.5f) - (buttonWidth / 2),
	         		buttonWidth, buttonHeight),
			"Menu")) 
		{
			Application.LoadLevel("Menu");
		}
	}
}
