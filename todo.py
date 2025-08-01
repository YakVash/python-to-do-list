def display_menu():
  print("\n--- TO-DO LIST ---")
  print("1. VIEW TASKS")
  print("2. ADD TASKS")
  print("3. DELETE TASKS")
  print("MARK TASK AS DONE")
  print("5. EXIT")

def main():
  tasks=[]
  while True:
    display_menu()
    choice=input("Enter your choice:")
    if choice=="1":
      if not tasks:
         print("No Tasks found.")
      else:
        for i,task in enumerate(tasks,start=1):
          print(f"{i}.{task}")
    elif choice=="2":
      task=input("Enter new task")
      tasks.append(task)
      print("Task added successfully.")
    elif choice=="3":
      try:
        task_num=int(input("Enter task number to delete:"))-1
        tasks.pop(task_num)
        print("task deleted.")
      except (IndexError,ValueError):
        print("Invalid task number.")
    elif choice=="4":
      print("Feature coming soon!")
    elif choice=="5":
      print("Exiting program. Goodbye!")
      break
    else:
      print("Invalid choice! Please try again.")
if __name__=="__main__":
  main()
      
