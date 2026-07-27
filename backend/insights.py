def pipeline_summary(deals):
    status = deals.get("status_summary", {})

    response = []
    response.append("📈 PIPELINE SUMMARY")
    response.append("=" * 40)
    response.append(f"Total Deals: {deals['rows']}")
    response.append("")

    response.append("Deal Status")
    for key, value in status.items():
        response.append(f"• {key}: {value}")

    response.append("")
    response.append("Recommendations")

    if status.get("Open", 0) > 40:
        response.append("• Prioritize follow-up on open deals.")

    if status.get("Dead", 0) > 100:
        response.append("• Review reasons for lost deals.")

    return "\n".join(response)


def sector_summary(deals):
    sectors = deals.get("sector_summary", {})

    response = []
    response.append("🏭 SECTOR ANALYSIS")
    response.append("=" * 40)

    if not sectors:
        response.append("No sector information available.")
    else:
        for sector, count in sorted(
            sectors.items(),
            key=lambda x: x[1],
            reverse=True,
        ):
            response.append(f"• {sector}: {count}")

    return "\n".join(response)


def leadership_update(deals, work):
    response = []

    response.append("📊 LEADERSHIP UPDATE")
    response.append("=" * 40)

    response.append(f"Total Deals: {deals['rows']}")
    response.append(f"Total Work Orders: {work['rows']}")

    status = deals.get("status_summary", {})

    response.append("")
    response.append(f"Open Deals: {status.get('Open', 0)}")
    response.append(f"Won Deals: {status.get('Won', 0)}")
    response.append(f"Dead Deals: {status.get('Dead', 0)}")

    response.append("")
    response.append("Recommendations")

    response.append("• Focus on converting open deals.")
    response.append("• Review lost opportunities.")
    response.append("• Monitor execution capacity.")

    return "\n".join(response)


def business_risks(deals):
    status = deals.get("status_summary", {})

    response = []

    response.append("⚠️ BUSINESS RISKS")
    response.append("=" * 40)

    dead = status.get("Dead", 0)
    open_ = status.get("Open", 0)

    if dead > 100:
        response.append(f"• High number of lost deals ({dead}).")

    if open_ > 40:
        response.append(f"• Large number of open deals ({open_}).")

    if dead == 0 and open_ == 0:
        response.append("No major risks detected.")

    return "\n".join(response)


def overall_summary(deals, work):
    response = []

    response.append("📊 OVERALL BUSINESS SUMMARY")
    response.append("=" * 40)

    response.append("")
    response.append("Sales")
    response.append(f"• Total Deals: {deals['rows']}")

    status = deals.get("status_summary", {})

    response.append(f"• Won: {status.get('Won', 0)}")
    response.append(f"• Open: {status.get('Open', 0)}")
    response.append(f"• Dead: {status.get('Dead', 0)}")

    response.append("")
    response.append("Operations")
    response.append(f"• Total Work Orders: {work['rows']}")

    response.append("")
    response.append("Top Sectors")

    sectors = deals.get("sector_summary", {})

    if sectors:
        top = sorted(
            sectors.items(),
            key=lambda x: x[1],
            reverse=True
        )[:3]

        for sector, count in top:
            response.append(f"• {sector}: {count}")

    response.append("")
    response.append("Recommendations")
    response.append("• Improve sales conversion.")
    response.append("• Reduce lost deals.")
    response.append("• Monitor operational workload.")

    return "\n".join(response)