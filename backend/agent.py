from monday import fetch_deals, fetch_work_orders
from analyzer import summarize


def answer(question):

    question = question.lower()

    deals = fetch_deals()
    work_orders = fetch_work_orders()

    deal_summary = summarize(deals)
    work_summary = summarize(work_orders)

    response = []

    response.append("📊 Skylark Business Intelligence Report")
    response.append("=" * 40)

    # -----------------------------
    # PIPELINE QUESTIONS
    # -----------------------------
    if any(word in question for word in ["pipeline", "deal", "sales", "revenue"]):

        response.append("")
        response.append("📈 Deal Funnel Summary")
        response.append(f"Total Deals: {deal_summary['rows']}")

        response.append("")
        response.append("Deal Status")

        for status, count in deal_summary["status_summary"].items():
            response.append(f"• {status}: {count}")

        if deal_summary["sector_summary"]:

            response.append("")
            response.append("Sector Distribution")

            for sector, count in deal_summary["sector_summary"].items():
                response.append(f"• {sector}: {count}")

        response.append("")
        response.append(f"Missing Values: {deal_summary['missing_values']}")

        response.append("")
        response.append("Recommendations")

        open_deals = deal_summary["status_summary"].get("Open", 0)
        dead_deals = deal_summary["status_summary"].get("Dead", 0)

        if open_deals > 30:
            response.append(
                "• Large number of open deals. Prioritize sales follow-ups."
            )

        if dead_deals > 100:
            response.append(
                "• High number of lost deals. Review reasons for deal failures."
            )

        if deal_summary["missing_values"] > 0:
            response.append(
                "• Improve data quality by completing missing records."
            )

    # -----------------------------
    # WORK ORDER QUESTIONS
    # -----------------------------
    elif any(word in question for word in ["work", "order", "project"]):

        response.append("")
        response.append("🛠 Work Order Summary")
        response.append(f"Total Work Orders: {work_summary['rows']}")

        response.append("")
        response.append("Status")

        for status, count in work_summary["status_summary"].items():
            response.append(f"• {status}: {count}")

        response.append("")
        response.append(f"Missing Values: {work_summary['missing_values']}")

        response.append("")
        response.append("Recommendations")

        if work_summary["missing_values"] > 0:
            response.append(
                "• Fill incomplete work-order records."
            )
        else:
            response.append(
                "• Work-order data quality looks good."
            )

    # -----------------------------
    # SECTOR QUESTIONS
    # -----------------------------
    elif "sector" in question:

        response.append("")
        response.append("📊 Pipeline by Sector")

        for sector, count in deal_summary["sector_summary"].items():
            response.append(f"• {sector}: {count}")

    # -----------------------------
    # OPEN DEALS
    # -----------------------------
    elif "open" in question and "deal" in question:

        open_deals = deal_summary["status_summary"].get("Open", 0)

        response.append("")
        response.append(f"There are currently {open_deals} open deals.")

    # -----------------------------
    # OVERALL BUSINESS SUMMARY
    # -----------------------------
    else:

        response.append("")
        response.append("Overall Business Summary")

        response.append(f"Total Deals: {deal_summary['rows']}")
        response.append(f"Total Work Orders: {work_summary['rows']}")

        response.append("")
        response.append("Cross-board Insights")

        open_deals = deal_summary["status_summary"].get("Open", 0)

        active_work_orders = (
            work_summary["status_summary"].get("In Progress", 0)
            + work_summary["status_summary"].get("Working", 0)
            + work_summary["status_summary"].get("Open", 0)
        )

        response.append(f"Open Deals: {open_deals}")
        response.append(f"Active Work Orders: {active_work_orders}")

        if open_deals > active_work_orders:

            response.append(
                "Insight: Sales pipeline is growing faster than execution capacity."
            )

        else:

            response.append(
                "Insight: Operational capacity appears sufficient for the current sales pipeline."
            )

        response.append("")
        response.append("Leadership Recommendations")

        if open_deals > 30:
            response.append(
                "• Prioritize conversion of open deals."
            )

        dead_deals = deal_summary["status_summary"].get("Dead", 0)

        if dead_deals > 100:
            response.append(
                "• Analyze why deals are being lost."
            )

        if deal_summary["missing_values"] > 0 or work_summary["missing_values"] > 0:
            response.append(
                "• Improve data quality before leadership reviews."
            )

    return "\n".join(response)