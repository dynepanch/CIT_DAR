# CIT_DAR

* このレポジトリはROS2のパッケージです

# send.py
このノードは千葉工業大学未来ロボティクス学科の教授の名前を受け取ると,その教授が4sで受け持っている授業を返すサービスです.
通信にはcomposition_interfacesのLoadNodeに内蔵されているnode_nameとfull_node_nameを用いています。
サービス名は/kyojuです
動作例

```
$端末1 ros2 run CIT_DAR send

$端末2  ros2 service call /kyoju composition_interfaces/srv/LoadNode "node_name: 上田隆一"

requester: making request: composition_interfaces.srv.LoadNode_Request(package_name='', plugin_name='', node_name='上田 隆一', node_namespace='', log_level=0, remap_rules=[], parameters=[], extra_arguments=[])

response:
composition_interfaces.srv.LoadNode_Response(success=False, error_message='', full_node_name='ロボットシステム学', unique_id=0)

```



# LICENSE
このソフトウェアパッケージは3条項BSDライセンスの元、再配布及び使用が許可されています。


連絡先:s21C1016HB@s.chibakoudai.jp

LICENSE:https://github.com/dynepanch/CIT_DAR/blob/master/LICENSE
千葉工業大学先進工学部未来ロボティクス学科のロボットシステム学で作成したレポジトリです。

©2022 Ken Inaba
