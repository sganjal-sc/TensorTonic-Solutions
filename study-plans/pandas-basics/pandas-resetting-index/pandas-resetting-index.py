import pandas as pd

def reset_index_demo(data: dict, index_col: str) -> list:
    """
    Returns [columns_before_reset, columns_after_reset], both lists of strings.
    """
    df = pd.DataFrame(data)
    df = df.set_index(index_col)
    
    # Returns [columns_before_reset, columns_after_reset], both lists of strings.
    before_reset_cols = df.columns.to_list()
    df = df.reset_index()
    after_reset_cols = df.columns.to_list()
    
    return [before_reset_cols, after_reset_cols]
