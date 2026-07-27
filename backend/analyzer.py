import pandas as pd


def summarize(df: pd.DataFrame):

    df = df.copy()

    df = df.fillna("Unknown")

    status_summary = {}
    sector_summary = {}

    # ---------- STATUS ----------
    status_col = None

    for col in df.columns:
        if "status" in col.lower():
            status_col = col
            break

    if status_col:

        invalid = [
            "",
            "Status",
            "Deal Status",
            "Unknown",
            "status"
        ]

        status_summary = (
            df[status_col]
            .replace(invalid, pd.NA)
            .dropna()
            .value_counts()
            .to_dict()
        )

    # ---------- SECTOR ----------
    sector_col = None

    for col in df.columns:
        if "sector" in col.lower():
            sector_col = col
            break

    if sector_col:

        invalid = [
            "",
            "Sector",
            "Sector/service",
            "Unknown"
        ]

        sector_summary = (
            df[sector_col]
            .replace(invalid, pd.NA)
            .dropna()
            .value_counts()
            .to_dict()
        )

    return {

        "rows": len(df),

        "status_summary": status_summary,

        "sector_summary": sector_summary,

        "missing_values": int(df.isna().sum().sum())
    }