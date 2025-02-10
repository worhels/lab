
list = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@mail.com", "address": "123 Elm St"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@mail.com", "address": "456 Oak St"},
    {"name": "Jon", "phone": "0631234567", "email": "jon@mail.com", "address": "789 Pine St"},
    {"name": "Zak", "phone": "0631234567", "email": "zak@mail.com", "address": "101 Maple St"}
]

def printAllList():
    for elem in list:
        strForPrint = f"Student name is {elem['name']},  Phone is {elem['phone']}, Email is {elem['email']}, Address is {elem['address']}"
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    address = input("Please enter student address: ")
    newItem = {"name": name, "phone": phone, "email": email, "address": address}
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del list[deletePosition]
        print("Element has been deleted")
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    for item in list:
        if name == item["name"]:
            print("Updating information. Leave fields blank to keep current values.")
            new_phone = input(f"Current phone ({item['phone']}): ")
            new_email = input(f"Current email ({item['email']}): ")
            new_address = input(f"Current address ({item['address']}): ")
            item["phone"] = new_phone if new_phone else item["phone"]
            item["email"] = new_email if new_email else item["email"]
            item["address"] = new_address if new_address else item["address"]
            list.sort(key=lambda x: x["name"])
            print("Element has been updated")
            return
    print("Element not found")
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
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
                print("Wrong chouse")

main()
