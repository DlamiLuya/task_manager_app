#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime
#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
# Open txt file user.txt and read it to users_contents which is then split to list "list_user_contents" using "\n" which is by line.
# Declare list variables that will sort and store the data in th users.txt file. 
users = open('user.txt', 'r')
users_contents = users.read()
list_users_contents = users_contents.split("\n")
# line_contents will store the data in the fashion["username, password", "username, password", ...etc]
# proper_list will store the data in the fashion of a list within a list[[username, password],[username, password], ...etc]
line_contents = []
proper_list = []
# Declare boolean variable that will store the results of the verification of the user logins.
user_boolean = False 
username_boolean = False
password_boolean = False

# For loop will run through the list of user contents and split them by the "," and store them into the list proper_list
for line in range(len(list_users_contents)):
    proper_list.append(list_users_contents[line].split(","))  

# While loop will verify the user name and password entered by the user with that in the database.
# Prompt user to enter username and password.
# The inner for loop will read through the proper_list, for the first index of the proper list verify the elements of first index at [0] and [1] for username and password respectively
# After verification of username and password make the respective boolean variables to true to indicate a succesfull verification, this will also prompt the closure of the while loop.
# The while loop is set so that so long as the password boolean is false, it will continue to propmpt user for the login details, until true, then opt out of the while loop.
while password_boolean == False:
    input_username = input("enter user name: ")
    input_password = input("enter password: ")
    for first_index in proper_list:
         if input_username == first_index[0]:
            username_boolean = True
            if input_password == first_index[1].strip():
                password_boolean = True
                print(f"Welcome {input_username}")
# Close the open txt file.
users.close()

# The purpose of this statement is to further verify that the user has logged in, it will set the username_boolean to true only if the login verification process was succesful.
if username_boolean == True and password_boolean == True:
    user_boolean = True   


# Define a function that will enable users to register new users
def reg_user():
    users = open('user.txt', 'r+')
    users_content = users.read()
    line_user_content= users_content.split("\n")
    while True:
        new_user = input("Enter new user name.: ") # Prompt user to enter credentials of the new user and password which is confirmed.
        new_password = input("Enter new user password.: ")
        confirm_password = input("Confirm user password.: ")
        count = 0
        for line in range(len(line_user_content)): # To check if the user already exists within the database of users.
            sub_list_nested_users = line_user_content[line].split(",")
            if sub_list_nested_users[0].strip() == new_user:
                count += 1
            
        if count > 0:
            print("user already exists, please try again")
        else:
            break
    while True:      
        if new_password == confirm_password: # This part confirms the password entered, if it doesnt match, it will prompt user to reenter till they match.
            users.write("\n"+new_user +"," + new_password)
            print("New user registered.")
            break
        else:
            print("password does not match")
            new_password = input("Enter new user password.: ")
            confirm_password = input("Confirm user password.: ")               
            
    users.close()


# Define a function that will allow the admin to add a new task.
def add_task():
    if input_username == "admin": # This is to check if the user who is logged in is an admin.
        users = open('user.txt', 'r')
        tasks = open('tasks.txt', 'a+')
        user_task = input("Task Assignee.: ")# Prompt admin to enter the person who they'll assign the task to.
        users_content = users.read()
        line_user_content= users_content.split("\n")
        user_count = 0
        for line in range(len(line_user_content)):# These statements are to check if the person that the admin is assigning the task to exists as a user in the database.
            list_contents_user = line_user_content[line].split(",")
            if list_contents_user[0].strip() == user_task:
                user_count += 1
                title_task = input("Enter title task.: ") # Prompt user to enter Task details and write on the task txt file.
                discription_task = input("Enter task discription.: ")
                while True:
                    task_due = input("Enter task due date. as dd-mm-yyyy: ")
                    try: # Statement to validate that the date given by the user is in the correct format.
                        date_valid = datetime.datetime.strptime(task_due,'%d-%m-%Y')
                        break
                    except ValueError:
                        print("You haven't given me the right date format, try agin")
                date_now = datetime.datetime.now().strftime("%d-%m-%Y") # Statement to get the current date.
                return tasks.write(f"\n{user_task}, {title_task}, {discription_task}, {date_now}, {task_due}, NO")
            
        if user_count == 0:
            print("The user does not exist, you can register them on the main menu.\n")

        tasks.close()
        users.close()
    else:
        return print("User prohibited, only admins allowed this function.")
    

# Define a function that will enable the user to view all the tasks in the database, whether complete or not and by all users.    
def view_all():
    tasks = open('tasks.txt', 'r')
    tasks_content = tasks.read()
    line_tasks_content= tasks_content.split("\n")
    for line in range(len(line_tasks_content)):
        list_contents_task = line_tasks_content[line].split(",")
        print('---------------------------------------------------------')
        print(f"Task no.: {line+1}")
        print(f'''Task:                 {list_contents_task[1]}
Assigned to:           {list_contents_task[0]}
Date assigned:        {list_contents_task[3]}
Due date:             {list_contents_task[4]}
Task Complete?        {list_contents_task[5]}
Task description:\n {list_contents_task[2]}\n''')
        print('---------------------------------------------------------')
    tasks.close() 

