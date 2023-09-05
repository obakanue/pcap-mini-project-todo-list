import task_program
import sys


def main():
    """
    Main entry point of the program.

    This function creates an instance of the TaskProgram class and
    starts the program.

    """
    tp = task_program.TaskProgram()
    tp.start_program()


if __name__ == '__main__':
    main()
