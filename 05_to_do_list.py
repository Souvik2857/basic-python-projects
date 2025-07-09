print("Welcome to to list")
task=[]
tasks=int(input("How many tasks you want to add?\n"))
for i in range(1,tasks+1):
    task_input=input(f"Enter your task {i}:")
    task.append(task_input)
print(f"your total tasks are {task}")



other_task=input("Do you want to edit this list:")
try:
    if(other_task=="yes"):
        while True:
            other_tasks=int(input("Select what you will want to do\n1.add\n2.replace\n3.delete\n4.view list\n5.close\n"))
            if(other_tasks==1):           
                add=input("What will you want to add: ")
                task.append(add)
                print(f"your task is succesfully added to your list")
            elif(other_tasks==2):
                old_task=input("what task will you want to replace: ")
                if old_task in task:
                    new_task=input("Enter your new task: ")
                    ind=task.index(old_task)
                    task[ind]=new_task
                    print(f"You task {old_task} is replaced by {new_task}")             
                else:
                    print(f"{old_task} is not in the list")
            elif(other_tasks==3):
                remove=input("Enter task you want to delete: ")
                if remove in task:
                    ind=task.index(remove)
                    del task[ind]
                    print(f"you succesfully delete {remove} task")
                else:
                    print(f"{remove} is not in the list")
            elif(other_tasks==4):
                print(f"your List is\n{task}")
            elif(other_tasks==5):
                print("closing this programme.......")
                break
            else:
                print("input unavailable")
    elif(other_task=="no"):
        print("Closing the programme.......")
    else:
        print("Enter yes or no")
except Exception as e:
    print(e)

        



