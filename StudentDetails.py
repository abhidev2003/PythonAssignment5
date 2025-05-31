studentdetails ={"Bruce Wayne":100,"Dick Grayson":98,"Jason Todd":97,"Barbara Gordon":95}
name = input("Enter the student's name")
if name not in studentdetails:
    print("Student not found")
else:
    print(f"{name}'s marks :{studentdetails[name]}")

