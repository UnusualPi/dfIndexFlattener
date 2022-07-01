def dfFlatIndex(df, resetIndex=True, sep='.'):
    """
    |--------------------------------------------------------------------
    | Requires Pandas MultiIndex DataFrame
    |
    | Parameters
    |--------------------------------------------------------------------
    | resetIndex : bool, default True
    |   Give the option to return a dataframe with or without an index
    |   True resets index
    | sep : str, default '.'
    |   When combining the indicies determines the separator
    """
    df.columns([f'{i}{sep}{j}' for i,j in df.columns])
    df.reset_index(inplace=resetIndex)
    return df
