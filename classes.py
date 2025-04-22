class Task:                                #creation of a class Task with attributes description, programmer, workload, status and id
    _id_counter = 1

    def __init__(self, description, programmer, workload):         #constructor for Task class via __init__ method
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.status = False
        self.id = Task._id_counter
        Task._id_counter += 1

    def is_finished(self):                                         #method to check if a task is finished
        return self.status

    def mark_finished(self):                                      #method to mark a task as finished
        self.status = True

    def __str__(self):                                           #method to return a string representation of a task                        
        return (f"{self.id} : " 
                f"{self.description} "
                f"({self.workload} hours), "
                f"programmer {self.programmer} "
                f"{'FINISHED' if self.status else 'NOT FINISHED'}")
                


#Test code for Task class

#t1 = Task("programm hello world", "Eric", 3)
#print(t1.id, t1.description, t1.programmer, t1.workload)
#print(t1)
#print(t1.is_finished())
#t1.mark_finished()
#print(t1)
#print(t1.is_finished()) 

#t2 = Task("programm webstore", "adele", 10)
#t3 = Task ("programm mobile app for workload accounting", "Eric", 25)
#print(t2)
#print(t3)


class OrderBook:                         #creation of a class OrderBook with attributes tasks                           
    def __init__(self):                 #constructor for OrderBook class via __init__ method
        self.tasks = []

    def add_order(self, description, programmer, workload):                         #method to add a new task to the list of tasks
        new_task = Task(description, programmer, workload)
        self.tasks.append(new_task)

    def all_orders(self):                                               #method to return all tasks
        return self.tasks   
    
    def programmers(self):                                          #method to return all programmers
        programmers = {task.programmer for task in self.tasks}
        return sorted(programmers)
    

    def task_by_programmer(self):                                   #method to return all tasks by programmer        
        tasks_by_programmer = {}
        for task in self.tasks:
            if task.programmer not in tasks_by_programmer:
                tasks_by_programmer[task.programmer] = []
            tasks_by_programmer[task.programmer].append(task.id)
        return tasks_by_programmer

    def mark_finished(self, task_id):               #method to mark a task as finished
        for task in self.tasks:
            if task.id == task_id:
                task.mark_finished()
                return
        raise ValueError

    def finished_tasks(self):                               #method to return all finished tasks
        return [task for task in self.tasks if task.is_finished()]
    
    def unfinished_tasks(self):                     #method to return all unfinished tasks          
        return [task for task in self.tasks if not task.is_finished()]
    

    def status_of_programmer(self, programmer):             #method to return the status of a programmer's workload and tasks   
        if programmer not in self.programmers():
            raise ValueError(f"No programmer found with name {programmer}")
        
        finished_tasks = 0                                  #initializing variables to count the number of finished and unfinished tasks and hours
        unfinished_tasks = 0
        finished_hours = 0
        unfinished_hours = 0

        for task in self.tasks:                         #loop to iterate through all tasks and count the number of finished and unfinished tasks and hours
            if task.programmer == programmer:
                if task.is_finished():
                    finished_tasks += 1
                    finished_hours += task.workload
                else:
                    unfinished_tasks += 1
                    unfinished_hours += task.workload

        return (finished_tasks, unfinished_tasks, finished_hours, unfinished_hours)

#test code 
#orders = OrderBook()
#orders.add_order("programm webstore", "Adele", 10)
#orders.add_order("programm mobile app for wokload accounting", "Adele", 25)
#orders.add_order("programm app for practising mathematics", "Adele", 100)
#orders.add_order("program teh next facebook", "Eric", 1000)


#orders.mark_finished(1)
#orders.mark_finished(2)



#for order in orders.all_orders():
    #print(order)

#status = orders.status_of_programmer("Adele")
#print(status)


    