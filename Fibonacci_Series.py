def main():
  num = int(input("Enter an Integer: "))
  pre = [0,1]
  if num == 0: print(0)
  elif num  == 1:
    for i in pre: print(i)
  else:
    while num:
      n = sum(pre)
      print(n)
      pre[0]=pre[1]
      pre[1]=n
      num -= 1
if __name__ == "__main__":
  main()
