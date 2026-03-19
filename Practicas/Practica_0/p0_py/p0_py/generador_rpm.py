import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math
import time

class GeneradorRPM(Node):
    def __init__(self):
        super().__init__('generador_rpm')
        self.publisher_ = self.create_publisher(Float64, 'rpm', 10)
        timer_period = 0.1 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.start_time = time.time()

    def timer_callback(self):
        msg = Float64()
        t = time.time() - self.start_time
        msg.data = 0.5 * math.sin(t) + 0.5
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: {msg.data:.4f} RPM')

def main(args=None):
    rclpy.init(args=args)
    nodo = GeneradorRPM()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()