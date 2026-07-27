import pandas as pd


def clean_dataframe(df: pd.DataFrame):

    # Replace empty values
    df = df.replace(
        ["", " ", "N/A", "NA", "NULL", "-", None],
        pd.NA
    )

    # Remove leading/trailing spaces
    df = df.apply(
        lambda col: col.str.strip()
        if col.dtype == "object"
        else col
    )

    return df