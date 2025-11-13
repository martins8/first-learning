using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy1Health : MonoBehaviour
{
    public int maxHealth;  // Vida máxima do inimigo
    private int currentHealth;
    // Start is called before the first frame update
    void Start()
    {
    // O inimigo começa com a vida máxima
        currentHealth = maxHealth;

    }
    // Função chamada para causar dano ao inimigo
    public void TakeDamage(int damage)
    {
        currentHealth -= damage;

        // Verifica se a vida do inimigo acabou
        if (currentHealth <= 0)
        {
            Die();
        }
    }

    void Die()
    {
        // Aqui você pode colocar a lógica de morte do inimigo
        Debug.Log("Inimigo destruído!");
        Destroy(gameObject);  // Destroi o inimigo ao morrer
    }

    void OnDestroy()
    {
        transform.parent.gameObject.AddComponent<GameOverScript>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
