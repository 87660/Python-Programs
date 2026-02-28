temp = int(input("Enter temp :"))
unit = input("Enter unit(C for celcius and F for fahrenheit): ")
C = 0
F = 0
if unit == C:
   C +=temp
   print("Converting celcius to fahrenheit")
   𝐹 = 𝐶 * 9/5 + 32
     

elif unit == F:
   F +=temp
   print("Converting fahrenheit to celcius")
   𝐶 = (𝐹 - 32) * 5/9

print(f"Result: \ncelcius:{C} \nfahrenheit:{F}")