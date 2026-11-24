status = ["UP", "DOWN", "UP", "DOWN"]
down = 0

for i in range(len(status)):
    if status[i] == "DOWN":
        down += 1

print("Down:", down)
