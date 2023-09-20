import pandas as pd

states = ['California', 'Texas', 'Florida', 'New York']
population = [1234456765432, 6738246971, 1637281698, 1268164]
dict_states = {'States': states, 'Population': population}
df_states = pd.DataFrame.from_dict(dict_states)
# print(df_states)
# index= False to get rid of indexes formatting
df_states.to_csv('States.csv', index=False)