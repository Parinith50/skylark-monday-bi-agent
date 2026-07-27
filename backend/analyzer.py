import pandas as pd


def summarize(df: pd.DataFrame):

    summary = {
        "rows": len(df),
        "missing_values": int(df.isna().sum().sum())
    }

    # ---------- Deal Status ----------
    status_col = None

    for col in df.columns:
        if "status" in col.lower():
            status_col = col
            break

    if status_col:
        summary["status_summary"] = (
            df[status_col]
            .replace("", "Unknown")
            .fillna("Unknown")
            .value_counts()
            .to_dict()
        )
    else:
        summary["status_summary"] = {}

    # ---------- Sector ----------
    sector_col = None

    for col in df.columns:
        if "sector" in col.lower():
            sector_col = col
            break

    if sector_col:
        summary["sector_summary"] = (
            df[sector_col]
            .replace("", "Unknown")
            .fillna("Unknown")
            .value_counts()
            .to_dict()
        )
    else:
        summary["sector_summary"] = {}

    # ---------- Deal Value ----------
    value_col = None

    for col in df.columns:
        if "value" in col.lower():
            value_col = col
            break

    if value_col:

        values = (
            df[value_col]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("$", "", regex=False)
        )

        values = pd.to_numeric(values, errors="coerce")

        summary["total_pipeline_value"] = float(values.sum())
        summary["average_deal_value"] = float(values.mean())

    else:

        summary["total_pipeline_value"] = 0
        summary["average_deal_value"] = 0

    return summary