# Linear_Regression_Finder

A python program to find the linear regression for simple data sets without using scikit-learn

# Data set format

    x       y
    1       2
    2       3
    3       4
    4       5
    5       6
    6       7
    7       8
    8       9
    9       10
    10      11
   
# Formulas

 y = (a * x) + b

 b = r * (sy / sx)

 a = y1 - (b * x1)

 r = sigma( (x - x1) * (y - y1) ) / sqrt( sigma( (x - x1)**0.5) * sigma( (y - y1)**0.5) )

# Procedure

1. Install python
2. Then install the following python pacakages
    a. matplotlib
    b. numpy
    c. csv
3. Run the the linear_regerssion_finder.py
4. Load the csv file by selecting option 1
5. Then find the linear regression equation by selecting option 2
6. Once we get the regression equation we can view the scatter plot by selecting option 4
7. Then to predict the value of y for a given x select option 5
8. To update the CSV with the predicted value select option 6
9. To load a different data set clear the previous data set by selecting option 7
10. Select option 8 to exit/ terminate the program
