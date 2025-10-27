# Salary Calculator
A simple Python program that calculates employee pay based on working hours and hourly rate, including overtime compensation.
## Features
- Calculates regular pay for up to 40 hours
- Automatically applies 1.5x overtime rate for hours worked beyond 40
- Input validation to ensure numeric and non-negative values
- User-friendly prompts and error messages

## Requirements
- Python 3.9.6 or higher

## Usage
Run the program from the command line:``` bash
python salary_calculator2.py


The program will prompt you to enter:
Total hours worked
Hourly rate
It will then calculate and display your total pay, accounting for overtime if applicable.
Example 
```
Write your working hours please: 45
Write your rate per hour please: 20
Pay: 950.0
```

In this example:
Regular pay (40 hours × 20):800
Overtime pay (5 hours × 30):150
Total: $950
How It Works
Regular hours: Hours up to 40 are paid at the standard rate
Overtime hours: Hours beyond 40 are paid at 1.5× the standard rate
Input validation: The program ensures all inputs are numeric and non-negative, re-prompting if invalid data is entered
License
This project is open source and available for personal and educational use.