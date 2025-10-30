def is_Armstrong(num):
  return int("".join(num)) == sum(map(lambda x: int(x)**len(num), num))

def main():
  num = list(input("Enter an Integer: "))
  if is_Armstrong(num):
    print(f"{"".join(num)} is Armstrong :> yeeee!")
  else:
    print(f"{"".join(num)} is not Armstrong :<")
if __name__ == "__main__":
  main()
