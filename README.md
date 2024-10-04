# aoki_lab

東京工科大学青木研究室のサーバーのGPUやCPUなどの使用状況を確認するシステムです。本システムは学内LANのみ（VPN接接可）有効です。

# Installation

GitHubからシステムを取得する
```bash
git clone https://github.com/c0b2113943/aoki_lab.git
```
Lyon-Envのディレクトリに移動する
```bash
cd aoki_lab/GPU_monitor_Fermi
```
aoki_lab/GPU_monitor_Fermi/workspace/get.sh　の編集を行う。「????????」をサーバーに合わせたパスワードを入れる。
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