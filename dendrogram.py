from scipy.cluster.hierarchy import dendrogram, linkage
from get_train import get, pre
import matplotlib.pyplot as plt
#%%
index = [
        'BAC', 
        'JPM', 
        'GS', 
        'C',
        'AAPL', 
        'IBM', 
        'MSFT', 
        'ORCL'
    ]

years = [
        2010,
        2013,
        2016
    ]

features = [
        'TOTAL ASSETS', 
        'Cash & Equivalents',
        'Receivables - Total (Net)',
        'Inventories - Total',
        'Sales (Net)',
        'Cost of Good Sold',
        'GROSS PROFIT'
    ]

methods = [
        'single', 
        'complete', 
        'average', 
        'ward'
    ]

#%%
fig, axes = plt.subplots(4, 3, figsize=(16, 9))
fig.tight_layout()
fig.subplots_adjust(wspace=0.05)

i = 0
j = 0
for year in years:
    train = get(year, features, index)
    train = pre(train)
    
    for method in methods:
        ax = axes[i, j]
        Z = linkage(train, method=method)
        dn = dendrogram(Z, ax=ax, labels=index)
        ax.set_yticks([])
        
        i += 1
    
    j += 1
    i = 0

for i in range(3):
    axes[i, 0].set_ylabel(
            methods[i], 
            rotation=0, 
            labelpad=25
        )
axes[3, 0].set_ylabel(
        'WARD', 
        rotation=0, 
        labelpad=25,
        color='r'
    )
    
for j in range(3):
    axes[0, j].set_title(years[j])
  