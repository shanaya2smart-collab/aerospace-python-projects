import math
user_name=(input("pleae enter your name"))
print(f"hi,{user_name}! please eneter your values for delta v calculation")
ve=float(input("enter ve(exhaust velocity of rocket):"))
m0=float(input("enter mass of rocket including fuel/systems:"))
mf=float(input("please enter the end mass of the rocket without fuel/systems:"))

mass_ratio=m0/mf
math.log(mass_ratio)
log_result=math.log(mass_ratio)*ve

print(f"{log_result} is the delta v of the specified rocket")

if log_result>=9400:
    print("this velocity is high enough to reach orbit")

else:
    print("this velocity isnt enough to reach orbit")
