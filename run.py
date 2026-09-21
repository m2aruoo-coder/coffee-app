import random
import time
import streamlit as st
from streamlit_cookies_controller import CookieController

# --- Initialize Cookies Controller for 24h Restriction ---
controller = CookieController()

# --- Page Setup ---
st.set_page_config(
    page_title="DRIP Specialty Coffee",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# --- Premium Custom Styling & Liquid Cup Animation ---
def inject_premium_ui():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Playfair+Display:wght@700;900&display=swap');

        /* Global Theme Setup */
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(135deg, #f4f9fc 0%, #e0f2fe 100%) !important;
            color: #0f172a !important;
        }

        /* Header UI */
        .brand-header {
            text-align: center;
            padding: 30px 20px 20px 20px;
            background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%);
            border-radius: 0 0 35px 35px;
            box-shadow: 0 10px 30px rgba(56, 189, 248, 0.25);
            margin-bottom: 35px;
        }

        .brand-title {
            font-family: 'Playfair Display', serif;
            font-size: 2.8rem;
            font-weight: 900;
            letter-spacing: 2px;
            color: #ffffff !important;
            margin: 0;
            text-transform: uppercase;
        }

        .brand-subtitle {
            font-family: 'Montserrat', sans-serif;
            font-size: 0.95rem;
            letter-spacing: 4px;
            color: #e0f2fe !important;
            margin-top: 5px;
            font-weight: 600;
            text-transform: uppercase;
        }

        /* Coffee Cup Animation Container */
        .cup-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 25px 0;
        }

        .coffee-cup {
            position: relative;
            width: 110px;
            height: 120px;
            background: rgba(255, 255, 255, 0.6);
            border: 5px solid #0284c7;
            border-radius: 0 0 45px 45px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
            overflow: hidden;
        }

        .coffee-cup::after {
            content: '';
            position: absolute;
            top: 20px;
            right: -22px;
            width: 20px;
            height: 50px;
            border: 5px solid #0284c7;
            border-radius: 0 15px 15px 0;
        }

        .coffee-liquid {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            background: linear-gradient(180deg, #603813 0%, #3c2415 100%);
            transition: height 0.8s cubic-bezier(0.4, 0, 0.2, 1);
            border-radius: 0 0 38px 38px;
        }

        /* Card Container */
        .quiz-card {
            background: #ffffff !important;
            padding: 30px;
            border-radius: 24px;
            box-shadow: 0 12px 35px rgba(15, 23, 42, 0.06);
            border: 1px solid rgba(56, 189, 248, 0.2);
            margin-bottom: 25px;
            backdrop-filter: blur(10px);
        }

        .quiz-card h4 {
            font-family: 'Montserrat', sans-serif;
            color: #0284c7 !important;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin: 0 0 10px 0;
            font-weight: 700;
        }

        .quiz-card p {
            color: #0f172a !important;
            font-size: 1.3rem !important;
            font-weight: 700 !important;
            line-height: 1.5;
            margin: 0;
        }

        /* Interactive Buttons */
        div.stButton > button {
            width: 100%;
            border-radius: 50px;
            height: 60px;
            background: #ffffff !important;
            color: #0284c7 !important;
            border: 2px solid #38bdf8 !important;
            font-family: 'Montserrat', sans-serif !font-family;
            font-weight: 700 !important;
            font-size: 1.05rem !important;
            letter-spacing: 0.5px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            margin-bottom: 12px;
            box-shadow: 0 4px 15px rgba(56, 189, 248, 0.1);
        }

        div.stButton > button:hover {
            background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%) !important;
            color: #ffffff !important;
            border-color: transparent !important;
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(56, 189, 248, 0.35);
        }

        /* Reward & Status Cards */
        .reward-card {
            background: #ffffff !important;
            border: 2px dashed #38bdf8;
            padding: 35px;
            border-radius: 28px;
            text-align: center;
            margin-top: 20px;
            box-shadow: 0 15px 35px rgba(56, 189, 248, 0.15);
        }

        .status-card {
            background: #ffffff !important;
            border: 2px solid #ef4444;
            padding: 35px;
            border-radius: 28px;
            text-align: center;
            margin-top: 20px;
            box-shadow: 0 15px 35px rgba(239, 68, 68, 0.1);
        }

        .promo-badge {
            background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);
            padding: 15px 30px;
            border-radius: 16px;
            display: inline-block;
            font-weight: 800;
            font-size: 1.4rem;
            color: #0284c7;
            letter-spacing: 2px;
            margin-top: 15px;
            border: 1px solid #7dd3fc;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


