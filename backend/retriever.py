import pandas as pd


def retrieve_relevant_data(question, deals_df, work_df):

    question = question.lower()

    deals = deals_df.copy()
    work = work_df.copy()

    # ------------------------------
    # Deal Status
    # ------------------------------

    if "open" in question:

        for col in deals.columns:
            if "status" in col.lower():
                deals = deals[
                    deals[col]
                    .astype(str)
                    .str.lower()
                    .str.contains("open", na=False)
                ]
                break

    elif "won" in question:

        for col in deals.columns:
            if "status" in col.lower():
                deals = deals[
                    deals[col]
                    .astype(str)
                    .str.lower()
                    .str.contains("won", na=False)
                ]
                break

    elif "dead" in question:

        for col in deals.columns:
            if "status" in col.lower():
                deals = deals[
                    deals[col]
                    .astype(str)
                    .str.lower()
                    .str.contains("dead", na=False)
                ]
                break

    # ------------------------------
    # Sector Search
    # ------------------------------

    sectors = [
        "renewables",
        "mining",
        "railways",
        "aviation",
        "construction",
        "manufacturing",
        "powerline",
        "security",
        "tender",
        "dsp"
    ]

    for sector in sectors:

        if sector in question:

            for col in deals.columns:

                if "sector" in col.lower():

                    deals = deals[
                        deals[col]
                        .astype(str)
                        .str.lower()
                        .str.contains(sector, na=False)
                    ]

                    break

    # ------------------------------
    # Client Search
    # ------------------------------

    for word in question.split():

        if len(word) < 4:
            continue

        if "deal" in deals.columns:

            matches = deals[
                deals["Deal"]
                .astype(str)
                .str.lower()
                .str.contains(word, na=False)
            ]

            if len(matches) > 0:
                deals = matches
                break

    return (
        deals.head(30),
        work.head(30)
    )