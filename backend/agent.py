from monday import fetch_deals, fetch_work_orders
from analyzer import summarize

from insights import (
    pipeline_summary,
    sector_summary,
    leadership_update,
    business_risks,
    overall_summary,
)


def detect_intent(question: str) -> str:

    question = question.lower()

    # Leadership
    if any(word in question for word in [
        "leadership",
        "executive",
        "ceo",
        "management",
        "board",
        "weekly update",
        "overall",
        "summary",
        "business",
    ]):
        return "leadership"

    # Sector
    elif any(word in question for word in [
        "sector",
        "industry",
        "renewables",
        "mining",
        "railways",
        "aviation",
        "construction",
        "manufacturing",
    ]):
        return "sector"

    # Risks
    elif any(word in question for word in [
        "risk",
        "risks",
        "problem",
        "problems",
        "issue",
        "issues",
        "warning",
        "concern",
    ]):
        return "risk"

    # Pipeline
    elif any(word in question for word in [
        "pipeline",
        "deal",
        "deals",
        "sales",
        "revenue",
        "conversion",
        "won",
        "dead",
        "open",
    ]):
        return "pipeline"

    # Default
    return "overall"


def answer(question: str):

    # Fetch Monday boards
    deals_df = fetch_deals()
    work_df = fetch_work_orders()

    # Analyze separately
    deal_summary = summarize(deals_df)
    work_summary = summarize(work_df)

    # Detect intent
    intent = detect_intent(question)

    # Route request
    if intent == "pipeline":
        return pipeline_summary(deal_summary)

    elif intent == "sector":
        return sector_summary(deal_summary)

    elif intent == "leadership":
        return leadership_update(
            deal_summary,
            work_summary
        )

    elif intent == "risk":
        return business_risks(deal_summary)

    else:
        return overall_summary(
            deal_summary,
            work_summary
        )