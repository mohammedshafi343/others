def calculate_bmi(weight, height):
    """Calculate the BMI using the formula: BMI = weight (kg) / height (m)^2."""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Determine the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def bmi_calculator():
    print("Welcome to the BMI Calculator!")
    
    while True:
        try:
            weight = float(input("Enter your weight in kilograms (kg): "))
            height = float(input("Enter your height in meters (m): "))
        except ValueError:
            print("Invalid input. Please enter numeric values for weight and height.")
            continue

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"BMI Category: {category}\n")

        play_again = input("Do you want to calculate BMI again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    bmi_calculator()
