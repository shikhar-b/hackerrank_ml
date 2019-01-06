# Enter your code here. Read input from STDIN. Print output to STDOUT
import pandas as pd

file1 = 'transactions_data.csv'
transactions_data = pd.read_csv(file1)

file2 = 'product_data.csv'
product_data = pd.read_csv(file2)

# prod_id = transactions_data.product_id
# colors = {}
# for idx in prod_id:
#     col = product_data[product_data.product_id == idx].color.values[0]
#     if col in colors:
#         colors[col]+=1
#     else:
#         colors[col] = 1
# maxval = 0
# maxcol = ''
# for key, value in colors.iteritems():
#     if value > maxval:
#         maxval = value
#         maxcol = key

transactions_data = transactions_data.set_index('product_id').join(product_data.set_index('product_id'))
maxcol = transactions_data.groupby('color').count().sort().index[-1]
print(maxcol)


