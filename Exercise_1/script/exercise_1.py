import pandas as pd # for reading the data
import numpy as np # for data manipulation
import scipy.optimize as opt # for optimization
import matplotlib.pyplot as plt


# Load pollution data
pollution_df = pd.read_csv("../data/pollution_cleaneddata.csv", encoding='utf-8')
# print the first 5 rows of the dataframe for a quick check of the data
pollution_df.head()

def local_x(x, y, x0, k):
    """
    Find the closest points to x0 by calculating the squared distance between each point in x and x0.
    k is the number of x closest points to x0 to return.
    The function returns a list of tuples containing the squared distance and the x and y coordinates for the k closest points.
    """
    # make a empty list for storing the squared distances between each point in x and x0 and the coordinates of the points in x and y
    squared_distances_list = []
    # loop through each point in x and calculate the squared distance between the point and x0
    for i in range(len(x)):
        squared_distance = float((x[i] - x0) ** 2)
        y_value = float(y[i])
        x_value = float(x[i])
        squared_distances_list.append((squared_distance, x_value, y_value))
    # sort list by the squared distances so that the closest points are at the beginning of the list
    squared_distances_list.sort()
    # return the k closest points
    return squared_distances_list[:k]

def optimize_sum_of_squares(beta, x_closest, y_closest, weights):
    """
    Find the optimal beta parameters for the weighted linear regression model by minimizing the sum of squares.
    """
    beta_0 = beta[0]
    beta_1 = beta[1]

    # calculate the sum of squares
    eq = weights * (y_closest - (beta_0 + beta_1 * x_closest)) ** 2
    return(eq.sum())

def weight_function(x_closest, x0):
    """
    Calculate the weights for each point in x based on the distance from x0 using a Gaussian kernel (function found online).
    """
    # compute the physical distance on the x-axis for each local point
    distances = np.abs(x_closest - x0)
    
    # compute the distance to the furthest of the k neighbors
    d_max = np.max(distances)
    
    if d_max == 0:
        return np.ones_like(distances)
    
    # Gaussian kernel normalized by d_max
    weights = np.exp(-0.5 * (distances / d_max) ** 2)
    return weights

def local_regression(x, y, x0, k):
    """
    Perform local regression on the data using the k closest points to x0. 
    Returns:
      - y_0: predicted expected value at x0
      - rse: standard deviation of residuals (Residual Standard Error)
      - se_y_hat: standard error of the expected value E[Y|x0]
    """
    # Allows x0 to be a list or array and returns a list of predicted values for each value in x0
    if isinstance(x0, (list, np.ndarray)):
        return [local_regression(x, y, val, k) for val in x0]
        
    # get the closets x and their coordinates of the k closest points to x0 by calling the local_x function
    closest_points = local_x(x, y, x0, k)

    # extract only the coordinates and make it into an array for easier calculations
    x_closest = np.array([point[1] for point in closest_points])
    y_closest = np.array([point[2] for point in closest_points])

    # I also have to calculate the weights for each point in x_closest based on the distance from x0 by calling the weight_function
    weights = weight_function(x_closest, x0)

    # find the most optimal beta parametes (fit the model)
    beta = opt.minimize(optimize_sum_of_squares, [0, 0], args=(x_closest, y_closest, weights)).x
    beta_0 = beta[0]
    beta_1 = beta[1]

    # predict expected value (y_0) at x0 using the fitted model
    y_0 = beta_0 + beta_1 * x0

    # calculate the residuals
    residuals = y_closest - (beta_0 + beta_1 * x_closest)

    # degrees of freedom for the residuals
    df = k - 2
    rse = np.sqrt(np.sum(residuals ** 2) / df)

    # Standard Error of the Expected Value SE(hat_y_0)
    x_bar = np.mean(x_closest)
    ss_x = np.sum((x_closest - x_bar) ** 2)
    se_y_hat = rse * np.sqrt((1 / k) + ((x0 - x_bar) ** 2) / ss_x)

    return float(y_0), float(rse), float(se_y_hat)

# Output the predicted value of y at x0 and the standard deviation of the residuals for each x0 in X0
# Also plot the data with the predicted values and the standard deviation of the residuals as error bars

# choosen x0 values to predict and set k value to 5
X0 =[10,18,25]
k_val = 5

# call the local_regression function 
results = local_regression(pollution_df['POOR'], pollution_df['MORT'], X0, k_val)

# get the predicted values, standard deviations and standard errors for predictions
predictions = [results[0] for result in results]
std_devs = [result[1] for result in results]
SE_y_hats = [result[2] for result in results]


# Plot the data with the predicted values and the standard deviation of the residuals as error bars
plt.figure(figsize=(8,6))
plt.title("MORT vs POOR with Local Regression Predictions")
plt.scatter(pollution_df['POOR'], pollution_df['MORT'], label='Observed Data', color='gray')
# set the x axis to be only whole numbers
plt.xticks(np.arange(0, 31, 2))
plt.errorbar(X0, [pred[0] for pred in predictions], yerr=std_devs, fmt='o', color='red', ecolor='black', capsize=5, label='Predictions with Std Dev')
plt.xlabel("Income (Percentage of families with income < $3000)")
plt.ylabel("Mortality (Total age-adjusted mortality rate per 100,000)")
plt.legend()
plt.show()

# Print the predicted values and standard deviations for each x0 in X0 as a table
results_df = pd.DataFrame({'x0': X0, 'Predicted y': [pred[0] for pred in predictions], 'Standard Error of the prediction': SE_y_hats})
print(results_df)
