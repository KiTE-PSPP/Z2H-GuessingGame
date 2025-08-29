# ZERO2HERO (Z2H) - Induction Program

![ZERO2HERO](https://placehold.co/1200x400/2d3748/ffffff?text=ZERO2HERO&font=inter)

Welcome, future tech wizards, to the **ZERO2HERO (Z2H) induction program**! 🚀  

This program is designed to take you from the very basics of programming to a point where you can confidently build simple applications.  
We'll be doing this by creating a classic **Number Guessing Game** in an iterative manner.  
Each module will add a new layer of complexity and introduce you to fundamental programming concepts in **Python**.  

---

## Module 1: Getting Started with Python

This module covers the absolute basics. We will learn how to display text on the screen, which is the first step in any programming language.

### 📌 Sub-module 1.1: Your First Words (`m1_1.py`)
Use the `print()` function to display a welcome message for our game.

**Expected Output:**
```
Welcome to Guessing game
```

### 📌 Sub-module 1.2: Simulating the Game (`m1_2.py`)
Lay out the entire flow of our game using just `print()` statements.  
It won’t be interactive yet, but it helps us visualize the game's structure from start to finish.

**Expected Output:**
```
G U E S S I N G    G A M E
--------------------------
Please think of a number (between 3 and 3)
Is it 3?
Number 3 guessed in 1 tries!
Thank you for playing!
```

---

## Module 2: Interacting with the User

This module is all about getting input from the user and using it in our program.

### 📌 Sub-module 2.1: Taking User Input (`m2_1.py`)
Use `input()` to ask the user for information and display it back.

**Expected Output (user enters 7):**
```
Enter the number you guess:7
You guessed 7
```

### 📌 Sub-module 2.2: Pausing the Game (`m2_2.py`)
Pause the program using `input()` and get user responses.

**Expected Output (user presses Enter, then types yes):**
```
G U E S S I N G    G A M E
--------------------------
Please think of a number (between 3 and 3) 
Press enter when you are ready!...
Is it 3? yes
Number 3 guessed in 1 tries!
Thank you for playing!
```

---

## Module 3: Making Decisions with Conditions

Programs need to make decisions. In this module, you'll learn **if-else** statements.

### 📌 Sub-module 3.1: if-else Statements (`m3_1.py`)
Check if a number is smaller or greater than 5.

**Expected Output (if user enters 3):**
```
Enter a number:3
The number is smaller than 5
```

**Expected Output (if user enters 8):**
```
Enter a number:8
The number is greater than 5
```

### 📌 Sub-module 3.2: Introduction to Lists (`m3_2.py`)
Learn how to store multiple items in a list and access them by index.

**Expected Output:**
```
The 3rd element is 30
```

### 📌 Sub-module 3.3: Conditional Logic in the Game (`m3_3.py`)
Add if-else to the game for user responses.

**Expected Output (if user enters yes):**
```
G U E S S I N G    G A M E
--------------------------
Please think of a number (between 3 and 3) 
Press enter when you are ready!...
Is it 3? yes
Number in 1 tries!
Thank you for playing!
```

**Expected Output (if user enters no):**
```
G U E S S I N G    G A M E
--------------------------
Please think of a number (between 3 and 3) 
Press enter when you are ready!...
Is it 3? no
I don't understand that!
Thank you for playing!
```

---

## Module 4: Handling Multiple Guesses

What if the computer's first guess is wrong? This module introduces **nested if-else**.

### 📌 Sub-module 4.1: Nested if-else (`m4_1.py`)
Make multiple guesses by nesting conditions.

**Expected Output (if user answers no then yes):**
```
G U E S S I N G    G A M E
--------------------------
Please think of a number (between 1 and 5) 
Press enter when you are ready!...
Is it 1? no
I don't understand that!
Is it 3? yes
Number 3 guessed in 2 tries!
Thank you for playing!
```

---

## Module 5: Using Loops for Repetitive Guessing

Why write the same code over and over? Loops help us repeat code efficiently.

### 📌 Sub-module 5.1: The while Loop (`m5_1.py`)
Keep running code while a condition is true.

**Expected Output:**
```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
```

### 📌 Sub-module 5.2: Breaking the Loop (`m5_2.py`)
Stop a loop early using `break`.

**Expected Output (example session):**
```
Enter a positive number: 10
The number is positive
Enter a positive number: -5
The number is negative
Enter a positive number: 0
Program stopped
```

### 📌 Sub-module 5.3: A Looping Guessing Game (`m5_3.py`)
Use a `while` loop to keep guessing until the number is found.

**Expected Output (if user’s number is 3):**
```
G U E S S I N G    G A M E
--------------------------
Please think of a number (between 1 and 5) 
Press enter when you are ready!...
Is it 1 ?
Is it correct? (Higher/H, Lower/L or yes) H
Is it 2 ?
Is it correct? (H, L or yes) H
Is it 3 ?
Is it correct? (H, L or yes) yes
Number of tries: 3
```

---

## Module 6: Putting It All Together - The Final Game

We’ll now use **functions** and a **smarter guessing strategy**.

### 📌 Sub-module 6.1: Introduction to Functions (`m6_2.py`)
Reusable blocks of code make programs more organized.

**Expected Output (user enters 5 and 10):**
```
Enter Number 1: 5
Enter Number 2: 10
The sum is 15
```

### 📌 Sub-module 6.2: The Final Game - A Smarter Way to Guess (`m6_1.py`)
Use **binary search** for efficient guessing.

**Expected Output (if user’s number is 76):**
```
G U E S S I N G    G A M E
--------------------------
Please think of a number (between 1 and 100) 
Press enter when you are ready!...
Is it 50? (Higher/H, Lower/L or yes) H
Is it 75? (Higher/H, Lower/L or yes) H
Is it 88? (Higher/H, Lower/L or yes) L
Is it 81? (Higher/H, Lower/L or yes) L
Is it 78? (Higher/H, Lower/L or yes) L
Is it 76? (Higher/H, Lower/L or yes) yes
Number of tries: 6
```

### 📌 Sub-module 6.3: Modularizing with Functions (`m6_3.py`)
Break down complex problems into smaller functions.

**Expected Output (if user’s number is 7):**
```
G U E S S I N G    G A M E
--------------------------
Please think of a number (between 1 and 100) 
Press enter when you are ready!...
Is it 1 ?
Is it correct? (Higher/H, Lower/L or yes) h
Is it 6 ?
Is it correct? (H, L or yes) h
Is it 8 ?
Is it correct? (H, L or yes) l
Is it 7 ?
Is it correct? (H, L or yes) yes
Number of tries: 4
Thank you for playing!
```

---
