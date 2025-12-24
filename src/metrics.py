import numpy as np

def add_conversion_rate(df):
    df = df.copy()

    df['conversion_rate'] = (
        df['# of Purchase'] / df['# of Website Clicks']
    )

    # Replace inf, -inf with NaN
    df['conversion_rate'].replace([np.inf, -np.inf], np.nan, inplace=True)

    # Drop invalid rows
    df.dropna(subset=['conversion_rate'], inplace=True)

    return df
