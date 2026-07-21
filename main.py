
todo_list = []

def addList():
    item = input("Enter a New task: ")
    todo_list.append(item)
    print(f"{item} added to the todo List")
def displayList():
    print("-----------")
    print("To Do List:")
    print("-----------")
    for index,item in enumerate(todo_list,start=1):
        print(f"{index}-{item}")
def removelist():
    displayList()
    index = int(input("enter Your Item number to remove:"))-1

    if 0<= index < len(todo_list):
        removed_item = todo_list.pop(index)
        print(f"{removed_item} removed From list")

    else:
        print("Invalid Input")

    
while True:

    print("******************")
    print(" To Do List App  ")
    print("******************")
    print("1 - Add To List ")
    print("2 - Display List ")
    print("3 - Remove From  List ")
    print("4 - Exit ")


    option = input("Select you option:")

    if option == '1':
        addList()
    elif option == '2':
        displayList()
    elif option =='3':
        removelist() 
    elif option == '4':
        print("Exit")
        break

    else:
        print("Invalid Option.......")





