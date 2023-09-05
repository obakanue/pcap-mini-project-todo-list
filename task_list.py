import task
import random


class TaskList():
    """
    A class representing a list of tasks.

    Attributes:
        ALPHA_NUMERICAL_LIST (list): A list of alphanumeric
        characters used for generating task IDs.
        FILE_NAME (str): The name of the file where tasks are
                         stored.
        TASK_ATTR_DIV (str): The divider used to separate task
                             attributes in the file.

    Methods:
        __init__(self, path=''): Initialize a new TaskList instance.
        __str__(self): Return a string representation of the
                       TaskList.
        add_task(self, task_desc_str, task_deadline_str):
            Add a new task to the TaskList.
        remove_task(self, task_id_remove_str): Remove a task from
                                               the TaskList.
        __generate_task_id(self): Generate a unique task ID.
        __generate_random_str(self, count, hyphen=True):
            Generate a random alphanumeric string.
        __load_saved_tasks(self): Load tasks from a file into the
                                  TaskList.
    """
    ALPHA_NUMERICAL_LIST = list(
        map(chr,
            [character_ord for character_ord in
             range(ord('a'), ord('z') + 1)])
        ) + [str(number) for number in range(0, 10)]
    FILE_NAME = 'tasks.txt'
    TASK_ATTR_DIV = '¤'

    def __init__(self, path=''):
        """
        Initialize a new TaskList instance.

        Args:
            path (str): Optional. The path to the file where tasks
                        are stored.
        """
        self.__tasks_dict = {}
        self.__file_path = path + TaskList.FILE_NAME
        self.__load_saved_tasks()

    def __str__(self):
        """
        Return a string representation of the TaskList.
        """
        task_list_str = '[YOUR TASKS]\n'
        if len(self.__tasks_dict) == 0:
            task_list_str += 'Empty list\n'
        else:
            for task_obj in self.__tasks_dict.values():
                task_list_str += str(task_obj) + '\n'
        return task_list_str

    def add_task(self, task_desc_str, task_deadline_str):
        """
        Add a new task to the TaskList.

        Args:
            task_desc_str (str): The description of the task.
            task_deadline_str (str): The deadline of the task.
        """
        task_id_str = self.__generate_task_id()
        task_obj = task.Task(
            task_id_str,
            task_desc_str,
            task_deadline_str
        )
        try:
            if TaskList.TASK_ATTR_DIV in [task_desc_str,
                                          task_deadline_str]:
                raise ValueError(
                    'May not use',
                    TaskList.TASK_ATTR_DIV,
                    ('in task description nor task deadline, used '
                     'as a divider in save file')
                )
            stream = open(self.__file_path, 'a+')
            line = TaskList.TASK_ATTR_DIV.join(
                [task_id_str,
                 task_desc_str,
                 task_deadline_str]
            )
            stream.write(line + '\n')
            self.__tasks_dict[task_id_str] = task_obj
        except Exception as e:
            print('An error occurred while adding task (',
                  task_obj,
                  '):',
                  e)

    def remove_task(self, task_id_remove_str):
        """
        Remove a task from the TaskList.

        Args:
            task_id_remove_str (str): The ID of the task to be removed.
        """
        try:
            stream = open(self.__file_path, 'r+')
            lines = []
            for line in stream.readlines():
                task_id_str, _, __ = line.split(TaskList.TASK_ATTR_DIV)
                if not task_id_remove_str == task_id_str:
                    lines.append(line)
            stream.close()
            stream = open(self.__file_path, 'w+')
            stream.writelines(lines)
            stream.close()
            del self.__tasks_dict[task_id_remove_str]
        except Exception as e:
            print('Something went wrong when completing the task:',
                  e)

    def __generate_task_id(self):
        """
        Generate a unique task ID.

        Returns:
            str: The generated task ID.
        """
        while True:
            task_id = ''
            task_id += self.__generate_random_str(8)
            task_id += self.__generate_random_str(4)
            task_id += self.__generate_random_str(4)
            task_id += self.__generate_random_str(12, False)
            if task_id not in self.__tasks_dict.keys():
                break
        return task_id

    def __generate_random_str(self, count, hyphen=True):
        """
        Generate a random alphanumeric string.

        Args:
            count (int): The length of the generated string.
            hyphen (bool): Optional. Whether to include a hyphen at
                           the end of the string.

        Returns:
            str: The generated random string.
        """
        random_str = ''.join(
            random.choice(TaskList.ALPHA_NUMERICAL_LIST)
            for _ in range(count)
        )
        if hyphen:
            random_str += '-'
        return random_str

    def __load_saved_tasks(self):
        """
        Load tasks from a saved file into the TaskList.

        This method reads tasks from a file and populates the TaskList
        with them. Each line in the file is expected to contain task
        attributes separated by '¤', including the task ID, description,
        and deadline.

        Raises:
            Exception: An error occurred while loading tasks, which
                       could be due to a file read error or improperly
                       formatted task entries.
        """
        try:
            stream = open(self.__file_path, 'r+')
            for line in stream.readlines():
                task_attr_list = line.split(TaskList.TASK_ATTR_DIV)
                if len(task_attr_list) == 3:
                    task_id_str, task_description_str, task_deadline_str = \
                        task_attr_list
                    self.__tasks_dict[task_id_str] = task.Task(
                        task_id_str,
                        task_description_str,
                        task_deadline_str
                    )
                else:
                    print('Skipping invalid task entry:', line)
            stream.close()
        except Exception as e:
            print("An error occurred while loading tasks:", e)
