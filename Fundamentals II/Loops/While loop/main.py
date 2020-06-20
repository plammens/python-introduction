import random


i = 1
while i <= 100:
    print(i)
    i += 1

my_list = []
while len(my_list) < 10:
    my_list.append(random.randint(1, 10))

roll = random.randint(1, 6)
while roll%2 == 0:
    print(roll)
    roll = random.randint(1, 6)

inp = None
while not inp:
    inp = input("Enter a nonempty string: ")

print(f"{inp=}")

# break
my_list = []
while len(my_list) < 10:
    num = random.randint(1, 4)
    if num == 3:
        print("alert! skipping 3")
        continue
    print(num)
    my_list.append(num)

# iteration
