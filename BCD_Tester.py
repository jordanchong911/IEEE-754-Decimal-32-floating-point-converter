from logic.densely_packed_BCD import densely_packed

def main():
    while True:
        # Ask the user for a number
        user_input = input("Enter a number (type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break  # Exit the loop if the user wants to quit
        
        try:
            # Convert user input to integer
            number = user_input
            
            # Call the densely_packed function
            result = densely_packed(number)
            
            # Print the result
            print("Result:", result)
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
