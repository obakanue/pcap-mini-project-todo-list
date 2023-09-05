import task_list


class TaskProgram():
    """
    A program to manage a to-do list.

    This class represents a program that allows users to manage
    their to-do list by displaying tasks, adding tasks, marking
    tasks as complete, and exiting the program.

    Attributes:
        MAIN_MENU_LIST (list): A list of main menu options.
        EXCEPTION_EXIT_STR (str): A message to display when
                                  instructing users to exit the
                                  program gracefully.

    Methods:
        __init__(self): Initializes the TaskProgram object.
        start_program(self): Starts the main program loop.
        __print_main_menu(self): Prints the main menu options.
        __handle_user_selection(self): Handles user menu selections.
        __show_tasks(self): Displays the list of tasks.
        __add_task(self): Adds a new task to the list.
        __complete_task(self): Marks a task as completed.
        __exit_program(self): Exits the program gracefully.
    """
    MAIN_MENU_LIST = [
        '[' + str(idx + 1) + '] ' + menu_item
        for idx, menu_item in enumerate([
           'show tasks',
           'add task',
           'complete task',
           'exit'
        ])
    ]
    EXCEPTION_EXIT_STR = ('Please select \'exit\' in the menu if you wish '
                          'to exit the program.')

    def __init__(self):
        """
        Initializes a new TaskProgram object.

        This constructor sets up the TaskProgram by initializing the
        task list and menu actions.
        """
        self.__task_list = task_list.TaskList()
        self.__menu_actions = {
            str(idx + 1): action for idx, action in enumerate([
                self.__show_tasks,
                self.__add_task,
                self.__complete_task,
                self.__exit_program
            ])
        }

    def start_program(self):
        """
        Starts the main program loop.

        This method initiates the main program loop, displaying the
        main menu, handling user selections, and continuing or
        exiting the program based on user input.

        Returns:
            bool: True to continue running the program, False to
                  exit.
        """
        run_program = True
        while run_program:
            self.__print_main_menu()
            run_program = self.__handle_user_selection()

    def __print_main_menu(self):
        """
        Prints the main menu options.

        This private method prints the main menu options available
        to the user.
        """
        print('== TODO LIST ==')
        for menu_item in TaskProgram.MAIN_MENU_LIST:
            print(menu_item)

    def __handle_user_selection(self):
        """
        Handles user menu selections.

        This private method takes user input, processes it based on
        the available menu actions, and executes the corresponding
        action or displays an error message.

        Returns:
            bool: True to continue running the program, False to
                  exit.
        """
        run_program = True
        while True:
            try:
                user_input = input('Your selection: ')
                print('\n')
                if user_input in self.__menu_actions:
                    run_program = self.__menu_actions[user_input]()
                    break
                else:
                    print(
                        'Invalid selection. Please choose a valid option.',
                        self.__menu_actions.keys()
                    )
            except KeyboardInterrupt as e:
                print(
                    'Program interrupted',
                    TaskProgram.EXCEPTION_EXIT_STR,
                    e
                )
            except EOFError as e:
                print(
                    'No more input.',
                    TaskProgram.EXCEPTION_EXIT_STR,
                    e)
            except Exception as e:
                print('An error occurred:', e)
        return run_program

    def __show_tasks(self):
        """
        Displays the list of tasks.

        This private method displays the list of tasks in the task
        list.

        Returns:
            bool: Always returns True to continue the program.
        """
        print(self.__task_list)
        return True

    def __add_task(self):
        """
        Adds a new task to the list.

        This private method prompts the user for task details, adds
        a new task to the task list object, and returns True to
        continue the program.

        Returns:
            bool: Always returns True to continue the program.
        """
        print('[ADD TASK]')
        task_desc_str = input('Describe your task: ')
        task_deadline_str = input('Type your deadline: ')
        self.__task_list.add_task(task_desc_str, task_deadline_str)
        return True

    def __complete_task(self):
        """
        Marks a task as completed.

        This private method displays the list of tasks, prompts the
        user to enter the ID of a completed task, and marks that
        task as completed in the task list (removes task from todo).

        Returns:
            bool: Always returns True to continue the program.
        """
        print("[COMPLETE TASK]")
        self.__show_tasks()
        task_id_str = input(
            '\n Enter ID of task you have completed: '
        )
        self.__task_list.remove_task(task_id_str)
        return True

    def __exit_program(self):
        """
        Exits the program.

        This private method displays an exit message and returns
        False to exit the program.

        Returns:
            bool: Always returns False to exit the program.
        """
        print("Exiting program...")
        return False
