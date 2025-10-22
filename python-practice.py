class Task:
    def __init__(self, title, description, status="Pending"):
        self.title = title
        self.description = description
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        return len(self.tasks) - 1  # Return task ID
    
    def complete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id].status = "Completed"
            return True
        return False
    
    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"Task {i}: {task.title} - {task.status}")
            print(f"Description: {task.description}\n")

def main():
    manager = TaskManager()
    
    # Adding sample tasks
    manager.add_task("Learn Python", "Study basic Python concepts")
    manager.add_task("Build Project", "Create a simple project using Python")
    
    # Display all tasks
    print("Current Tasks:")
    manager.list_tasks()
    
    # Complete a task
    manager.complete_task(0)
    
    print("\nAfter completing task 0:")
    manager.list_tasks()

if __name__ == "__main__":
    main()
    
    
    # Test push from local
# Test push from local
# Test push from local
# Test push from local
