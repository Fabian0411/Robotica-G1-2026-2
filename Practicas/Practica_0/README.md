# Práctica 0: Nodos Publicador y Subscriptor en ROS 2
**Materia:** Robótica 2135 
**Semestre:** 2026-2  
**Autor:** Ortiz Carreño Fabián 

---

## 1. Objetivo de la Práctica
Desarrollar y comprender la comunicación asíncrona entre nodos en ROS 2 mediante la creación de un sistema de conversión de unidades de velocidad angular. Se programó un nodo publicador que genera una señal senoidal simulando Revoluciones Por Minuto (RPM) y un nodo subscriptor-publicador que intercepta dicha señal, la transforma a radianes por segundo (rad/s) y la republica en un nuevo tópico.

---

## 2. Marco Teórico: Nodos en ROS 2

Como parte de la fundamentación de esta práctica, es esencial comprender la unidad básica de procesamiento en la arquitectura de ROS 2: **los nodos**.

### ¿Qué son los nodos?
En el ecosistema de ROS (Robot Operating System), un nodo es un proceso ejecutable independiente que realiza tareas de computación específicas. En lugar de programar un robot mediante un único código monolítico y gigantesco, ROS propone una arquitectura distribuida (un grafo) donde múltiples nodos operan simultáneamente y se comunican entre sí [1]. 

### ¿Cómo funcionan?
En ROS 2, los nodos están construidos sobre el estándar de comunicación DDS (*Data Distribution Service*), lo que les permite descubrirse automáticamente en una red local sin necesidad de un nodo maestro (como ocurría en ROS 1). 
Los nodos funcionan interactuando bajo distintos paradigmas de comunicación [2]:
* **Tópicos (Publish/Subscribe):** Un nodo transmite un flujo de datos continuo (como los valores de nuestro motor) para que cualquier otro nodo interesado lo escuche de forma asíncrona.
* **Servicios (Request/Reply):** Comunicación síncrona donde un nodo pide un dato puntual y espera la respuesta.
* **Acciones:** Para tareas largas e ininterrumpibles (como mover un brazo robótico), donde se requiere retroalimentación constante.

### ¿Para qué sirven en la robótica mecatrónica?
La utilidad principal de los nodos es la modularidad y la tolerancia a fallos. Sirven para dividir el control de un robot en pequeños bloques funcionales independientes. Por ejemplo, en un sistema robótico quirúrgico, un nodo puede encargarse exclusivamente de leer los encoders de los motores, otro nodo de procesar la cinemática inversa, y otro de la interfaz gráfica. Si el nodo de la interfaz gráfica se traba o falla, el nodo de control de motores sigue funcionando de manera segura, evitando catástrofes en tiempo real [2].

---

## 3. Configuración del Entorno y Requisitos Previos

Para la correcta ejecución de este paquete, se trabajó sobre una Máquina Virtual con Linux, utilizando **ROS 2 Jazzy Jalisco**. A continuación, se documentan los comandos utilizados en clase para la preparación del entorno de trabajo, instalación de dependencias y activación de licencias.

### 3.1 Creación del Paquete y licencia MIT
El paquete fue generado inicialmente desde la terminal utilizando las herramientas de ROS 2, declarando desde el inicio el tipo de compilación (Python) y la licencia de código abierto (MIT):
```bash
ros2 pkg create --build-type ament_python --license MIT p0_py
```
### 3.2. Activación del Entorno y ROS 2
Siempre que se abre una nueva terminal, es necesario cargar las variables de entorno de ROS 2:
```bash
# Cargar la instalación principal de ROS 2 Jazzy
source /opt/ros/jazzy/setup.bash
```
### 3.3 Instalación de dependecias (rosdep)
Para asegurar que todas las librerias necesarias estén presentes en la máquina antes de compilar;
```bash
sudo rosdep init
rosdep update 
rosdep install -i --from-path src --rosdistro jazzy -y
```
---

## 4. Arquitectura del Software (Desarrollo)

La práctica consta del paquete `p0_py` que contiene dos nodos principales:

### 4.1. Nodo Generador (`generador_rpm.py`)
Actúa como un publicador puro. Utiliza el reloj del sistema para calcular el valor de una función senoidal.
- **Tópico de publicación:** `/rpm`
- **Tipo de mensaje:** `std_msgs/msg/Float32`
- **Frecuencia:** 10 Hz (0.1 segundos)
- **Función matemática:** f(t) = 100 * sin(t)

### 4.2. Nodo Convertidor (`convertidor_rads.py`)
Actúa como un nodo híbrido (Subscriptor y Publicador). Escucha los valores del primer nodo y les aplica la transformación matemática de Revoluciones por Minuto a radianes por segundo.
- **Tópico de subscripción:** `/rpm`
- **Tópico de publicación:** `/rad_s`
- **Fórmula aplicada:** rad/s = RPM * (2 * pi / 60)

---

## 5. Instrucciones de Compilación y Ejecución

Para ejecutar este proyecto, sigue estos pasos en la terminal de Linux:

**Paso 1: Compilar el espacio de trabajo**
```bash
cd ~/ROS2Dev/ws_sem26_2
colcon build
```
**Paso 2: Ejecutar el nodo Generador (Terminal 1)**
```bash
source install/setup.bash
ros2 run p0_py generador
```

**Paso 3: Ejecutar el nodo Convertidor (Terminal 2)**
```bash
cd ~/ROS2Dev/ws_sem26_2
source install/setup.bash
ros2 run p0_py convertidor
```

---

## 6. Referencias Bibliográficas

[1] Open Robotics, "Understanding ROS 2 nodes," *ROS 2 Documentation: Jazzy Jalisco*, 2024. [En línea]. Disponible en: [https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html). [Accedido: 18-mar-2026].

[2] S. Macenski, T. Foote, B. Gerkey, C. Lalancette, y W. Woodall, "Robot Operating System 2: Design, architecture, and uses in the wild," *Science Robotics*, vol. 7, no. 66, pp. 1-12, May 2022.

---

## 7. Licencia
Este proyecto está bajo la Licencia **MIT**. Consulta el archivo `package.xml` para más detalles sobre los derechos de uso, copia y modificación.

***
