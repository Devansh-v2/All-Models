import pandas as pd

print("--" * 15)
print("Machine Learning Models")
print("--" * 15)

i = 1
while i == 1:

    # Menu Function

    def menu():
        print("Press 1 To Predict House Value")
        print("Press 2 To Predict Flower Species")
        print("Press 3 To Predict Company's Profit")
        print("Press 4 To Find Customer For Loan")
        print("Press 5 To Find Heart Disease")
        print()


    menu()

    # User Response will be Saved Here

    choice = int(input("Type your number here (1-5) :"))

    # To Create List

    if choice == 1:
        print()
        print("Enter the following Values to Calculate Your House Value")
        print()

        m = pd.read_pickle("House Price Predictor.pkl")

        income = eval(input("Enter Your Income:"))
        house_age = eval(input("Enter Your House Age:"))
        room = eval(input("Enter Your No.of Rooms:"))
        pop = eval(input("Enter Population in your area:"))

        query = pd.DataFrame(
            {'Avg. Area Income': [income], 'Avg. Area House Age': [house_age], 'Avg. Area Number of Rooms': [room],
             "Area Population": [pop]})

        print()
        print("Your House value is:", round(m.predict(query)[0], 2))
        print()
        cont = input("Will you like to Continue [y/n]")
        print()
        if cont.lower() == 'y':
            i = 1
        else:
            i = 0

    elif choice == 2:
        print()
        print("Enter the following Values to Calculate Flower Species")
        print()
        n = pd.read_pickle("Iris Species Predictor")

        sepL = eval(input("Enter Sepal Length:"))
        sepW = eval(input("Enter Sepal Width:"))
        petL = eval(input("Enter Petal Length:"))
        petW = eval(input("Enter Petal Width:"))

        query2 = pd.DataFrame(
            {'sepal_length': [sepL], 'sepal_width': [sepW], 'petal_length': [petL], "petal_width": [petW]})

        print()
        print(n.predict(query2), "is the Flower Species")
        print()
        cont = input("Will you like to Continue [y/n]")
        print()
        if cont.lower() == 'y':
            i = 1
        else:
            i = 0

    elif choice == 3:
        print()
        print("Enter the following Values to Calculate your Company's Profits")
        print()
        b = pd.read_pickle("Company Profits Predictor.pkl")

        rd = eval(input("Enter Your Company's Research & Development Expenditure:"))
        adm = eval(input("Enter Your Company's Administration Expenditure:"))
        msp = eval(input("Enter Your Company's Marketing Expenditure:"))

        query3 = pd.DataFrame({'R&D Spend': [rd], 'Administration': [adm], 'Marketing Spend': [msp]})

        print()
        print(round(b.predict(query3)[0], 2))
        print()
        cont = input("Will you like to Continue [y/n]")
        print()
        if cont.lower() == 'y':
            i = 1
        else:
            i = 0

    elif choice == 4:
        print()
        print("Enter the following Values to Find your Customer")
        print()

        v = pd.read_pickle("Loan Predictor.pkl")

        inc = eval(input("Enter Annual income of the customer ($000):"))
        fam = eval(input("Enter Family size of the customer:"))
        edu = eval(input("Enter Education Level:- 1: Undergrad, 2: Graduate, 3: Advanced/Professional:"))
        cda = eval(
            input("Enter Does the customer have a certificate of deposit (CD) account with the bank? (0:No,1:Yes):"))
        cca = eval(input("Enter Avg. spending on credit cards per month ($000):"))

        query4 = pd.DataFrame(
            {'Income': [inc], 'Family': [fam], 'Education': [edu], "CD Account": [cda], 'CCAvg': [cca]})
        print()

        if v.predict(query4) == 0:
            print('Not a Potential Customer')
            print()
            cont = input("Will you like to Continue [y/n]")
            print()
            if cont.lower() == 'y':
                i = 1
            else:
                i = 0

        else:
            print("Potential Customer")
            print()
            cont = input("Will you like to Continue [y/n]")
            print()
            if cont.lower() == 'y':
                i = 1
            else:
                i = 0

    elif choice == 5:
        print()
        print("Enter the following Values to Predict Heart Disease")
        print()
        b = pd.read_pickle("Heart Disease Predictor")

        CPT = eval(input(
            "Enter chest pain type:- Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, "
            "Value 4: asymptomatic:"))
        SoT = eval(input(
            "Enter the slope of the peak exercise ST segment:- Value 1: upsloping, Value 2: flat, Value 3: downsloping:"))
        NVF = eval(input("Enter number of major vessels (0-3) colored by flourosopy:"))
        Tha = eval(input("Enter Thallium:- 3 = normal; 6 = fixed defect; 7 = reversable defect:"))

        query = pd.DataFrame(
            {'Chest pain type': [CPT], 'Slope of ST': [SoT], 'Number of vessels fluro': [NVF], "Thallium": [Tha]})

        print()
        print((b.predict(query)), "of Heart Disease")
        print()
        cont = input("Will you like to Continue [y/n]")
        print()
        if cont.lower() == 'y':
            i = 1
        else:
            i = 0

    else:
        print("Invalid input")
        print()
        cont = input("Will you like to Continue [y/n]")
        print()
        if cont.lower() == 'y':
            i = 1
        else:
            i = 0
