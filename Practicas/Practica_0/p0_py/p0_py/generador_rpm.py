import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math
import time

class GeneradorRPM(Node):
    def __init__(self):
        # Nombramos el nodo
        super().__init__('generador_rpm')
        # Creamos el publicador en el tópico 'rpm'
        self.publisher_ = self.create_publisher(Float32, 'rpm', 10)
        # Hacemos que publique cada 0.1 segundos (10 Hz)
        timer_period = 0.1 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.start_time = time.time()

    def timer_callback(self):
        msg = Float32()
        # Calculamos el tiempo transcurrido
        t = time.time() - self.start_time
        # Generamos la señal senoidal (Amplitud de 100)
        msg.data = 100.0 * math.sin(t)
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: {msg.data:.2f} RPM')

def main(args=None):
    rclpy.init(args=args)
    nodo = GeneradorRPM()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()