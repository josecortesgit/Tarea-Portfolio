import math

operations = 0

while True:
    op = input("Operation (+ - * / q): ").strip().lower()

    if op == "q":
        break

    if op not in ("+", "-", "*", "/"):
        print("Unknown operation")
        continue

    try:
        a = float(input("a: "))
        b = float(input("b: "))

        if not math.isfinite(a) or not math.isfinite(b):
            raise ValueError("Non-finite number")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        else:
            result = a / b

        if not math.isfinite(result):
            raise OverflowError("Result out of range")

    except ValueError:
        print("Error: enter valid finite numbers")
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
    except OverflowError:
        print("Error: result out of range")
    else:
        print("Result:", result)
    finally:
        operations += 1

print("Operations attempted:", operations)
