
def ask_for_file():
  print("Provide partial or complete path to a file")
  print("if not provided program will default to (/boring_files/count_alphabat_test.txt)")
  file = input("File: ")
  if file == " " or file == '':
    return None
  else:
    return file

def use_file(file, func):
  with open(file, 'r') as f:
    return func(f)

def count_vowels(file_hendal):
  text = file_hendal.read()
  text = text.lower()
  CX = lambda x, y: x.count(y)
  return CX(text, "a") + CX(text, "e") + CX(text, "i") + CX(text, "o") + CX(text, "u")

def count_consonants(file_hendal):
  text = file_hendal.read()
  count = 0
  for char in text:
      if char.isalpha():
          count += 1
  file_hendal.seek(0)
  return count - count_vowels(file_hendal)

def count_uppercase(file_hendal):
  text = file_hendal.read()
  count = 0
  for char in text:
      if char.isupper():
          count += 1
  return count

def count_lowercase(file_hendal):
  text = file_hendal.read()
  count = 0
  for char in text:
      if char.islower():
          count += 1
  return count

def main():
  file = ask_for_file()
  file = "./boring_files/count_alphabat_test.txt" if file is None else file
  n_voval = use_file(file, count_vowels)
  n_consonants = use_file(file, count_consonants)
  n_uppercase = use_file(file, count_uppercase)
  n_lowercase = use_file(file, count_lowercase)

  print()
  print(f"Number of Voval: {n_voval}")
  print(f"Number of Consonants: {n_consonants}")
  print(f"Number of UpperCase: {n_uppercase}")
  print(f"Number of LowerCase: {n_lowercase}")

if __name__ == "__main__":
  main()
