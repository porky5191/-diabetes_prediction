from scipy.stats import boxcox
from scipy.stats import skew 
import numpy as np


# ----------------------------------CHECK FOR SKEWNESS--------------------------------------
def skewness(df, threshold=0.75):
    '''
    This method finds skewness of the columns. More +ve the value is more right skewed the 
    distribution is. More -ve the value is more left skewed the distribution is.
    
    Parameters
    ------------------
    df: rectangular dataset
        2D dataset that can be coerced into an ndarray. If a Pandas DataFrame
        is provided, the index/column information will be used to label the
        columns and rows.
    threshold: float, optional
        minimum absolute skewness value. All columns having skewness value more than 
        threshold are considered.
        
    Returns
    ------------------
    skewness: pandas.core.series.Series
        returns list of all the columns having skewness more than threshold along with 
        skewness value.
    '''
    skewness = df.apply(lambda z: skew(z.dropna()))
    skewness = skewness[abs(skewness) > threshold]
    return skewness

# --------------------------------LOG TRANSFORMATION-----------------------------------------
def apply_log(df, columns):
    '''
    This method applies log transformation to all the values of the column
    to convert skew distribution into Gaussian distribution.
    
    Parameters
    --------------------
    df: rectangular dataset
        2D dataset that can be coerced into an ndarray. If a Pandas DataFrame
        is provided, the index/column information will be used to label the
        columns and rows.
    columns: list/set/Series
        List of all the column on which log transformation is to apply
        
    Returns
    -------------------
    df: transformed dataset
    '''
    for col in columns:
        if (df[col] == 0).any():
            df[col] = np.log1p(df[col])
        else:
            df[col] = np.log(df[col])
    return df

# ----------------------------------SQUARE ROOT TRANSFORMATION----------------------------------------
def apply_sqrt(df, columns):
    '''
    This method applies square root transformation to all the values of the column
    to convert skew distribution into Gaussian distribution.
    
    Parameters
    --------------------
    df: rectangular dataset
        2D dataset that can be coerced into an ndarray. If a Pandas DataFrame
        is provided, the index/column information will be used to label the
        columns and rows.
    columns: list/set/Series
        List of all the column on which log transformation is to apply
        
    Returns
    -------------------
    df: transformed dataset
    '''
    for col in columns:
        df[col] = df[col]**(0.5)
    return df

# --------------------------------RECIPROCAL TRANSFORMATION--------------------------
def apply_reciprocal(df, columns):
    '''
    This method applies reciprocal transformation to all the values of the column
    to convert skew distribution into Gaussian distribution.
    
    Parameters
    --------------------
    df: rectangular dataset
        2D dataset that can be coerced into an ndarray. If a Pandas DataFrame
        is provided, the index/column information will be used to label the
        columns and rows.
    columns: list/set/Series
        List of all the column on which log transformation is to apply
        
    Returns
    -------------------
    df: transformed dataset
    '''
    for col in columns:
        if (df[col] == 0).any():
            df[col] = 1/(df[col]+1)
        else:
            df[col] = 1/df[col]
    return df

# ---------------------------------------BOXCOX TRANSFORMATION--------------------------------
def apply_boxcox(df, columns):
    '''
    This method applies BoxCox transformation to all the values of the column
    to convert skew distribution into Gaussian distribution.
    
    Parameters
    --------------------
    df: rectangular dataset
        2D dataset that can be coerced into an ndarray. If a Pandas DataFrame
        is provided, the index/column information will be used to label the
        columns and rows.
    columns: list/set/Series
        List of all the column on which log transformation is to apply
        
    Returns
    -------------------
    df: transformed dataset
    '''
    for col in columns:
        df[col], lmbda = boxcox(df[col], lmbda=None)