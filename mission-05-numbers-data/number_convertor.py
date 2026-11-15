def convert_number():
    try:
        # Leaving input() empty removes the prompt text from the output
        user_input = input()
        decimal_num = int(user_input)
        
        binary_result = f"{decimal_num:b}"
        hex_result = f"{decimal_num:x}"
        
        # Only printing Binary and Hexadecimal
        print(f"Binary:      {binary_result}")
        print(f"Hexadecimal: {hex_result}")
        
    except ValueError:
        print("Invalid input! Please enter a whole decimal number (integer).")

if __name__ == "__main__":
    convert_number()