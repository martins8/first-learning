using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class E1BulletDamage : MonoBehaviour
{
    public int damage = 1;  // Dano causado pela bala
    // Start is called before the first frame update
     void OnTriggerEnter2D(Collider2D other)
    {
        // Verifique se a bala colidiu com o jogador
        if (other.CompareTag("Player"))
        {
            // Aplica o dano ao jogador
            other.GetComponent<PlayerHealth>().TakeDamage(damage);

            // Destruir a bala após a colisão
            Destroy(gameObject);
        }
    }
}
