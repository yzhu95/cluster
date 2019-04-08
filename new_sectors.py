import pandas as pd
from get_train import get, pre
from sklearn.cluster import AgglomerativeClustering

def get_sectors(year, n_sectors):
    
    old_sectors = pd.read_csv('spy500.csv')[['Symbol', 'Sector']]
    
    universe = pd.read_csv('universe.csv', header=None)
    symbols = list(universe[0])
    
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
    
    train = get(year, features, symbols)
    train = pre(train)
    
    clustering = AgglomerativeClustering(
            n_clusters = n_sectors,
            linkage = 'ward'
        )
    
    res = clustering.fit_predict(train)
    
    res = pd.DataFrame({
            'Symbol': symbols,
            'group': res
        })
    
    res = res.merge(old_sectors, on='Symbol')
    
    res.columns = [
            'Symbol',
            'New Sector',
            'Old Sector',
        ]
    
    return res