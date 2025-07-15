import time
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
            time.sleep(0.7)
        else:
            mem += let
            chk = 0
            m += 1
            break
print("capten_price2008")