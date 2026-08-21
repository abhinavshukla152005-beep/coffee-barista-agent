# agent.py — Uses free Gemini API key (no billing/GCP needed)
import json
import os
from google.adk.agents import LlmAgent

def get_menu() -> str:
    """Retrieves the coffee shop menu from menu.json.

    Returns:
        str: A JSON string representing the list of menu items.
    """
    try:
        with open("menu.json", "r") as f:
            menu_data = json.load(f)
            return json.dumps(menu_data)
    except Exception as e:
        return json.dumps({"error": f"Could not retrieve menu: {str(e)}"})

# Create the barista agent — uses GOOGLE_API_KEY env var (free AI Studio key)
barista_agent = LlmAgent(
    name="barista_agent",
    model="gemini-2.0-flash",
    instruction="""You are a friendly barista at ☕ Coffee Shop.
Your job is to recommend drinks and pastries to customers based on their preferences.

Rules you MUST follow:
1.  You must recommend items ONLY from the menu returned by get_menu().
2.  Do NOT recommend or suggest any item that is not present in the menu.
3.  If a user's preference is vague or unclear, ask exactly ONE friendly clarifying question to narrow down what they want (e.g., cold or hot, sweet or strong, coffee or pastry).
4.  Be warm and welcoming, but remain professional.
5.  Ground your recommendations in the actual tags, descriptions, and allergens listed in the menu (e.g., if a user is dairy-free, recommend ONLY items tagged 'dairy-free' or with no dairy allergens).
""",
    tools=[get_menu]
)

from google.adk.apps import App

app = App(
    name="coffee_barista_app",
    root_agent=barista_agent
)
