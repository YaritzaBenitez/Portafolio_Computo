Kenny Yaritza Benitez Renteral | 210300510

# Despliegue de Wordpress en HA con un LB con HAProxy y una BD sincronizada en 3 nodos. 

Inicamos una carpeta para posicionarnos en ella y clonar ahí el repositorio “GALERA - DOCKER”

foto 1

Ejecutamos el comando build para armar la imagen de galera. 
``
docker build -t mycluster/galera
``
foto 2

Y validamos que se haya creado bien la imagen galera
``docker images | grep galera``

Foto 3

Creamos una nueva red para poder trabajar en ella y que no haya cruce con otro proyecto.
``docker network create --subnet 172.18.0.0/16 galera``

Verificamos que se haya  creado correctamente con
``docker network ls``

Foto 4

Crea una carpeta llamada *galera* y nos hubicaremospara crear 3 carpetas una por cada nodo 

``
mkdir galera 
cd galera
mkdir node{1,2,3}
``

9.Nos posicionamos en cualquiera de las 3 carpetas de node (1, 2, 3).
10. Creamos un archivo con el nombre node1.cnf (lo mismo con 2 y 3) que contendrá lo
siguiente:
“[mysqld]
wsrep_cluster_address = "gcomm://172.18.0.101,172.18.0.102,172.18.0.103"
wsrep_cluster_name = "galera-cluster"
wsrep_node_name = "node1"
wsrep_node_address = "172.18.0.101"”
Solo cambiarán los campos “wsrep_node_name” y “wsrep_node_address” dependiendo en
que carpeta lo estés creando, en este caso como es en la carpeta “node2” se le nombre
node 2 y el ip 102 al final.
11.Después procedemos a darle permisos de ejecución a las carpetas
