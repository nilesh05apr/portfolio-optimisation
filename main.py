import pandas as pd
import numpy as np

# Read in the data
portfolio = pd.read_csv('data/portfolio.csv', index_col=0)
marketcap = pd.read_csv('data/marketcap.csv', index_col=0)
roe = pd.read_csv('data/roe.csv', index_col=0)

# Calculate the returns
returns = portfolio.pct_change().dropna()

# Calculate the mean returns
mean_returns = returns.mean()
print("Mean returns: \n", mean_returns)

# Calculate the covariance matrix
cov_matrix = returns.cov()
print("Covariance matrix: \n", cov_matrix)

# Calculate the correlation matrix
corr_matrix = returns.corr()
print("Correlation matrix: \n", corr_matrix)

# Calculate the standard deviation
std_dev = returns.std()
print("Standard deviation: \n", std_dev)

# Calculate the Sharpe ratio
sharpe_ratio = mean_returns / std_dev
print("Sharpe ratio: \n", sharpe_ratio)

# Calculate the annualised Sharpe ratio
annualised_sharpe_ratio = sharpe_ratio * np.sqrt(252)
print("Annualised Sharpe ratio: \n", annualised_sharpe_ratio)

# Calculate the annualised mean returns
annualised_mean_returns = mean_returns * 252
print("Annualised mean returns: \n", annualised_mean_returns)

# Calculate the annualised standard deviation
annualised_std_dev = std_dev * np.sqrt(252)
print("Annualised standard deviation: \n", annualised_std_dev)

# Calculate the annualised covariance matrix
annualised_cov_matrix = cov_matrix * 252
print("Annualised covariance matrix: \n", annualised_cov_matrix)

# Calculate the annualised correlation matrix
annualised_corr_matrix = corr_matrix * 252
print("Annualised correlation matrix: \n", annualised_corr_matrix)

# Calculate the weights
weights = np.array(marketcap['marketcap']/np.sum(marketcap['marketcap']))
print("Weights: \n", weights)

# Calculate the portfolio variance
portfolio_variance = np.dot(weights.T, np.dot(annualised_cov_matrix, weights))
print("Portfolio variance: \n", portfolio_variance)

# Calculate the portfolio standard deviation
portfolio_std_dev = np.sqrt(portfolio_variance)
print("Portfolio standard deviation: \n", portfolio_std_dev)

# Calculate the portfolio return
portfolio_return = np.sum(annualised_mean_returns * weights)
print("Portfolio return: \n", portfolio_return)

# Calculate the portfolio Sharpe ratio
portfolio_sharpe_ratio = portfolio_return / portfolio_std_dev
print("Portfolio Sharpe ratio: \n", portfolio_sharpe_ratio)



