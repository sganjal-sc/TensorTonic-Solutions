import pandas as pd

def inspect_dataframe(data: dict) -> dict:
    """
    Returns rows, cols, columns, dtypes, and total_values in a dictionary.
    """
    # Create the DataFrame
    df = pd.DataFrame(data)
    
    # Extract inspection metadata
    return {
        
        "rows": df.shape[0],
        "cols": df.shape[1],
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "total_values": df.size
    }