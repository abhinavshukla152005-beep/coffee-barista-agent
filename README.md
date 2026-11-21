# Coffee Barista Agent

A coffee-shop agent that is only allowed to talk about the menu it was given. Ask for something
vague ("I want something cold and sweet") and it asks exactly one clarifying question. Ask for a
drink that does not exist and it says so instead of inventing one.

Built on **Google ADK** with Gemini (`gemini-2.0-flash`, AI Studio key, no billing) and a
**Streamlit** chat UI.

## Run it

```bash
pip install -r requirements.txt
export GOOGLE_API_KEY=<your AI Studio key>
streamlit run app.py
```

## How it stays inside the menu

`agent.py` defines an `LlmAgent` whose only tool, `get_menu()`, reads `menu.json`. The instruction
tells the model to recommend only items that call returns, and to ask one narrowing question —
cold or hot, sweet or strong, coffee or pastry — before recommending anything.

## Files

| File | Purpose |
| --- | --- |
| `agent.py` | ADK agent, instruction and the `get_menu` tool |
| `app.py` | Streamlit chat UI driving the agent through `InMemoryRunner` |
| `menu.json` | The menu, and the only source of recommendations |
