import project
import pytest
from unittest.mock import patch, mock_open


def test_first_time_authentication(capsys):
    with patch("builtins.open", mock_open(read_data="")), patch(
        "builtins.input", side_effect=["password"]
    ):
        project.authentication()
        captured = capsys.readouterr()
        expected_output = "Set a first-time password for the password manager: "
        assert expected_output in captured.out


def test_short_password_authentication(capsys):
    with patch("builtins.open", mock_open(read_data="")), patch(
        "builtins.input", side_effect=["1234", "password"]
    ):
        project.authentication()
        captured = capsys.readouterr()
        expected_output = "Password is too short. Must be more than 5 characters"
        assert expected_output in captured.out


def test_correct_authentication(capsys):
    with patch("builtins.open", mock_open(read_data="correct_password")), patch(
        "builtins.input", side_effect=["correct_password"]
    ):
        assert project.authentication() == True


def test_incorrect_authentication(capsys):
    with patch("builtins.open", mock_open(read_data="correct_password")), patch(
        "builtins.input", side_effect=["incorrect_password", "correct_password"]
    ):
        project.authentication()
        captured = capsys.readouterr()
        expected_output = "Wrong password, try again"
        assert expected_output in captured.out


def test_main_menu_option(capsys):
    with patch("builtins.input", side_effect=["6"]), pytest.raises(
        SystemExit
    ) as excinfo:
        project.main_menu()
        assert excinfo.code.value == 0
    captured = capsys.readouterr()
    expected_output = "Main Menu:\n-----------\n1) Passwords list.\n2) Add a password\n3) Edit an existing password\n4) Generate a password.\n5) Search passwords by linked account/keyword.\n6) Exit"
    assert expected_output in captured.out


def test_main_menu_non_numric_input(capsys):
    with patch("builtins.input", side_effect=["abc", "6"]), pytest.raises(
        SystemExit
    ) as excinfo:
        project.main_menu()
        assert excinfo.code.value == 0
    captured = capsys.readouterr()
    expected_output = "Please pick a number between 1 and 6"
    assert expected_output in captured.out


def test_main_menu_out_of_range_input(capsys):
    with patch("builtins.input", side_effect=["8", "6"]), pytest.raises(
        SystemExit
    ) as excinfo:
        project.main_menu()
        assert excinfo.code.value == 0
    captured = capsys.readouterr()
    expected_output = "Please pick a number between 1 and 6"
    assert expected_output in captured.out


def test_list_saved_passwords_while_empty(capsys):
    with patch("builtins.open", mock_open(read_data="")), patch(
        "builtins.input", side_effect=["2"]
    ), pytest.raises(SystemExit) as excinfo:
        project.list_saved_passwords()
        assert excinfo.code.value == 0
    captured = capsys.readouterr()
    expected_output = "No saved passwords yet!"
    assert expected_output in captured.out


def test_list_saved_password_while_not_empty(capsys):
    with patch("builtins.open", mock_open(read_data="first,account")), patch(
        "builtins.input", side_effect=["2"]
    ), pytest.raises(SystemExit) as excinfo:
        project.list_saved_passwords()
        assert excinfo.code.value == 0
    captured = capsys.readouterr()
    expected_output = "first➡️ account"
    assert expected_output in captured.out
