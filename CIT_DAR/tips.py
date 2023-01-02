#SPDX-FileCopyrightText: 2022 Ken Inaba rightman20020920@yahoo.co,jp
#SPDX-Licence-Identifire: BSD-3-Clause
import rclpy
from rclpy.node import Node
from composition_interfaces.srv import LoadNode

def main():
    rclpy.init()
    node = Node("tips")
    client = node.create_client(LoadNode, 'kyoju')
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('ちょっと待ってね')

    req = LoadNode.Request()
    req.node_name = "上田隆一"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("subject: {}".format(response.full_node_name))
            break
    req.node_name = "大川茂樹"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("subject: {}".format(response.full_node_name))
            break
    req.node_name = "太田祐介"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("subject: {}".format(response.full_node_name))
            break
    
    req.node_name = "菊池耕生"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("subject: {}".format(response.full_node_name))
            break
    
    req.node_name = "大久保宏樹"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("subject: {}".format(response.full_node_name))
            break
    
    req.node_name = "林原靖男"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("subject: {}".format(response.full_node_name))
            break
    
    req.node_name = "青木岳史"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("subject: {}".format(response.full_node_name))
            break
    
    req.node_name = "王志東"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("subject: {}".format(response.full_node_name))
            break
    
    req.node_name = "南方英明"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("subject: {}".format(response.full_node_name))
            break
    
    req.node_name = "藤井浩光 "
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("subject: {}".format(response.full_node_name))
            break
    
    req.node_name = "米田完"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("subject: {}".format(response.full_node_name))
            break
    
    req.node_name = "藤江真也"
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("subject: {}".format(response.full_node_name))
            break
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

