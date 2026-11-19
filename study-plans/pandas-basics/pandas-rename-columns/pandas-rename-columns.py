import pandas as pd

def rename_columns(data: dict, rename_map: dict) -> dict:
    """
    Returns a dictionary mapping renamed column names to their value lists.
    """
    df =pd.DataFrame(data)
    return df.rename(columns=rename_map).to_dict(orient='list')
