import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class DistancePublisher(Node):

    def __init__(self):
        super().__init__('distance_publisher')

        # Create a publisher for distance
        self.publisher = self.create_publisher(Float32, 'distance', 10)

        # Publish once every second
        self.timer = self.create_timer(1.0, self.send_distance)

    def send_distance(self):
        msg = Float32()

        # Generate a distance value
        msg.data = random.uniform(0.5, 5.0)

        # Publish the message
        self.publisher.publish(msg)

        # Print to terminal
        self.get_logger().info('Publish distance: %.2f m' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node = DistancePublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
