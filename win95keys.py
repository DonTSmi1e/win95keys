import time, sys, random

def retail_keys(setting=None):
    print("Generating keys, please wait...")
    time.sleep(1)
    valid = []
    blacklist = str(random.randint(100, 333))
    for key in range(0, 9999999):
        result = 0
        key = str(key)
        key = "0" * (7 - len(key)) + key
        for letter in key:
            result += int(letter)
        if result % 7 == 0:
            fullkey = f"{blacklist}-"+key
            if setting != "silent":
                print(fullkey)
            valid.append(fullkey)
    return valid

if len(sys.argv) > 1:
    if sys.argv[1] == "-r":
        keys = retail_keys("silent")
        print(f"Random key: {keys[random.randint(0,len(keys))]}")
        quit()

print("Hi there!\nThis simple program generates all possible retail installation keys for Windows 95.")
print("\nAn example on which the generation is based: 111-11111111")
print("111 - Blacklist\n1111111 - Sum divisible by 7")
print("Source: https://www.youtube.com/watch?v=cwyH59nACzQ\n")
print("By the way, if you have a wooden PC, the system may slow down a little during the process.")
print("Well, 'Blacklist' is actually any number between 000 and 332. It will only be used one for all keys.")

question = input("Let's start? ('yes' to start, else - ignore): ")
if question == "yes":
    start_time = time.time()
    keys = retail_keys()
    timer = int(time.time() - start_time)

    print("\nDone!")
    print(f"Keys: {len(keys)}")
    print(f"Time for generate: {timer} seconds")

    print("Here are your well-deserved 5 keys.")
    for key in range(0, 5):
        print(keys[random.randint(0, len(keys))])

    print("\n--- Save ---\nIt will take an incredibly long time (+1-2gb on hdd), maybe not?")
    if input("Save to file? ('yes' to save, else - ignore): ") == "yes":
        print("Please wait..")
        text = ""
        for line in keys:
            text += line + "\n"
        with open("keys.txt", "w") as file:
            file.write(text)
            file.close()
