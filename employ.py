from os import path
import csv

def line():
  print('-'*40)

def find_record(empid, rec):
  index = 0
  for tpl in rec:
    if tpl[0] == empid:
      return index
    else:
      index += 1
  return None

def use_file(file, mode, func, *ar):
  with open(file, mode, newline='') as f:
    return func(f, *ar)

def load_file(file):
  read = lambda f: list(csv.reader(f))
  return use_file(file,'r',read)

def dump(file, rec):
  writer = csv.writer(file)
  writer.writerows(rec)

def csv_wright(file, rec):
  if not path.exists(file) or path.getsize(file) == 0:
    head = ["Employ ID", "Employ Name", "Employ Salary", "Date of Joining"]
    rec.insert(0, head)
  else:
    old_rec = load_file(file)
    old_rec.extend(rec)
    rec = old_rec
  use_file(file, 'w', dump, rec)

def add_record(file):
  add_more_record = True
  rec = []
  while add_more_record:
    print()
    line()
    empid = input("Enter Employ ID: ")
    empname = input("Enter Employ Name: ")
    salary = input("Enter Employ Salary: ")
    doj = input("Enter Employ Date of Joining: ")

    tpl = [empid, empname, salary, doj]
    rec.append(tpl)
    add_more_record = input("Do You want to add an other record (y/n): ").lower() == 'y'
  csv_wright(file, rec)

def display_record(file):
  empid = input("Enter Employ ID: ")
  rec = load_file(file)
  rec = rec[1:]
  index = find_record(empid, rec)
  if index is None:
    print(f"Given Employ ID '{empid}' does not exist! :<")
  else:
    empid, empname, salary, doj = rec[index]
    print()
    line()
    print(f"Employ ID: {empid}")
    print(f"Employ Name: {empname}")
    print(f"Employ Salary: {salary}")
    print(f"Employ Date of Joining: {doj}")

def change_salary(file):
  empid = input("Enter Employ ID: ")
  new_salary = input("Enter new Salary: ")
  rec = load_file(file)
  head = rec[0]
  rec = rec[1:]
  index = find_record(empid, rec)
  if index is None:
    print(f"Given Employ ID '{empid}' does not exist! :<")
  else:
    rec[index][2] = new_salary
    print("Salary updated successfully!")
    rec.insert(0, head)
    use_file(file, 'w', dump, rec)

def del_record(file):
  empid = input("Enter Employ ID: ")
  rec = load_file(file)
  head = rec[0]
  rec = rec[1:]
  index = find_record(empid, rec)
  if index is None:
    print(f"Given Employ ID '{empid}' does not exist! :<")
  else:
    rec.pop(index)
    print("Record deleted successfully!")
    rec.insert(0, head)
    use_file(file, 'w', dump, rec)

def main():
  print("Enter 'n' for selecting '(n) option'")
  print("(1) Enter new Record")
  print("(2) Search Record by empid")
  print("(3) Modify salary")
  print("(4) Delete record")
  line()
  option = int(input("=> "))

  option_func = {
    1:add_record,
    2:display_record,
    3:change_salary,
    4:del_record
  }

  FILE = r"./boring_files/employ.csv"
  func = option_func[option]
  func(FILE)

if __name__ == "__main__":
  main()
