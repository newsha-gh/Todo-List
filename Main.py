title = input("Enter Title:\n")
todolist = []
while title.lower() != "exit":
    if title.strip():
     todolist.append(title)
    else:
        print("Please enter a valid title.")
    title = input("Enter Title:\n")
    if title.lower() == "show cards":
        for i in range(0, len(todolist)):
            print(f"{i+1}) {todolist[i]}")
