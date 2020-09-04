# Author: John Malay jmm9098@psu.edu
# Collaborator: Drew Kennedy ajk6604@psu.edu
# Collaborator: Mattelynn Beahan mjb7643@psu.edu
# Collaborator: Ian Munzo ijm5204@psu.edu

temp = float(input("Enter temperature: "))
unit = (input("Enter unit in F/f or C/c: "))
if unit == "F" or unit == "f":
  f = temp
  c = float((5/9)*(f-32))
  print(f"{f}° in Fahrenheit is equivalent to {c}° Celsius.")
elif unit == "C" or unit == "c":
  c = temp
  f = float((9/5)*(c)+32)
  print(f"{c}° in Celsius is equivalent to {f}° Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")