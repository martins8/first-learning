using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerHealth : MonoBehaviour
{
    public int maxHealth;  // Vida máxima do jogador
    private int currentHealth;   // Vida atual do jogador
    
    // Start is called before the first frame update
    void Start()
    {
           // No início do jogo, a vida do jogador é a máxima
        currentHealth = maxHealth;
    }

    public void TakeDamage(int damage)
    {
        currentHealth -= damage;

        // Verifica se a vida caiu a 0 ou menos
        if (currentHealth <= 0)
        {
            Die();  // Chama a função de morte do jogador
        }
    }

    void Die()
    {
        // Aqui você pode adicionar a lógica de morte do jogador, como reiniciar o jogo
        Debug.Log("Jogador morreu!");
        Destroy(gameObject);  // Destroi o jogador
    }

    void OnDestroy()
    {
        Application.LoadLevel("GameOver");

    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
