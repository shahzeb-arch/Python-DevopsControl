# level=logging.INFO — INFO aur usse higher severity ke logs dikhata hai.
# format — log ke saath timestamp, severity aur message dikhata hai.
# getLogger(...) — hamare application ke liye logger object deta hai.
# 2026-10-22 10:30:00 | INFO | devops-control-center | Application started
# 1st steps learn logging
# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
# )

# logger = logging.getLogger("devops-control-center")

# 2nd steps

# ogging.StreamHandler() — logs terminal mein dikhata hai.
# logging.FileHandler() — logs ko app.log file mein save karta hai.
# app.log — project root mein create hogi.

# import logging
# from pathlib import Path

# log_file = Path(__file__).parent.parent / "app.log"

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
#     handlers=[
#         logging.StreamHandler(),
#         logging.FileHandler(log_file, encoding="utf-8"),
#     ],
# )

# logger = logging.getLogger("devops-control-center")

# 3rd steps logs roatte krna refrence task.md 1-6 line


import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

log_file = Path(__file__).parent.parent / "app.log"

file_handler = RotatingFileHandler(
    log_file,
    maxBytes=1_000_000,
    backupCount=3,
    encoding="utf-8",
)

console_handler = logging.StreamHandler()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[console_handler, file_handler],
)

logger = logging.getLogger("devops-control-center")
