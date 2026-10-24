# Ye separation kyun?
# - Server — server data validate karta hai.
# - ServerStats — statistics response ka structure define karta hai.
# - ServerUpdate — PATCH request mein partial updates allow karta hai.
# Ab ye models ek central file mein hain. Future mein validation rules change karne hon,
# toh unhe ek hi jagah manage kar sakte hain.

from pydantic import BaseModel


class Server(BaseModel):
    name: str
    status: str
    cpu: float


class ServerStats(BaseModel):
    total_servers: int
    running_servers: int
    stopped_servers: int
    high_cpu_servers: list[str]


class ServerUpdate(BaseModel):
    status: str | None = None
    cpu: float | None = None


class ServerRecord(Server):
    id: int
