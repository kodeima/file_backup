import os

def copy_file():
    """copy the contents of a file into another"""

    source_file = input('Enter the source file name: ')
    destination_file = input('Enter the destination file name: ')

    try:
        # Check if the source file exists
        if not os.path.exists(source_file):
            print('Source file does not exist.')
            return
        
        # Prevent overwriting the destination file if it already exists
        if os.path.exists(destination_file):
            print('Error: The destination file already exists. Please choose a different name.')
            return
        
        # Read from the source file
        with open(source_file, 'r') as source:
            content = source.read()

        # Write to the destination file
        with open(destination_file, 'w') as destination:
            destination.write(content)

        print('\nFile copied successfully!')
        print(f'Backup of "{source_file}" created as "{destination_file}".')

    except PermissionError:
        print('Permission denied. Please check your file permissions.')

    except IOError as error:
        print(f'An I/O error occurred: {error}')

    except Exception as error:
        print(f'An unexpected error occurred: {error}')

def main():
    print('=== File Backup Program ===')
    copy_file()

if __name__ == '__main__':
    main()
