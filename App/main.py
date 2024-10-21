import logging
from typing import List, Optional
from .api import ApiClass
from tabulate import tabulate

from .models import User, Post


def create_logger(name: Optional[str] = None) -> logging.Logger:
    """Creates and configures a logger instance.

    Args:
        name (Optional[str]): Name of the logger. If None, the root logger is used.

    Returns:
        logging.Logger: Configured logger instance.
    """

    log_obj = logging.getLogger(name)
    log_obj.setLevel(logging.INFO)

    if not log_obj.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(formatter)
        log_obj.addHandler(console_handler)

    return log_obj


class MainApp(object):
    """ Class for main execution of the application """

    def __init__(self, log_obj: logging.Logger) -> None:
        """ Constructor to load all required objects for the class """

        self.log = log_obj
        self.api_obj = ApiClass(self.log)

    def print_user_data(self) -> None:
        """ Print User data from /users api

        :return: None
        """

        user_data: List[User] = self.api_obj.get_users()
        table_data = []
        for user in user_data:
            table_data.append([user.id, user.name, user.username, user.email, user.phone])
        headers = ["ID", "Name", "Username", "Email", "Phone"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def print_posts_data(self) -> None:
        """ Print User data from /posts api

        :return: None
        """

        posts: List[Post] = self.api_obj.get_posts()
        table_data = []
        for post in posts:
            table_data.append([post.id, post.userId, post.title])

        headers = ["ID", "User ID", "Title"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    @staticmethod
    def exit_app() -> None:
        """ Exists the application

        :return: None
        """

        print("Application exit option chosen.\nThanks you!!!")

    def main_process(self) -> None:
        """ Main method to control flow of app execution

        :return: None
        """

        user_choice: int = 0
        func_map = {
            1: self.print_user_data,
            2: self.print_posts_data,
            3: self.exit_app
        }
        while user_choice != 3:
            try:
                user_choice = int(input("""Please select the following options to get data from the APIs :
                        1. Press 1 for getting all the user data
                        2. Press 2 for getting all the posts from the APIs
                        3. To exit the Application\n"""))
            except ValueError:
                self.log.error("Obtained Error in User choice please choose a valid choice")
            if user_choice not in func_map:
                self.log.warning("The user choice is not valid, please choose a valid option!")
            else:
                func_map[user_choice]()
        self.log.info("Application Terminated!")


if __name__ == "__main__":  # calling main process
    logger = create_logger('AppLogger')
    main_obj = MainApp(logger)
    main_obj.main_process()
