app/
├── __init__.py
├── main.py
├── models.py
├── services.py
└── routes/
    ├── __init__.py
    ├── health.py
    └── servers.py         
         
         
          servers.py
Server-related endpoints ka department
router.get() · router.post() · router.patch()

           app.include_router()

                main.py
Main application — sab departments ko connect karti hai
     app = FastAPI()


     python -m uvicorn app.main:app --reload

Is command ka meaning:
- app.main → app folder ke andar main.py module.
- :app → us file ke andar FastAPI object ka naam.
- --reload → code changes hone par development server automatically reload hoga.
Open karo: [Swagger UI — DevOps Control Center](http://127.0.0.1:8000/docs?utm_source=chatgpt.com)
Check karo ki ye endpoints dikh rahe hain:
- GET /health
- GET /servers
- GET /servers/{server_name}
- POST /servers
- PATCH /servers/{server_name}
- DELETE /servers/{server_name}

Abhi tum Swagger mein manually endpoints test karte ho. Automated tests se Python khud check karega ki API expected result de rahi hai ya nahi.

logger.exception() ka main benefit: error message ke saath poora traceback bhi log hota hai, jisse debugging easy hoti hai.


logs related
Logging ka quick revision
Level	Kab use karte hain?
DEBUG	Detailed troubleshooting
INFO	Successful events aur normal activity
WARNING	Unexpected situation, jaise server not found
ERROR	Operation fail hona
CRITICAL	Bahut serious failure
Ab hamara next goal: logging ko production-minded banana. Ek important improvement hai—logs ko sirf terminal par dikhane ke bajaye file mein bhi save karna, taaki application restart hone ke baad bhi purane logs available rahen.