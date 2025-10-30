file = r"./boring_files/boring_file.txt"

with open(file, "w") as f:

# write

  f.write("Hello world (0_0)\n")

with open(file, "a") as f:
# update

  f.write("Hello world (0_0)")

with open(file, "r") as f:
# read

  print(f.read())
