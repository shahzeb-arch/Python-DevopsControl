def greet():
    print("Welcome to DevOps Control Center!")

greet()

import json
from pathlib import Path

json_file_path = Path(__file__).parent / "servers.json"
try:
    with open(json_file_path, "r", encoding="utf-8") as file:
        servers = json.load(file)
except FileNotFoundError:
    print("Error: servers.json file not found.")
    exit(1)
except json.JSONDecodeError:
    print("Error: Failed to decode JSON from servers.json.")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit(1)
def server_analyzer(servers):
    total_servers = 0
    running_servers = 0
    stopped_servers = 0
    high_cpu_servers = []
#     Current CPU validation ko complete karna.
# name aur status ki basic validation add karna.
# Server analysis ko clean, reusable functions mein organize karna.
# Is module ko complete karke agle Python concept par jaana.
    
    # Yahan servers variable ke andar JSON data ab Python objects ke form mein aa gaya hai.
    for server in servers:
        total_servers += 1
        if "cpu" not in server:
            print("Error: Server CPU is missing")
            continue
        if server["cpu"] > 80:
            high_cpu_servers.append(server["name"])
        if server["status"] == "running":
            running_servers += 1
        elif server["status"] == "stopped":
            stopped_servers += 1
    return {
        "total_servers": total_servers,
        "running_servers": running_servers,
        "stopped_servers": stopped_servers,
        "high_cpu_servers": high_cpu_servers
    }
server_stats = server_analyzer(servers)
print(f"Total Servers: {server_stats['total_servers']}")
print(f"Running Servers: {server_stats['running_servers']}")
print(f"Stopped Servers: {server_stats['stopped_servers']}")

print(f"Servers with high CPU usage: {server_stats['high_cpu_servers']}")