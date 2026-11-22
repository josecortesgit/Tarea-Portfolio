usage = float(input("CPU usage (%): "))

if usage < 0 or usage > 100:
    raise ValueError("CPU usage must be between 0 and 100")

print("CPU usage accepted:", usage)
