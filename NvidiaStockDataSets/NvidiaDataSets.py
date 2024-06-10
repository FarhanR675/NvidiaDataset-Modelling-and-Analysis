import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

file_path  = "C:/Users/Farha/Downloads/nvidia_stock_dataset.csv"
df = pd.read_csv(file_path)

loop = True
while loop is True:
    print("Enter a following number to select your options: "
          "\n1. Basic Information"
          "\n2. First 5 Rows"
          "\n3. Basic Statistics"
          "\n4. Missing Values"
          "\n5. Full Dataset"
          "\n6. Plotting"
          "\n7. Prediction Model"
          "\n8. Exit")
    userOptions = input("Selected Option: ")

    if userOptions == "1":
        print("Basic Information: ")
        print(df.info())
        userInput = input("Do you want continue (y/n): ")
        if userInput == "n":
            break
        elif userInput == "y": continue

    elif userOptions == "2":
        print("\nFirst 5 Rows: ")
        print(df.head())
        userInput = input("Do you want continue (y/n): ")
        if userInput == "n":
            break
        elif userInput == "y": continue

    elif userOptions == "3":
        print("\nBasic Statistics: ")
        print(df.describe())
        userInput = input("Do you want continue (y/n): ")
        if userInput == "n":
            break
        elif userInput == "y": continue

    elif userOptions == "4":
        print("\n Missing Values: ")
        print(df.isnull().sum)
        userInput = input("Do you want continue (y/n): ")
        if userInput == "n":
            break
        elif userInput == "y": continue

    elif userOptions == "5":
        print("\nNvidia Full Dataset: ")
        print(df.to_string(max_rows=None))
        userInput = input("Do you want continue (y/n): ")
        if userInput == "n":
            break
        elif userInput == "y": continue

    elif userOptions == "6":
        print("Plotting Options:"
        "\n1. Open Prices"
        "\n2. High Prices"
        "\n3. Low Prices"
        "\n4. Close Prices"
        "\n5. Adj Close Prices")
        userPlot = input("Selected Option: ")

        if userPlot == "1":
            numerical_columns = "Open"
        elif userPlot == "2":
            numerical_columns = "High"
        elif userPlot == "3":
            numerical_columns = "Low"
        elif userPlot == "4":
            numerical_columns = "Close"
        elif userPlot == "5":
            numerical_columns = "Adj Close"
        else:
            print("Invalid option. Please try again.")
            continue

        plt.figure(figsize=(10, 6))
        sns.histplot(df[numerical_columns], kde= True)
        plt.title(f"Distribution of {numerical_columns}")
        plt.xlabel(numerical_columns)
        plt.ylabel("Frequency")
        plt.show()

        userInput = input("Do you want continue (y/n): ")
        if userInput == "n":
            break
        elif userInput == "y":
            continue

    elif userOptions == "7":
        df["Prediction"] = df["Close"].shift(-1)
        df = df[:-1]
        x = df[["Close"]]
        y = df["Prediction"]

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(x_train, y_train)

        y_prediction = model.predict(x_test)

        print("Mean Squared Error: ", mean_squared_error(y_test, y_prediction))
        print("R^2 Score: ", r2_score(y_test, y_prediction))

        plt.figure(figsize=(10, 6))
        plt.plot(y_test.values, label="Actual Prices")
        plt.plot(y_prediction, label="Predicted Prices")
        plt.title("Actual vs Predicted Prices")
        plt.legend()
        plt.show()

        userInput = input("Do you want continue (y/n): ")
        if userInput == "n":
            break
        elif userInput == "y":
            continue


    elif userOptions == "8":
        loop = False
    else:
        print("ERROR: Invalid option. Please try again")
