import time
dots = ["...", "..", ".", ""]
n = 5
for i in range(n):
    for anim in dots:
        print(f"Initializing generator, please wait{anim}", end="\r", flush=True)
        time.sleep(0.5)