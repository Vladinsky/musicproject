import pandas as pd

# Create a dictionary to map the values to integers
def map_effects(effect,effects):
    if effect == effects[0]:
        return 2
    elif effect == effects[1]:
        return 1
    elif effect == effects[2]:
        return 0
    else:
        return 


# Function to load and clean the data
def load_and_clean_data(file_path) -> pd.DataFrame:
    # Load the data
    df = pd.read_csv(file_path)
    
    # Substitute NaN with the mean value in the numerical columns
    df.fillna({col: df[col].mean() for col in df.select_dtypes(include=['number']).columns}, inplace=True)

    # Substitute NaN with the mode value in the object columns
    df.fillna({col: df[col].mode()[0] for col in df.select_dtypes(include=['object']).columns}, inplace=True)

    effects = df['Music effects'].value_counts().index

    # Create a new column with the mapped values
    df['Music effects enc'] = df['Music effects'].map(lambda effect : map_effects(effect,effects))


    return df