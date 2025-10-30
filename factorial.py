def fac(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fac(n - 1)

def main():
  num = int(input("Enter an Integer: "))
  print(f"Factorial of {num} is => {fac(num)}")
if __name__ == "__main__":
  main()
