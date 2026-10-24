from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
import json
from pathlib import Path

class ServerUpdate(BaseModel):
    status: str | None = None
    cpu: float | None = None

class Server(BaseModel):
    name: str
    status: str
    cpu: float

class ServerStats(BaseModel):
    total_servers: int
    running_servers: int
    stopped_servers: int
    high_cpu_servers: list[str]
app = FastAPI(title="DevOps Control Center")

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "app": "DevOps Control Center"
    }
@app.patch("/servers/{server_name}")
def update_server(server_name: str, update: ServerUpdate):
    servers = load_servers()

    for server in servers:
        if server["name"] == server_name:
            changes = update.model_dump(exclude_unset=True)

            if not changes:
                raise HTTPException(
                    status_code=400,
                    detail="Provide at least one field to update."
                )

            server.update(changes)

            json_file_path = Path(__file__).parent / "servers.json"
            with open(json_file_path, "w", encoding="utf-8") as file:
                json.dump(servers, file, indent=2)

            return {
                "message": "Server updated successfully",
                "server": server
            }

    raise HTTPException(
        status_code=404,
        detail="Server not found."
    )

def load_servers():
    json_file_path = Path(__file__).parent / "servers.json"

    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [Server(**server).model_dump() for server in data]


def server_analyzer(servers):
    total_servers = 0
    running_servers = 0
    stopped_servers = 0
    high_cpu_servers = []

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

@app.get("/servers", response_model=ServerStats)
def get_servers():
    try:
        servers = load_servers()
    except FileNotFoundError:
        raise HTTPException(
            status_code=500,
            detail="Server data file is missing."
        )
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="Server data file contains invalid JSON."
        )
    except ValidationError as e:
        raise HTTPException(
# HTTPException — API ko controlled HTTP response deta hai.
            status_code=500,
            detail="Server data validation failed."
        ) from e

    

    return server_analyzer(servers)
@app.post("/servers")
def add_server(server: Server):
    servers = load_servers()
    for existing_server in servers:
        if existing_server["name"] == server.name:
            raise HTTPException(
                status_code=409,
                detail="Server name already exists."
            )
   

    servers.append(server.model_dump())

    json_file_path = Path(__file__).parent / "servers.json"

    with open(json_file_path, "w", encoding="utf-8") as file:
        json.dump(servers, file, indent=2)

    return {
        "message": "Server added successfully",
        "server": server
    }
@app.get("/server/{server_name}")
def get_server(server_name: str):
    servers = load_servers()

    for server in servers:
        if server["name"] == server_name:
            return server

    raise HTTPException(
        status_code=404,
        detail="Server not found."
    )

@app.delete("/servers/{server_name}")
def delete_server(server_name: str):
    servers = load_servers()

    for server in servers:
        if server["name"] == server_name:
            if server["name"] == server_name
            servers.remove(server)

            json_file_path = Path(__file__).parent / "servers.json"

            with open(json_file_path, "w", encoding="utf-8") as file:
                json.dump(servers, file, indent=2)

            return {
                "message": "Server deleted successfully",
                "server": server
            }

    raise HTTPException(
        status_code=404,
        detail="Server not found."
    )
