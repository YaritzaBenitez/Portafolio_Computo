### ¿Qué es HPC?

High Performance Computing (HPC) agrupa múltiples ordenadores que colaboran para resolver tareas de gran complejidad, como simulaciones meteorológicas, análisis genómico o modelado financiero.

El ecosistema de herramientas open source para Linux se encarga de gestionar, acelerar y supervisar estos entornos colaborativos.



### 1. Gestión de trabajos y recursos

Para coordinar cientos o miles de nodos, es esencial disponer de un programador de trabajo que distribuya las tareas de forma inteligente y evite cuellos de botella.

**Slurm** destaca por su escalabilidad y tolerancia a fallos, pues no requiere cambios en el kernel ni servicios externos; muchas de las supercomputadoras más grandes del mundo lo emplean para asignar CPUs, GPUs y definir políticas de prioridad.

Por otro lado, **TORQUE** hereda la simplicidad de PBS, ofreciendo comandos familiares (`qsub`, `qstat`, etc.) y compatibilidad con scripts heredados, mientras que su sucesor **OpenPBS** añade rendimiento, seguridad y flexibilidad en la planificación de trabajos, ideal para entornos académicos y corporativos.



### 2. Programación paralela

Cuando una sola CPU no basta, el paralelismo se extiende dentro de un nodo o a través de una red de máquinas:

* Con **MPI** (por ejemplo OpenMPI o MPICH) cada proceso en un nodo puede intercambiar mensajes con otros en la red, acelerando simulaciones numéricas y modelados científicos.

* **OpenMP** simplifica la creación de hilos dentro de un programa en C/C++ o Fortran usando directivas, aprovechando todos los núcleos de cada servidor.

* En el caso de GPUs, **CUDA** pone al alcance miles de núcleos especializados, multiplicando el rendimiento en tareas de aprendizaje automático y procesamiento de grandes volúmenes de datos.

* Finalmente, **Charm++** introduce objetos paralelos con balance dinámico de carga, ocultando la complejidad de la asignación de tareas y mejorando la resiliencia de aplicaciones a gran escala.



### 3. Monitoreo y visualización

Detectar problemas antes de que afecten la producción requiere métricas en tiempo real:

* **Ganglia** recopila datos de CPU, memoria y red con mínimo impacto en cada nodo, organizándolos de forma jerárquica.

* **Prometheus** guarda métricas en series temporales y permite consultas avanzadas, mientras que complementa su visión con **Grafana**, que ofrece paneles interactivos para seguir tendencias y configurar alertas.

* Como alternativa, **Nagios** supervisa servicios críticos (SSH, NFS, espacio disco) y despliega notificaciones instantáneas en caso de fallo.



### 4. Sistemas de archivos distribuidos

Los HPC necesitan acceso rápido y simultáneo a enormes volúmenes de datos:

* **Lustre** divide archivos y metadatos entre servidores de almacenamiento, alcanzando anchos de banda agregados impresionantes.

* **BeeGFS** distribuye tanto datos como metadatos, facilitando despliegues sencillos y alto rendimiento en proyectos de inteligencia artificial.

* **Ceph** brilla por su versatilidad: ofrece bloques, objetos y un sistema de archivos completo, y crece de forma horizontal sin un punto único de fallo.



### 5. Contenedores especializados

Para reproducir entornos y simplificar instalaciones complejas:

* **Apptainer** (antes Singularity) ejecuta contenedores sin permisos de root, integrándose de forma nativa con GPUs, redes de alta velocidad y sistemas de archivos paralelos.

* Cada vez más, **Kubernetes** orquesta cargas de trabajo en contenedores, aportando autoescalado y alta disponibilidad, especialmente en clusters de aprendizaje automático.



### 6. Desarrollo y ciencia de datos

Acelerar la investigación y la colaboración también implica:

* **JupyterHub**, que facilita cuadernos interactivos multiusuario, ofreciendo entornos preconfigurados en el propio clúster.

* **Spack** y **EasyBuild**, dos gestores de compilación que resuelven dependencias de software científico, garantizando instalaciones reproducibles.

* Lenguajes como **Python** (con NumPy, SciPy, pandas) y **R**, que aportan bibliotecas optimizadas para cómputo numérico, estadística y visualización.



### 7. Seguridad y acceso

Proteger recursos y datos sensibles implica:

* **Kerberos**, que autentica usuarios mediante tickets cifrados sin transmitir contraseñas en texto claro.

* **MUNGE**, un sistema ligero para validar la identidad de procesos dentro de un clúster.

* Soluciones de directorio centralizado como LDAP o FreeIPA, y accesos federados mediante SSH con claves o plataformas IAM como Keycloak.



### 8. Automatización y provisión

Para desplegar y mantener la infraestructura:

* **Ansible** dirige configuraciones y tareas a decenas o cientos de nodos vía SSH, sin necesidad de agentes adicionales.

* **Terraform** define recursos de nube o locales de forma declarativa, replicando de manera predecible entornos de cálculo en cualquier proveedor.


