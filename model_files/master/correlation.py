def corr(df, threshold=0.9, strategy=None):
    '''
    Find columns with correlation more then threshold. 
    
    Parameters
    -------------
    df: rectangular dataset
        2D dataset that can be coerced into an ndarray. If a Pandas DataFrame
        is provided, the index/column information will be used to label the
        columns and rows.
    threshold: float, optional
        All columns having more correlation value then threshold will be 
        taken into cosideration.
    strategy: string, optional
        Only two value is accepted ie. None & 'drop'
        If None then set of all the columns having correlation more then
        threshold will be returned.
        If 'drop' then all the columns having correlation more then 
        threshold will be droped from the dataset passed.
        
    Returns
    ------------
    df: rectangular dataset
        df is modified dataset after all the steps are done.
    col_corr: set
        set of all the columns with correlation more than threshold.
    '''
    col_corr = set() # Set of all the names of correlated columns
    corr_matrix = df.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j] > threshold): #we are interest in absolute coeff value
                colname = corr_matrix.columns[i] #getting the name of the column
                col_corr.add(colname)
                    
    if strategy=='drop':
        df = df.drop(col_corr, axis=1)
    return df, col_corr

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ALL METHOD <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def summary():
    '''
                        All methods
    -------------------------------------------------------------
    corr: This method finds correlation of all the columns of a
        dataframe whose value is greater then a threshold value.
    '''
    print(summary.__doc__)