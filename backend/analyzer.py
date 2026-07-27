import pandas as pd


def summarize(df: pd.DataFrame):

    df = df.copy()

    # Count missing values BEFORE filling
    missing_values = int(df.isna().sum().sum())

    # Replace NaN
    df = df.fillna("Unknown")

    status_summary = {}
    sector_summary = {}

    status_col = None
    sector_col = None

    # Detect status & sector columns automatically
    for col in df.columns:

        lower = col.lower()

        if "status" in lower and status_col is None:
            status_col = col

        if "sector" in lower and sector_col is None:
            sector_col = col

    # ---------------- STATUS ---------------- #

    if status_col:

        invalid = [
            "",
            "Unknown",
            "Status",
            "Deal Status",
            "status"
        ]

        status_summary = (
            df[status_col]
            .replace(invalid, pd.NA)
            .dropna()
            .value_counts()
            .to_dict()
        )

    # ---------------- SECTOR ---------------- #

    if sector_col:

        invalid = [
            "",
            "Unknown",
            "Sector",
            "Sector/service"
        ]

        sector_summary = (
            df[sector_col]
            .replace(invalid, pd.NA)
            .dropna()
            .value_counts()
            .to_dict()
        )

    rows = len(df)

    # ---------- Top Status ----------

    top_status = None

    if status_summary:
        top_status = max(status_summary, key=status_summary.get)

    # ---------- Top Sector ----------

    top_sector = None

    if sector_summary:
        top_sector = max(sector_summary, key=sector_summary.get)

    # ---------- Pipeline Health ----------

    won = status_summary.get("Won", 0)
    dead = status_summary.get("Dead", 0)
    open_deals = status_summary.get("Open", 0)

    conversion_rate = 0

    if rows > 0:
        conversion_rate = round((won / rows) * 100, 2)

    pipeline_health = "Healthy"

    if dead > won:
        pipeline_health = "Needs Attention"

    elif open_deals > won:
        pipeline_health = "Growing"

    return {

        "rows": rows,

        "status_summary": status_summary,

        "sector_summary": sector_summary,

        "missing_values": missing_values,

        "top_sector": top_sector,

        "top_status": top_status,

        "won": won,

        "dead": dead,

        "open": open_deals,

        "conversion_rate": conversion_rate,

        "pipeline_health": pipeline_health
    }