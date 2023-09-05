class Task():
    """
    A class representing a task with an ID, description, and
    deadline.

    Attributes:
        BOUNDARY_STR (str): The boundary string used to format task
                            information.

    Args:
        task_id (str): The unique identifier for the task.
        task_desc_str (str): The description of the task.
        task_deadline_str (str): The deadline of the task.

    """

    BOUNDARY_STR = ' | '

    def __init__(self, task_id, task_desc_str, task_deadline_str):
        """
        Initialize a new Task object.

        Args:
            task_id (str): The unique identifier for the task.
            task_desc_str (str): The description of the task.
            task_deadline_str (str): The deadline of the task.

        """
        self.__task_id = task_id
        self.__task_desc_str = task_desc_str
        self.__task_deadline_str = task_deadline_str

    def __str__(self):
        """
        Return a formatted string representation of the task.

        Returns:
            str: A formatted string representing the task.

        """
        return (self.__task_id +
                Task.BOUNDARY_STR +
                self.__task_desc_str +
                Task.BOUNDARY_STR +
                self.__task_deadline_str)

    def get_task_id(self):
        """
        Get the unique identifier of the task.

        Returns:
            str: The task's unique identifier.

        """
        return self.__task_id
