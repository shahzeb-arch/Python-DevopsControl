# APIRouter() — related API endpoints ko ek jagah group karta hai.
# Server, ServerStats, ServerUpdate — models ko models.py se import karte hain.
# load_servers — data loading function ko services.py se import karta hai.
# ..models aur ..services — app package ke parent level se nahi, balki current routes package se ek level upar jaakar import karte hain.
# Server related endpoints
# Ye path servers.py se project root tak jaata hai.


# INFO — informational log.
# devops-control-center — hamare logger ka naam.
# Server created successfully — event ka message.
# shahzeb — actual server name, jo %s ki jagah aaya.

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
import json
from pathlib import Path

from ..models import Server, ServerStats, ServerUpdate
from ..services import load_servers, server_analyzer
from ..logging_config import logger

router = APIRouter()
# Yahan @router.get() endpoint ko router object ke saath register karta hai.

@router.get("/servers", response_model=ServerStats)
def get_servers():
    logger.info("Fetching server statistics")
    try:
        servers = load_servers()
    except FileNotFoundError:
        logger.exception("Server data file is missing")
        raise HTTPException(
            status_code=500,
            detail="Server data file is missing."
        )
    except json.JSONDecodeError:
        logger.exception("Server data file contains invalid JSON")
        raise HTTPException(
            status_code=500,
            detail="Server data file contains invalid JSON."
        )
    except ValidationError as e:
        logger.exception("Server data validation failed")
        raise HTTPException(
            status_code=500,
            detail="Server data validation failed."
        ) from e

    return server_analyzer(servers)


@router.get("/servers/{server_name}")
def get_server(server_name: str):
    servers = load_servers()

    for server in servers:
        if server["name"] == server_name:
            return server

    raise HTTPException(
        status_code=404,
        detail="Server not found."
    )


# CRUD ENDPOINTS POST

@router.post("/servers")
def add_server(server: Server):
    servers = load_servers()

    for existing_server in servers:
        if existing_server["name"] == server.name:
            raise HTTPException(
                status_code=409,
                detail="Server name already exists."
            )

    servers.append(server.model_dump())

    json_file_path = Path(__file__).parent.parent.parent / "servers.json"

    with open(json_file_path, "w", encoding="utf-8") as file:
        json.dump(servers, file, indent=2)
    logger.info("Server created successfully: %s", server.name)
    return {
        "message": "Server added successfully",
        "server": server
    }

# PATCH UPDATE EXISTING SERVERS
@router.patch("/servers/{server_name}")
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

            json_file_path = Path(__file__).parent.parent.parent / "servers.json"

            with open(json_file_path, "w", encoding="utf-8") as file:
                json.dump(servers, file, indent=2)
            logger.info("Server updated successfully: %s", server_name)
            return {
                "message": "Server updated successfully",
                "server": server
            }

    raise HTTPException(
        status_code=404,
        detail="Server not found."
    )

# 3. DELETE — REMOVE THE SERVER
@router.delete("/servers/{server_name}")
def delete_server(server_name: str):
    servers = load_servers()

    for server in servers:
        if server["name"] == server_name:
            servers.remove(server)

            json_file_path = Path(__file__).parent.parent.parent / "servers.json"
# Ye path servers.py se project root tak jaata hai.
            with open(json_file_path, "w", encoding="utf-8") as file:
                json.dump(servers, file, indent=2)
            logger.info("Server deleted successfully: %s", server_name)
            return {
                "message": "Server deleted successfully",
                "server": server
            }
    logger.warning("Cannot delete server; not found: %s", server_name)
    raise HTTPException(
        status_code=404,
        detail="Server not found."
    )