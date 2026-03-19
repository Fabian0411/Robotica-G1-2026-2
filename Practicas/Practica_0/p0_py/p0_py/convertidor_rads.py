import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math

class ConvertidorRads(Node):
    def __init__(self):
        super().__init__('convertidor_rads')
        
        self.subscription = self.create_subscription(
            Float64,
            'rpm',
            self.listener_callback,
            10)
            
        self.publisher_ = self.create_publisher(Float64, 'rad_s', 10)

    def listener_callback(self, msg):
        rpm = msg.data
        rad_s = rpm * (2.0 * math.pi / 60.0)
        
        nuevo_msg = Float64()
        nuevo_msg.data = rad_s
        self.publisher_.publish(nuevo_msg)
        
        self.get_logger().info(f'Recibido: {rpm:.4f} RPM | Transformado: {rad_s:.4f} rad/s')

def main(args=None):
    rclpy.init(args=args)
    nodo = ConvertidorRads()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()