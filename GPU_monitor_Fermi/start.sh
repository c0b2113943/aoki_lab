docker compose up -d
docker exec -it gpu_m bash -c "chmod +x /workspace/start_py.sh && /workspace/start_py.sh"