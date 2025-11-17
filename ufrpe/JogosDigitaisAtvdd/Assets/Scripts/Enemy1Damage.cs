using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy1Damage : MonoBehaviour
{
    public int damage = 1;  // Dano que o inimigo causará ao jogador

    void OnCollisionEnter2D(Collision2D collision)
    {
        // Verifica se o inimigo colidiu com o jogador
        PlayerHealth player = collision.gameObject.GetComponent<PlayerHealth>();
        if (player != null)
        {
            // Aplica dano ao jogador
            player.TakeDamage(damage);
        }
    }
}
