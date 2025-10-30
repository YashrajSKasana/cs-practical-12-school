def is_palinfrome(num):
  return num == "".join(reversed(num))

def main():
  num = input("Enter A Number: ")
  if is_palinfrome(num):
    print(f"{num} is a Palinfrome :> ")
  else:
    print(f"{num} is not a Palinfrome :< ")
if __name__ == "__main__":
  main()
