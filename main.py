from math_utils import divide
from config import DEFAULT_PRECISION

def main():
    a = 10
    b = 2
    result = divide(a, b)
    print(f"Result: {round(result, DEFAULT_PRECISION)}")

if __name__ == "__main__":
    main()