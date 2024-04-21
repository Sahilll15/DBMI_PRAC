import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

# Load the dataset
data = pd.read_csv('fpgrowth_text_dataset.csv')

# Drop any rows with missing values
data.dropna(inplace=True)

# Convert the textual data into a list of transactions
transactions = [transaction.split(',') for transaction in data['Transaction']]

# Convert the transactions into a one-hot encoded format
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)

# Print the frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)
