using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerDamage : MonoBehaviour
{
    public int damage;  // Dano que a bala causa
     [HideInInspector] public GameObject shooter;  // O jogador que disparou a bala

    void OnTriggerEnter2D(Collider2D collision)
    {
        // Ignora colisões com o jogador que disparou a bala
        if (collision.gameObject == shooter)
        {
            return;  // Não causa dano e não destrói a bala
        }

        // Verifica se colidiu com um inimigo
        Enemy1Health enemy = collision.GetComponent<Enemy1Health>();
        if (enemy != null)
        {
            enemy.TakeDamage(damage);  // Aplica dano ao inimigo
            Destroy(gameObject);  // Destroi a bala após o impacto
        }

    }
}
