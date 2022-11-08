# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley Brown
#               Connor McGuire
#               Gretta Weich
#               Collin Alexander
# Section:      563
# Assignment:   Lab 4.13: Pretty_Equation
# Date:         09/23/22

# Quadradic = ax^2+bx +c = 0

coeA = int(input("Please enter the coefficient A: "))
coeB = int(input("Please enter the coefficient B: "))
coeC = int(input("Please enter the coefficient C: "))
strA = "x^2 "
strB = "x "
strC = ""

# COEA formatting the second term of the equation
if((coeA == -1) or (coeA == 1)):
  if(coeA == -1):
    strA = f"- {strA}"
elif(coeA == 0):
  strA = ""
else:
  if(coeA > 0):
    strA = f"{coeA}{strA}"
  else:
    strA = f"- {abs(coeA)}{strA}"

# COEB formatting the second term of the equation
if((coeB == -1) or (coeB == 1)):
  if(coeB == -1):
    strB = f"- {strB}"
  else:
    if(strA != ""):
        strB = f"+ {strB}"
elif(coeB == 0):
  strB = ""
else:
  if(coeB > 0):
    if(strA == ""):
        strB = f"{coeB}{strB}"
    else:
        strB = f"+ {coeB}{strB}"
  else:
    strB = f"- {abs(coeB)}{strB}"

# COEC formatting the third term of the equation
if(coeC == 0):
  strC = ""
else:
  if(coeC > 0):
    strC = f"+ {coeC} "
  else:
    strC = f"- {abs(coeC)} "
print(f"The quadratic equation is {strA}{strB}{strC}= 0")
