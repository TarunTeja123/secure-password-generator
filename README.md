# Secure Password Generator 🔒

A command-line tool built with Python to generate cryptographically secure passwords and evaluate their strength. It guarantees that every password meets modern complexity requirements for maximum security.

---
### ⚙️ Key Features
---

* **Cryptographically Secure :** Uses Python's built-in **`secrets`** module for generation, ensuring the randomness is suitable for security and cryptography.
* **Guaranteed Complexity :** Every password is guaranteed to contain at least one uppercase letter, one lowercase letter, one digit, and one symbol.
* **Built-in Strength Checker :** Rates generated passwords as **Strong**, **Medium**, or **Weak** based on length and character diversity.
* **User-Friendly Interface :** Simple command-line input for setting the number of passwords and the required length.

---
### 🚀 Getting Started
---

### Prerequisites

You only need **Python 3.x** installed on your system. No external libraries are required.

### Installation & Usage

1.  **Clone the repository :**
    ```bash
    git clone https://github.com/TarunTeja123/secure-password-generator.git
    cd secure-password-generator
    ```

2.  **Run the script :**
    ```bash
    python password_generator.py
    ```

3.  **Follow the prompts** to enter the desired number of passwords and the required length.

### Example Output
```bash
How Many Passwords You Want To Generate : 5
Enter The Password Length : 16

Generated Passwords : 5
----------------------------------------
j!J6BfD.u4iS/cRj ===> Strong 💪
H>n{oF-q2zE/kP9Q ===> Strong 💪
:W5o^q_gX%a9v.M/ ===> Strong 💪
m2e(K1t,L#;{sZ_U ===> Strong 💪
7<T)g0!Y]O'8[vNf ===> Strong 💪
----------------------------------------
```
---
### 🛡️ Strength Rating Criteria
---

The built-in `password_strength` function rates passwords based on both **length** and **character count (uppercase, lowercase, digit, symbol)**:

* **Strong 💪 :** Length $\ge 12$ AND all 4 character types present.
* **Medium 👍 :** Length $\ge 8$ AND at least 3 character types present.
* **Weak ⚠️ :** Anything else.

---
### 💡 Future Plans
---

* Implement a full Graphical User Interface (GUI) using Streamlit.
* Add an option to automatically copy the generated password to the clipboard.

---
### 📜 License
---

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
