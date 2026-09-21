import random
import time
import streamlit as st
from streamlit_cookies_controller import CookieController

# --- Initialize Cookies Controller for 24h Device Limit ---
controller = CookieController()

# --- Page Setup ---
st.set_page_config(
    page_title="DRIP | Master Brew Challenge",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# --- Premium Custom Styling ---
def inject_ultra_premium_ui():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@600;700;800;900&family=Montserrat:wght@400;600;700;800;900&family=Playfair+Display:ital,wght@0,700;0,900;1,400&display=swap');

        /* Dark Luxe Canvas */
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Montserrat', 'Cairo', sans-serif;
            background: radial-gradient(circle at 50% 10%, #1e293b 0%, #0f172a 60%, #050914 100%) !important;
            color: #f8fafc !important;
        }

        #MainMenu, footer, header {visibility: hidden;}

        /* Header UI */
        .brand-header {
            text-align: center;
            padding: 30px 20px 20px 20px;
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 0 0 40px 40px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            margin-bottom: 25px;
        }

        .brand-title {
            font-family: 'Playfair Display', serif;
            font-size: 3rem;
            font-weight: 900;
            letter-spacing: 4px;
            background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
            text-transform: uppercase;
        }

        .brand-subtitle {
            font-size: 0.8rem;
            letter-spacing: 6px;
            color: #94a3b8 !important;
            margin-top: 5px;
            font-weight: 700;
            text-transform: uppercase;
        }

        /* Glassmorphism Quiz Card */
        .glass-card {
            background: rgba(255, 255, 255, 0.05) !important;
            backdrop-filter: blur(20px);
            padding: 25px 20px;
            border-radius: 24px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 20px;
            text-align: right;
            direction: rtl;
        }

        .glass-card h4 {
            font-family: 'Montserrat', sans-serif;
            color: #38bdf8 !important;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin: 0 0 10px 0;
            font-weight: 800;
            direction: ltr;
            text-align: left;
        }

        .glass-card p {
            font-family: 'Cairo', sans-serif;
            color: #ffffff !important;
            font-size: 1.25rem !important;
            font-weight: 700 !important;
            line-height: 1.6;
            margin: 0;
        }

        /* Photorealistic Liquid Coffee Cup with Steam */
        .cup-wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px 0;
            position: relative;
        }

        .steam-container {
            position: absolute;
            top: -25px;
            display: flex;
            gap: 8px;
        }

        .steam {
            width: 6px;
            height: 20px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            animation: steamAnim 2s infinite ease-out;
        }

        .steam:nth-child(2) { animation-delay: 0.4s; }
        .steam:nth-child(3) { animation-delay: 0.8s; }

        @keyframes steamAnim {
            0% { transform: translateY(0) scaleX(1); opacity: 0; }
            50% { opacity: 0.6; }
            100% { transform: translateY(-25px) scaleX(2); opacity: 0; }
        }

        .coffee-cup {
            position: relative;
            width: 110px;
            height: 120px;
            background: rgba(255, 255, 255, 0.08);
            border: 4px solid rgba(56, 189, 248, 0.6);
            border-radius: 0 0 45px 45px;
            box-shadow: 0 0 30px rgba(56, 189, 248, 0.2);
            overflow: hidden;
        }

        .coffee-cup::after {
            content: '';
            position: absolute;
            top: 22px;
            right: -22px;
            width: 20px;
            height: 50px;
            border: 4px solid rgba(56, 189, 248, 0.6);
            border-radius: 0 16px 16px 0;
        }

        .coffee-liquid {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            background: linear-gradient(180deg, #c084fc 0%, #603813 30%, #29180c 100%);
            transition: height 0.8s ease-in-out;
            border-radius: 0 0 40px 40px;
            box-shadow: 0 -5px 15px rgba(192, 132, 252, 0.4);
        }

        /* Buttons */
        div.stButton > button {
            width: 100%;
            border-radius: 50px;
            height: 60px;
            background: rgba(255, 255, 255, 0.04) !important;
            color: #f8fafc !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            font-family: 'Cairo', sans-serif !important;
            font-weight: 700 !important;
            font-size: 1.1rem !important;
            transition: all 0.3s ease;
            margin-bottom: 12px;
            backdrop-filter: blur(10px);
            direction: rtl;
        }

        div.stButton > button:hover {
            background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%) !important;
            color: #ffffff !important;
            border-color: transparent !important;
            box-shadow: 0 10px 30px rgba(56, 189, 248, 0.4);
        }

        /* Promo & Status Cards */
        .reward-card {
            background: rgba(255, 255, 255, 0.05) !important;
            backdrop-filter: blur(25px);
            border: 1px solid rgba(56, 189, 248, 0.4);
            padding: 35px 25px;
            border-radius: 28px;
            text-align: center;
            margin-top: 15px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        }

        .status-card {
            background: rgba(255, 255, 255, 0.04) !important;
            backdrop-filter: blur(25px);
            border: 1px solid rgba(239, 68, 68, 0.4);
            padding: 35px 25px;
            border-radius: 28px;
            text-align: center;
            margin-top: 15px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        }

        .promo-badge {
            background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
            padding: 14px 32px;
            border-radius: 18px;
            display: inline-block;
            font-weight: 900;
            font-size: 1.5rem;
            color: #ffffff;
            letter-spacing: 3px;
            margin-top: 15px;
            box-shadow: 0 10px 30px rgba(56, 189, 248, 0.4);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


inject_ultra_premium_ui()

# --- Arabic Question Bank ---
QUESTIONS_BANK = [
    {
        "q": "ما هي الدولة التي تـُعتبر الموطن الأصلي التاريخي لشجرة القهوة (الأرابيكا)؟",
        "options": ["إثيوبيا", "اليمن", "البرازيل", "كولومبيا"],
        "answer": "إثيوبيا",
    },
    {
        "q": "ماذا يعني مصطلح 'إسبريسو' حرفياً في الثقافة الإيطالية؟",
        "options": ["السريع جداً", "المعصور طازجاً", "المركز القوي", "القهوة الداكنة"],
        "answer": "المعصور طازجاً",
    },
    {
        "q": "ما هو العنصر الأساسي الذي يميّز الفلات وايت عن الكابتشينو؟",
        "options": ["كثافة ورغوة الحليب", "درجة تحميص البن", "درجة حرارة الماء", "نوع كوب التقديم"],
        "answer": "كثافة ورغوة الحليب",
    },
    {
        "q": "أي من أدوات تحضير القهوة المختصة التالية تتبع أسلوب التقطير بالفلتر الورقي؟",
        "options": ["V60", "French Press", "Moka Pot", "Ibrik"],
        "answer": "V60",
    },
    {
        "q": "ما هي النسبة الذهبية القياسية الموصى بها بين القهوة والماء عند تحضير الـ V60؟",
        "options": ["1:15", "1:5", "1:30", "1:50"],
        "answer": "1:15",
    },
    {
        "q": "أي من سلالات حبوب القهوة التالية تحتوي على نسبة كافيين أعلى وطعم أكثر حدة؟",
        "options": ["روبوستا", "أرابيكا", "ليبيريكا", "إكسيلسا"],
        "answer": "روبوستا",
    },
    {
        "q": "ما هو المشروب الكلاسيكي الذي يتكون فقط من شوط إسبريسو مع ماء ساخن؟",
        "options": ["أمريكانو", "لاتيه", "ماكياتو", "فلات وايت"],
        "answer": "أمريكانو",
    },
]

# --- Header ---
st.markdown(
    """
    <div class="brand-header">
        <div class="brand-title">DRIP</div>
        <div class="brand-subtitle">Specialty Coffee Outlets</div>
    </div>
""",
    unsafe_allow_html=True,
)

# --- 24-Hour Device Cooldown via Cookies ---
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
            <h2 style="color: #ef4444; margin: 0; font-family: 'Playfair Display', serif;">DAILY LIMIT REACHED ⏳</h2>
            <p style="font-size: 1.1rem; color: #cbd5e1; margin-top: 15px;">You have already completed today's challenge.</p>
            <p style="font-size: 0.95rem; color: #94a3b8;">Your device can attempt again in <b style="color: #38bdf8;">{max(1, hours_remaining)} hours</b>.</p>
            <p style="font-size: 0.8rem; color: #64748b; margin-top: 25px; letter-spacing: 2px; text-transform: uppercase;">NO SLEEP, JUST DRIP</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

else:
    # --- Session State ---
    if "game_started" not in st.session_state:
        st.session_state.game_started = False
    if "current_q_idx" not in st.session_state:
        st.session_state.current_q_idx = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "used_questions" not in st.session_state:
        st.session_state.used_questions = []

    # --- Render Animated Cup ---
    def render_steam_cup(score_level):
        fill_pct = int((score_level / 3) * 100)
        st.markdown(
            f"""
            <div class="cup-wrapper">
                <div class="steam-container">
                    <div class="steam"></div>
                    <div class="steam"></div>
                    <div class="steam"></div>
                </div>
                <div class="coffee-cup">
                    <div class="coffee-liquid" style="height: {fill_pct}%;"></div>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )

    # --- Initial Screen ---
    if not st.session_state.game_started:
        render_steam_cup(0)
        st.markdown(
            "<div style='margin-top: 30px;'></div>", unsafe_allow_html=True
        )

        if st.button("READY 🚀"):
            st.session_state.game_started = True
            st.session_state.used_questions = random.sample(
                QUESTIONS_BANK, min(3, len(QUESTIONS_BANK))
            )
            st.session_state.current_q_idx = 0
            st.session_state.score = 0
            st.rerun()

    # --- Challenge Screen ---
    else:
        q_idx = st.session_state.current_q_idx

        if q_idx < len(st.session_state.used_questions):
            render_steam_cup(st.session_state.score)

            current_q = st.session_state.used_questions[q_idx]

            # Question Card
            st.markdown(
                f"""
                <div class="glass-card">
                    <h4>QUESTION {q_idx + 1} OF 3</h4>
                    <p>{current_q['q']}</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

            # Answer Options
            for opt in current_q["options"]:
                if st.button(opt, key=f"btn_{q_idx}_{opt}"):
                    if opt == current_q["answer"]:
                        st.session_state.score += 1
                    st.session_state.current_q_idx += 1
                    st.rerun()

        # --- Reward Screen ---
        else:
            controller.set("drip_last_played", str(time.time()))

            score = st.session_state.score
            render_steam_cup(score)

            if score == 3:
                st.balloons()
                promo_code = f"DRIP-{random.randint(1000, 9999)}"
                offer = "20% OFF YOUR FAVOURITE CRAVING COMBO ☕🍰"

                st.markdown(
                    f"""
                    <div class="reward-card">
                        <h2 style="color: #38bdf8; margin: 0; font-family: 'Playfair Display', serif; font-size: 2.2rem;">PERFECT SCORE! (3/3) 🎉</h2>
                        <p style="font-size: 0.85rem; color: #94a3b8; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-top: 15px;">Exclusive Barista Pass</p>
                        <p style="font-size: 1.3rem; font-weight: 800; color: #ffffff; margin: 12px 0;">{offer}</p>
                        <p style="font-size: 0.9rem; color: #cbd5e1;">Present this ticket to the Barista to redeem your reward.</p>
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
                        <h2 style="color: #ef4444; margin: 0; font-family: 'Playfair Display', serif; font-size: 2rem;">BETTER LUCK NEXT TIME ☕</h2>
                        <p style="font-size: 1.2rem; color: #ffffff; margin-top: 15px;">Your Score: <b style="color: #ef4444;">{score} of 3</b></p>
                        <p style="font-size: 0.95rem; color: #94a3b8;">A perfect 3/3 score is required to unlock today's reward.</p>
                        <p style="font-size: 0.8rem; color: #64748b; margin-top: 20px; text-transform: uppercase; letter-spacing: 2px;">Challenge resets in 24 hours.</p>
                    </div>
                """,
                    unsafe_allow_html=True,
                )
