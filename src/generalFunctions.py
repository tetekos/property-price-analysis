#!/usr/bin/python3

import pandas as pd

def iqr_filter(df, column, number=1.5):
    #med = df[column].median()
    q1 = df[column].quantile(.25)
    q3 = df[column].quantile(.75)
    
    iqr = q3-q1
    
    mask = df[column].between(q1-(number*iqr),q3+(number*iqr), inclusive=True)
    to_keep = df.loc[mask]
    outliers = df.loc[~mask]
    
    #prints
    num_rows_dropped = df.shape[0] - to_keep.shape[0]
    print("Number of rows dropped: " + str(num_rows_dropped))
    
    return to_keep,outliers



def less_iqr_filter(df, column, number=1.5):
    #med = df[column].median()
    q1 = df[column].quantile(.25)
    q3 = df[column].quantile(.75)
    
    iqr = q3-q1
    
    mask = df[column]<q1-(number*iqr)
    to_keep = df.loc[mask]
    
    return to_keep


def more_iqr_filter(df, column, number=1.5):
    #med = df[column].median()
    q1 = df[column].quantile(.25)
    q3 = df[column].quantile(.75)
    
    iqr = q3-q1
    
    mask = df[column]>q3+(number*iqr)
    to_keep = df.loc[mask]
    
    return to_keep