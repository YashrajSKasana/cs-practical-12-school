from os import path
import pickle
def line():
  print('-'*40)

def use_file(file, mode, func, *ar):
  with open(file, mode) as f:
    return func(f, *ar)

def load_file(file):
  read = lambda f: pickle.load(f)
  return use_file(file,'rb',read)

def bit_wright(file, rec):
  if not path.exists(file) or path.getsize(file) == 0:
    head = ["Roll No", "Name"]
    rec.insert(0, head)
  else:
    old_rec = load_file(file)
    old_rec.extend(rec)
    rec = old_rec
  dump = lambda f, rec: pickle.dump(rec, f)
  use_file(file, 'wb', dump, rec)

def add_record(file):
  add_more_record = True
  rec = []
  while add_more_record:
    print()
    line()
    rollno = input("Enter Roll No.: ")
    name = input("Enter Name: ")
    tpl = (rollno, name)
    rec.append(tpl)
    add_more_record = input("Do You want to add an other record (y/n): ").lower() == 'y'
  bit_wright(file, rec)

def display_record(file):
  rollno = input("Enter Roll No.: ")
  rec = load_file(file)
  rec = rec[1:]
  hashed_rec = dict(rec)
  name = hashed_rec.get(rollno, False)
  if not name:
    print(f"Given Roll No. '{rollno}' does not exist! :<")
  else:
    print()
    line()
    print(f"Roll No.: {rollno}")
    print(f"Name: {name}")

def display_all(file):
  rec = load_file(file)
  rec = rec[1:]
  for rollno,name in rec:
    line()
    print(f"Roll No.: {rollno}")
    print(f"Name: {name}")


def main():
  print("Enter 'n' for selecting '(n) option'")
  print("(1) Add new record")
  print("(2) display specific record")
  print("(3) display all records")
  line()
  option = int(input("=> "))

  option_func = {
    1:add_record,
    2:display_record,
    3:display_all
  }

  FILE = r"./boring_files/students.dat"
  func = option_func[option]
  func(FILE)

if __name__ == "__main__":
  main()
