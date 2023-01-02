#SPDX-FileCopyrightText: 2022 Ken Inaba rightman20020920@yahoo.co,jp
#SPDX-Licence-Identifire: BSD-3-Clause
import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def cb(request, response):
    if request.name == "上田隆一":
        response.tips = "ロボットシステム学"
    elif request.name == "太田祐介":
        response.tips = "ロボットマニピレータ"
    elif request.name == "大川茂樹":
        response.tips = "数値解析学１・信号処理論"
    elif request.name == "王志東":
        response.tips = "センサ工学"
    elif request.name == "大久保宏樹":
        response.tips = "メカニクス２"
    elif request.name == "南方英明":
        response.tips = "未来ロボティクス総合セミナー"
    elif request.name == "青木岳史":
        response.tips = "未来ロボティクス総合セミナー"
    elif request.name == "藤江真也":
        response.tips = "未来ロボティクス総合セミナー"
    elif request.name == "林原靖男":
        response.tips = "未来ロボティクス総合セミナー"
    elif request.name == "藤井浩光 ":
        response.tips = "未来ロボティクス総合セミナー"
    elif request.name == "菊池耕生":
        response.tips = "ロボット設計制作論実習"
    elif request.name == "米田完":
        response.tips = "ロボット設計制作論実習"
    else: 
        response.tips = "未実装"

    return response

rclpy.init()
node = Node("send")
srv = node.create_service(Query, "kyoju", cb)
rclpy.spin(node)
