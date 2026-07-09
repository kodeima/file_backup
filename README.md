# File Backup Tool

## Program Overview

The Simple File Backup Tool is a Python console application that copies the contents of one file into another. It prompts the user for the source file and the destination file, then creates a backup by copying the contents from the source to the destination.

---

## Features

- Prompts the user for a source file name.
- Prompts the user for a destination file name.
- Copies the contents of the source file to the destination file.
- Checks whether the source file exists before attempting to read it.
- Prevents accidental overwriting by checking if the destination file already exists.
- Handles permission and file input/output errors gracefully.
- Displays clear success and error messages.
- Uses functions to keep the code organized and easy to maintain.

---

## What the Program Does

When the program is executed, it performs the following steps:

1. Asks the user to enter the name of the source file.
2. Asks the user to enter the name of the destination file.
3. Verifies that the source file exists.
4. Checks whether the destination file already exists to prevent overwriting.
5. Reads the contents of the source file.
6. Creates a new destination file and writes the copied content into it.
7. Displays a success message if the backup is created successfully.
8. If an error occurs, the program catches the exception and displays an informative error message.

---

## Libraries Used

- The built-in `os` module.
- Python's built-in `open()` function.

---

## How to Run

1. Ensure Python 3 is installed on your computer.
2. Save the script as `file_backup.py`.
3. Create a text file within the selected folder.
4. Open a terminal or command prompt in the project folder.
5. Run the program using:

```bash
python file_backup.py
```

6. Enter the source file name when prompted.
7. Enter a new destination file name for the backup.

---

## Error Handling

The program handles several common file-related errors, including:

- Source file does not exist.
- Destination file already exists.
- Permission denied when accessing a file.
- General input/output (I/O) errors.
- Unexpected exceptions.

These checks make the application more reliable when working with files.

---

## Usage

```text
=== File Backup Program ===
Enter the source file name: notes.txt
Enter the destination file name: backup_notes.txt

File copied successfully!
Backup of "notes.txt" created as "backup_notes.txt".
```