inject_premium_ui()

# --- Coffee Question Bank (English Only) ---
QUESTIONS_BANK = [
    {
        "q": "Which country is celebrated as the birthplace of Arabica coffee?",
        "options": ["Ethiopia", "Yemen", "Brazil", "Colombia"],
        "answer": "Ethiopia",
    },
    {
        "q": "What does the term 'Espresso' literally translate to in Italian?",
        "options": [
            "Fast & Strong",
            "Pressed Out",
            "Concentrated Shot",
            "Pure Dark",
        ],
        "answer": "Pressed Out",
    },
    {
        "q": "What primarily distinguishes a Flat White from a Cappuccino?",
        "options": [
            "Milk Foam Thickness",
            "Bean Roast Level",
            "Water Temperature",
            "Added Sugar",
        ],
        "answer": "Milk Foam Thickness",
    },
    {
        "q": "Which brewing method utilizes a paper filter and manual pour-over technique?",
        "options": ["V60", "French Press", "Moka Pot", "Aeropress"],
        "answer": "V60",
    },
    {
        "q": "What is the golden coffee-to-water ratio typically recommended for V60?",
        "options": ["1:15", "1:5", "1:30", "1:50"],
        "answer": "1:15",
    },
    {
        "q": "Which coffee bean species contains higher natural caffeine content?",
        "options": ["Robusta", "Arabica", "Liberica", "Excelsa"],
        "answer": "Robusta",
    },
    {
        "q": "Which classic drink consists solely of Espresso and hot water?",
        "options": ["Americano", "Latte", "Macchiato", "Mocha"],
        "answer": "Americano",
    },
]

# --- Header ---
st.markdown(
    """
    <div class="brand-header">
        <div class="brand-title">DRIP</div>
        <div class="brand-subtitle">Specialty Coffee</div>
    </div>
""",
    unsafe_allow_html=True,
)

# --- Check 24-Hour Cooldown via Cookies ---
last_played = controller.get("drip_last_played")
current_time = time.time()
SECONDS_IN_24_HOURS = 86400

