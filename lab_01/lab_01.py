student_list = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "address": "123 Street"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@example.com", "address": "456 Avenue"},
    {"name": "Jon",  "phone": "0631234567", "email": "jon@example.com", "address": "789 Boulevard"},
    {"name": "Zak",  "phone": "0631234567", "email": "zak@example.com", "address": "101 Road"}
]

def printAllList():
    for elem in student_list:
        print(f"Student name is {elem['name']}, Phone is {elem['phone']}, Email is {elem['email']}, Address is {elem['address']}")
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    address = input("Please enter student address: ")
    newItem = {"name": name, "phone": phone, "email": email, "address": address}
    
    insertPosition = 0
    for item in student_list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    student_list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in student_list:
        if name == item["name"]:
            deletePosition = student_list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del student_list[deletePosition]
        print("Element has been deleted")
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    for student in student_list:
        if student["name"] == name:
            print("Updating details for student:", name)
            phone = input("Enter new phone (or leave empty to keep current): ")
            email = input("Enter new email (or leave empty to keep current): ")
            address = input("Enter new address (or leave empty to keep current): ")

            if phone:
                student["phone"] = phone
            if email:
                student["email"] = email
            if address:
                student["address"] = address

            student_list.sort(key=lambda x: x['name'])
            print("Student information updated")
            return

    print("Student not found")

def main():
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")

main()