# Function that will print out the login user's tasks and give each task a number as a reference.
def view_mine():
    tasks = open('tasks.txt', 'r+')
    tasks_content = tasks.read()
    line_tasks_content= tasks_content.split("\n")
    for line in range(len(line_tasks_content)):
        list_contents_task = line_tasks_content[line].split(",")
        if list_contents_task[0].strip() == input_username:
            print('---------------------------------------------------------')
            print(f"Task no.: {line+1}")
            print(f'''Task:                 {list_contents_task[1]}
Assigned to:           {list_contents_task[0]}
Date assigned:        {list_contents_task[3]}
Due date:             {list_contents_task[4]}
Task Complete?        {list_contents_task[5]}
Task description:\n {list_contents_task[2]}\n''')
            print('---------------------------------------------------------')
            
# Retrive users chosen task and print it out.
    task_number = int(input("Choose a task, enter the Task no: "))
    list_contents_task = line_tasks_content[task_number-1].split(",")
    if list_contents_task[0].strip() == input_username:
        print(f"Task no.: {task_number}")
        print(f'''Task:                 {list_contents_task[1]}
Assigned to:           {list_contents_task[0]}
Date assigned:        {list_contents_task[3]}
Due date:             {list_contents_task[4]}
Task Complete?        {list_contents_task[5]}
Task description:\n {list_contents_task[2]}\n''')
        tasks.close()

        # This smaller menu will allow the user to chose what they would like to do to their task.
        edit_choice= input('''1. Complete task
2. Edit task
3. exit
Enter option no.: ''')
        if edit_choice == "1": # Option one changes the Task complete? part to Yes and amend this on the txt file.
            tasks = open('tasks.txt', 'w')
            list_contents_task[5] = "YES"
            line_tasks_content[task_number-1] = ",".join(list_contents_task)
            line_tasks_content = "*".join(line_tasks_content)
            line_tasks_content= line_tasks_content.replace("*","\n")
            tasks.write(line_tasks_content)
            tasks.close() 
            print("Your task has been amended as complete\n")

        elif edit_choice == "2": # Option two enables the user to edit their task only if it has not yet been complete. 
            if list_contents_task[5].strip() == "NO":
                new_assignee = input("Enter new Task Assignee.: ") # Prompt user to enter the new user of the task and the new due date.
                while True:
                    new_date = input("Enter task due date. as dd-mm-yyyy: ")
                    try: # Statement to validate that the date given by the user is in the correct format.
                        date_valid = datetime.datetime.strptime(new_date,'%d-%m-%Y')
                        break
                    except ValueError:
                        print("You haven't given me the right date format, try agin")
                users = open('user.txt', 'r')
                users_content = users.read()
                line_user_content= users_content.split("\n")
                user_count = 0
                for line in range(len(line_user_content)):
                    list_contents_user = line_user_content[line].split(",")
                    if list_contents_user[0].strip() == new_assignee: # This is to check if the new user assigned exists within the user database.
                        user_count += 1
                        list_contents_task[0] = new_assignee # If the user exists, amend the task and write on the task txt file.
                        list_contents_task[4] = new_date
                        line_tasks_content[task_number-1] = ",".join(list_contents_task)
                        line_tasks_content = "*".join(line_tasks_content)
                        line_tasks_content = line_tasks_content.replace("*","\n")
                        tasks = open('tasks.txt', 'w')
                        tasks.write(line_tasks_content)
                        print("Your task has been amended\n")
                if user_count == 0:
                    print("oops, user doesnt exist\n")

                tasks.close()
                users.close()
            else:
                print("This task is already complete, you cannot edit.\n")
            
        elif edit_choice == "3":
            quit()
        else:
            print("oops, you've made a mistake.\n")
    
    else:
        print("No such task number exists for you.\n")
    tasks.close()


# This function will create a txt file that will contain stats of the tasks associated with task_manager.py.
def create_task_overview():
    task_stats = open("task_overview.txt",'w+')
    number_tasks_completed = 0 # define varibles that will store the stats prior to being written on the txt file, assign 0 to them as a base before any stats are added.
    number_tasks_incomplete = 0
    overdue_tasks = 0
    tasks = open('tasks.txt', 'r+')
    tasks_content = tasks.read()
    line_tasks_content= tasks_content.split("\n")
    task_stats.write(f"Number of tasks: {len(line_tasks_content)}\n") # This will count the total number of tasks

    for line in range(len(line_tasks_content)):
        list_contents_task = line_tasks_content[line].split(",")
        if list_contents_task[5].strip() == "YES": # This will count the total number of tasks completed and write it on the txt file.
            number_tasks_completed += 1
        elif list_contents_task[5].strip() == "NO":# Counts the total number of tasks that are not complete
            number_tasks_incomplete += 1
            due_date = datetime.datetime.strptime(list_contents_task[4].strip(),'%d-%m-%Y') # due date and the current date conversion into comparable format.
            date_now = datetime.datetime.now().strptime(datetime.datetime.now().strftime("%d-%m-%Y"),"%d-%m-%Y")
            if due_date < date_now :# Comparing the dates to see if any is overdue.
                overdue_tasks += 1 
     #Write the stats on the txt file in a user friendly manner and also print appropriate message. 
    task_stats.write(f'''Number of Completed Tasks:       {number_tasks_completed} 
Number of uncompleted Tasks:     {number_tasks_incomplete}
Number of overdue Tasks:         {overdue_tasks}
Percentage of Incomplete Tasks:  {round((number_tasks_incomplete/len(line_tasks_content))*100,2)}%
Percentage of overdue Tasks:     {round((overdue_tasks/len(line_tasks_content))*100,2)}%\n''')

    print("\nYour task_overview.txt stats have been generated.\n")

    tasks.close()
    task_stats.close()


