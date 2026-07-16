# Wine & Spirits Menu Analyzer (demo)

A throwaway proof-of-concept: a sales rep photographs a drinks menu, a vision model reads it (via the Kilo OpenAI-compatible gateway), we compare it against a William Grant & Sons knowledge base, and return sales intelligence. Streamlit frontend, Python pipeline, one JSON knowledge base — no database, no auth, no persistence; everything runs per-session.

## Run it

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in KILO_BASE_URL / KILO_API_KEY / KILO_MODEL
streamlit run app.py
```
