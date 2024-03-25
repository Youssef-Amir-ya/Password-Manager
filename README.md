# Password Manager

#### Video Demo: <https://youtu.be/O-mrNd2DxEI>

#### Description:
The Password Manager is a command-line application designed to securely manage passwords for various accounts, services, and websites. It provides essential functionalities such as password authentication, password addition, editing, generation, and searching. The application ensures the security of stored passwords while offering user-friendly interactions for efficient password management.

Features:
Authentication: The Password Manager prompts users to set a master password for accessing the application, ensuring security and privacy.
Main Menu Navigation: Users can navigate through a main menu offering options to list saved passwords, add a new password, edit existing passwords, generate strong passwords, search for passwords, and exit the application.
Password Storage: Passwords are stored securely in a CSV file, maintaining organization and accessibility for users.
Password Addition and Editing: Users can add new passwords along with linked account information and edit existing passwords as needed.
Password Generation: The Password Manager offers a built-in password generator to create strong and randomized passwords based on user preferences.
Search Functionality: Users can search for passwords based on linked account information or keywords, facilitating quick access to specific passwords.
Design Choices:
File Storage: Passwords are stored in a CSV file format to ensure encryption and separation from the source code, enhancing security and organization.
Error Handling: The application incorporates robust error handling to manage unexpected inputs or errors, providing informative messages to guide users through the application.
Dependencies:
This project relies on the following Python packages:

termcolor: For colored text output in the command-line interface.
pyperclip: For copying generated passwords to the clipboard.
Usage:
To use the Password Manager:

Run the main.py script.
Follow the prompts to authenticate and navigate the main menu for password management tasks.
Utilize options such as adding passwords, editing existing passwords, generating strong passwords, searching for passwords, and more.
Compatibility:
The Password Manager is compatible with Python 3.x and can be run on various operating systems supporting Python.
TODO
This project relies on the following python packages:
- `termcolor`
- `pyperclip`
