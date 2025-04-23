import random, time, sys
from pathlib import Path
from datetime import datetime

seedList = []

def mainMenu():
    a = int(input("----Witamy w SeedGEN!----\nCo chciał(a)byś zrobić?\n* [1] Wylosować seed\n* [2] Wygenerować seed z ciągu znakowego\n"))
    if a == 1:
        drawSeed()
    elif a == 2:
        genSeed()
    else:
        #handling exception
        return
            
def drawSeed():
    seed = random.randint(-9223372036854775808, 9223372036854775807)
    seedList.append((seed, ""))
    print(f"Oto wylosowany seed: {seed}")
    whatNext()

def genSeed():
    seed = 0
    s = input("Wprowadź ciąg znakowy: ")
    for ch in s:
        seed = (31 * seed + ord(ch)) & 0xFFFFFFFFFFFFFFFF
        if seed >= 0x8000000000000000:
            seed -= 0x10000000000000000
    seedList.append((seed, s))
    print(f"Oto seed wygenerowany z twojego ciągu znakowego '{s}': {seed}")
    whatNext()

def whatNext():
    b = int(input("Co chcesz dalej zrobić?:\n* [1] Wylosować seed\n* [2] Wygenerować seed z ciągu literowego\n* [3] Zapisać sesję do pliku tekstowego\n* [4] Zakończyć sesję\n"))
    if b == 1:
        drawSeed()
    elif b == 2:
        genSeed()
    elif b == 3:
        saveTXT()
    elif b == 4:
        print("Dzięki za skorzystanie z programu ;)")
        time.sleep(2)
        sys.exit()
    else:
        print("Nieprawidłowa komenda!!!")
        whatNext()

def saveTXT():
    path = Path.home()/ "Desktop" / "seedGEN"
    path.mkdir(exist_ok=True)
    
    file = str(input("Wprowadź nazwę pliku, do którego chcesz zapisać seed: "))
    
    with open(path / file, "a") as f:
        f.write(f"----Sesja z {datetime.now().strftime('%d-%m-%Y %H:%M')}----\n")
        for i in range(0, len(seedList)):
            if seedList[i][1] == "":
                f.write(f"{i+1}. {seedList[i][0]}\n")
            else:
                f.write(f"{i+1}. {seedList[i][0]} ({seedList[i][1]})\n")
    print(f"Zapisano Twój/Twoje seed/seedy do pliku o nazwie {file} w folderze o adresie {path}")
    whatNext()
        
mainMenu()
    

