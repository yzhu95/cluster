from scipy.cluster.hierarchy import dendrogram, linkage
from get_train import get, pre
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#%%
index = [
        'BAC', 
        'JPM', 
        'GS', 
        'C',
        'AAPL', 
        'IBM', 
        'MSFT', 
        'ORCL',
        'XOM',
        'CVX',
        'EOG',
        'PSX',
        'AMZN'
    ]

years = [
        2010,
        2011,
        2012,
        2013,
#        2014,
#        2015,
#        2016,
#        2017,
    ]

features = [
        'TOTAL ASSETS', 
        'Cash & Equivalents',
        'Receivables - Total (Net)',
        'Inventories - Total',
        'Sales (Net)',
        'Cost of Good Sold',
        'GROSS PROFIT',
        
        'OPERATING INCOME BEFORE DEPREC',
        'Depreciation, Depletion & Amortization',
        'Interest Expense',
        'Non-Operating Income/Expense',
        'Income Taxes - Total',
        'Advertising Expense',
        'Research & Development Expense',
        'Operating Cash Flow',
    ]

methods = [
        #'single', 
        #'complete', 
        #'average', 
        'ward'
    ]

#%%
fig, axes = plt.subplots(4, 1, figsize=(12, 9))
fig.tight_layout()

i = 0
for year in years:
    train = get(year, features, index)
    train = pre(train)
    
    for method in methods:
        ax = axes[i]
        Z = linkage(train, method=method)
        dn = dendrogram(Z, ax=ax, labels=index)
        ax.set_yticks([])
        
        i += 1
    
for i in range(4):
    axes[i].set_ylabel(
            years[i], 
            rotation=0, 
            labelpad=20
        )
    
axes[0].set_title('Hierarchy (Ward)')

#%% K-Means
for year in range(2010, 2018):
    train = get(year, features, index)
    train = pre(train)
    kmeans = KMeans(n_clusters=3).fit(train)
    print(kmeans.labels_)  