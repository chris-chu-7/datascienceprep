import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


#linear regression to prep for data science interview 

def calculate_linear_regression(data):
    frame = pd.DataFrame(data)
    x = frame.iloc[:, 0]
    y = frame.iloc[:, 1]
    
    # average of x and y
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # slope has a numerator and denominator
    numer = np.sum((x - mean_x) * (y - mean_y))
    denom = np.sum((x - mean_x) ** 2)
    alpha = numer / denom

    # intercept is basically the y mean - the x mean * slope
    beta = mean_y - alpha * mean_x

    # linear regression least squares line
    x_range = np.linspace(0, 100, 100)
    y_range = alpha * x_range + beta
    
    #each point rounded to hundredths point
    plt.plot(x_range, y_range, '-r', label=f'Linear Regression: y = {alpha:.2f}x + {beta:.2f}')

    plt.scatter(x, y, color='blue', label='Data Points')

    # labels/title
    plt.title('Crime Rate vs Home Value')
    plt.xlabel('Crime Rate')
    plt.ylabel('Home Value')

    #show plot and legend
    plt.legend()
    plt.show()

    return alpha, beta

column_names = ['crimerate', 'zoneproportion', 'nonretailbusinessacres', 'charlesriverdummy', 'nitricoxide',
                'roomsperdwelling', 'proportionownedbefore1940', 'distanceforemploymentcenter', 'accessibilityofradialhighways',
                'propertytax', 'pupilteacherratio', 'africanamericanpopulation', 'lowerstatus', 'homevalue']


#parsing the data and putting it into a table with columns. this data is like a Scanner in Java. 
boston_data = pd.read_csv('housing.csv', header=None, delimiter=r"\s+", names=column_names)


selected_columns = boston_data[['crimerate', 'homevalue']]

calculate_linear_regression(selected_columns)


