import pandas as pd

def drop_duplicates(data: dict) -> list:
    """
    Returns [rows_before, rows_after, cleaned_data], with integer counts and a dictionary of lists.
    """
    df = pd.DataFrame(data)
    return [len(df), len(df.drop_duplicates()), df.drop_duplicates().to_dict(orient='list')]
