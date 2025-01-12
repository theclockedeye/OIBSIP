# Advanced Random Password Generator

This project is an **Advanced Random Password Generator** built using Python and Tkinter for the graphical user interface (GUI). The password generator allows users to specify their password requirements, such as length and character types (letters, digits, symbols). It also ensures that the generated passwords meet security rules and provides an easy way to copy the generated password to the clipboard.

## Features

- **Password Length**: Users can define the desired length of the password.
- **Character Types**: Users can select whether to include:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Symbols
- **Security Rules**: The password generator ensures that the password is secure based on selected character types.
- **Clipboard Integration**: After generating a password, users can easily copy it to the clipboard for quick use.
- **Intuitive GUI**: The app features a user-friendly graphical interface built with Tkinter.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/random-password-generator.git
    cd random-password-generator
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    *Note: You may need to install `pyperclip` for clipboard functionality. You can install it manually by running:*

    ```bash
    pip install pyperclip
    ```

3. Run the application:

    ```bash
    python main.py
    ```

## Usage

1. **Enter the password length** in the provided input field.
2. **Select the character types** (uppercase, lowercase, digits, symbols) you want to include in the password.
3. Click **Generate Password** to create a random password based on your specifications.
4. The generated password will appear in the result area.
5. To copy the password to the clipboard, click the **Copy to Clipboard** button.

## Example

1. Enter length as `12`.
2. Select **Include Uppercase**, **Include Digits**, and **Include Symbols**.
3. Click **Generate Password**.
4. A password like `T7@w3S1bLz0A` will be generated.

## Project Structure

random-password-generator/ │ ├── main.py # Main entry point to run the app ├── ui/ │ ├── gui.py # Tkinter GUI interface │ ├── utils/ │ ├── password_generator.py # Password generation logic and clipboard functionality │ ├── data/ │ ├── password_rules.py # Password length validation │ ├── requirements.txt # Dependencies └── README.md # Project documentation


## Dependencies

- `tkinter`: For creating the graphical user interface.
- `pyperclip`: For clipboard functionality to copy the password.
- `string`: For handling character sets (letters, digits, symbols).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Tkinter documentation for creating the GUI.
- pyperclip library for clipboard functionality.


