# load_servers() data deta hai 
# → get_servers() us data ko pass karta hai
# → server_analyzer() uska analysis karta hai.







# @app.get("/servers") URL ko function se connect karta hai. Request aane par function execute hota hai.
# @app.get("/servers") # /servers URL par GET request handle karega.

# Toh iska meaning hai: jab client GET /servers request bheje, FastAPI get_servers() execute kare.
# def get_servers(): # request aane par execute hoga.
#     servers = load_servers()
#     server_stats = server_analyzer(servers)
#     return server_stats


# except Exception as e:
    #   raise HTTPException(
    #       status_code=500,
    #       detail="Server data validation failed."
    #   ) from e

    #     Current CPU validation ko complete karna.
# name aur status ki basic validation add karna.
# Server analysis ko clean, reusable functions mein organize karna.
# Is module ko complete karke agle Python concept par jaana.
    
    # Yahan servers variable ke andar JSON data ab Python objects ke form mein aa gaya hai.

    # server ek dictionary hai.
# **server dictionary ki keys aur values ko model ke fields ke saath match karta hai.
# Missing name, status, cpu ya incorrect value hone par Pydantic validation error deta hai.

# Maan lo servers.json mein 5 servers hain. data unki list hai.
# - Server(**server) dictionary ke data ko Pydantic model se validate karta hai.
# - .model_dump() validated model ko dobara dictionary mein convert karta hai.

Ek important concept: /servers/{server_name} mein curly braces batate hain ki URL ka woh part dynamic hai.


health main.py mein kyun hai?
Humne code ko responsibility ke basis par divide kiya hai.
- main.py — application create karta hai aur routers ko connect karta hai. Abhi humne simple health endpoint bhi yahin rakha hai.
- routes/servers.py — server-related endpoints: GET, POST, PATCH, DELETE.
Lekin bhai, /health ka main.py mein hona compulsory nahi hai. Hum use alag file mein bhi rakh sakte hain.
Professional structure
app/main.py

FastAPI app create karega aur routers register karega.

app/routes/health.py

Health-check endpoint rakhega.

app/routes/servers.py

Saare server-related endpoints rakhega.

Isse kya fayda hoga?
Kal ko application mein ye endpoints aaye:
- /health
- /servers
- /monitoring
- /deployments


installed package test
python -m pip freeze