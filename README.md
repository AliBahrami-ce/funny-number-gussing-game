# 🎯 Funny Number Guessing Game  
A simple (and sarcastic 😄) Python CLI game where you try to guess a number between **0 and 10** — while the program roasts you for every mistake!

---

## 📌 Features
- 🎲 Random number generation (0–10)  
- 😂 Funny roast messages for wrong inputs  
- 🧠 Handles invalid numeric input gracefully  
- 🧹 Clears screen based on OS  
- 🔁 Menu system with retry logic  

---

## 📦 Requirements
This project has **no external libraries**.  
You only need:

- **Python 3.8 or higher**
- A terminal/command prompt to run the script
- OS: Windows, Linux, or macOS

All modules used (`random`, `os`) are built into Python.

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/AliBahrami-ce/funny-number-gussing-game.git
```

### 2. Navigate into the folder
```bash
cd funny-number-gussing-game
```

### 3. Run the game
```bash
python number_guessing.py
```

---

## 🕹️ How the Game Works

1. The program picks a random number between 0 and 10.

2. You enter your guess.

3. If you're wrong → the program roasts you 😄

4. If you enter something invalid → you get roasted harder 😂

5. If you're right → congratulations, you win!

---

## 💻 Code Highlights
### 🔹 Clear screen depending on OS
```python
def clear_screan():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
```

### 🔹 Input validation with funny messages
```python
try:
    your_number = int(input("What's your guess?(number between 0 and 10) "))
except ValueError:
    print("--> You broke math. Congrats...")
```

### 🔹 Guess comparison
```python
if your_number == random_number:
    print("Finally! Don't spend all your luck at once :)")
else:
    print(f"You worked so hard to be wrong… I admire your consistency. (number : {random_number})")
```

---

## 🤝 Contributing

Contributions, improvements, and funnier roast ideas are welcome!
Feel free to open issues or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Ali Bahrami**
GitHub: https://github.com/AliBahrami-ce
