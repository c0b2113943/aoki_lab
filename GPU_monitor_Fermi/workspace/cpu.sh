#!/bin/bash

# CPU 使用率を取得
cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
echo "CPU Usage: $cpu_usage%" 

# RAM 使用率を取得
ram_usage=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
echo "RAM Usage: $ram_usage%" 

echo "ユーザー名              CPU使用率"

# top コマンドで最初の20行を取得し、プロセスIDとCPU使用率を抽出
top -b -o +%CPU | head -n 20 | tail -n +8 | awk '
{
    # プロセスIDとCPU使用率を変数に保存
    pid[$1] = $1
    cpu[$1] = $9
}
END {
    # 各PIDに対してユーザー名を取得し、CPU使用率を合算
    for (p in pid) {
        cmd = "ps -o user= -p " p
        cmd | getline user
        close(cmd)
        user_cpu[user] += cpu[p]
    }

    # 結果を表示
    for (u in user_cpu) {
        printf "%-25s %.2f%%\n", u, user_cpu[u]/40
    }
}' | sort -k2 -nr | head -n 5

