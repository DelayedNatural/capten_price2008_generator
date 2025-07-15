import textwrap
import time
import msvcrt
dots = ["...", "..", ".", ""]
n = 2

def gen():
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z','!', '"', '#', '$', '%', '&', "'", '(', ')', '*','+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
        '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|','}', '~', "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    chk = 0 #se poio gramma einai
    mem = ""
    word = "capten_price2008"
    m = 0
    while m < len(word):
        while True:
            let = abc[chk]
            if let != word[m]:
                print(mem+let)
                chk +=1
                time.sleep(0.07)
            else:
                mem += let
                chk = 0
                m += 1
                break
    print("capten_price2008")
        

for i in range(n):
    for anim in dots:
        print(f"Initializing generator{anim}")
        time.sleep(0.5)
        print("\n" * 70)
print("Initialization Complete!")
for i in range(n):
    for anim in dots:
        print("Initialization Complete!")
        print(f"Parsing configuration files{anim}")
        time.sleep(0.5)
        print("\n" * 70)
print("Parsing complete!")
for i in range(n):
    for anim in dots:
        print("Initialization Complete!")
        print("Parsing complete!")
        print(f"Compiling runtime environment{anim}")
        time.sleep(0.5)
        print("\n" * 70)
print("Initialization Complete!")
print("Parsing complete!")
print("Runtime environment compiled!")
option = input('Program is ready to execute. Type your option and press enter to confirm. Type "Y" to start, "N" to abort.')
if option == "N" or option == "n":
    print("Aborting program...")
    time.sleep(0.5)
    exit()
elif option == "y" or option == "Y":
    print("Welcome to the capten_price2008 generator!")
    option = input("Begin generating? (Y/N)")
    if option == "N" or option == "n":
        print("Aborting program...")
        time.sleep(0.5)
    elif option == "Y" or option == "y":
        gen()
    else:
        print(textwrap.dedent("""
        [CRIT] 0x0042F9A0: Invalid directive passed to input handler.
            Expected: ASCII(0x59) or ASCII(0x4E)
            Received: Unrecognized input

        [SYS]  0x1001E7B4: Branch execution halted.
            Reason: Unsafe execution path detected in user input branch.

        [IO]   0x003AFF10: Standard input buffer mismatch.
            Status: IO_BUFFER_FAULT
            Descriptor: stdin@0x00000002

        [MEM]  0x0080021C: Stack integrity check skipped due to directive failure.
            Flagged for delayed review on next safe boot.

        [PROC] 0x00FF1372: Session token invalidated.
                Execution ID: 9F-22-A3-C7-88
                Flags: [HARD_ABORT] [ECHO_SUPPRESS] [RETRY_DISABLED]

        [CORE] 0x0000DEAD: Instruction stream terminated.
                Exit code: 0xC0000142
        """))
        print("CONSULT YOUR DEVICE'S MANUAL OR CONTACT TECHNICAL SUPPORT IMMEDIATELY. ABORTING IN 10 seconds!")
        time.sleep(10)
        exit()
else:
    print(textwrap.dedent("""
    [CRIT] 0x0042F9A0: Invalid directive passed to input handler.
           Expected: ASCII(0x59) or ASCII(0x4E)
           Received: Unrecognized input

    [SYS]  0x1001E7B4: Branch execution halted.
           Reason: Unsafe execution path detected in user input branch.

    [IO]   0x003AFF10: Standard input buffer mismatch.
           Status: IO_BUFFER_FAULT
           Descriptor: stdin@0x00000002

    [MEM]  0x0080021C: Stack integrity check skipped due to directive failure.
           Flagged for delayed review on next safe boot.

    [PROC] 0x00FF1372: Session token invalidated.
            Execution ID: 9F-22-A3-C7-88
            Flags: [HARD_ABORT] [ECHO_SUPPRESS] [RETRY_DISABLED]

    [CORE] 0x0000DEAD: Instruction stream terminated.
            Exit code: 0xC0000142
    """))
    print("CONSULT YOUR DEVICE'S MANUAL OR CONTACT TECHNICAL SUPPORT IMMEDIATELY. ABORTING IN 10 seconds!")
    time.sleep(10)
    exit()