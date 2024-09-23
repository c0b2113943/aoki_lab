# Pythonの公式イメージを使用
FROM python:3.9-slim

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y sshpass



# Pythonスクリプトと必要なファイルをコピー
COPY requirements.txt /install/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r /install/requirements.txt

# Webサーバ用にポートを公開
EXPOSE 8000



ENTRYPOINT ["bash"]
