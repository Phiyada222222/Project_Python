print("***Conver BMI***")
K = int(input("Enter your weight (kg) :"))
S = float(input("Enter your height(m) :")) 

bmi = K/(S**2)
print("You BMI is : ","{:.5f}".format(bmi))