if last_played and (current_time - float(last_played) < SECONDS_IN_24_HOURS):
    hours_remaining = int(
        (SECONDS_IN_24_HOURS - (current_time - float(last_played))) // 3600
    )
    st.markdown(
        f"""
        <div class="status-card">
            <h2 style="color: #ef4444; margin: 0; font-family: 'Playfair Display', serif;">Daily Limit Reached ⏳</h2>
            <p style="font-size: 1.1rem; color: #475569; margin-top: 12px;">You have already claimed today's challenge. Please return in <b>{max(1, hours_remaining)} hours</b>.</p>
            <p style="font-size: 0.85rem; color: #94a3b8; margin-top: 20px; letter-spacing: 1px; text-transform: uppercase;">Enjoy your hand-crafted brew at DRIP!</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

else:
    # --- Session State Logic ---
    if "game_started" not in st.session_state:
        st.session_state.game_started = False
    if "current_q_idx" not in st.session_state:
        st.session_state.current_q_idx = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "used_questions" not in st.session_state:
        st.session_state.used_questions = []

    # --- Animated Cup Render Function ---
    def render_animated_cup(score_level):
        fill_percentage = int((score_level / 3) * 100)
        st.markdown(
            f"""
            <div class="cup-container">
                <div class="coffee-cup">
                    <div class="coffee-liquid" style="height: {fill_percentage}%;"></div>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )

    # --- Intro Screen ---
    if not st.session_state.game_started:
        render_animated_cup(0)
        st.markdown(
            "<div style='margin-top: 30px;'></div>", unsafe_allow_html=True
        )

        if st.button("READY TO BREW 🚀"):
            st.session_state.game_started = True
            st.session_state.used_questions = random.sample(
                QUESTIONS_BANK, min(3, len(QUESTIONS_BANK))
            )
            st.session_state.current_q_idx = 0
            st.session_state.score = 0
            st.session_state.start_time = time.time()
            st.rerun()

    # --- Gameplay Screen ---
    else:
        q_idx = st.session_state.current_q_idx

        if q_idx < len(st.session_state.used_questions):
            # Render current coffee cup fill status based on correct answers
            render_animated_cup(st.session_state.score)

            current_q = st.session_state.used_questions[q_idx]

            # Timer Calculation
            elapsed = time.time() - st.session_state.get(
                "start_time", time.time()
            )
            remaining = max(0, int(15 - elapsed))

            timer_placeholder = st.empty()
            timer_placeholder.progress(
                remaining / 15, text=f"⏱️ Time Remaining: {remaining}s"
            )

            # Question Display
            st.markdown(
                f"""
                <div class="quiz-card">
                    <h4>Question {q_idx + 1} of 3</h4>
                    <p>{current_q['q']}</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

            # Option Buttons
            for opt in current_q["options"]:
                if st.button(opt, key=f"btn_{q_idx}_{opt}"):
                    if opt == current_q["answer"]:
                        st.session_state.score += 1
                    st.session_state.current_q_idx += 1
                    st.session_state.start_time = time.time()
                    st.rerun()

            # Timer Live Loop
            if remaining > 0:
                time.sleep(1)
                st.rerun()
            else:
                st.session_state.current_q_idx += 1
                st.session_state.start_time = time.time()
                time.sleep(0.5)
                st.rerun()

        # --- Completion Screen ---
        else:
            # Set cookie upon completion to block repeat tries for 24 hours
            controller.set("drip_last_played", str(time.time()))

            score = st.session_state.score
            render_animated_cup(score)

            # Requires 3/3 Perfect Score
            if score == 3:
                st.balloons()
                promo_code = f"DRIP-{random.randint(1000, 9999)}"
                offer = "20% OFF ANY SIGNATURE DRINK & DESSERT 🍰☕"

                st.markdown(
                    f"""
                    <div class="reward-card">
                        <h2 style="color: #0284c7; margin: 0; font-family: 'Playfair Display', serif;">PERFECT SCORE! (3/3) 🎉</h2>
                        <p style="font-size: 0.9rem; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 15px;">Your Exclusive Reward</p>
                        <p style="font-size: 1.25rem; font-weight: 800; color: #0f172a; margin: 10px 0;">{offer}</p>
                        <p style="font-size: 0.9rem; color: #64748b;">Show this screen to our Barista to redeem.</p>
                        <div class="promo-badge">
                            {promo_code}
                        </div>
                    </div>
                """,
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"""
                    <div class="status-card">
                        <h2 style="color: #ef4444; margin: 0; font-family: 'Playfair Display', serif;">BETTER LUCK NEXT TIME! ☕</h2>
                        <p style="font-size: 1.1rem; color: #0f172a; margin-top: 12px;">Your Score: <b>{score} of 3</b></p>
                        <p style="font-size: 0.95rem; color: #64748b;">Full 3/3 score is required to unlock today's discount code.</p>
                        <p style="font-size: 0.8rem; color: #94a3b8; margin-top: 15px; text-transform: uppercase; letter-spacing: 1px;">Challenge resets in 24 hours.</p>
                    </div>
                """,
                    unsafe_allow_html=True,
                )
