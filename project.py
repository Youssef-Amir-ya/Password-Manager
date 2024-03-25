from termcolor import colored
import csv
import pyperclip
import random
import string
import sys
import time


def main():
    authentication()
    main_menu()


def authentication():
    with open("program password.txt", "r") as file:
        lines = file.readline()
    if not lines:
        print("Set a first-time password for the password manager: ")
        while True:
            set_password = input().strip()
            if set_password == " " or len(set_password) < 5:
                print(
                    colored(
                        "Password is too short. Must be more than 5 characters", "red"
                    )
                )
            else:
                with open("program password.txt", "w") as file:
                    file.writelines(set_password)
                    break
    else:
        while True:
            login = input("Password: ").strip()
            with open("program password.txt", "r") as file:
                lines = file.readline()
                if lines == login:
                    return True
                elif lines != login:
                    print(colored("Wrong password, try again", "red"))


def main_menu():
    print(
        "Main Menu:\n-----------\n1) Passwords list.\n2) Add a password\n3) Edit an existing password\n4) Generate a password.\n5) Search passwords by linked account/keyword.\n6) Exit"
    )
    while True:
        user_input = input().strip()
        if user_input.isnumeric() == False or 0 <= int(user_input) > 6:
            print(colored("Please pick a number between 1 and 6", "yellow"))
        else:
            break
    if user_input == "1":
        list_saved_passwords()
    elif user_input == "2":
        add_password()
    elif user_input == "3":
        edit_password()
    elif user_input == "4":
        generate()
    elif user_input == "5":
        search()
    elif user_input == "6":
        sys.exit(0)


def list_saved_passwords():
    with open("saved passwords.csv", "r") as file:
        reader = file.readlines()
        print("")
        if reader:
            for row in reader:
                try:
                    password, is_linked_to = row.split(",")
                    print(f"{password}➡️ {is_linked_to}", end="")
                except ValueError:
                    pass
        else:
            print(colored("No saved passwords yet!", "yellow"))
        while True:
            out_of_listing = input("1) Main Menu\n2) Exit\n")
            if out_of_listing == "1":
                main_menu()
            elif out_of_listing == "2":
                sys.exit()


def add_password():
    print(
        "\nPlease enter a the password and it's related page/app/website/service etc..., separated with a comma only."
    )
    while True:
        try:
            added_password = input().strip()
            new_password, linked_to = added_password.split(",")
            break
        except ValueError:
            print(
                colored(
                    "Invalid input: Please enter password and linked information separated by a comma only.",
                    "red",
                )
            )

    with open("saved passwords.csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            try:
                saved_password, _ = line.split(",")
                if new_password == saved_password:
                    print(
                        colored(
                            "WARNING: Password repeated, check your listed passwords.",
                            "red",
                        )
                    )
                    time.sleep(0.5)
                    break
            except (ValueError, UnboundLocalError):
                pass
            else:
                pass
        print(
            colored("Password and linked information are saved successfully.", "green")
        )
        special_char = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")")
        if any(char in special_char for char in new_password) and len(new_password) > 7:
            print(colored("\nNOTE: Your password is strong", "light_green"))
        elif 8 <= len(new_password) <= 16:
            print(
                colored(
                    "\nNOTE: Your password is fair, consider adding a special character.",
                    "yellow",
                )
            )
        else:
            print(
                f"{colored('\nNOTE: Your password is weak, consider make it longer and contain special character.', 'red')} {colored('\nYou can also use password generator.', 'blue')}"
            )
    with open("saved passwords.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([new_password, linked_to])
    out_of_adding = input("1) Main Menu\n2) Generate Password\n3) Exit\n").strip()
    if out_of_adding == "1":
        main_menu()
    elif out_of_adding == "2":
        generate()
    if out_of_adding == "3":
        sys.exit()


def edit_password():
    while True:
        user_keyword_to_edit_password = input(
            "Enter linked account or keyword to edit it's password.\n"
        ).strip()
        if not user_keyword_to_edit_password:
            pass
        else:
            break
    found = False
    with open("saved passwords.csv", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            try:
                old_password, current_keyword = line.split(",")
            except ValueError:
                pass
            if user_keyword_to_edit_password.strip() == current_keyword.strip():
                found = True
                print(f"Old password is {old_password}")
                new_enterd_password = input("Enter new password: ")
                lines[i] = f"{new_enterd_password},{current_keyword}"
                with open("saved passwords.csv", "w") as file2:
                    file2.writelines(lines)
                    break
    if found:
        print(colored("\nPassword updated successfully!\n", "green"))
        main_menu()
    else:
        exit_or_not = input("\nNo matching keywords. Exit? [Yes/No]").strip().lower()
        if exit_or_not == "yes":
            sys.exit()
        else:
            edit_password()


def generate():
    char = string.ascii_letters + string.digits + string.punctuation + "!@#$%^&*()"
    print(
        "To ensure your password's strength, please select a desired password length. Remember, longer passwords are generally more secure."
    )
    while True:
        length = input().strip()
        try:
            generated_password = "".join(
                random.choice(char) for _ in range(int(length))
            )
            break
        except ValueError:
            print("Please select a number\n")

    print(generated_password)
    copy_or_not = input("Copy to clipboard?[Yes/No] ").lower()

    if copy_or_not == "yes":
        pyperclip.copy(generated_password)
        print("\nCopied to clipboard!\n")
    elif copy_or_not == "no":
        main_menu()


def search():
    found_match = False
    user_keyword = input("Keyword: ")
    with open("saved passwords.csv", "r") as file:
        reader = file.readlines()
        print()
        for row in reader:
            try:
                the_password, searching_keyword = row.split(",")
                if user_keyword == searching_keyword.strip():
                    found_match = True
                    print(colored(f"A Matching password: {the_password}", "green"))
            except ValueError:
                pass
    print()
    if not found_match:
        print(colored("No matching passwords with entered keyword!\n", "yellow"))
        main_menu()

    out_of_searching = input("1) Main Menu\n2) Exit\n")
    if out_of_searching == "1":
        main_menu()
    elif out_of_searching == "2":
        sys.exit()


if __name__ == "__main__":
    main()
