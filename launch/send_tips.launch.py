#SPDX-FileCopyrightText: 2022 Ken Inaba rightman20020920@yahoo.co,jp
#SPDX-Licence-Identifire: BSD-3-Clause
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
import time
def generate_launch_description():
    send = launch_ros.actions.Node(
        package='CIT_DAR',
        executable='send',
    )
    time.sleep(5) 
    tips = launch_ros.actions.Node(
        package='CIT_DAR',
        executable='tips',
        output='screen'
    )

    return launch.LaunchDescription([send, tips])

#いろいろ思う事があるので、ここにだらだら書き連ねていく

#皆のためと時間もないのに一所懸命頑張って、掛けられる言葉は「遅くね？」の一言、何もしないのなら文句を言うな。
#「仕事を振れよ」と言うが、お前は津田沼祭のシフトにも来なかった。前に頼んだ部会ログ、一度だって思い出したこともないだろう。
#2月中に走りますとか、体のいいことばかりを言ってもう3月だ。設計を凝るのはいいがとっとと作れ。自分の都合だけで動く癖に、大事な仕事を任される立場にあると思っているのか。
#自分に信用がないのを思い出せ。

#書いてみると、思いのほかどうでもいい。さっき一瞬彼のことが嫌いになったが、吐き出してしまえばなんてことの無い。彼は相変わらずだったというだけだ。
#なるほど、裏垢を作る人間の気持ちが理解できた。おそらく、誰にでも見られるような場所に、誰にも見られないように置いておくことにも価値があるのだろう。この文章をネットのどこかに流しておくのもまたオツだろうか。

