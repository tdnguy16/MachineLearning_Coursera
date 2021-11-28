import pandas as pd

data = {'x0':[1,1,1,1],'x1':[2104,1416,1534,852],'x2':[5,3,3,2],'x3':[1,2,2,1],'x4':[45,40,30,36],'y':[460,232,315,178]}
df = pd.DataFrame(data)
print(df)

x = df[['x0','x1','x2','x3','x4']].to_numpy()
print(x)

y = df['y'].to_numpy()
print(y)