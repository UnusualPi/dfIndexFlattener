def dfFlatIndex(df, resetIndex=True, sep='.', inplace=False):
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
    df = df.copy(deep=True) if inplace==False else df
    df.reset_index(inplace=resetIndex)
    cols = []
    for i,j in df.columns:
        cols.append(f'{i}{sep}{j}' if j != '' else f'{i}')
    df.columns = df.columns.to_flat_index()
    df.columns = cols
    return df
