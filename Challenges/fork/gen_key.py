import random

for i in range(255):
    print("0x%08X," % random.randint(0, (1 << 32) - 1))

