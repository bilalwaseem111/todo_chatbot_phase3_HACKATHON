import streamlit as st
from backend.bot import TodoChatBot


st.set_page_config(
    page_title="Hackathon Phase III | Todo AI Chatbot",
    layout="wide"
)

st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #0b0f1a !important;
    color: #ffffff !important;
}

.stApp {
    background: radial-gradient(circle at top, #111827, #020617);
}

h1, h2, h3, h4, h5, p, span, label {
    color: #ffffff !important;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #38bdf8, #22c55e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 18px;
}

.card-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 40px;
}

.card {
    background: linear-gradient(145deg, #0f172a, #020617);
    border-radius: 18px;
    padding: 24px;
    border: 1px solid #1e293b;
    transition: all 0.35s ease;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

.card:hover {
    transform: translateY(-8px) scale(1.02);
    border-color: #38bdf8;
}

.card h3 {
    margin-bottom: 12px;
    color: #38bdf8;
}

.card ul {
    padding-left: 18px;
}

.card li {
    color: #cbd5f5;
    margin-bottom: 8px;
}

.chat-section {
    margin-top: 60px;
}

.chat-box {
    background: #020617;
    padding: 16px;
    border-radius: 14px;
    margin-bottom: 12px;
    border: 1px solid #1e293b;
}

.user {
    color: #38bdf8;
    font-weight: 600;
}

.bot {
    color: #22c55e;
    font-weight: 600;
}

input, textarea {
    background-color: #020617 !important;
    color: #ffffff !important;
    border: 1px solid #1e293b !important;
}

footer {
    visibility: hidden;
}

.footer {
    margin-top: 80px;
    padding-top: 30px;
    border-top: 1px solid #1e293b;
    text-align: center;
    color: #94a3b8;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ================= HERO =================
st.markdown("<div class='hero-title'>Hackathon Phase III</div>", unsafe_allow_html=True)
st.markdown(
    "<p class='hero-subtitle'>Todo AI Chatbot • MCP-inspired Stateless Conversational System</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; max-width:900px; margin:auto; color:#cbd5f5;'>"
    "<strong>Objective:</strong> Develop a stateless, AI-powered todo management chatbot that interprets natural language command task operations through an MCP inspired server architecture, leveraging Claude Code and Spec-Kit Plus."
    "</p>",
    unsafe_allow_html=True
)

# ================= CARDS =================
st.markdown("""
<div class="card-grid">

<div class="card">
<h3>Objective</h3>
<p>
To build an AI-powered conversational interface that manages todo tasks using
natural language commands, following a stateless request-response architecture.
</p>
</div>

<div class="card">
<h3>Core Capabilities</h3>
<ul>
<li>Natural language interaction for task management</li>
<li>Stateless conversation handling</li>
<li>Persistent chat history</li>
<li>Dark-themed, distraction-free interface</li>
</ul>
</div>

<div class="card">
<h3>System Design (Frontend View)</h3>
<ul>
<li>User interacts via chat interface</li>
<li>Message processed by chatbot logic</li>
<li>Intent-response system simulates AI behavior</li>
<li>Response returned with confirmation</li>
</ul>
</div>

</div>
""", unsafe_allow_html=True)

# ================= CHATBOT =================
st.markdown("<div class='chat-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>Todo AI Chat Interface</h2>", unsafe_allow_html=True)

bot = TodoChatBot()

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input(
    "Enter your message",
    placeholder="Try: Add task, Show tasks, Help..."
)

if user_input:
    response = bot.get_response(user_input)
    st.session_state.chat.append(("User", user_input))
    st.session_state.chat.append(("Assistant", response))

for sender, msg in st.session_state.chat:
    role = "user" if sender == "User" else "bot"
    st.markdown(f"""
    <div class="chat-box">
        <span class="{role}">{sender}:</span>
        <span style="color:white;"> {msg}</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div class="footer">
    <p><strong>Hackathon Phase III – Todo AI Chatbot</strong></p>
    Made by <strong>Bilal Waseem Roll Number (00471327)</strong></p>
</div>
""", unsafe_allow_html=True)
