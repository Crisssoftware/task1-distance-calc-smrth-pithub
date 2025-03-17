import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float32
import math

class DistanceCalculate(Node):
    def __init__(self):
        super().__init__('distance_calculate')

        self.distance_publisher = self.create_publisher(Float32, '/turtle1/distance_from_origin', 10)

        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',  
            self.pose_callback,
            10
        )

    def pose_callback(self, msg):
        x = msg.x
        y = msg.y

        distance = math.sqrt(x**2 + y**2)
        self.get_logger().info(f'distance from origin: {distance:.2f}')

        distance_msg = Float32()
        distance_msg.data = distance
        self.distance_publisher.publish(distance_msg)

def main(args=None):
    rclpy.init(args=args)
    node = DistanceCalculate()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
