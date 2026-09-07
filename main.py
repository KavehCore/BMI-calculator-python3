#getting user inputs as height and weight
def get_user_inputs():
    weight = float(input("enter your weight (kg):"))
    height = float(input("enter your height (M):"))
    return weight,height


# calculate BMI
def calculate_bmi(weight,height):
    return weight//(height**2)


# get the BMI result
def get_bmi_result(bmi):
    print(f"BMI: {bmi}\nresult:")
    if bmi < 18.5:
        print("under weight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("over weight")
    else:
        print("obese")

# create main function to run
def main():
    weight,height = get_user_inputs()
    bmi = calculate_bmi(weight,height)
    get_bmi_result(bmi)

if __name__ == "__main__":
    main()