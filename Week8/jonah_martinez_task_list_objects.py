# Assignment: Task List Objects
# Class: DEV 128
# Date: 06/02/2025
# Author: Jonah Martinez
# Description: Implements the business tier classes for a task list application.


class Task:
    def __init__(self, id: int, description: str, completed: bool = False):
        self.__id = id
        self.__description = description
        self.__completed = completed

    @property
    def id(self):
        return self.__id

    @property
    def completed(self):
        return self.__completed

    @property
    def description(self):
        return self.__description

    # Setter for description with validation to ensure it is not empty
    @description.setter
    def description(self, value: str):
        if not isinstance(value, str) or not value.strip():
            print("Description cannot be empty")
            return
        self.__description = value.strip()

    def mark_completed(self):
        self.__completed = True

    def mark_incomplete(self):
        self.__completed = False

    # Override the string representation of the Task object
    def __str__(self):
        return (
            f"Description: {self.__description} {"(DONE!)" if self.__completed else ""}"
        )


class TaskList:
    def __init__(self, name: str):
        self.__tasks = (
            {}
        )  # Dictionary to hold tasks with task ID as key, and Task object as value
        self.__name = name
        self.__next_id = 1  # auto-incrementing task id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name cannot be empty")
        self.__name = value.strip()

    # Add a task to the task dictionary
    def add_task(self, description: str):
        task = Task(self.__next_id, description)
        self.__tasks[self.__next_id] = task
        self.__next_id += 1  # auto-increment task id

    # Get a task by its id
    def get_task(self, task_id: int):
        if task_id not in self.__tasks:
            raise ValueError(f"Task with ID {task_id} not found.")
        return self.__tasks[task_id]

    # Remove a task by its id
    def remove_task(self, task_id: int):
        if task_id not in self.__tasks:
            raise ValueError(f"Task with ID {task_id} not found.")
        del self.__tasks[task_id]

    # List all tasks in the task dictionary
    # If no tasks are present, it will print a message indicating that no tasks are in the list
    def list_tasks(self):
        if not self.__tasks:
            print(f"No tasks in {self.name}.")
            return
        for task in self.__tasks.values():
            print(task)

    # Override the string representation of the TaskList object
    def __str__(self):
        return f"{self.name.capitalize()}"


def main():
    print("Task - Tester")
    print()

    # Create two task lists: Business and Personal
    business_tasks = TaskList("Business Tasks")
    personal_tasks = TaskList("Personal Tasks")

    # Add tasks to each list
    business_tasks.add_task("Prepare presentation for client meeting")
    business_tasks.add_task("Review quarterly budget report")
    personal_tasks.add_task("Buy groceries for the week")
    personal_tasks.add_task("Schedule dentist appointment")
    personal_tasks.add_task("Plan weekend hiking trip")

    # List tasks in each list
    print("Business Tasks:")
    business_tasks.list_tasks()
    print("\nPersonal Tasks:")
    personal_tasks.list_tasks()

    # Mark a task as completed
    print("\nMarking task 1 as completed in Business Tasks:")
    business_tasks.get_task(1).mark_completed()
    print("Marking task 2 as completed in Personal Tasks:")
    personal_tasks.get_task(2).mark_completed()

    # Display specific tasks marked as completed
    print("\nCompleted Tasks:")
    print(f"{business_tasks.get_task(1)}")
    print(f"{personal_tasks.get_task(2)}")

    # Mark a task as incompleted
    print("\nMarking task 1 as incomplete in Business Tasks:")
    business_tasks.get_task(1).mark_incomplete()
    print(f"{business_tasks.get_task(1)}")

    # Update a task description
    print("\nUpdating task 1 description in Business Tasks:")
    business_tasks.get_task(1).description = (
        "Prepare presentation for client meeting with updated data"
    )
    print(f"{business_tasks.get_task(1)}")

    # Remove a task
    print("\nRemoving task 2 from Business Tasks:")
    business_tasks.remove_task(2)
    print("Removing task 3 from Personal Tasks:")
    personal_tasks.remove_task(3)

    print("\nBusiness Tasks:")
    business_tasks.list_tasks()
    print("\nPersonal Tasks:")
    personal_tasks.list_tasks()

    # Update the name of a task list
    print("\nUpdating name of Personal Tasks:")
    personal_tasks.name = "Updated Personal Tasks"
    print(f"Updated Task List Name: {personal_tasks}")

    # Try to update the description of a task to an empty string
    print("\nUpdating description to an empty string:")
    personal_tasks.get_task(1).description = ""
    print(personal_tasks.get_task(1))


if __name__ == "__main__":
    main()
