### ¿Qué es HPC?

Es el uso de varias computadoras trabajando juntas para resolver problemas complejos, como lo son simulaciones climáticas, análisis de ADN, etc.

El uso de cada herramienta dependera de su categoria.

### 1. **Gestión de trabajos y recursos**
Estas herramientas permiten controlar qué trabajos se ejecutan, cuándo y en qué computadoras del clúster. Son muy utiles cuando se tienen 
muchos usuarios y nodos, ya que, se asignan los recursos de forma inteligente para evitar conflictos y optimizar el rendimiento.

* Slurm: Esta diseñado para clústeres Linux grandes y pequeños, siendo altamente escalable y tolerante a fallos. Permitiendo asignar
  recursos de cómputo, gestionar colas de trabajos y políticas de planificación mediante plugins. No requiere modificaciones al kernel
  ni servicios externos, debido a ello es muy usado en supercomputadoras por su rendimiento y versatilidad. 

* TORQUE: Es un gestor distribuido de recursos basado en el sistema de colas Portable Batch System. Controlando el envío y supervisión
  de jobs en un clúster. Por ejemplo, TORQUE deriva del proyecto OpenPBS original. Proporciona comandos estándar (`qsub`, `qstat`, etc.)
  y permite políticas de colas y prioridades. Aunque en algunos entornos ha sido remplazado por Slurm, sigue en uso en sistemas basados en PBS/Moab.
  *Ventaja:* compatibilidad con scripts y flujos de trabajo PBS antiguos. Documentación: [TORQUE PBS](http://www.adaptivecomputing.com/products/open-source/torque/) (Adaptive Computing).

* OpenPBS: Es la versión moderna de PBS mantenida por Altair (anteriormente como open source). Optimiza la planificación de trabajos en entornos HPC (clusters, nubes, supercomputadoras). OpenPBS es rápido, escalable, seguro y tolerante a fallos. Ofrece amplias opciones de políticas de scheduling y soporte para sistemas modernos. Se distribuye bajo licencia abierta y cuenta con comunidad activa.
  *Caso de uso:* Clusters académicos o comerciales que requieren un planificador robusto con compatibilidad PBS. Más info: [OpenPBS](https://openpbs.org).


### 2. **Programación paralela**
Nos permite escribir programas que usan varias computadoras a la vez. Haciendo que el software sea mucho más rápido al usar múltiples 
procesadores en paralelo.

Las aplicaciones HPC aprovechan paralelismo a nivel de múltiples núcleos/nodos. Destacan:

* **MPI (Message Passing Interface)** – por ejemplo *OpenMPI*, *MPICH*: Es el estándar de facto para paralelo en memoria distribuida. MPI permite que procesos en distintos nodos intercambien mensajes. OpenMPI es una implementación open source desarrollada por un consorcio académico-industrial. Ofrece escalabilidad, portabilidad y un amplio soporte de hardware. MPI se usa en simulaciones numéricas, cómputo científico, modelado, etc., donde un mismo programa corre en paralelo en varios nodos compartiendo datos por paso de mensajes.

* **OpenMP**: Es un estándar abierto de directivas de compilador para paralelismo en memoria compartida (threads) en C/C++ y Fortran. OpenMP permite paralelizar secciones de código simplemente con pragmas (por ejemplo `#pragma omp parallel for`). Es útil para aprovechar todos los núcleos de un nodo. Lo apoyan compiladores comunes (GCC, Intel, LLVM) y se emplea en HPC para acelerar bucles y regiones críticas en programas científicos.

* **CUDA**: Plataforma de programación paralela de NVIDIA para GPUs. CUDA permite ejecutar miles de hilos en la GPU, aprovechando su alta capacidad de procesamiento y ancho de banda de memoria (mucho mayor que la CPU). Es propietaria, pero es muy utilizada en HPC acelerado por GPU (por ejemplo en simulaciones numéricas, aprendizaje profundo, análisis de grandes datos). NVIDIA ofrece documentación completa: [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/).

* **Charm++**: Es un framework de programación paralela en C++ con ejecución soportada por un runtime adaptativo. Charm++ abstrae los detalles de procesadores e hilos, permitiendo dividir la aplicación en objetos paralelos (chare) con balance automático de carga. Ha sido usado en múltiples aplicaciones científicas de gran escala. Su runtime provee asignación dinámica de tareas y tolerancia a fallos. Es un proyecto activo de la UIUC (Parallel Programming Laboratory).

### 3. **Monitoreo y visualización**
Vigilan el uso de los recursos del clúster. Permitiendo detectar problemas y tomar decisiones para mejorar el desempeño del sistema.
Las herramientas de monitoreo permiten vigilar estado de nodos y métricas de rendimiento:

* **Ganglia**: Sistema escalable de monitoreo distribuido, enfocado en clústeres y grids HPC. Utiliza una arquitectura jerárquica donde cada nodo reporta métricas vía XML/XDR a instancias agregadoras, almacenando datos con RRDtool. Ganglia tiene baja sobrecarga por nodo y es BSD-licenciado. Se usa en miles de clústeres universitarios e industriales para recolectar métricas de CPU, memoria, red, etc. (ver [página oficial](http://ganglia.sourceforge.net)).

* **Prometheus**: Plataforma open source de monitoreo basada en métricas de series temporales. Prometheus recoge métricas mediante scraping HTTP desde *exporters* y las almacena en una base de datos TSDB eficiente. Tiene un lenguaje de consulta (PromQL) muy flexible para filtrar y agregar datos. Se integra fácilmente con gráficos en Grafana. Cada servidor Prometheus funciona independiente (con su almacenamiento local) y no requiere agentes adicionales. Es ampliamente usado en cloud y comienza a adoptarse en HPC para monitorear nodos, contenedores, GPUs, etc. (licencia Apache 2, código en GitHub).

* **Grafana**: Herramienta web open source de visualización de datos. Grafana permite crear dashboards interactivos con gráficos, alertas y paneles, conectándose a múltiples fuentes de datos (p. ej. Prometheus, InfluxDB, Graphite, Elasticsearch). Es una aplicación multiplataforma que produce gráficos y alertas basados en consultas definidas por el usuario. En HPC se suele usar junto con Prometheus o InfluxDB para mostrar tendencias de performance de recursos (CPU, memoria, red, sensores), facilitando la detección de cuellos de botella.

* **Nagios**: Software clásico de monitoreo de infraestructura open source. Nagios Core supervisa hosts y servicios definidos (por ejemplo, procesos, puertos de red, espacio en disco) y envía alertas ante fallos. Es maduro y ampliamente documentado. Aunque su enfoque tradicional (monitoreo intensivo de configuración) es distinto al modelo pull de Prometheus, muchos centros HPC lo usan para supervisar la salud de servicios (SSH, NFS, hardware) en conjunto con scripts de notificación. (Más info: [Nagios Core](https://www.nagios.org/projects/nagios-core/)).

### 4. **Sistemas de archivos paralelos**
Ayuda a que muchas computadoras accedan, lean y escriban a los mismos datos rápidamente sin ocasionar un cuello de botella.
Para datos masivos y I/O de alta velocidad, se emplean:

* **Lustre**: Un sistema de archivos paralelo open source ampliamente usado en supercomputadoras. Lustre divide los datos entre múltiples *OSS* (Object Storage Servers) y metadatos en *MDS*, permitiendo un ancho de banda agregado muy alto. Fue diseñado para entornos de simulación de clase líder (p. ej. top500). Soporta clusters de miles de nodos y ofrece herramientas de tuning y monitorización. Documentación en [lustre.org](https://lustre.org).

* **BeeGFS**: Sistema de archivos de clúster paralelo, optimizado para HPC, AI/ML y entornos de datos intensivos. Diseñado para alto rendimiento y escalabilidad, BeeGFS es independiente de hardware y fácil de desplegar. Divide metadatos y datos en nodos distribuidos para maximizar throughput. Viene en edición Community (código fuente disponible) y Enterprise (con alta disponibilidad). Se utiliza en investigación y empresas que requieren accesos rápidos a grandes conjuntos de datos.

* **Ceph**: Plataforma unificada de almacenamiento distribuido open source. Ceph provee block, objeto y sistema de archivos en un solo clúster. Escala horizontalmente distribuyendo datos con el algoritmo CRUSH. Ofrece alta tolerancia a fallos al replicar o usar codificación de borrado. En HPC se usa principalmente CephFS (sistema de archivos POSIX) y RADOS (objeto) para almacenamiento compartido en grandes infraestructuras. Ventajas: flexibilidad, escalabilidad y licenciamiento libre.

### 5. **Contenedores para HPC**
Ejecutan aplicaciones en entornos controlados y portables, facilitando la instalación de softwares complejos, mantener reproducibilidad
y mover aplicaciones entre entornos.

Los contenedores facilitan la portabilidad de aplicaciones científicas, y sistemas como Kubernetes permiten orquestarlos:

* **Singularity / Apptainer**: Plataforma de contenedores orientada a HPC. Apptainer (nombre actual de Singularity) permite crear y ejecutar contenedores sin permisos de root, usando imágenes SIF portables. Se integra con recursos de HPC: por defecto accede a GPUs, redes de alta velocidad y sistemas de archivos paralelos del anfitrión. Fue diseñado originalmente para ejecutar aplicaciones complejas en clústeres HPC de forma reproducible, y ahora es ampliamente utilizado en HPC y entornos académicos.
  *Ventajas:* integración transparente con MPI, GPUs, facilidad de uso (solo archivos únicos) y modelo de seguridad simple (usuario dentro del contenedor es el mismo del host). Documentación: [Singularity/Apptainer User Guide](https://apptainer.org/docs).

* **Kubernetes**: Sistema open source de orquestación de contenedores desarrollado por CNCF. Kubernetes automatiza el despliegue, escalado y administración de aplicaciones en contenedores. Aunque fue concebido para microservicios en la nube, en HPC se está usando cada vez más para tareas específicas (por ejemplo, clústeres de AI/ML, portabilidad de pipelines, GPU scheduling). Kubernetes maneja pods (uno o varios contenedores) sobre nodos, soporta plugins de GPUs y brinda autoescalado y alta disponibilidad. En la práctica, algunas organizaciones integran Kubernetes con sus gestores HPC tradicionales (por ejemplo, operadores que vinculan Slurm/Torque con Kubernetes).
  *Ventaja:* Proporciona abstracción uniforme de contenedores y puede aprovechar infraestructuras on-premise o en la nube. Ver [documentación de Kubernetes](https://kubernetes.io).

## 6. Entornos de desarrollo y herramientas científicas

Herramientas para facilitar el desarrollo y ejecución de código científico en HPC:

* **JupyterHub**: Plataforma multiusuario para Jupyter Notebooks. JupyterHub permite que cada usuario acceda a su propio servidor de notebook (Python, R, Julia, etc.) a través de la web. Ideal para entornos educativos o colaborativos, ya que simplifica el acceso a entornos de cómputo sin preocuparse por instalaciones locales. Se usa en clusters HPC para ofrecer cuadernos interactivos usando los recursos del clúster (a menudo sobre contenedores o ambientes aislados). Más info: [JupyterHub docs](https://jupyterhub.readthedocs.io).

* **Spack**: Gestor de paquetes especializado en HPC. Permite instalar desde fuentes múltiples versiones de software científico (bibliotecas, herramientas, aplicaciones) con diversas dependencias, arquitecturas y compiladores. Spack no está ligado a un lenguaje específico: puede instalar ecosistemas Python, R, C/C++, Fortran, etc., cambiando fácilmente versiones de compiladores o microarquitecturas. Muy útil para crear builds reproducibles en supercomputadoras (usa recetas “packages” y genera módulos de entorno). Ver [Spack homepage](https://spack.io).

* **EasyBuild**: Framework de construcción e instalación de software para HPC. EasyBuild facilita compilar e instalar (sobre todo desde código fuente) paquetes científicos complejos. Define recetas (*easyconfigs*) que especifican las herramientas requeridas y opciones de compilación. Automatiza la creación de módulos de entorno listos para usar. Se utiliza en centros HPC para estandarizar instalaciones de librerías (p. ej. MPI, Python, paquetes numéricos) y garantizar consistencia entre usuarios. Guía: [EasyBuild docs](https://docs.easybuild.io).

* **R**: Lenguaje de programación open source enfocado en análisis estadístico y visualización. R proporciona un rico conjunto de paquetes para estadística, bioinformática, aprendizaje automático, etc. Ha sido adoptado en minado de datos y ciencia (genómica, econometría). Si bien R suele ejecutarse en CPU, se integra en flujos de trabajo HPC (por ejemplo, clusters para cálculos paralelos con Rmpi o SparkR).
  *Fuente:* Wikipedia R.

* **Python + SciPy stack**: Python es un lenguaje muy popular en HPC por sus bibliotecas científicas. NumPy ofrece arrays N-dimensionales y funciones matemáticas básicas; SciPy agrega algoritmos de optimización, integración numérica, estadística, EDO, etc. SciPy resume: “algoritmos fundamentales para cómputo científico”. Estas bibliotecas open source (licencia BSD) permiten escribir código de alto nivel mientras aprovechan código optimizado en C/Fortran bajo el capó. Además se usan pandas, matplotlib, scikit-learn, entre otras. (Ver [scipy.org](https://scipy.org)).

## 7. Seguridad y autenticación en entornos HPC

Asegurar el acceso a sistemas HPC es crítico. Se emplean soluciones de autenticación confiables y control de acceso:

* **Kerberos**: Protocolo de autenticación en red basado en tickets. Muchos centros HPC (por ejemplo, DoD HPCMP) emplean Kerberos para autenticar usuarios sin transmitir contraseñas en texto claro. Kerberos usa criptografía simétrica y un servidor de autenticación central (KDC) para emitir tickets. Así, los usuarios obtienen un ticket y con él acceden a sistemas HPC protegidos. Es fuerte y extensamente documentado.

* **MUNGE**: Servicio ligero de autenticación para clústeres HPC (MUNGE = *MUNGE Uid 'N' Gid Emporium*). Permite a un proceso validar la identidad (UID/GID) de otro proceso en un grupo de hosts con usuarios/grupos comunes, usando una clave criptográfica compartida. Es altamente escalable y no requiere privilegios root ni puertos especiales. Se utiliza frecuentemente con Slurm/OpenHPC para autenticar las tareas dentro del clúster y evitar que se forjen identidades de usuario.

* **LDAP / FreeIPA**: Muchos clústeres integran un servicio LDAP (o FreeIPA, Active Directory) para gestionar cuentas de usuario de forma centralizada. LDAP facilita mantener usuarios, grupos y políticas de acceso comunes. FreeIPA combina LDAP y Kerberos para una solución integrada de autenticación/autorización en Linux.

* **SSH**: El acceso SSH con claves es estándar. Se configura a menudo con control de acceso de red (firewalls) y escaneo de vulnerabilidades. En HPC se pueden usar herramientas de auditoría (por ejemplo, CILogon) para accesos federados.

* **Keycloak**: Plataforma open source de gestión de identidades y acceso (IAM) de Red Hat. Keycloak provee inicio de sesión único (SSO), federación de usuarios (LDAP/AD), autenticación fuerte y autorización fina. Es compatible con protocolos estándar (OpenID Connect, OAuth2, SAML). Puede usarse para gestionar usuarios en portales web de HPC o aplicaciones internas, simplificando la autenticación de múltiples servicios.

## 8. Automatización y aprovisionamiento

Para desplegar y gestionar la infraestructura HPC se emplean herramientas de *infraestructura como código* (IaC) y automatización:

* **Ansible**: Herramienta de automatización de TI open source. Ansible usa playbooks YAML para definir configuraciones y procedimientos a realizar en nodos vía SSH (sin agentes). Es simple y flexible, ideal para instalar software (e.g., MPI, bibliotecas, configuraciones) y mantener la consistencia en cientos de nodos HPC. Muchos centros HPC utilizan Ansible (o OpenStack-Ansible) para aprovisionar nuevos clústeres, aplicar parches y gestionar usuarios de forma automatizada. (Documentación: [docs.ansible.com](https://docs.ansible.com)).

* **Terraform**: Herramienta IaC de HashiCorp para aprovisionar infraestructuras en la nube o local. Permite definir instancias de cómputo, redes y almacenamiento de forma declarativa y reproducible. En entornos HPC se usa Terraform para desplegar nodos en la nube, configurar entornos virtualizados o integrar servicios (e.g., lanzar clusters en AWS, Azure u OpenStack). Terraform gestiona versiones de configuración y asegura provisiones de recursos de manera predictiva.

* **Otras herramientas**: Además existen soluciones específicas como Warewulf (para aprovisionamiento de nodos bare metal), Foreman/Cobbler (gestión de instalación de sistemas), o plataformas como OpenStack (nubes privadas HPC). Sin embargo, Ansible y Terraform son las más comunes en entornos HPC modernos.

