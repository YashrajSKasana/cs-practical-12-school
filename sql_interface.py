# Note:
# This program assumes all datatypes of records entered by the user are correct.
# It may not work properly for some tables

import mysql.connector

def line():
  print('-'*40)

def ask_for(info):
  info_data = {}
  for q in info:
    info_data[q] = input(f"Enter {q}: ")
  return info_data

def save(db):
  db.commit()
  print("Your changes have been saved :>")

def connect_sql(host, user, password, database):
  db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
  )
  print("Connection established successfully :>")
  return db

def get_head(cur, table):
  cur.execute(f"SHOW COLUMNS FROM {table}")
  return [col[0] for col in cur.fetchall()]

def get_primary_key(cur, table):
  cur.execute(f"SHOW KEYS FROM {table} WHERE Key_name = 'PRIMARY'")
  pks_table = cur.fetchall()
  pks = [row[4] for row in result]
  if pks is None:
    print("No primary key found :<")
    return None
  if len(pks) == 1:
    pk = pks[0]
  else:
    print()
    print("Choose a primary key to make the search")
    line()
    print("Enter 'n' for selecting '(n) option'")
    for j, i in enumerate(pks):
      print(f"({j}) {i}")
    line()
    option = int(input("=> "))
    pk = pks[option]
  return pk

def get_record(cur, table, key_column, key_value):
  query = f"SELECT * FROM {table} WHERE {key_column} = %s"
  cur.execute(query, (key_value,))
  record = cur.fetchone()
  return record

def add_record(cur, table):
  head = get_head(cur, table)
  print()
  line()
  head_parameters = ask_for(head)
  values = [head_parameters[h] for h in head]
  query = f"INSERT INTO {table} ({', '.join(head)}) VALUES ({', '.join(['%s']*len(head))})"
  cur.execute(query, values)
  print("Record added successfully :>")

def display_record(cur, table):
  pk = get_primary_key(cur, table)
  if pk is None:
    return
  rec_ID = input(f"Enter {pk}: ")
  rec = get_record(cur, table, pk, rec_ID)
  if rec is None:
    print(f"There is no record with primary key '{rec_ID}' :<")
  else:
    head = get_head(cur, table)
    line()
    for row, col in zip(head, rec):
      print(f"{row}: {col}")

def change_record(cur, table):
  pk = get_primary_key(cur, table)
  if pk is None:
    return
  rec_ID = input(f"Enter {pk}: ")
  rec = get_record(cur, table, pk, rec_ID)
  if rec is None:
    print("Record not found :<")
    return
  head = get_head(cur, table)
  line()
  print("Leave field empty to keep old value.")
  new_data = {}
  for i, h in enumerate(head):
    val = input(f"{h} [{rec[i]}]: ")
    new_data[h] = val if val != "" else rec[i]
  set_statement = ", ".join([f"{h}=%s" for h in head])
  values = [new_data[h] for h in head]
  query = f"UPDATE {table} SET {set_statement} WHERE {pk}=%s"
  cur.execute(query, values + [rec_ID])
  print("Record updated successfully :>")

def del_record(cur, table):
  pk = get_primary_key(cur, table)
  if pk is None:
    return
  rec_ID = input(f"Enter {pk} of record to delete: ")
  query = f"DELETE FROM {table} WHERE {pk} = %s"
  cur.execute(query, (rec_ID,))
  print("Record deleted successfully :>")

def main():
  quit = False
  while not quit:
    credentials = ("Host", "User", "Password", "Database", "Table")
    credentials = ask_for(credentials)
    mydb = connect_sql(
      credentials["Host"],
      credentials["User"],
      credentials["Password"],
      credentials["Database"]
    )
    cur = mydb.cursor()
    table = credentials["Table"]
    print()
    print("Enter 'n' for selecting '(n) option'")
    print("(0) Quit")
    print("(1) Insert Records")
    print("(2) View Records")
    print("(3) Modify Records")
    print("(4) Delete Records")
    print("(5) Save Changes")
    line()
    option = int(input("=> "))
    quit = option == 0
    if option == 5:
      save(mydb)
      continue
    option_func = {
      1: add_record,
      2: display_record,
      3: change_record,
      4: del_record
    }
    func = option_func.get(option, lambda x, y: print("Thanks !!!"))
    func(cur, table)
  save(mydb)

if __name__ == "__main__":
  main()
