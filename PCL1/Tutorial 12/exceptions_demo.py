def function_with_exception_handling(input):
    try:
        # Simulate some processing
        result = 10 / input
        print(f"Result is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Processing completed successfully.")
        
    print(10+input)   
        
if __name__ == "__main__":
    # Test with valid input
    function_with_exception_handling(2)
    
    # Test with zero to trigger exception
    function_with_exception_handling(0)
    
    # Test with invalid input to trigger unexpected exception
    function_with_exception_handling("a")