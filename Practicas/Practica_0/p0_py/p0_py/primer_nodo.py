#!urs/bin/env phython3

import rclpy 
from rclpy.node import Node
from std_msgs.msg import Int64


class MyNode(Node):
    def _init_(self):
        super()._init_("suscribe_node")
        self.counter_=0
        self.create_subscription(msg_type= Int64,callback= self. sub_cbck, topic="topic_1",qos_profile=10)
        self.publisher_counter_ =self.create_publisher(msg_tyoe= Int64, topic= 'counter_topic', qos_profile=10)
    def sub_cbck(self, msg):
        self.counter_+=msg
        new_msg = Int64()
        new_msg.data =self.counter_


        # self.publicador_m = self.create_publisher(msg_type= Int64, topic= "topic_1", qos_profile=10)
        # self.timer_ =self.create_timer(timer_period_sec=1.0, callback=self.cbck )
        # self.get_logger().info("activate node")
    # def cbck(self,msg):
    #     msg=Int64()
    #     msg.data = self.number_
    #     self.publicador_.pulish(msg)
    #     self.get_logger().info("Hola Mundo")
    def main(args=None):
        rclpy.init(args=args)
        node = MyNode()
        rclpy.spin(node)
        rclpy.shutdown()
    if __name__ =='_main_':
        main()