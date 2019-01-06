# Enter your code here. Read input from STDIN. Print output to STDOUT
import pandas as pd

file1 = 'transactions_data.csv'
transactions_data = pd.read_csv(file1)

file2 = 'product_data.csv'
product_data = pd.read_csv(file2)

transactions_data = transactions_data.set_index('product_id').join(product_data.set_index('product_id'))
transactions_data['transaction_date'] = pd.to_datetime(transactions_data['transaction_date'])
transactions_before = transactions_data[(transactions_data['transaction_date'] < '2012-10-1 00:00:00')]
transactions_after = transactions_data[(transactions_data['transaction_date'] >= '2012-10-1 00:00:00')]

columns = ['no_transactions','total_spent', 'label']
index = set(transactions_data['customer_id'])
features = pd.DataFrame(index=index, columns=columns)
features['no_transactions'] = transactions_before['customer_id'].value_counts()
features['total_spent'] = transactions_before.groupby('customer_id')['unit_product_price'].sum()

features = features.fillna(0)
features['label'] = transactions_after['customer_id'].value_counts()
features = features.fillna(0)
features['label'].where(features['label']>0 , 1)
features.to_csv('features_data.csv')