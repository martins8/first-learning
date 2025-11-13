using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerScript : MonoBehaviour
{
    
    public float speed;

    // Update is called once per frame
    void Update()
    {
       Move();
    }

    void Move()
    {
         // Pega o input horizontal (A/D ou setas esquerda/direita)
        float moveX = Input.GetAxis("Horizontal");
        
        // Pega o input vertical (W/S ou setas cima/baixo)
        float moveY = Input.GetAxis("Vertical");

        // Cria um vetor de movimento com base nas entradas (X = Horizontal, Y = Vertical)
        Vector2 movement = new Vector2(moveY, moveX);

        // Move o personagem com base na direção e na velocidade configurada
        transform.Translate(movement * speed * Time.deltaTime);
    }

}
