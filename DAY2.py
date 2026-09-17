# BMI (Body Mass Index)

# Formula of BMI - (weight)/((height)**2) , weight-kg , height-m
n = int(input("enter no. of records:"))
for i in range(n):
    name = input(f'\nenter your name{i+1}:')
    weight = float(input("enter your weight in kgs:"))
    height = float(input("enter your height in meters:"))
    if weight > 0 and height > 0:
        BMI = (weight)/((height)**2)
        if BMI < 18.5:
            print(f'{name} is in Under Weight and BMI is {BMI:.2f}\n')
        elif 18.5 <= BMI <=24.9:
            print(f'{name} is in Normal Weight and BMI is {BMI:.2f}\n')
        elif 25 <= BMI <=29.9:
            print(f'{name} is in Over Weight and BMI is {BMI:.2f}\n')
        else:
            print(f'{name} is in Obesity and BMI is {BMI:.2f}\n')
    else:
        print("your weight and height should strictly greater than 0\n")
