Maan lo, future mein hamare project ko ye Python packages chahiye:
- fastapi — web application aur API banane ke liye.
- uvicorn — API server run karne ke liye.
- pytest — code testing ke liye.
In packages ki list hum requirements.txt mein rakhte hain. Isse doosre developer ya deployment pipeline ko required dependencies install karna aasaan hota hai.


requirements.txt root folder mein rakhne ke 3 main reasons hain:
1. Centralized dependencies: Saare required Python packages ki list ek jagah milti hai.
2. Easy installation: Project ke root se command run karke dependencies install kar sakte hain.
3. Deployment: CI/CD pipeline ya doosra developer isi file se dependencies install kar sakta hai.


Ye command file mein listed packages ko current Python environment mein install karti hai. Hamare case mein, .venv active hone par packages usi environment mein install honge.
Ek important correction: Har folder ki dependencies alag-alag manage karne ke liye requirements.txt nahi banate. Hamare project mein filhaal ek central dependency file kaafi hai.
python -m pip install -r requirements.txt