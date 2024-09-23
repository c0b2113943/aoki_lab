import subprocess

# バックグラウンドでHTTPサーバーを起動するコマンド
command = "nohup python3 -m http.server 8000 &"

# コマンドを実行してサーバーをバックグラウンドで起動する
subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("HTTPサーバーがバックグラウンドで起動しました。")
