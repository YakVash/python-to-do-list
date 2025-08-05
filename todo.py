#todolist
def display_menu():
  print("\n--- TO-DO LIST ---")
  print("1. VIEW TASKS")
  print("2. ADD TASKS")
  print("3. DELETE TASKS")
  print("4. MARK TASK AS DONE")
  print("5. EXIT")
def mark_done(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        tasks[task_num]["done"] = True
        print("Task marked as done.")
    except (IndexError, ValueError):
        print("Invalid task number.")


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
          status = "✅" if task["done"] else "❌"
          print(f"{i}. {task['task']} [{status}]")
    elif choice=="2":
      task_name=input("Enter new task")
      tasks.append({"task": task_name, "done": False})
      print("Task added successfully.")
    elif choice=="3":
      try:
        task_num=int(input("Enter task number to delete:"))-1
        tasks.pop(task_num)
        print("task deleted.")
      except (IndexError,ValueError):
        print("Invalid task number.")
    elif choice=="4":
      mark_done(tasks)
    elif choice=="5":
      print("Exiting program. Goodbye!")
      break
    else:
      print("Invalid choice! Please try again.")
if __name__=="__main__":
  main()
      
