import streamlit as st
import google.generativeai as genai

# Set your Gemini API key
genai.configure(api_key="AIzaSyB1Afqs85_MAT63hdVGy4qrHbfJf4rn794")

# Function to build prompt and warnings
def create_prompt(log):
    warnings = []
    try:
        if int(log['Load Rating']) > 8:
            warnings.append("⚠️ High load yesterday. Reduce today's intensity.")
        if int(log['Balls Bowled']) > 120:
            warnings.append("⚠️ High volume. Watch out for shoulder fatigue.")
        if int(log['Video Accuracy'].replace('%', '')) < 60:
            warnings.append("⚠️ Low video accuracy. Focus on consistency.")
    except Exception as e:
        warnings.append("⚠️ Error in warning logic: " + str(e))

    prompt = f"""
You are CoachBot, a cricket bowling assistant. Based on this training log:

Pace: {log['Pace']}  
Balls Bowled: {log['Balls Bowled']}  
Load Rating: {log['Load Rating']}  
Video Accuracy: {log['Video Accuracy']}  
Focus Goal: {log['Focus Goal']}

Generate today’s plan:
- Goal for the day
- Rest Advice
- Drills (3 max)
- Warning if needed
- Coaching Note or Mindset Tip

Output in bullet points.
"""
    return prompt, warnings

# Streamlit page config
st.set_page_config(page_title="🏏 CoachBot - Bowling Assistant")
st.title("🏏 CoachBot - AI Daily Bowling Planner")

# Training log input form
with st.form("training_log_form"):
    pace = st.text_input("Pace (e.g., 128 km/h)", "130 km/h")
    balls = st.text_input("Balls Bowled", "100")
    load = st.text_input("Load Rating (1-10)", "7")
    accuracy = st.text_input("Video Accuracy (%)", "85%")
    goal = st.text_input("Focus Goal (e.g., consistency)", "accuracy in yorkers")
    submitted = st.form_submit_button("Generate Plan")

# After form is submitted
if submitted:
    log = {
        "Pace": pace,
        "Balls Bowled": balls,
        "Load Rating": load,
        "Video Accuracy": accuracy,
        "Focus Goal": goal
    }

    prompt, warnings = create_prompt(log)

    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt)

    st.subheader("📋 Today's Training Plan")
    st.markdown(response.text)

    if warnings:
        st.subheader("⚠️ Physical Load Warnings")
        for w in warnings:
            st.warning(w)

    # Store model and chat session
    st.session_state.model = model
    st.session_state.chat = model.start_chat(history=[
        {"role": "user", "parts": [prompt]},
        {"role": "model", "parts": [response.text]},
    ])
    st.session_state.chat_history = []

# Callback to handle chat input
def handle_chat():
    user_question = st.session_state.chat_input.strip()
    if user_question:
        reply = st.session_state.chat.send_message(user_question)
        st.session_state.chat_history.append((user_question, reply.text))
        st.session_state.chat_input = ""  # Safe here

# Chat section
if "chat" in st.session_state:
    st.subheader("💬 Ask CoachBot Anything")

    st.text_input(
        "Your question",
        key="chat_input",
        on_change=handle_chat
    )

    for q, a in st.session_state.chat_history:
        st.markdown(f"**You:** {q}")
        st.markdown(f"**CoachBot:** {a}")