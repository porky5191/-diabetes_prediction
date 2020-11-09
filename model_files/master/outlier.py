import numpy as np

# ------------------------------- REPLACE ALL WHICH ARE OUT OF 3STD------------------------------
def apply_3std(df, columns, strategy='replace'):
    '''
    This method removes all outliers and replace it with a maximum value 
    ie. 3rd standard deviation value.
    
    Parameters
    --------------------
    df: rectangular dataset
        2D dataset that can be coerced into an ndarray. If a Pandas DataFrame
        is provided, the index/column information will be used to label the
        columns and rows.
    columns: list/set/Series
        List of all the column on which log transformation is to apply
    strategy: replace/remove, optional
        if "replace" then replace the outliers will be replaced with 3rd standard 
        deviation value
        if "remove" then remove all the rows having outliers
        
    Returns
    -------------------
    df: dataset after acting on the outliers
    '''
    for col in columns:
        # find the upper limit
        upper = df[col].mean() + 3* df[col].std()
        # find the lower limit
        lower = df[col].mean() - 3* df[col].std()
        
        if strategy == 'replace':
            df[col] = np.where(df[col]>upper, upper, df[col])
            df[col] = np.where(df[col]<lower, lower, df[col])
        elif strategy == 'remove':
            df.drop(df[df[col] > upper].index, axis=0, inplace=True)
            df.drop(df[df[col] < lower].index, axis=0, inplace=True)
    return df