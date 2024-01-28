import torch 
import torch.nn as nn
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import heapq
import scipy.sparse as sp
import math
import argparse
import json

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, ndcg_score

# Load the model
device = 'cuda' if torch.cuda.is_available() else 'cpu'
class CFModel(nn.Module):
    def __init__(self, n_users, n_items, n_factors=20):
        super().__init__()
        self.user_factors = nn.Embedding(n_users, n_factors)
        self.item_factors = nn.Embedding(n_items, n_factors)

    def forward(self, user, item):
        return (self.user_factors(user) * self.item_factors(item)).sum(1)
    
def recommend(investor_id, model, n_items, k):
    # Set model to evaluation mode
    model.eval()

    # Create tensor of item IDs
    items = torch.arange(n_items, device=device)

    # Repeat investor ID for each item
    investors = torch.full((n_items,), investor_id, device=device)

    # Get predictions
    with torch.no_grad():
        preds = model(investors, items)

    # Get indices of top predictions
    top_items = preds.topk(k, largest=True).indices

    return top_items

def main(userID, num_companies):
    # Use relative paths
    company_df = pd.read_csv('./Companies.csv')
    mapping_df = pd.read_csv('./mapping.csv')
    investor_df = pd.read_csv('./Investors.csv')
    n_users = investor_df['InvestorID'].nunique()
    n_items = company_df['CompanyID'].nunique()
    model = CFModel(n_users, n_items)  # Initialize the model
    model.load_state_dict(torch.load('newModel.pth'))  # Load the parameters
    model.to(device)  # Move the model to the device
    investor_id = userID # The ID of the investor you want to generate recommendations for
    k = num_companies  # The number of recommendations to generate

    recommendations = recommend(investor_id, model, n_items, k)

    recommended_companies = company_df[company_df['CompanyID'].isin(recommendations.cpu().numpy())]

    # Convert DataFrame to JSON
    recommended_companies_json = recommended_companies.to_json(orient='records')

    # Return JSON string
    return recommended_companies_json

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--userID', type=int, help='User ID')
    parser.add_argument('--num_companies', type=int, help='Number of companies needed')
    args = parser.parse_args()

    result = main(args.userID, args.num_companies)
    print(result)
