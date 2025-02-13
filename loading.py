import time
import sys
import random
import art

def load(item: str):
   
    print(f"your {item} is being ready please wait")

    it = random.randint(3, 7)

    for _ in range(it):
        for dots in range(20):
            print("\r" + "." * dots + "   ", end="", flush=True)
            time.sleep(0.05)

    
    



