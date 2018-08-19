"""

Linear Regression Finder : Given a csv file of the following format calculates the linear regression for the given data.

    Data format:

    x     y
    
    1	  2
    2	  3
    3	  4
    4	  5
    5	  6
    6	  7
    7	  8
    8	  9
    9	  10
    10	  11

    Formula :
    
    y = a + (b * x)

    b = r * (sy / sx)

    a = y1 - (b * x1)

    r = sigma( (x - x1) * (y - y1) ) / sqrt( sigma( (x - x1)**0.5) * sigma( (y - y1)**0.5) )

"""
from sys import stdin, stdout
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import time
import csv


def load_csv():

    # Getting the name of the csv file to be loaded

    file_name = input("enter the name of the csv file : ")

    x = []

    y = []

    # Loading csv file

    try:

        with open(file_name+".csv") as csvfile:

            reader = csv.DictReader(csvfile)

            for row in reader:

                x.append(float(row['x']))

                y.append(float(row['y']))

        return x, y, file_name

    except:

        print("\nThe entered csv file dosent exixt.\n\nPlease check the name and try again.\n")

def show_data(x, y):

    # Displaying the content of the csv file

    for i in range(len(x)):

        print(str(x[i])+"\t"+str(y[i]))

def linear_reg(x, y):

    # Finding means of x and y as x1 and y1

    x1 = sum(x)/len(x)

    y1 = sum(y)/len(y)

    # Finding the numerator part to calculate r

    x = [i-x1 for i in x]

    y = [i-y1 for i in y]

    z = [x[i]*y[i] for i in range(len(x))]

    # Finding the denominator part to calculate r

    x = [i*i for i in x]

    y = [i*i for i in y]

    # Calculation of r, sy and sx

    r = sum(z)/((sum(x)*sum(y))**0.5)

    sy = (sum(y)/(len(y)-1))**0.5

    sx = (sum(x)/(len(x)-1))**0.5

    # Calculating a and b

    b = r * (sy / sx)

    a = y1 - (b * x1)

    # Finding and displaying y

    val = str(a)+" + ( "+str(b)+" * x )"

    return val, a, b

def scatter_plot(x, y, a, b):

    # Ploting the scatter plot

    area = 100

    colors = np.random.rand(len(x))

    fig, ax = plt.subplots()

    data = plt.scatter(x, y, s=area, c=colors, alpha=1)

    # Finding ends of the regression line
    
    start = [min(x), max(x)]

    end = [(b * min(x)) + a, (b * max(x)) + a]

    # Plotting the regression line

    reg_line = lines.Line2D(start, end,  lw=2, color='black', axes=ax)

    ax.add_line(reg_line)

    # Displaying the plots

    ax.grid(True)

    plt.axis('equal')

    plt.tight_layout()

    plt.show()

def predict(a, b):

    test_x = float(input("Enter the value of x for which y is to be predicted : "))

    test_y = a + (b * test_x)

    print("\nFor x = "+str(test_x)+" y = "+str(test_y)+"\n")

    return test_x, test_y

def update_csv(test_x, test_y, file_name):

    # Updating the CSV file with the predicted value

    fields = [test_x, test_y]

    with open(file_name+".csv", 'a') as f:

        writer = csv.writer(f)

        writer.writerow(fields)

def clear_data_set():

    # Clearing the data set by resetting the values

    x = []

    y = []

    a = 0

    b = 0

    val = ""

    return x, y, a, b, val
    
def main():

    try:

        op = 0
        
        while op != 8:

            op = int(input("Choose your option :\n\n1. Load csv\n2. Show data\n3. Find Linear regression equ\n4. Show scatter plot\n5. Predict\n6. Update CSV\n7. Clear Data Set\n8. Exit\n\n"))

            print()
            
            if op == 1:

                x, y, file_name = load_csv()

                x = np.array(x)

                y = np.array(y)

                print()

            elif op == 2:

                show_data(x, y)

                print()

            elif op == 3:

                val, a, b = linear_reg(x, y)

                print("y = "+val)

                print()

            elif op == 4:

                scatter_plot(x, y, a, b)

            elif op == 5:

                test_x, test_y = predict(a, b)

            elif op == 6:

                update_csv(test_x, test_y, file_name)

            elif op == 7:

                x, y, a, b, val = clear_data_set()

            elif op == 8:

                exit()

            else:

                print("\ninvalid input\n\nplease select a valid input\n")

    except:

        print("Something went wrong try again.")

if __name__ == "__main__":

    main()
