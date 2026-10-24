# from .routes.servers import router — servers.py se router object lao.
# as servers_router — us imported object ko main.py mein servers_router naam se use karo.
# app.include_router(servers_router) — us router ke registered endpoints
# ko main FastAPI application mein include karo.
# Yahan app.include_router(servers_router) hamare servers.py
# ke endpoints ko main FastAPI application ke saath connect karega.

from fastapi import FastAPI
from .routes.servers import router as servers_router
from .routes.health import router as health_router
from .logging_config import logger

app = FastAPI(title="DevOps Control Center")
logger.info("DevOps Control Center application initialized")


app.include_router(servers_router)
app.include_router(health_router)

# Ek important observation:
# - servers_router — server-related endpoints register karta hai.
# - health_router — health-check endpoint register karta hai.
# - app.include_router() — dono ko main application ke saath connect karta hai.