accessAddress = []

with open("subnet_list.txt") as file:
    lines = file.readlines()
    for line in lines:
        accessAddress.append(line[:-1])
file.close()
print(f"accessible Sub-network: {accessAddress}")
