import rclpy
from rclpy.node import Node
from composition_interfaces.srv import LoadNode

def cb(request, response):
    if request.node_name == "上田隆一":
        response.full_node_name = "ロボットシステム学"
    elif request.node_name == "太田祐介":
        response.full_node_name = "ロボットマニピレータ"
    elif request.node_name == "大川茂樹":
        response.full_node_name = "数値解析学１・信号処理論"
    elif request.node_name == "王志東":
        response.full_node_name = "センサ工学"
    elif request.node_name == "大久保宏樹":
        response.full_node_name = "メカニクス２"
    elif request.node_name == "南方英明":
        response.full_node_name = "未来ロボティクス総合セミナー"
    elif request.node_name == "青木岳史":
        response.full_node_name = "未来ロボティクス総合セミナー"
    elif request.node_name == "藤江真也":
        response.full_node_name = "未来ロボティクス総合セミナー"
    elif request.node_name == "林原靖男":
        response.full_node_name = "未来ロボティクス総合セミナー"
    elif request.node_name == "藤井浩光 ":
        response.full_node_name = "未来ロボティクス総合セミナー"
    elif request.node_name == "菊池耕生":
        response.full_node_name = "ロボット設計制作論実習"
    elif request.node_name == "米田完":
        response.full_node_name = "ロボット設計制作論実習"
    else: 
        response.full_node_name = "未実装"

    return response

rclpy.init()
node = Node("send")
srv = node.create_service(LoadNode, "LoadNode", cb)
rclpy.spin(node)
