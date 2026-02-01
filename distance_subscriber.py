import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class DistanceSubscriber(Node):

    def __init__(self):
        super().__init__('distance_subscriber')

        # Subscribe to published distance
        self.subscription = self.create_subscription(Float32, 'distance', self.receive_distance, 10)

    def receive_distance(self, msg):
        # Print received distance
        self.get_logger().info('Received distance: %.2f m' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node = DistanceSubscriber()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
