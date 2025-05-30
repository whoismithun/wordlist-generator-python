# Personal Info-Based Wordlist Generator with Leet Support

This is a Python-based script that generates **probable password combinations** based on a user's personal information, such as name, age, pet name, date of birth, and favorite color. It also includes **leet speak** variations to enhance password coverage — useful for cybersecurity awareness, penetration testing, and ethical hacking training.

---

## Features

- Accepts user input for common personal details
- Generates permutations of input data to create password candidates
- Automatically applies **leet transformations** (e.g., `a` → `@`, `e` → `3`, `s` → `$`, etc.)
- Saves all generated passwords to a text file
- Human-readable and beginner-friendly script

---

## Requirements

- Python 3.x  
(No external libraries are needed — uses only built-in modules.)

---

## How to Use

1. **Clone the repository or download the script**:

    ```bash
    git clone https://github.com/your-username/wordlist-generator.git
    cd wordlist-generator
    ```

2. **Run the script**:

    ```bash
    python wordlist_gen.py
    ```

3. **Enter the personal information** as prompted:
    - Name
    - Age (optional)
    - Pet’s name (optional)
    - Date of birth or birth year
    - Favorite color (optional)
    - Name of the file to store the passwords in 

4. **View results**:
    - All generated password variants will be displayed on the screen.
    - A file with the name you entered will be created in the same directory, containing the full wordlist.

---

## Output

- A file with the name you previously entered is created and contains all generated passwords, one per line.

---

## Author

[Mithun Kailash]
