# #!/bin/bash

# ユーザー名とパスワードを適宜変更


# IPアドレスのリスト
IP_LIST=("10.202.82.13" "10.202.82.12" "10.202.82.121" "10.204.227.43" "10.204.227.42" "10.204.227.44") 

while true; do
   for ip_address in "${IP_LIST[@]}"; do
      echo "Processing $ip_address..."
      log_file="/workspace/log/$ip_address.txt"

      case "$ip_address" in
         "10.202.82.12")
            sshpass -p "????????" ssh -o StrictHostKeyChecking=no "aoki_admin@$ip_address" 'bash -s' < gpu_process_uid_12.sh > "$log_file"
            ;;
         "10.204.227.42")
            sshpass -p "????????" ssh -o StrictHostKeyChecking=no "aokilab_admin@$ip_address" 'bash -s' < cpu.sh > "$log_file"
            ;;
         "10.204.227.43")
            sshpass -p "????????" ssh -o StrictHostKeyChecking=no "aokilab_admin@$ip_address" 'bash -s' < gpu_process_uid_Lyon.sh > "$log_file"
            ;;
         "10.204.227.44")
            sshpass -p "????????" ssh -o StrictHostKeyChecking=no "kaggle_admin@$ip_address" 'bash -s' < gpu_process_uid_Lyon.sh > "$log_file"
            ;;
         "10.202.82.13")
            sshpass -p "????????" ssh -o StrictHostKeyChecking=no "aoki_admin@$ip_address" 'bash -s' < gpu_process_uid.sh > "$log_file"
            ;;
         "10.202.82.121")
            sshpass -p "????????" ssh -o StrictHostKeyChecking=no "aoki_admin@$ip_address" 'bash -s' < gpu_process_uid.sh > "$log_file"
            ;;
         *)
            echo "No script defined for $ip_address"
            ;;
      esac

   done

   python3 /workspace/make_html.py

done

