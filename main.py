from classes import OrderBook                                    #importing the OrderBook class from classes.py

def main():                                                       #main function to run the program
    order_book = OrderBook()                                      #creating an instance of the OrderBook class
    while True:                                                   #while loop to run the program       
            command = input("command: ").strip()                  #input to get the command from the user

            if not command:                             
                print("erroneous input.")
                continue

            parts = command.split(" ")                            #splitting the command into parts

            if parts[0] == "0":                                   #exit the program when the user enters 0     
                print("exiting...")
                break                                             #break statement to exit the loop when the user enters 0

            elif parts[0] == "1":                                 #add order when the user enters 1
                description = input("description: ").strip()      #input to get the description of the task from the user
                programmer_info = input("programmer and workload estimate: ").strip()   #input to get the programmer and workload estimate from the user

                try:                                              #try block to catch any exceptions
                    programmer, workload = programmer_info.rsplit(" ", 1)
                    workload = int(workload)                      #converting the workload to an integer
                    order_book.add_order(description, programmer, workload)   #calling the add_order method to add the task to the list of tasks
                    print("added!")                               #printing added when the task is added   
                except ValueError:                                #except block to catch any value errors       
                    print("erroneous input.")                     #printing erroneous input when there is an error

            elif parts[0] == "2":                                 #list finished tasks when the user enters 2
                finished = order_book.finished_tasks()            #calling the finished_tasks method to get all the finished tasks
                if finished:                                      #if statement to check if there are any finished tasks
                    for task in finished:                         #loop to iterate through all the finished tasks  
                        print(task)                               #printing the task
                else:
                    print("no finished tasks")                    #printing no finished tasks when there are 0 finished tasks      

            elif parts[0] == "3":                                 #list unfinished tasks when the user enters 3
                unfinished = order_book.unfinished_tasks()        #calling the unfinished_tasks method to get all the unfinished tasks
                if unfinished:                                    #if statement to check if there are any unfinished tasks
                    for task in unfinished:                       #loop to iterate through all the unfinished tasks
                        print(task)
                else:
                    print("No unfinished tasks.")                 #printing no unfinished tasks when there are 0 unfinished tasks

            elif parts[0] == "4":                                 #mark task as finished when the user enters 4
                try:                                              #try block to catch any exceptions
                    task_id = int(input("Id: ").strip())        
                    order_book.mark_finished(task_id)             #calling the mark_finished method to mark the task as finished
                    print(f"marked as finished.")
                except ValueError:                                #except block to catch any value errors
                    print("erroneous input.")               

            elif parts[0] == "5":                                 #programmers : print programmers sorted by their total workload when the user enters 5
                programmers = order_book.programmers()            #calling the programmers method to get all the programmers
                if programmers:                                   #if statement to check if there are any programmers              
                    workload_dict = {programmer: 0 for programmer in programmers}   #initializing a dictionary to store the workload of each programmer
                    for task in order_book.all_orders():                            #loop to iterate through all the tasks
                        workload_dict[task.programmer] += task.workload             #adding the workload of each task to the workload of the programmer
                    sorted_programmers = sorted(workload_dict.items(), key=lambda x: x[1], reverse=True)        #sorting the programmers by their total workload
                    for programmer, workload in sorted_programmers:
                        print(programmer)
                else:
                    print("No programmers found.")

            elif parts[0] == "6":                                 #status of programmer's workload and tasks when the user enters 6
                programmer = input("programmer: ").strip()      
                try:                
                    status = order_book.status_of_programmer(programmer)            #calling the status_of_programmer method to get the status of the programmer's workload and tasks
                    print(f"tasks: Finished {status[0]}, not finished {status[1]}, "                            #printing the status of the programmer's workload and tasks
                          f"hours: done {status[2]}, scheduled {status[3]}")   
                except ValueError:                                #except block to catch any value errors
                    print("Erroneous input.")

            else:
                print("Erroneous input.")           



if __name__ == "__main__":           
    main()