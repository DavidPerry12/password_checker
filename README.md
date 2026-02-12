# Password Strength Checker

## Overview
This is a simple Python password strength checker that runs in the terminal. The program asks the user to enter a password and then evaluates its strength using basic rules such as length and characters. A score out of six points is assigned, and the program provides suggestions for how the password could be improved.

The purpose of this project is educational. It demonstrates how software can encourage better security habits while also raising ethical questions about how automated tools should be used responsibly. It also shows how easy it is to write a code that can verify that a given password is sufficiently complicated so as to be secure, protecting the password from hackers and guessers.

## Features
The password checker evaluates several common strength indicators:

- Length of at least 8 characters
- Length of at least 12 characters
- Presence of lowercase letters
- Presence of uppercase letters
- Presence of numbers
- Presence of symbols

Additional safety checks:
- Detecting extremely common passwords
- Warning the user if a character repeats three times in a row, which is often a sign of weak patterns

The program assigns a score based on these criteria and displays a strength label:
- Weak
- Moderate
- Strong

## How to Run the Program

### Requirements
- Python 3.x installed
- No external libraries are required

### Running the Script
Open a terminal in the project folder and run:

``bash

python password_checker.py

The program will prompt you to enter a password and will display the strength result and feedback in the terminal.

### Example Behavior
The program prints:

A strength category (Weak, Moderate, Strong)

A score out of 6

Suggestions for improving the password if needed

## Limitations and Important Warnings:
This program is a basic educational example and should not be used to seriously evaluate real world password security. 

  Some important limitations include:
    It does not measure true password entropy, or check against known data breaches.
    It does not account for advanced attack methods, which can include things like dictionary attacks or brute force modeling.
    A password rated “Strong” by this program may still be insecure depending on context.
    Because of these limitations, the tool should only be used for learning purposes.

## Ethical Considerations and Responsible Use:
Software that evaluates passwords can create a false sense of security if users assume a score automatically means their password is safe. For this reason, the program is including this warning and intentionally simple logic to emphasize transparency rather than authority. This tool should not be used to enforce password policies or to audit real systems. 

It is istead meant to help users think about common password weaknesses and to encourage responsible software design that clearly communicates its limits. Developers have an ethical responsibility to avoid overstating what their tools can do. By keeping the design simple and clearly documenting its limitations, I am aiming to demonstrate responsible and honest software practices.

## Author
David Perry
CS 3090 – Block 2 Project
02/11/26
