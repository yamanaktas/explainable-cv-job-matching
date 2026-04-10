# ==========================================================
# PYTHON LAB 1 — BASICS + DATA PROCESSING (STUDENT VERSION)
# ==========================================================
# Instructions:
# - Complete all TODO sections
# - Do NOT remove existing code unless instructed
# - Test your code step by step
# ==========================================================


# ==========================================================
# PART 1 — VARIABLES & DATA TYPES
# ==========================================================

print("=== PART 1: VARIABLES ===")

# TODO 1:
# Create variables:
# name (string)
# age (int)
# height (float)
# is_student (bool)

# Example:
# name = "Samed"

name = None
age = None
height = None
is_student = None

# TODO 2:
# Print all variables in a readable format

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

print()


# ==========================================================
# PART 2 — LISTS
# ==========================================================

print("=== PART 2: LISTS ===")

# TODO 3:
# Create a list called 'data' with at least 6 integer values
# Example: [10, 20, 30, 40]

data = []

# TODO 4:
# Print:
# - Full list
# - First element
# - Last element
# - Length of list

print("Data:", data)
# print("First:", ?)
# print("Last:", ?)
# print("Length:", ?)

print()


# ==========================================================
# PART 3 — FUNCTIONS
# ==========================================================

print("=== PART 3: FUNCTIONS ===")

# TODO 5:
# Write a function to calculate SUM

def calculate_sum(numbers):
    # TODO: implement
    return 0


# TODO 6:
# Write a function to calculate AVERAGE

def calculate_average(numbers):
    # TODO: implement (be careful: division by zero)
    return 0


# TODO 7:
# Write a function to find MAX value

def find_max(numbers):
    # TODO: implement
    return 0


# TODO 8:
# Write a function to find MIN value

def find_min(numbers):
    # TODO: implement
    return 0


# ==========================================================
# PART 4 — DATA ANALYSIS
# ==========================================================

print("=== PART 4: DATA ANALYSIS ===")

# TODO 9:
# Use your functions to compute:
# total, average, max, min

total = None
average = None
maximum = None
minimum = None

# TODO 10:
# Print results

print("Total:", total)
print("Average:", average)
print("Max:", maximum)
print("Min:", minimum)

print()


# ==========================================================
# PART 5 — FILTERING
# ==========================================================

print("=== PART 5: FILTERING ===")

# TODO 11:
# Write a function that returns values greater than a threshold

def filter_above_threshold(numbers, threshold):
    result = []
    # TODO: loop through numbers and append values > threshold
    return result


# TODO 12:
# Call function with threshold = 100

filtered_data = []

print("Filtered Data:", filtered_data)

print()


# ==========================================================
# PART 6 — USER INPUT
# ==========================================================

print("=== PART 6: USER INPUT ===")

# TODO 13:
# Ask user to input numbers separated by space

user_input = ""

# TODO 14:
# Convert input string to list of integers
# Hint:
# split() + int()

user_numbers = []

# TODO 15:
# Print:
# - Entered numbers
# - Average of numbers

print("You entered:", user_numbers)
print("Average:", 0)

print()


# ==========================================================
# BONUS PART (OPTIONAL)
# ==========================================================

print("=== BONUS PART ===")

# TODO 16:
# Write a function to count how many numbers are EVEN

def count_even(numbers):
    # TODO: implement
    return 0


# TODO 17:
# Write a function to count how many numbers are ODD

def count_odd(numbers):
    # TODO: implement
    return 0


# TODO 18:
# Test your functions using 'data'

even_count = 0
odd_count = 0

print("Even count:", even_count)
print("Odd count:", odd_count)

print()


# ==========================================================
# END OF LAB
# ==========================================================
# Make sure:
# - All TODOs are completed
# - Code runs without errors
# ==========================================================