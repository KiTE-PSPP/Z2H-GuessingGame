
# ZERO2HERO (Z2H) - Induction Program

![ZERO2HERO Banner](https://placehold.co/1200x400/2d3748/ffffff?text=ZERO2HERO&font=inter)

Welcome, future tech wizards, to the ZERO2HERO (Z2H) induction program!

This program is designed to take you from the very basics of programming to a point where you can confidently build simple applications. We'll be doing this by creating a classic "Number Guessing Game" in an iterative manner. Each module will add a new layer of complexity and introduce you to fundamental programming concepts in Python.

Let's get started on your journey from Zero to Hero!

---

## Module 1: Getting Started with Python

This module covers the absolute basics. We will learn how to display text on the screen, which is the first step in any programming language.

### 📌 Sub-module 1.1: Your First Words (m1_1.py)
This small step is a giant leap for a new programmer! We will use the `print()` function to display a welcome message for our game.

**Expected Output:**
```
Welcome to Guessing game
```

### 📌 Sub-module 1.2: Simulating the Game (m1_2.py)
Here, we'll lay out the entire flow of our game using just `print()` statements. It won't be interactive yet, but it helps us visualize the game's structure from start to finish.

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

Now, let's make our program dynamic! This module is all about getting input from the user and using it in our program.

### 📌 Sub-module 2.1: Taking User Input (m2_1.py)
We'll learn how to use the `input()` function to ask the user for information and then display the entered information back to them.

**Expected Output (user enters 7):**
```
Enter the number you guess:7
You guessed 7
```

### 📌 Sub-module 2.2: Pausing the Game (m2_2.py)
Let's add `input()` to our game. For now, we'll use it to pause the program and wait for the user to press "Enter", and then to get their response to a question. This makes the game feel more interactive.

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

Programs need to make decisions. In this module, you'll learn how to control the flow of your program using conditional logic (if-else statements).

### 📌 Sub-module 3.1: if-else Statements (m3_1.py)
We'll write a program that takes a number and checks if it's smaller or greater than 5 using an `if-else` block.

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

### 📌 Sub-module 3.2: Introduction to Lists (m3_2.py)
We'll take a quick detour to learn about lists, which are used to store multiple items in a single variable.

**Expected Output:**
```
The 3rd element is 30
```

### 📌 Sub-module 3.3: Conditional Logic in the Game (m3_3.py)
Now we'll add `if-else` to our game. The program will ask the user a question and will respond differently based on whether the user types "yes" or something else.

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

What if the computer's first guess is wrong? This module introduces nested conditions to handle more complex scenarios.

### 📌 Sub-module 4.1: Nested if-else (m4_1.py)
We will expand our game to make multiple guesses.

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

Coming Soon!

Get ready to learn how to make the computer guess again and again without writing the same code over and over.

---

## Module 6: Putting It All Together - The Final Game

Coming Soon!

In the final module, we will combine everything we've learned to create the complete, interactive Number Guessing Game!
