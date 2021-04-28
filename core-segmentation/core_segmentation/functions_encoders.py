# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:50:51 2021

@author: chris.cirelli
"""
#from CoreSegmentationWheel.__init__ import *
#import logging
#logging.basicConfig(level=logging.INFO)
import pandas as pd
import numpy as np


def encode_cat_features(df, encoder, all_col_names, cat_col_names,
                       float_col_names, int_col_names):
    """
    Function to encode categorical features & transform input before being passed
    to lightgbm model.
    -------------------------------
    df: DataFrame;
        Contains the column names and a single row of input values.
    all_col_names: List;
        List of all column names
    cat_col_names: List;
        List of all categorical column names.
    float_col_names: list;
        List of all float column names.
    -------------------------------
    return:
        Dataframe w/ cat, int, float columns transformed for input into model.
    """

    # Convert Integer Cols to Integers
    for col in int_col_names:
        try:
            df[col] = list(map(lambda x: int(x) if x else None, df[col].values))
        except Exception as error:
            print(f'Encoder error => {error}')

    # Convert Integer Cols to Integers
    for col in float_col_names:
        try:
            df[col] = list(map(lambda x: float(x) if x else None, df[col].values))
        except Exception as error:
            print.error(f'Encoder error => {error}')
    
    # Convert Categorical Columns to Strings
    for col in cat_col_names:
        try:
            df[col] = list(map(lambda x: str(x) if x else None, df[col].values))
        except Exception as error:
            print(f'Encoder error => {error}')

    # Convert Coastal Count to int
    df['CoastalCounty'] = list(map(lambda x: 1 if True else 0, df['CoastalCounty'].values))

    # Encode Categorical Columns
    encoder.handle_unknown='use_encoded_value'           # return np.nan for unknown categorical values.
    encoder.unknown_value=None                           # change made on 04/15/2021               
    cols_encoded = encoder.transform(df[cat_col_names])
    
    # Create DataFrame of Encoded Columns
    df_encoded = pd.DataFrame(cols_encoded, columns=cat_col_names)
    
    # Replace Original Columns w/ Encoded Values
    for col in cat_col_names:
        df[col] = df_encoded[col].values
    
    # Return original dataframe w/ new cols
    return df


def get_segment(yhat):
    # Get Value Within List Object
    yhat_value = yhat

    # If isinstance str convert to float
    if isinstance(yhat, str):
        yhat_value = float(yhat_value)
    
    # Assign segment
    if yhat >= 0.9:
        segment = 'Decline'
    elif yhat < 0.9 and yhat >= 0.65:
        segment = 'Surplus'
    else:
        segment = 'Admitted'
    # Return segment
    return segment


# Blob Storage Log Function
def log2blobstorage(ncollector, list_obj):
    try:
        narray = np.array(list_obj)
        ncollector.collect(narray)
        print(f'{narray} saved to blob storage')
    except Exception as error:
        print(f'Blob storage error => {error}')