# Define a function that will create a txt file that will house the user stats.
def create_users_overview():
    users = open('user.txt', 'r')
    tasks = open('tasks.txt', 'r')
    user_stats = open("user_overview.txt",'w+')
    users_contents = users.read()
    line_users_content= users_contents.split("\n")
    user_stats.write(f"Total number of users :     {len(line_users_content)}\n")
    tasks_contents = tasks.read()
    line_tasks_content= tasks_contents.split("\n")
    user_stats.write(f"Total number of tasks :     {len(line_tasks_content)}\n")
    
    for line in range(len(line_users_content)):
        list_users_contents = line_users_content[line].split(',')
        users_task_count = 0 # variables that will store the data used in the calculation of stats.
        users_task_count_complete = 0
        users_task_count_incomplete = 0
        overdue_tasks = 0
        for line in range(len(line_tasks_content)):# following statements are those that give values to the afore mentioned variables for stats use.
            list_contents_task = line_tasks_content[line].split(",")
            if list_users_contents[0].strip() == list_contents_task[0].strip():
                users_task_count += 1
                if list_contents_task[5].strip() == "YES":
                    users_task_count_complete +=1
                elif list_contents_task[5].strip() == "NO":
                    users_task_count_incomplete += 1
                    due_date = datetime.datetime.strptime(list_contents_task[4].strip(),'%d-%m-%Y') # due date and the current date conversion into comparable format.
                    date_now = datetime.datetime.now().strptime(datetime.datetime.now().strftime("%d-%m-%Y"),"%d-%m-%Y")
                    if due_date < date_now :# Comparing the dates to see if any is overdue.
                        overdue_tasks += 1 
        user_stats.write(f'''----------------------------------------------------------
{list_users_contents[0]}'s Stats\n''')
        user_stats.write(f"Number of tasks: {users_task_count}\n")
        try: # this statements writes the defined user stats on the txt file, if user does not have any tasks, it will write the latter stats.
            user_stats.write(f'''Percentage of tasks assigned:    {round((users_task_count/len(line_tasks_content))*100,2)}%
Percentage of tasks complete:    {round((users_task_count_complete/users_task_count)*100,2)}%
Percentage of tasks incomplete:  {round((users_task_count_incomplete/users_task_count)*100,2)}%
Percentage of overdue Tasks:     {round((overdue_tasks/len(line_tasks_content))*100,2)}%\n''')
        except ZeroDivisionError:
            user_stats.write('''Percentage of tasks assigned:    0%
Percentage of tasks complete:   0%
Percentage of tasks incomplete: 0%
Percentage of overdue Tasks:    0%\n''')

    print("Your user_overview.txt stats have been generated.\n")
    users.close()
    tasks.close()
    user_stats.close()

        

# A while loop that will only initiate once the login verification is succesful.
while user_boolean == True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if input_username == "admin":# admin menu
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display stats
e - Exit
: ''').lower()
    else:# general user menu
        menu = input('''Select one of the following Options below: 
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
        
    
    # If statements that call on functions that are specified by the users input.
    if menu == 'r':# Option to register a new user.
        reg_user()


    elif menu == 'a':# Option only available to admin, will add a new task and assign it to an existing user.
        add_task()


    elif menu == 'va':# Option allows user to view all tasks.
        view_all()


    elif menu == 'vm':# Option allows logged in user to view their tasks and edit them.
        view_mine()


    elif menu == 'gr':# This option creates stats and writes them on a txt file.
        create_task_overview()
        create_users_overview()

        
    elif menu == 'ds':
        # Option will create the user and task stats then print them out on the terminal from their respective txt files.
        create_task_overview()
        create_users_overview()
        user_stats = open("user_overview.txt",'r')
        user_stats_content= user_stats.read()
        task_stats = open("task_overview.txt",'r')
        task_stats_content = task_stats.read()
        print(f"Task overview stats\n______________________\n{task_stats_content}")
        print(f"User overview stats\n______________________\n{user_stats_content}")
        user_stats.close()
        task_stats.close()
                
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

