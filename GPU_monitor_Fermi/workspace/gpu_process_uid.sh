#!/bin/bash

# nvidia-smi の出力を取得する
nvidia_smi_output=$(nvidia-smi)

cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')

echo " CPU Usage: $cpu_usage%"

ram_usage=$(free | grep Mem | awk '{print $3/$2 * 100.0}')

echo " RAM Usage: $ram_usage%"
# 出力のヘッダー部分を表示する

# 出力のヘッダー部分を表示する
echo "$nvidia_smi_output" | head -n 17

echo "+-----------------------------------------------------------------------------------------+"
echo "| Processes:                                                                              |"
echo "|  GPU   GI   CI    User                   Type  Process name              GPU Memory     |"
echo "|        ID   ID                                                           Usage          |"
echo "|=========================================================================================|"

nvidia_smi_output=$(nvidia-smi)

# プロセス部分の行を抽出
processes=$(echo "$nvidia_smi_output" | awk '/\| Processes:/,/^$/')

# プロセス情報の行数を確認
process_count=$(echo "$processes" | wc -l)

# プロセス情報の行を処理して表示
echo "$processes" | awk 'NR > 4 {print}' | while IFS= read -r line; do
    # 行から情報を抽出
    gpu=$(echo "$line" | awk '{print $2}')
    if [ "$gpu" == "No" ]; then
        echo "| No running processes found                                                              |"
        break
    fi
    pid=$(echo "$line" | awk '{print $5}')
    process_name=$(echo "$line" | awk '{for(i=6;i<=NF-2;++i) printf "%s ", $i}')
    used_memory=$(echo "$line" | awk '{print $(NF-1)}')

    if [ -n "$pid" ]; then
        # プロセスのユーザー名を取得
        user=$(ps -o user= -p "$pid" | tail -n 1)

        # もしpsコマンドがPIDを見つけられない場合、PIDを表示
        if [ -z "$user" ]; then
            user="PID: $pid"
        fi

        printf "|    %d   N/A  N/A   %-20s    %-32s %8s MiB |\n" "$gpu" "$user" "$process_name" "$used_memory"
    fi
done


echo "+-----------------------------------------------------------------------------------------+"
