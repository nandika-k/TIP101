def get_highest_priority_task(tasks):
	highest_priority = ("task", 0)
	
	#for task, priority in zip(tasks.keys(), tasks.values()):
	for task, priority in tasks.items(): #easier to do tasks.items()
		if priority > highest_priority[1]:
			highest_priority=(task, priority)
	high_priority_task = highest_priority[0]
	tasks.pop(high_priority_task)
	return high_priority_task
		

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)