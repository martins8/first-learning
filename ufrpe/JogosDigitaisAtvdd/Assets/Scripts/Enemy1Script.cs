using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy1Script : MonoBehaviour
{
    public float moveSpeed = 5f;  // Velocidade do inimigo
    private Vector2 movementDirection;  // Direção de movimento do inimigo

    private Rigidbody2D rb;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();

        // Define uma direção inicial aleatória
        movementDirection = new Vector2(Random.Range(-1f, 1f), Random.Range(-1f, 1f)).normalized;
    }

    void Update()
    {
        // Move o inimigo na direção atual
        rb.velocity = movementDirection * moveSpeed;
    }

    void OnCollisionEnter2D(Collision2D collision)
    {
        // Quando colidir com algo, muda a direção do movimento
        movementDirection = Vector2.Reflect(movementDirection, collision.contacts[0].normal);
    }
}
