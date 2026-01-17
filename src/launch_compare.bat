@echo off
:: Change directory to where the .bat file is located... The .bat folder is in /src so you don't need this but I kept it as a note
:: cd /d "%~dp0src"

:: Run the scripts from inside src
:: start cmd /k python main.py
:: start cmd /k python mainv2.py
start python rps.py
start python main.py
start python mainv2.py

:: Pause main launcher window
echo All versions launched. 
echo Original version is rps.py (slightly modified for new location of folder for assets)
echo Second version is main.py which attempted to increase readability through separation of logic and UI
echo Third version is mainv2.py which attempted to reduce code through more separation and adding methods to create UI buttons, text, labels, and frames with less lines of code
echo Project results show that for a small project handling things in a single file is probably better and easier to read than using lots of files
echo Using multiple files increased amount of lines of code, debugging, and complexity unnecessarily even though it was intended to increase efficiency and readability.
echo This shows making libraries and multiple files for projects is only best done when there are more than 3 uses of the methods in the file. 
echo Over complicating a project's architecture can increase workload and reduce efficiency for projects but if readability is more important it might be worth doing.
echo A general guideline is to not change the architecture of the project outside of a single file if it doesn't get used more than 3 times.
echo Press any key to close this launcher...
pause