# Rock Paper Scissors Game – CS 1010 Final Project
## 📌 Project Overview
This is a classic **Rock Paper Scissors** game developed for my **CS 1010: Introduction to Higher Programming** course at **California State University, Los Angeles (CSULA)**.  The goal of the project was to practice basic programming logic by creating a functional game where a user can play against the computer. The project demonstrates fundamental programming concepts, including control flow, user input handling, and basic GUI/asset management.

## 🎮 How It Works
- **User Input**: The player selects Rock, Paper, or Scissors.
- **Computer Choice**: The computer randomly selects an option.
- **Logic**: The program uses basic `if/else` statements to determine the winner based on the choices made.
- **Score Tracking**: The game tracks wins and losses and updates the score after each round.
- **Display**: A simple textbox updates to show who won the round and the current score.

## Application Running

### Initial Game State<br/>
<img width="500" height="395" alt="Initial Game State" src="https://github.com/user-attachments/assets/6eaa1d80-929d-4286-934f-6a6975748b48" /><br/>
### Round 1<br/>
<img width="516" height="395" alt="Round 1" src="https://github.com/user-attachments/assets/0fee51ff-5dd4-4b5a-ac1c-8f86bb53406d" /><br/>
### Round 2<br/>
<img width="516" height="395" alt="Round 2" src="https://github.com/user-attachments/assets/762c1955-db23-4bd2-80d5-a04a29f0071e" /><br/>
### Command Prompt - Game History<br/>
<img width="1115" height="154" alt="Game Ends on application close" src="https://github.com/user-attachments/assets/dd1db303-ee9b-4b63-b856-1682ea8c640f" /><br/>

## EasyGP Methods<br/>
### Setup_window<br/>
<img width="1105" height="615" alt="setup_window" src="https://github.com/user-attachments/assets/018466b8-93c8-418f-beb4-a0e6969afbb7" /><br/>
### Add_button<br/>
<img width="744" height="212" alt="add_button" src="https://github.com/user-attachments/assets/1b83f2c9-384e-4cc2-91d4-e03f13755ede" /><br/>
### Add_frame<br/>
<img width="809" height="236" alt="add_frame" src="https://github.com/user-attachments/assets/23f83317-d2c3-4590-98d2-44f491af214b" /><br/>
### Add_label<br/>
<img width="466" height="172" alt="add_label" src="https://github.com/user-attachments/assets/f605ee64-c591-4517-9492-8b90a37201e5" /><br/>
### Add_text<br/>
<img width="606" height="177" alt="add_text" src="https://github.com/user-attachments/assets/f164b0a9-ca26-4281-8d52-1734e9ad59f0" /><br/>
### Add_input<br/>
<img width="219" height="168" alt="add_input and add_button1" src="https://github.com/user-attachments/assets/19a76d9f-4ff1-4756-907a-5f9ed7e25e3c" /><br/>

## 🛠️ Built With
- **Programming Language**: `Python`
- **Libraries/Tools**: `tkinter`, `os`, `random`, 
- **Software**: `Notepad`, `VS Code`, `GitHub`, `Command Prompt`
- **Assets**: Simple image files for Rock, Paper, and Scissors sourced from Google Images. (`rock.png`, `paper.png`, `scissors.png`).

## 📂 File Structure
- `rock.png:`, `paper.png`, `scissor.png`: Visual choices stored in `src/assets`
- `README.md`: Project description and credits
- `rps.py`: Original source code of the core game in a single file (version 0).
- `main.py`: Program's launcher for version 1 separating original source code into `rpswindow.py` and `rpsgame.py`
- `mainv2.py`: Program's launcher for version 2 which implements `easygp.py`
- `rpsgame.py`: Handler for scoring logic and round results for `mainv2.py`
- `rpswindow.py`: Handler for `tkinter` and app UI's layout, colors, buttons, and labels
- `easygp.py`: EasyGridPacker managing UI from tkinter
- `rpswindoweasygp`: UI implementing the EasyGridPacker

## 🚀 How to Run
1. Download or clone the repository:

```Bash
git clone https://github.com/kuyaEJ/Rock-Paper-Scissors-Game.git
```

2. Open the project in your code editor or open a command line. Navigate to the folder:

```Bash
cd "Rock-Paper-Scissors-Game"
```

3. Run the script with the command:
```Python
python src/main.py
```

4. Test and compare the other versions of the application with `launch_compare.bat`


## 🎓 Academic Context
This project was completed as part of the CS 1010 curriculum at CSULA. It emphasizes:
- Using conditional statements for game rules.
- Managing and updating variables (scores).
- Linking simple UI elements (textboxes and images) to the code logic.

## Credits
Final Project (rps.py) submitted from CS 1010 by Group 10: Kyle Chau, Micheal Buna, and Erick Vergara
(New commits are made by Erick)
