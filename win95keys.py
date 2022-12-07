import time
import sys
import random

settings_generate = False
settings_save = False
settings_silent = False
settings_random = False


def retail_keys():
    print("Generating keys, please wait...")
    time.sleep(1)
    valid = []
    blacklist = str(random.randint(100, 333))
    for temp in range(0, 9999999):
        result = 0
        temp = str(temp)
        temp = "0" * (7 - len(temp)) + temp
        for letter in temp:
            result += int(letter)
        if result % 7 == 0:
            fullkey = f"{blacklist}-" + temp
            if not settings_silent:
                print(fullkey)
            valid.append(fullkey)
    return valid


if len(sys.argv) > 1:
    if "-r" in sys.argv:
        settings_random = True
        settings_silent = True
    elif "-g" in sys.argv:
        settings_generate = True
    elif "-gs" in sys.argv:
        settings_generate = True
        settings_save = True
    if "-s" in sys.argv:
        settings_silent = True
else:
    print("""
    Hi there!
    This simple program generates all possible retail installation keys
    for Windows 95.
    By the way, if you have a wooden PC,
    the system may slow down a little during the process.
    I recommend using PyPy for faster script performance.
    """)
if settings_random:
    print("Please wait...")
    keys = retail_keys()
    print(keys[random.randint(0, len(keys))])
if settings_generate:
    start_time = time.time()
    keys = retail_keys()
    timer = int(time.time() - start_time)

    print("\nDone!")
    print(f"Keys: {len(keys)}")
    print(f"Time for generate: {timer} seconds")
    print("Here are your well-deserved 5 keys.")
    for key in range(0, 5):
        print(keys[random.randint(0, len(keys))])

    if settings_save:
        print("Saving keys in keys.txt, please wait..")
        text = ""
        for line in keys:
            text += line + "\n"
        with open("keys.txt", "w") as file:
            file.write(text)
            file.close()
