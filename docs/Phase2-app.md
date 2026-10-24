# Ye code kya kar raha hai?
# - from fastapi import FastAPI — FastAPI framework ko import karta hai.
# - app = FastAPI(...) — hamari web application create karta hai.
# - @app.get("/health") — batata hai ki /health URL par HTTP GET request aane par neeche wala function chalega.
# - health_check() — health-check endpoint ka function hai.
# - return {...} — dictionary return karta hai, jise FastAPI JSON response mein convert karta hai.



python -m uvicorn app:app --reload

Iska meaning:
- app — app.py file ka naam, .py ke bina.
- app — us file ke andar app = FastAPI(...) object.
- --reload — development ke dauran code change hone par server automatically reload hoga.