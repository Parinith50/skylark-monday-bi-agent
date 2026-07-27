from monday import fetch_deals, fetch_work_orders
from analyzer import summarize


def answer(question):

    question = question.lower()

    deals = fetch_deals()
    work_orders = fetch_work_orders()

    deal_summary = summarize(deals)
    work_summary = summarize(work_orders)

    response = []

    response.append("📊 Skylark Business Intelligence Report\n")

    # Pipeline Questions
    if any(word in question for word in ["pipeline", "deal", "revenue", "sales"]):

        response.append("Deal Funnel Summary")
        response.append(f"• Total Deals: {deal_summary['rows']}")

        if deal_summary["status_summary"]:
            response.append("\nDeal Status:")
            for status, count in deal_summary["status_summary"].items():
                response.append(f"   - {status}: {count}")

        if deal_summary["sector_summary"]:
            response.append("\nSector Distribution:")
            for sector, count in deal_summary["sector_summary"].items():
                response.append(f"   - {sector}: {count}")

        response.append(
            f"\nMissing Values: {deal_summary['missing_values']}"
        )

    # Work Order Questions
    elif any(word in question for word in ["work", "project", "order"]):

        response.append("Work Order Summary")
        response.append(f"• Total Work Orders: {work_summary['rows']}")

        if work_summary["status_summary"]:
            response.append("\nStatus:")
            for status, count in work_summary["status_summary"].items():
                response.append(f"   - {status}: {count}")

        response.append(
            f"\nMissing Values: {work_summary['missing_values']}"
        )

    # General Questions
    else:

        response.append("Overall Business Overview")

        response.append(f"• Total Deals: {deal_summary['rows']}")
        response.append(f"• Total Work Orders: {work_summary['rows']}")

        response.append(
            f"• Deal Missing Values: {deal_summary['missing_values']}"
        )

        response.append(
            f"• Work Order Missing Values: {work_summary['missing_values']}"
        )

        response.append("\nRecommendations:")

        response.append(
            "- Follow up on deals that are still open."
        )

        response.append(
            "- Complete records with missing information."
        )

        response.append(
            "- Review delayed work orders regularly."
        )

    return "\n".join(response)