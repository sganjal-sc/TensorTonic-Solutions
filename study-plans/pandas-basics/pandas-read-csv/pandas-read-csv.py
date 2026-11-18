import pandas as pd

def create_dataframe(data: dict) -> dict:
    """
    Returns a dictionary with data, shape [rows, columns], and ordered column names.
    """
    columns = list(data.keys())
    
    # Handle the case where the dictionary is empty
    num_cols = len(columns)
    num_rows = len(data[columns[0]]) if num_cols > 0 else 0
    
    return {
        "data": data,
        "shape": [num_rows, num_cols],
        "columns": columns
    }