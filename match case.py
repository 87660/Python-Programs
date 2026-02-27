x=int(input("Enter value :"))
match x:
    case 0:
     print("case id incorrect")
    case 2:
      print("case not found")
    case 3:
      print("error")
    case _:
      print(x)