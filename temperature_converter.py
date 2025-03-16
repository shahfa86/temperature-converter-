"""
Temperature Converter Program

This Python program allows users to convert temperatures between Celsius and Fahrenheit.
Users can choose to convert a single temperature or a range of temperatures with a step size.
The program includes error handling for invalid inputs.
"""

while True:
    # Ask the user for conversion type
    choice = input("Convert from Celsius to Fahrenheit (C) or Fahrenheit to Celsius (F)? (Type 'exit' to quit): ").strip().lower()

    if choice == "exit":
        print("Goodbye! Thanks for using the converter.")
        break  # Exit the loop

    elif choice in ["c", "f"]:
        # Ask if they want to convert a single temperature or a range
        mode = input("Do you want to convert a single temperature or a range? (single/range): ").strip().lower()

        if mode == "single":
            while True:
                try:
                    temperature = float(input("Enter temperature: "))  # Convert input to float
                    break  # If successful, exit the loop
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

            # Perform the conversion based on user choice
            if choice == "c":
                converted = (9/5) * temperature + 32
                print(f"Temperature in Fahrenheit: {converted:.2f}")
            else:
                converted = (5/9) * (temperature - 32)
                print(f"Temperature in Celsius: {converted:.2f}")

        elif mode == "range":
            while True:
                try:
                    start_temp = float(input("Enter the starting temperature: "))
                    end_temp = float(input("Enter the ending temperature: "))
                    step = float(input("Enter the step size: "))

                    if step <= 0:
                        print("Step size must be a positive number.")
                        continue  # Ask again if step is invalid

                    break  # Exit the loop if all inputs are valid
                except ValueError:
                    print("Invalid input. Please enter numeric values.")

            # Display the conversion results
            print("\nTemperature Conversions:")
            print("------------------------")
            print("Input Temp  |  Converted Temp")

            current_temp = start_temp
            while current_temp <= end_temp:
                if choice == "c":
                    converted = (9/5) * current_temp + 32
                    print(f"{current_temp:.2f}\u00b0C  ->  {converted:.2f}\u00b0F")
                else:
                    converted = (5/9) * (current_temp - 32)
                    print(f"{current_temp:.2f}\u00b0F  ->  {converted:.2f}\u00b0C")

                current_temp += step  # Increase the temperature by step size

        else:
            print("Invalid choice. Please enter 'single' or 'range'.")

        # Ask if the user wants to convert another temperature
        again = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
        if again == "no":
            print("Goodbye! Thanks for using the converter.")
            break  # Exit the loop
        elif again != "yes":
            print("Invalid input. Please enter 'yes' or 'no'.")

    else:
        print("Invalid choice. Please enter 'C', 'F', or 'exit'.")
