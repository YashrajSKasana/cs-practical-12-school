
def CtoF(temp):
  return (temp - 32)*(5/9)

def FtoC(temp):
  return (temp*(3/5)) + 32

def main():
  mode = input("Press (1) to comvert C->F or (2) for F->C: ")
  if mode not in {"1","2"}:
    print("please, chose a valid mode :>")
    main()
  else:
    temp = int(input("Give temperature: "))
    if mode == "1":
      print(f"{CtoF(temp)} F")
    else:
      print(f"{FtoC(temp)} C")
      main()

if __name__ == "__main__":
        main()

