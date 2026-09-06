import pandas as pd # for data manipulation
import numpy as np # for data manipulation


# load bird data
bird_df = pd.read_csv("../data/bird_count.csv")
bird_df_sorted = bird_df.sort_values(by='yr')
# extract values into NumPy arrays
x = bird_df_sorted['yr'].values
y = bird_df_sorted['count'].values
# center the year so that 1999 becomes the baseline (instead of year 0)
x_centered = x - x.min()

# Function for poission regression
def predict_lambda(beta, x):
    """
    Find the estimated rate by computing the mean average. 
    """
    beta_0 = beta[0]
    beta_1 = beta[1]
    return(np.exp(beta_0 + beta_1 * x))

def maximum_likelihood_estimation(beta, x, y):
    """
    Computes log-likelihood for Poisson regression.
    """
    # get the lambda (estimated rate)
    lambda_i = predict_lambda(beta, x)

    # compute the log-likelihood function 
    log_likelihood = np.sum(y * np.log(lambda_i) - lambda_i)
    return -log_likelihood

def optimize_parameters(beta, x, y):
    # use built in function for optimizing of parameters using scipy.optimize.minimize
    fit_result = opt.minimize(maximum_likelihood_estimation, beta, args=(x, y))

    # Extract optimal parameters
    beta_hat = fit_result.x
    return(beta_hat)

# set initial guess for [beta_0, beta_1] to (0,0)
initial_beta = [0.0, 0.0]

first_estimate = optimize_parameters(initial_beta, x_centered, y)
print(first_estimate)
first_beta = [2.32533195 -0.03244318]
second_estimate = optimize_parameters(first_beta, x_centered, y)
print(second_estimate)