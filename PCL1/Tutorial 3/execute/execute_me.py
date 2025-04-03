#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Voting Eligibility Check

while True:
    age_input = input("Please enter your age (or type 'exit' to quit): ")
    
    if age_input.lower() == 'exit':
        print("Exiting the program.")
        break # important command to break the "while True" loop
    
    # Check if the input is a digit
    if age_input.isdigit():
        age = int(age_input)
        
        if age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    else:
        print("Invalid input! Please enter a valid number for your age.")
