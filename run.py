import random
import time
import streamlit as st

# --- 1. إعدادات الصفحة والهوية البصرية لـ Drip ---
st.set_page_config(
    page_title="Drip Specialty Coffee - Trivia Challenge",
    page_icon="☕",
    layout="centered",
)


def inject_custom_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Poppins', sans-serif;
            background-color: #f4f9fc;
        }

        /* الهيدر العلوي */
        .drip-header {
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #87CEFA 0%, #00BFFF 100%);
            color: white;
            border-radius: 0 0 30px 30px;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0, 191, 255, 0.2);
        }

        .drip-header h1 {
            margin: 0;
            font-weight: 700;
            font-size: 2.2rem;
            letter-spacing: 1px;
        }

        /* كارت السؤال */
        .question-card {
            background: #ffffff;
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
            border-right: 6px solid #87CEFA;
            margin-bottom: 20px;
        }

        /* أزرار الإجابة */
        div.stButton > button {
            width: 100%;
            border-radius: 25px;
            height: 50px;
            background-color: #ffffff;
            color: #008B8B;
            border: 2px solid #87CEFA;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            margin-bottom: 10px;
        }

        div.stButton > button:hover {
            background-color: #87CEFA;
            color: #ffffff;
            border-color: #87CEFA;
            box-shadow: 0 4px 12px rgba(135, 206, 250, 0.4);
        }

        /* كود الخصم */
        .promo-box {
            background: #e6f7ff;
            border: 2px dashed #00BFFF;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


inject_custom_css()

# --- 2. بنك الأسئلة المتنوعة ---
QUESTIONS_BANK = [
    {
        "q": "ما هي الدولة التي تعتبر الموطن الأصلي لشجرة القهوة (الأرابيكا)؟",
        "options": ["إثيوبيا", "اليمن", "البرازيل", "كولومبيا"],
        "answer": "إثيوبيا",
    },
    {
        "q": "ماذا تعني كلمة 'إسبريسو' باللغة الإيطالية؟",
        "options": ["السريع", "المُعَد القوي", "المعصور طازجاً", "المركز"],
        "answer": "المعصور طازجاً",
    },
    {
        "q": "ما الفرق الرئيسي بين الفلات وايت والكابتشينو؟",
        "options": [
            "سمك رغوة الحليب",
            "نوع القهوة",
            "درجة حرارة الماء",
            "إضافة السكر",
        ],
        "answer": "سمك رغوة الحليب",
    },
    {
        "q": "أي من أدوية التحضير التالية تستخدم التقطير بالتقطير الورقي؟",
        "options": ["V60", "French Press", "Moka Pot", "Aeropress"],
        "answer": "V60",
    },
    {
        "q": "ما هي نسبة القهوة إلى الماء المثالية تقريباً في تحضير V60؟",
        "options": ["1:15", "1:5", "1:30", "1:50"],
        "answer": "1:15",
    },
    {
        "q": "أي نوع من حبوب القهوة يحتوي على نسبة كافيين أعلى؟",
        "options": ["روبوستا", "أرابيكا", "ليبيريكا", "إكسيلسا"],
        "answer": "روبوستا",
    },
    {
        "q": "ما المشروب الذي يتكون من الإسبريسو والماء الساخن فقط؟",
        "options": ["أمريكانو", "لاتيه", "ماكياتو", "موكا"],
        "answer": "أمريكانو",
    },
    {
        "q": "درجة الطحن المناسبة لتحضير الإسبريسو تكون:",
        "options": [" ناعمة جداً", "خشنة", "متوسطة", "خشنة جداً"],
        "answer": " ناعمة جداً",
    },
]

# --- 3. إدارة جلسة اللعب (Session State) ---
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "current_q_idx" not in st.session_state:
    st.session_state.current_q_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "used_questions" not in st.session_state:
    st.session_state.used_questions = []

# --- 4. الواجهة الرئيسية ---
st.markdown(
    """
    <div class="drip-header">
        <h1>DRIP SPECIALTY COFFEE</h1>
        <p style="margin: 5px 0 0 0; opacity: 0.9;">No Sleep, Just Drip ☕</p>
    </div>
""",
    unsafe_allow_html=True,
)

if not st.session_state.game_started:
    st.markdown(
        """
        <div style="text-align: center; padding: 20px;">
            <h3>جاهز تتحدى معلوماتك وتكسب خصمك؟ 🎯</h3>
            <p>عندك 15 ثانية لكل سؤال.. جاوب صح واكسب عرض كرايف فوراً!</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    if st.button("ابدأ التحدي الآن 🚀"):
        st.session_state.game_started = True
        st.session_state.used_questions = random.sample(
            QUESTIONS_BANK, min(3, len(QUESTIONS_BANK))
        )
        st.session_state.current_q_idx = 0
        st.session_state.score = 0
        st.session_state.start_time = time.time()
        st.rerun()

else:
    q_idx = st.session_state.current_q_idx

    if q_idx < len(st.session_state.used_questions):
        current_q = st.session_state.used_questions[q_idx]

        # التايمر (15 ثانية)
        elapsed = time.time() - st.session_state.get("start_time", time.time())
        remaining = max(0, int(15 - elapsed))

        st.progress(remaining / 15, text=f"⏱️ الوقت المتبقي: {remaining} ثانية")

        if remaining == 0:
            st.warning("⏰ انتهى الوقت!")
            st.session_state.current_q_idx += 1
            st.session_state.start_time = time.time()
            time.sleep(1)
            st.rerun()

        st.markdown(
            f"""
            <div class="question-card">
                <h4 style="margin:0; color:#333;">السؤال {q_idx + 1} من 3:</h4>
                <p style="font-size: 1.2rem; margin-top: 10px; font-weight:600;">{current_q['q']}</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

        for opt in current_q["options"]:
            if st.button(opt, key=f"btn_{q_idx}_{opt}"):
                if opt == current_q["answer"]:
                    st.session_state.score += 1
                st.session_state.current_q_idx += 1
                st.session_state.start_time = time.time()
                st.rerun()

    else:
        # شاشة النتيجة والعرض
        score = st.session_state.score
        st.balloons()

        st.markdown(
            f"""
            <div style="text-align: center;">
                <h2>🎉 عاش جداً!</h2>
                <p style="font-size: 1.2rem;">إجاباتك الصحيحة: <b>{score} من 3</b></p>
            </div>
        """,
            unsafe_allow_html=True,
        )

        promo_code = f"DRIP-{random.randint(1000, 9999)}"

        if score == 3:
            offer = "خصم 20% على أي مشروب سيجنتشر + حلو 🍰☕"
        elif score >= 1:
            offer = "خصم 10% على طلبك القادم من DRIP ☕"
        else:
            offer = "ترقية حجم مشروبك للـ Large مجاناً 🥤"

        st.markdown(
            f"""
            <div class="promo-box">
                <h3 style="color: #008B8B; margin: 0;">عرضك الخاص من DRIP:</h3>
                <p style="font-size: 1.3rem; font-weight: bold; margin: 10px 0;">{offer}</p>
                <p style="font-size: 1rem; color: #555;">ورّي الشاشة دي للكاشير واستمتع بعرضك!</p>
                <div style="background: #ffffff; padding: 10px; border-radius: 10px; display: inline-block; font-weight: bold; font-size: 1.2rem; color: #00BFFF;">
                    {promo_code}
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )

        if st.button("العب مرة ثانية 🔄"):
            st.session_state.game_started = False
            st.rerun()
