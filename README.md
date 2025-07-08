# 🏏 CoachBot - Your Daily Bowling Assistant

CoachBot is an AI-powered assistant built to help cricket bowlers plan their daily training based on how they performed yesterday.

It reads simple performance logs — like pace, workload, and video accuracy — and generates a focused plan for the day: drills, rest tips, goals, and warnings if needed.

It also works like a mini coach. You can ask it follow-up questions like:
> “Why this drill today?”  
> “How to improve yorker accuracy with pace?”

---

## 🤔 Why I Built This

I’ve seen how repetitive and vague bowling training can get. Sometimes you overtrain, sometimes you don’t know what to focus on next. What if there was an assistant that:
- Read your logs from yesterday
- Gave a plan you can trust
- Let you ask questions like a real coach

So I built **CoachBot**.

---

## 🧠 How It Works

1. **Input Yesterday’s Log:**
   - Pace (e.g., 128 km/h)
   - Balls Bowled (e.g., 110)
   - Load Rating (1–10)
   - Video Accuracy (%)
   - Focus Goal (like consistency or yorkers)

2. **AI Reasoning (via Gemini Pro):**
   - Generates a training plan (goal, drills, rest tip, mindset)

3. **Hardcoded Warnings:**
   - If load is too high or accuracy is low, it shows a caution

4. **Conversational Mode:**
   - You can chat with CoachBot for follow-ups
   - It remembers the session like a real assistant

---

## 🚀 Run Locally

### Requirements
- Python 3.8+
- Streamlit
- Google Generative AI (Gemini) SDK

### Setup

```bash
pip install streamlit google-generativeai
