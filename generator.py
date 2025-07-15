import time
import msvcrt
dots = ["...", "..", ".", ""]
n = 3
for i in range(n):
    for anim in dots:
        print(f"Initializing generator{anim}")
        time.sleep(0.5)
        print("\n" * 30)
print("Initialization Complete!")
for i in range(n):
    for anim in dots:
        print("Initialization Complete!")
        print(f"Parsing configuration files{anim}")
        time.sleep(0.5)
        print("\n" * 30)
print("Parsing complete!")
for i in range(n):
    for anim in dots:
        print("Initialization Complete!")
        print("Parsing complete!")
        print(f"Compiling runtime environment{anim}")
        time.sleep(0.5)
        print("\n" * 30)
print("Initialization Complete!")
print("Parsing complete!")
print("Runtime environment compiled!")
option = input('Program is ready to execute. Type your option and press enter to confirm. Type "Y" to start, "N" to abort.')
if option == "N":
    msvcrt.getch()