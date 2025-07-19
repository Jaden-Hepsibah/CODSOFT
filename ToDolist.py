ToDolist=[]
def Add_task():
  task=input("Enter a new task: ")
  ToDolist.append({"task" : task, "Status" : "pending"})
  print("New task is added sucessfully!\n")


def View_task():
  print("Your To-Do List")
  if len(ToDolist)==0:
    print("No pending taks")
  else:
    for index, task in enumerate(ToDolist, 1):
      print(f" {index}: {task['task']} - {task['Status']}")
  print("\n")

def  Remove_task():
  if len(ToDolist)==0:
    print("List is empty")
  else:
    try:
      searchIndex=int(input("Enter a task number to remove : ")) -1
      if 0<=searchIndex<len(ToDolist):
        removed_task=ToDolist.pop(searchIndex)
        print(f"Task removed: {removed_task['task']}")
      else:
        print("Invalid task number")
    except ValueError:
      print("Please enter a valid task number.")
      
def Mark_task():
  if len(ToDolist)==0:
    print("List is empty")
  else:
    try:
      searchIndex=int(input("Enter a task number to mark as done: ")) -1
      if 0<=searchIndex<len(ToDolist):
        ToDolist[searchIndex]['Status']='done'
        print(f"Task '{ToDolist[searchIndex]['task']} has been marked as done")
      else:
        print("Invalid task number")
    except ValueError:
      print("Please enter a valid task number.")

      
def menu():
  while True:
    print("____MAIN MENU___")
    print("(1) Add a new task")
    print("(2) View all tasks")
    print("(3) Remove a task")
    print("(4) Mark a task as done")
    print("(5) Exit")
    
    option= int(input("Enter an option: "))
    
    if option==1:
      Add_task()
    elif option==2:
      View_task()
    elif option==3:
      Remove_task()
    elif option==4:
      Mark_task()
    elif option==5:
      print("Exiting the application")
      break
    else:
      print("Invalid option. Try Again!")
menu()
    
