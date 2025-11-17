using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyShooting : MonoBehaviour
{
    public GameObject bulletPrefab;      // O prefab da bala do inimigo
    public float fireRate = 2f;          // Tempo entre os disparos
    public float bulletSpeed = 5f;       // Velocidade da bala
    public Transform[] firePoints;       // Array de pontos de disparo ao redor do inimigo

    private float fireTimer = 0f;

    // Update é chamado uma vez por frame
    void Update()
    {
        // Controle do tempo para disparo
        fireTimer += Time.deltaTime;

        // Verifica se já é hora de atirar novamente
        if (fireTimer >= fireRate)
        {
            Shoot();
            fireTimer = 0f;  // Reinicia o timer para o próximo disparo
        }
    }

    void Shoot()
    {
        // Loop pelos pontos de disparo ao redor do inimigo
        foreach (Transform firePoint in firePoints)
        {
            // Instancia a bala na posição de cada firePoint
            GameObject bullet = Instantiate(bulletPrefab, firePoint.position, firePoint.rotation);
            
            // Adiciona movimento à bala
            Rigidbody2D rb = bullet.GetComponent<Rigidbody2D>();
            if (rb != null)
            {
                rb.velocity = Vector2.left * bulletSpeed;
            }
        }
    }
}
