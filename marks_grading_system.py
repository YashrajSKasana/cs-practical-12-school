grsding_table = {
  (100, 75):"A",
  (75, 50):"B",
  (50, 25):"C",
  (25,0):"D"
}

def grade(marks):
  if marks == 0:
    return "D"
  for rag in grsding_table.keys():
    if rag[0] >= marks > rag[1]:
      return grsding_table[rag]

def main():
  marks = int(input("Enter Marks: "))
  if not (100 >= marks >= 0):
    print("invalid marks :<")
  print(f"You Got {grade(marks)}")

if __name__ == "__main__":
   main()
