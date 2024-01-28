import pandas as pd
import numpy as np
import random
import string

# Function to generate random names
def generate_random_names(n):
    names = []
    for _ in range(n):
        name_length = np.random.randint(low=5, high=10)
        name = ''.join(random.choices(string.ascii_uppercase, k=name_length))
        names.append(name)
    return names

# Number of companies and investors
num_companies = 100000
num_investors = 5000

# Generate random company names
company_names = generate_random_names(num_companies)

# Generate random company parameters
company_sizes = np.random.randint(low=50, high=500, size=num_companies)
company_profits = np.random.randint(low=10, high=100, size=num_companies)
company_industries = np.random.choice(['Tech', 'Health', 'Finance'], size=num_companies)

# Create company dataframe and save it to a CSV file
company_df = pd.DataFrame({
    'CompanyID': range(1, num_companies + 1),
    'Company': company_names,
    'Size': company_sizes,
    'Profit': company_profits,
    'Industry': company_industries,
})
company_df.to_csv('Companies.csv', index=False)

# Generate random investor names
investor_names = generate_random_names(num_investors)

# Generate random investor parameters
risk_tolerance = np.random.choice(['High', 'Moderate', 'Low'], size=num_investors)
time_horizon = np.random.choice(['Short term', 'Medium term', 'Long term'], size=num_investors)
income_needs = np.random.randint(low=50000, high=200000, size=num_investors)
liquidity_needs = np.random.choice(['High', 'Moderate', 'Low'], size=num_investors)
tax_considerations = np.random.choice(['Yes', 'No'], size=num_investors)
account_type = np.random.choice(['Taxable', 'IRA', '401k'], size=num_investors)
age = np.random.randint(low=25, high=75, size=num_investors)
investment_experience = np.random.choice(['Experienced', 'Novice'], size=num_investors)
other_assets = np.random.randint(low=100000, high=1000000, size=num_investors)
risk_capacity = np.random.choice(['High', 'Moderate', 'Low'], size=num_investors)

# Create investor dataframe and save it to a CSV file
investor_df = pd.DataFrame({
    'InvestorID': range(1, num_investors + 1),
    'Investor': investor_names,
    'RiskTolerance': risk_tolerance,
    'TimeHorizon': time_horizon,
    'IncomeNeeds': income_needs,
    'LiquidityNeeds': liquidity_needs,
    'TaxConsiderations': tax_considerations,
    'AccountType': account_type,
    'Age': age,
    'InvestmentExperience': investment_experience,
    'OtherAssets': other_assets,
    'RiskCapacity': risk_capacity,
})
investor_df.to_csv('Investors.csv', index=False)

# Generate random investments for each investor
mapping = []
for investor_id in range(1, num_investors + 1):
    num_investments = np.random.randint(low=1, high=10)
    invested_companies = np.random.choice(range(1, num_companies + 1), size=num_investments, replace=False)
    for company_id in invested_companies:
        mapping.append([investor_id, company_id])

# Create mapping dataframe and save it to a CSV file
mapping_df = pd.DataFrame(mapping, columns=['InvestorID', 'CompanyID'])
mapping_df.to_csv('mapping.csv', index=False)
