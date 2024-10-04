# aoki_lab

東京工科大学青木研究室のサーバーのGPUやCPUなどの使用状況を確認するシステムです。本システムは学内LANのみ（VPN接接可）有効です。

# Installation

GitHubからシステムを取得する
```bash
git clone https://github.com/c0b2113943/aoki_lab.git
```
ディレクトリを移動する
```bash
cd aoki_lab/GPU_monitor_Fermi
```
`aoki_lab/GPU_monitor_Fermi/workspace/get.sh`の編集を行う。case文内の「????????」をサーバーに合わせたパスワードを入れる。場合によっては「＠」前の「aokilab_admin」も適宜ログインユーザーに置き換える。
```bash
timeout 5s sshpass -p "????????" ssh -o StrictHostKeyChecking=no "aokilab_admin@$ip_address" 'bash -s' < cpu.sh > "$log_file"
```
Docker-composeでビルドとイメージの起動、GPUモニターの起動をする
```bash
bash start.sh
```



# ReleaseNote
## 2024-9-23　Version1.0-release
* ファストコミット。
## 2024-10-04　Version1.0a-release
* タイムアウトエラーを追加しました。これにより一部サーバーでSSH接続のエラーが出た時スキップしGPU情報更新が止まらないようになりました。
## 2024-10-05　Version2.0-release
* タイムアウトエラーが続けて二回起こった時、サーバーエラー通知をslackにて通知し、復旧時復旧したことを通知するようにしました。

* しかしデフォルトではこの機能はOFFになっているので、ONにしたいときは`aoki_lab/GPU_monitor_Fermi/workspace/start_py.sh` の５行目 `bash /workspace/get.sh` を `bash /workspace/get_add_SLACK.sh` に書き換えてください。