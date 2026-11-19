import pandas as pd

def set_index_column(data: dict, index_col: str) -> dict:
    """
    Returns index_values and columns as lists, plus data as a dictionary of lists.
    """
    df = pd.DataFrame(data)
    df = df.set_index(index_col)
    
    return {
        "index_values" : df.index.to_list(),
        "columns" : df.columns.to_list(),
        "data" : df.to_dict(orient='list')
    }
