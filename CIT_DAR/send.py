import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def cb(request, response):
    if request.name == "上田隆一":
        response.tips = "ロボットシステム学"

    return response

rclpy.init()
node = Node("send")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)
