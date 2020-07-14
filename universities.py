import pandas as pd

universty_towns = []
with open('Datasets/university_towns.txt') as file:
    for line in file:
        if '[edit]' in line:
            # Remember this state until the next is found
            state = line
        else:
            # Othewise, we have a city; keep 'state' as last-seen
            universty_towns.append((state, line))

# print(universty_towns[:5])

# Wrap this list to a dataframe
towns_df = pd.DataFrame(universty_towns, columns = ['state', 'RegionName'])
# print(towns_df.head())

def get_cityState(item):
    if ' (' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item

towns_df = towns_df.applymap(get_cityState)

print(towns_df.head())