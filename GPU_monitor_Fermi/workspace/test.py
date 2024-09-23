import psutil



# CPU使用率を取得する
cpu_usage = psutil.cpu_percent(interval=1)

print(f"CPU 使用率: {cpu_usage}%")

ram = psutil.virtual_memory()

# RAMの総量（単位: バイト）と使用量（単位: バイト）を取得
total_ram = ram.total
used_ram = ram.used

# 単位をメガバイトに変換して表示
total_ram_mb = total_ram / (1024 * 1024)
used_ram_mb = used_ram / (1024 * 1024)

# print(f"RAM 総量: {total_ram_mb:.2f} MB")
# print(f"RAM 使用量: {used_ram_mb:.2f} MB")
print(f"RAM 使用率: {((used_ram_mb/total_ram_mb)*100):.2f}%")

