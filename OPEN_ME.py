from new_sectors import get_sectors

#%% Input
year = 2010
n_sectors = 10 # number of new sectors

#%% Output
# 'result' is a DataFrame with 3 columns
# | Symbol | New Sector | Old Sector |

result = get_sectors(year, n_sectors)
