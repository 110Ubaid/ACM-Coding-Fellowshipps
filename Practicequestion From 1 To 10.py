# def find_average(numbers):
#     if not numbers:
#         return None

#     total_sum = sum(numbers)
#     average = total_sum / len(numbers)
#     return average

# # Example usage:
# # Replace the list below with your own set of numbers.
# numbers_list = [10, 20, 30, 40, 50]
# result = find_average(numbers_list)
# print("Average:", result)
# #############QUESION NO 1#################
# def find_average(numbers):
#     if not numbers:
#         return None

#     total_sum = sum(numbers)
#     average = total_sum / len(numbers)
#     return average

# def get_user_input():
#     try:
#         N = int(input("Enter the total number of elements (N): "))
#         numbers = []
#         for i in range(N):
#             num = float(input(f"Enter number {i + 1}: "))
#             numbers.append(num)
#         return numbers
#     except ValueError:
#         print("Invalid input. Please enter valid numbers.")
#         return []

# # Get user input
# numbers_list = get_user_input()
# average = find_average(numbers_list)
# 2
# if average is not None:
#     print("Average:", average)
# else:
#     print("No numbers entered. Cannot calculate the average.")
    #-----------------------
    ###############QUESTION NO 2#################
    # from datetime import datetime

    # # Get the current date and time
    # current_datetime = datetime.now()

    # # Format and print the current date and time
    # print("Current Date and Time:", current_datetime)

#########QUESTION 3################
# import math

# def circle_area(radius):
#     if radius < 0:
#         return None
#     else:
#         return math.pi * radius ** 2

# # Example usage:
# radius = 5  # Replace 5 with the desired radius value
# area = circle_area(radius)
# if area is not None:
#     print("Area of the circle:", area)
# else:
#     print("Invalid radius. Radius cannot be negative.")
##########qUESTION 4 ##########
# def reverse_string(input_string):
#     return input_string[::-1]

# # Example usage:
# text = "Hello, World!"
# reversed_text = reverse_string(text)
# print("Reversed String:", reversed_text)
########qUESTION 05#############
def find_biggest_and_smallest(numbers):
    if len(numbers) != 3:
        return None, None
    else:
        biggest = max(numbers)
        smallest = min(numbers)
        return biggest, smallest

# Example usage:
# Replace the list below with your own set of three numbers.
# #find the Biggest and Smallest of 3 numbers using lists in Python
# numbers_list = [10, 5, 15]
# biggest_number, smallest_number = find_biggest_and_smallest(numbers_list)

# if biggest_number is not None and smallest_number is not None:
#     print("Biggest Number:", biggest_number)
#     print("Smallest Number:", smallest_number)
# else:
#     print("Please provide a list of exactly three numbers.")
##########QUESTION 06 ############
#How to calculate the sum of elements in a list in Python
# Example list of numbers
# numbers_list = [10, 20, 30, 40, 50]

# # Calculate the sum of elements in the list
# total_sum = sum(numbers_list)

# # Print the result
# print("Sum of elements in the list:", total_sum)
###########QUESTION NO 7 ###########
#How to find area of a triangle in Python
# def triangle_area(base, height):
#     if base < 0 or height < 0:
#         return None
#     else:
#         return (base * height) / 2

# # Example usage:
# base_length = 10   # Replace 10 with the length of the base of the triangle
# height_length = 5  # Replace 5 with the height of the triangle
# area = triangle_area(base_length, height_length)

# if area is not None:
#     print("Area of the triangle:", area)
# else:
#     print("Invalid base or height. Base and height cannot be negative.")
############QUESTION NO 08 ################
#How to extract extension from filename in python
# #import os

# def get_file_extension(filename):
#     _, extension = os.path.splitext(filename)
#     return extension

# # Example usage:
# file_name = "example.txt"
# extension = get_file_extension(file_name)
# print("File Extension:", extension)
###########QUESTION NO 09 ###########
#How to create a list and tuple with comma separated numbers in Python
# def create_list_and_tuple(input_string):
#     # Split the input string using commas as separators
#     numbers_list = input_string.split(',')
    
#     # Convert the list of strings to a list of integers (or floats)
#     numbers_list = [int(num) for num in numbers_list]  # Use `float(num)` for floats
    
#     # Create a tuple from the list
#     numbers_tuple = tuple(numbers_list)
    
#     return numbers_list, numbers_tuple

# # Example usage:
# input_numbers = "1,2,3,4,5"
# list_of_numbers, tuple_of_numbers = create_list_and_tuple(input_numbers)

# print("List of Numbers:", list_of_numbers)
# print("Tuple of Numbers:", tuple_of_numbers)
#########QUESTION 10 #############
#How to calculate the distance between two points in Python
# import math

# def calculate_distance(x1, y1, x2, y2):
#     distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#     return distance

# # Example usage:
# x1, y1 = 1, 2  # Replace with the coordinates of the first point
# x2, y2 = 4, 6  # Replace with the coordinates of the second point

# distance = calculate_distance(x1, y1, x2, y2)
# print("Distance between the two points:", distance)


