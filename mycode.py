import pandas as pd
import os


data = {'Name':['Alice','Rob','Charlie'],
        'Age': [25,30,35],
        'City': ['New York','Los Angeles','Chicago']
}

df = pd.DataFrame(data)


# Adding new row to df for V2
new_row = {'Name':'Riya','Age':22,'City':'Mumbai'}
df.loc[len(df.index)] = new_row

# Adding new row to df for V3
new_row_2 = {'Name':'Tina','Age':80,'City':'Bangalore'}
df.loc[len(df.index)] = new_row_2

data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"csv file saved to {file_path}")