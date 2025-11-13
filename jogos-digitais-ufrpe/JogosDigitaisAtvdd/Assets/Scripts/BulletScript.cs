using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BulletScript : MonoBehaviour
{
    public GameObject bulletPrefab;  // Prefab da bala
    public float bulletSpeed = 10f;  // Velocidade da bala
    public Transform firePoint;      // Ponto de origem do disparo
    // Update is called once per frame


    void Start()
    {
    }
    void Update()
    {
        // Atira quando o jogador pressiona a barra de espaço
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Shoot();
        }
    }

    void Shoot()
    {
        // Instancia a bala no ponto de disparo
        GameObject bullet = Instantiate(bulletPrefab, firePoint.position, firePoint.rotation);


        // Obtém o Rigidbody2D da bala e aplica uma força para movê-la da esquerda para a direita
        Rigidbody2D rb = bullet.GetComponent<Rigidbody2D>();
        rb.velocity = Vector2.right * bulletSpeed;  // Movimento horizontal para a direita
    }
}
