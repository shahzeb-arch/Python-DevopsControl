# os.getenv() environment variable ki value read karta hai.
# Agar CPU_THRESHOLD set nahi hai, toh default "80" use hota hai.
# float() value ko number mein convert karta hai.

import os

CPU_THRESHOLD = float(os.getenv("CPU_THRESHOLD", "80"))
