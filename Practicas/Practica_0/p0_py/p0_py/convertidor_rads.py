import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math

class ConvertidorRads(Node):
    def __init__(self):
        super().__init__('convertidor_rads')
        
        # 1. Se suscribe al tópico 'rpm' (escucha)
        self.subscription = self.create_subscription(
            Float32,
            'rpm',
            self.listener_callback,
            10)
            
        # 2. Crea un publicador en el tópico 'rad_s' (habla)
        self.publisher_ = self.create_publisher(Float32, 'rad_s', 10)

    def listener_callback(self, msg):
        rpm = msg.data
        # Aplicamos la transformación matemática
        rad_s = rpm * (2.0 * math.pi / 60.0)
        
        # Creamos el nuevo mensaje y lo publicamos
        nuevo_msg = Float32()
        nuevo_msg.data = rad_s
        self.publisher_.publish(nuevo_msg)
        
        self.get_logger().info(f'Recibido: {rpm:.2f} RPM | Transformado: {rad_s:.2f} rad/s')

def main(args=None):
    rclpy.init(args=args)
    nodo = ConvertidorRads()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()