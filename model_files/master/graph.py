import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import pylab
import math
import numpy as np

# -------------------------------------TO PLOT HISTOGRAM------------------------------------------
def plot_hist(df, columns, figuresize=(10, 10), bins=40, color='blue'):
    '''
    Plot histogram for all the columns provided using
    matplotlib
    
    Parameters
    -------------
    df: rectangular dataset
        2D dataset that can be coerced into an ndarray. If a Pandas DataFrame
        is provided, the index/column information will be used to label the
        columns and rows.
    columns: list/set/tuple
        list of all the colum names. It must be an iterable like list, set, 
        touple etc
    figsize: tuple, optional
        size of the figure to be plot. value should be passed in tuple. 
        figuresize=(width, height).
    bins:Int, optional 
        what is the size of each bar. By default it is 40.
    color: string, optional
        specify the color of the graph. eg 'red', 'green', 'darkred', 'darkgreen' etc.
    
    Returns
    ----------
    None: This method returns None.
    '''
    # fix the figure size
    plt.figure(figsize=figuresize)
    
    # find how many rows 
    # no1 = len(columns)/2
    # no2 = len(columns)//2
    # no = no2 if no1==no2 else no2+1
    no = math.ceil(len(columns)/2)
   
    # for each column plot a graph in the figure
    for index, col in enumerate(columns):
        plt.subplot(no, 2, index+1)
        plt.hist(x=col, data=df, color=color, bins=bins)
        plt.title(col)
    plt.show()

# ----------------------------------------TO PLOT DISTPLOT---------------------------------------------
def plot_dist(df, columns, figuresize=(10, 10), bins=40, color='blue'):
    '''
    This method plots the distplot for all the columns provided using seaborn.
    
    Parameters
    --------------
    df: rectangular dataset
        2D dataset that can be coerced into an ndarray. If a Pandas DataFrame
        is provided, the index/column information will be used to label the
        columns and rows.
    columns: list/set/tuple
        list of all the colum names. It must be an iterable like list, set, 
        touple etc
    figuresize: tuple, optional
        size of the figure to be plot. value should be passed in tuple. 
        figuresize=(width, height).
    bins: Int, optional
        size of each bar. By default it is 40.
    color: string, optional
        color of each bar. eg. 'red', 'green', 'darkred', 'darkgreen' etc
    
    Returns
    --------------
       This method returns None.
    '''
    # fix the figure size
    plt.figure(figsize=figuresize)
    
    # find how many rows 
    # no1 = len(columns)/2
    # no2 = len(columns)//2
    # no = no2 if no1==no2 else no2+1
    no = math.ceil(len(columns)/2)
   
    # for each column plot a graph in the figure
    for index, col in enumerate(columns):
        plt.subplot(no, 2, index+1)
        sns.distplot(df[col], color=color, bins=bins)

# --------------------------------------------TO PLOT BOXPLOT------------------------------------------
def plot_box(df, columns, figuresize=(10, 10)):
    '''
    This method plots the boxplot for all the columns provided.
    
    Parameters
    -------------
    df: rectangular dataset
        2D dataset that can be coerced into an ndarray. If a Pandas DataFrame
        is provided, the index/column information will be used to label the
        columns and rows.
    columns: list/set/tuple
        list of all the colum names. It must be an iterable like list, set, 
        touple etc
    figuresize: tuple, optional
        size of the figure to be plot. value should be passed in tuple. 
        figuresize=(width, height).
    
    Returns
    -------------
    None: This method returns None.
    '''
    # fix the figure size
    plt.figure(figsize=figuresize)
    
    # find how many rows 
    # no1 = len(columns)/2
    # no2 = len(columns)//2
    # no = no2 if no1==no2 else no2+1
    no = math.ceil(len(columns)/2)
   
    # for each column plot a graph in the figure
    for index, col in enumerate(columns):
        plt.subplot(no, 2, index+1)
        plt.boxplot(x=col, data=df)
        plt.title(col)
    plt.show()

# ----------------------------------------PLOT QQ GRAPH---------------------------------------------
def plot_QQ(df, columns, figuresize=(10, 20), color='blue', bins=40):
    '''
    Plots QQ graph for all the columns provided.
    
    QQ graph is used to check the distribution of the columns, whether it is
    in Gaussian or not. More the blue points are align with the straight red
    line more Gaussian the distribution is else not.
    
    Parameters
    --------------
    df: rectangular dataset
        2D dataset that can be coerced into an ndarray. If a Pandas DataFrame
        is provided, the index/column information will be used to label the
        columns and rows.
    columns: list/set/tuple
        list of all the colum names. It must be an iterable like list, set, 
        touple etc
    figuresize: tuple, optional
        size of the figure to be plot. value should be passed in tuple. 
        figuresize=(width, height).
    color: string, optional
        color of the histogram of each column.
    bins: int, optional
        size of each histogram bar.
    
    Return
       This method returns None.
    '''
    # fix the figure size
    plt.figure(figsize=figuresize)
    
    # find how many rows 
    no = len(columns)
   
    # for each column plot a graph in the figure
    count = 1
    for index, col in enumerate(columns):
        plt.subplot(no, 2, count)
        plt.hist(x=col, data=df, color=color, bins=bins)
        plt.title(col)
        plt.subplot(no, 2, count+1)
        stats.probplot(df[col], dist='norm', plot=pylab)
        count = count + 2
        
    plt.show()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ALL METHOD <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def summary():
    '''
                        All methods
    -------------------------------------------------------------
    plot_hist: This method plots histplot using matplotlib
    plot_dist: This method plots distplot using seaborn
    plot_box: This method plots box plot using dataframe's inbuild
        method.
    plot_QQ: This method plots QQ curve using scipy
    '''
    print(summary.__doc__)