import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# get data from raw_data.xlsx
def get(year, features, index=None):
    df = pd.read_excel('raw_data.xlsx')
    
    data = df[df.iloc[:, 1] == features[0]].iloc[:, [0, year-2006]]
    data.columns = ['Ticker', features[0]]
    data.set_index('Ticker', inplace=True)
    
    for feature in features[1:]:
        data[feature] = df[df.iloc[:, 1] == feature].iloc[:, year-2006].values
    
    if index == None:
        return data
    return data.reindex(index)

# preprocessing
def pre(data):
    data = data.apply(ratio, axis=1)

    pip = Pipeline([
            ('imputer', SimpleImputer(strategy='mean')),
            ('std_scaler', StandardScaler()),
        ])
    
    return pip.fit_transform(data)

def ratio(Series):
    return Series / Series[0]





