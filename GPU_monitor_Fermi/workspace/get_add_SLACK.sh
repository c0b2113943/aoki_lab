
#!/bin/bash

IP_LIST=("10.202.82.13" "10.202.82.12" "10.202.82.121" "10.204.227.43" "10.204.227.42") # "10.204.227.44")

# Slack Webhook URL
SLACK_WEBHOOK_URL="your/slack/URL"

# エラーサーバーの状態を管理するファイル
error_file="Error_Log.txt"

# サーバーごとのタイムアウトカウントを保持する連想配列
declare -A timeout_count

# Slackにメッセージを送信する関数
send_slack_message() {
    local message="$1"
    payload="{\"text\": \"$message\"}"
    curl -X POST -H 'Content-type: application/json' --data "$payload" "$SLACK_WEBHOOK_URL"
}

# エラーファイルがなければ作成
touch $error_file

while true; do
    for ip_address in "${IP_LIST[@]}"; do
        echo "Processing $ip_address..."
        log_file="/workspace/log/$ip_address.txt"

        case "$ip_address" in
            "10.202.82.12")
                timeout 5s sshpass -p "????????" ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 "aoki_admin@$ip_address" 'bash -s' < gpu_process_uid_12.sh > "$log_file" || error_occurred=true
                ;;
            "10.204.227.42")
                timeout 5s sshpass -p "????????" ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 "aokilab_admin@$ip_address" 'bash -s' < cpu.sh > "$log_file" || error_occurred=true
                ;;
            "10.204.227.43")
                timeout 5s sshpass -p "????????" ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 "aokilab_admin@$ip_address" 'bash -s' < gpu_process_uid_Lyon.sh > "$log_file" || error_occurred=true
                ;;
            "10.204.227.44")
                timeout 5s sshpass -p "????????" ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 "kaggle_admin@$ip_address" 'bash -s' < gpu_process_uid_Lyon.sh > "$log_file" || error_occurred=true
                ;;
            "10.202.82.13")
                timeout 5s sshpass -p "????????" ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 "aoki_admin@$ip_address" 'bash -s' < gpu_process_uid.sh > "$log_file" || error_occurred=true
                ;;
            "10.202.82.121")
                timeout 5s sshpass -p "????????" ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 "aoki_admin@$ip_address" 'bash -s' < gpu_process_uid.sh > "$log_file" || error_occurred=true
                ;;
            *)
                echo "No script defined for $ip_address"
                ;;
        esac

        # エラー処理
        if [ "$error_occurred" = true ]; then
            echo "SSH接続エラー" >> "$log_file"

            # サーバーごとのタイムアウトカウントをインクリメント
            timeout_count["$ip_address"]=$((timeout_count["$ip_address"] + 1))

            # 2回連続でタイムアウトが発生したら通知
            if [ "${timeout_count[$ip_address]}" -ge 2 ]; then
                # サーバーが既にエラーファイルに存在しているかチェック
                if ! grep -q "$ip_address" $error_file; then
                    echo "$ip_address" >> $error_file
                    send_slack_message "サーバーエラーが発生しました: $ip_address"
                fi
            fi
        else
            # 復旧処理
            if grep -q "$ip_address" $error_file; then
                # エラーファイルからサーバーのIPを削除
                sed -i "/$ip_address/d" $error_file
                send_slack_message "サーバーが復旧しました: $ip_address"
            fi
            # タイムアウトカウントをリセット
            timeout_count["$ip_address"]=0
        fi

        # エラー状態をリセット
        error_occurred=false
    done

    python3 /workspace/make_html.py

done
