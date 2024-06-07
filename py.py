# This is a basic Python program that calculates the area of a rectangle

# Function to calculate the area of a rectangle
def calculate_area(length, width):
    area = length * width
    return area

# Main function where the program execution begins
def main():
    # Input length and width of the rectangle from the user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the area using the calculate_area function
    area = calculate_area(length, width)

    # Display the calculated area
    print("The area of the rectangle is:", area)