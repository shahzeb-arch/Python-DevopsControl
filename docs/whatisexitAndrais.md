exit(1)
Program ko terminate karne ke liye.
print("Error occurred")exit(1)

Yahan program band ho sakta hai. 1 generally unsuccessful exit status ko indicate karta hai.


raise
Exception ko generate ya dobara propagate karne ke liye.
try:    open("servers.json")except FileNotFoundError:    raise



Yahan original error aage propagate hota hai. Calling code decide kar sakta hai ki use kaise handle karna hai.