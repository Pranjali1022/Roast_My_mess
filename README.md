# Roast My Mess — IIT KGP 🔥
**AI Campus Companion built with Streamlit + Claude API**

---

## Setup & Run

### 1. Install dependencies
```bash
pip install streamlit anthropic
```

### 2. Set your API key
```bash
# Mac/Linux
export ANTHROPIC_API_KEY="sk-ant-..."

# Windows (Command Prompt)
set ANTHROPIC_API_KEY=sk-ant-...

# Or create a .env file (if using python-dotenv)
echo ANTHROPIC_API_KEY=sk-ant-... > .env
```

### 3. Run the app
```bash
streamlit run app.py
```
App opens automatically at `http://localhost:8501`

---

## File Structure
```
roast_my_mess/
├── app.py        ← Main Streamlit app (UI + API calls)
├── data.py       ← All static data, prompts, sample content
└── README.md     ← This file
```

---

## How it works

| Component | What it does |
|-----------|-------------|
| `st.tabs()` | 3-tab navigation (Roast / Feed / Authority) |
| `st.session_state` | Persists roast results and community posts across reruns |
| `anthropic.Anthropic()` | API client — reads key from environment automatically |
| `st.spinner()` | Loading indicator while Claude generates the roast |
| `st.download_button()` | Lets users save roasts and authority reports |
| `st.metric()` | KPI cards on the authority dashboard |
| `st.bar_chart()` | Hall complaint volume chart |
| `st.progress()` | Complaint bars on authority dashboard |

---

## Tone modes

| Tone | Style | System prompt focus |
|------|-------|---------------------|
| Savage | Brutal, punchy, shareable | Indian English slang, 4-5 lines, harsh rating |
| Mild | Friendly disappointment | Sympathetic but honest, relatable |
| Poetic Tragedy | Shakespearean drama | Flowery metaphors, funny tragedy |
| IIT Jhola Guy | Intellectual + campus refs | Physics/algo metaphors, Hindi-English mix |

---

## Pitch alignment (Zupee assessment)

| Requirement | Implementation |
|-------------|---------------|
| Usable prototype | Full working Streamlit app with live AI |
| TAM | 40M students; IIT KGP 23K as launch campus |
| Why adopt | Daily mess = daily trigger; every roast = shareable meme |
| Growth | Meme cards → WhatsApp; campus ambassador; "Mess of Shame" |
| Authority hook | Dashboard tab with complaint data + downloadable report |
| Failure mitigations | Food-only roasting, authority dashboard, community moderation |
