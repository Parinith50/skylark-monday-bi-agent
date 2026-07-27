import json
import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


SYSTEM_PROMPT = """
You are Skylark Drones' Internal AI Business Intelligence Assistant.

You have access to two Monday.com boards:

1. Deal Funnel
2. Work Orders

You also receive Python-generated analytics.

Your responsibilities:

- Answer naturally.
- Never invent numbers.
- Use ONLY the supplied data.
- Explain trends.
- Explain business implications.
- Recommend actions.
- Think like a CEO dashboard.
- If information isn't available, clearly state that.

When answering:

• Start with a short executive summary.
• Then explain the findings.
• End with actionable recommendations.

Keep responses professional and concise.
"""


def ask_llm(question, analytics, deals_df, work_df):

    deals = deals_df.to_dict(orient="records")
    work = work_df.to_dict(orient="records")

    prompt = f"""
{SYSTEM_PROMPT}

==============================
USER QUESTION
==============================

{question}

==============================
BUSINESS ANALYTICS
==============================

{json.dumps(analytics, indent=2)}

==============================
RELEVANT DEALS
==============================

{json.dumps(deals, indent=2)}

==============================
RELEVANT WORK ORDERS
==============================

{json.dumps(work, indent=2)}

Answer using ONLY the supplied information.
Do NOT invent values.
"""

    response = model.generate_content(prompt)

    return response.text