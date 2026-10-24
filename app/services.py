import json
from pathlib import Path

from .models import Server
from .config import CPU_THRESHOLD


def load_servers():
    json_file_path = Path(__file__).parent.parent / "servers.json"

    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [Server(**server).model_dump() for server in data]


def server_analyzer(servers, cpu_threshold=CPU_THRESHOLD):
    total_servers = len(servers)
    running_servers = 0
    stopped_servers = 0
    high_cpu_servers = []

    for server in servers:
        if server["cpu"] > cpu_threshold:
            high_cpu_servers.append(server["name"])

        if server["status"] == "running":
            running_servers += 1
        elif server["status"] == "stopped":
            stopped_servers += 1

    return {
        "total_servers": total_servers,
        "running_servers": running_servers,
        "stopped_servers": stopped_servers,
        "high_cpu_servers": high_cpu_servers,
    }