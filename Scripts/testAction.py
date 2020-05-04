import time
# import random
# from pathlib import Path

# random.seed()
# x = random.randint(1, 1000000)
# Path(f'c:\Users\Mine\Desktop\HERE\ServiceTest\{x}.txt').touch()
def writeSomething():
    x = 0
    while x < 10:
        f = open(r"C:\Users\Mine\Desktop\HERE\ServiceTest\demofile2.txt", "a")
        f.write("Now the file has more content!")
        f.close()
        x += 1
        time.sleep(5)

# time.sleep(15)
if __name__ == '__main__':
    writeSomething()