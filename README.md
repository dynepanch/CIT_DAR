# CIT_DAR

![test](https://github.com/dynepanch/CIT_DAR/actions/workflows/test.yml/badge.svg)

* このレポジトリはROS2のパッケージです

# send.py
このノードは千葉工業大学未来ロボティクス学科の教授の名前を受け取ると、その教授が4sで受け持っている授業を返すサービスです。

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
# tips.py
このノードはsend.pyを用いて千葉工業大学未来ロボティクス学科の4sの専門授業を列挙します。

動作例
```
$端末1 ros2 run CIT_DAR send

$端末2 ros2 run CIT_DAR tips

[INFO] [1672286253.443813900] [tips]: subject: ロボットシステム学
[INFO] [1672286253.444931600] [tips]: subject: 数値解析学１・信号処理論
[INFO] [1672286253.446124400] [tips]: subject: ロボットマニピレータ
[INFO] [1672286253.447131600] [tips]: subject: ロボット設計制作論実習
[INFO] [1672286253.448035200] [tips]: subject: メカニクス２
[INFO] [1672286253.448883500] [tips]: subject: 未来ロボティクス総合セミナー
[INFO] [1672286253.449806100] [tips]: subject: 未来ロボティクス総合セミナー
[INFO] [1672286253.450779700] [tips]: subject: センサ工学
[INFO] [1672286253.453418100] [tips]: subject: 未来ロボティクス総合セミナー
[INFO] [1672286253.454564000] [tips]: subject: 未来ロボティクス総合セミナー
[INFO] [1672286253.455868300] [tips]: subject: ロボット設計制作論実習
[INFO] [1672286253.456830800] [tips]: subject: 未来ロボティクス総合セミナー

```

# send_tips.launch.py
このノードはsendとtipsを同時に起動するlaunchファイルです。

テストの際に使用しています

```
$ ros2 launch CIT_DAR send_tips.launch.py

[INFO] [launch]: All log files can be found below /home/dynepanch/.ros/log/2022-12-29-13-01-17-612986-DESKTOP-NA5BOEE-2709
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [send-1]: process started with pid [2710]
[INFO] [tips-2]: process started with pid [2712]
[tips-2] [INFO] [1672286482.849743700] [tips]: subject: ロボットシステム学
[tips-2] [INFO] [1672286482.850665600] [tips]: subject: 数値解析学１・信号処理論
[tips-2] [INFO] [1672286482.851435500] [tips]: subject: ロボットマニピレータ
[tips-2] [INFO] [1672286482.852384700] [tips]: subject: ロボット設計制作論実習
[tips-2] [INFO] [1672286482.853121900] [tips]: subject: メカニクス２
[tips-2] [INFO] [1672286482.853819200] [tips]: subject: 未来ロボティクス総合セミナー
[tips-2] [INFO] [1672286482.854496400] [tips]: subject: 未来ロボティクス総合セミナー
[tips-2] [INFO] [1672286482.855160400] [tips]: subject: センサ工学
[tips-2] [INFO] [1672286482.855833500] [tips]: subject: 未来ロボティクス総合セミナー
[tips-2] [INFO] [1672286482.856506100] [tips]: subject: 未来ロボティクス総合セミナー
[tips-2] [INFO] [1672286482.857175700] [tips]: subject: ロボット設計制作論実習
[tips-2] [INFO] [1672286482.857928700] [tips]: subject: 未来ロボティクス総合セミナー
[INFO] [tips-2]: process has finished cleanly [pid 2712]

```


# テスト環境

* Ubuntu22.04.1LTS
* ros2-desktop
テストの結果は問題なく動作しています。

千葉工業大学の上田隆一先生のソースコードを授業のため流用しています。

Github Actionsのテストには千葉工業大学の上田隆一先生のコンテナを使用しています

URL:https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2

# LICENSE
このソフトウェアパッケージは3条項BSDライセンスの元、再配布及び使用が許可されています。

連絡先:s21C1016HB@s.chibakoudai.jp

千葉工業大学先進工学部未来ロボティクス学科のロボットシステム学で作成したレポジトリです。


LICENSE:https://github.com/dynepanch/CIT_DAR/blob/master/LICENSE

©2022 Ken Inaba
