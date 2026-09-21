import random
import time
import streamlit as st

# --- 1. إعدادات الصفحة والـ Theme ---
st.set_page_config(
    page_title="Drip Specialty Coffee",
    page_icon="☕",
    layout="centered",
)


def inject_custom_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

        /* تثبيت ألوان الصفحة لتغطي الـ Dark/Light Mode */
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Poppins', sans-serif;
            background-color: #f4f9fc !important;
            color: #1a1a1a !important;
        }

        /* الهيدر العلوي */
        .drip-header {
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #87CEFA 0%, #00BFFF 100%);
            color: white !important;
            border-radius: 0 0 30px 30px;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(0, 191, 255, 0.2);
        }

        .drip-header h1 {
            margin: 0;
            font-weight: 700;
            font-size: 2.2rem;
            color: white !important;
        }

        /* كارت السؤال مع توضيح لون النص */
        .question-card {
            background: #ffffff !important;
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
            border-right: 6px solid #87CEFA;
            margin-bottom: 20px;
        }

        .question-card h4 {
            color: #008B8B !important;
            margin: 0;
            font-size: 1.1rem;
        }

        .question-card p {
            color: #111111 !important; /* لون غامق جداً وواضح */
            font-size: 1.3rem !important;
            font-weight: 700 !important;
            margin-top: 10px;
        }

        /* أزرار الإجابة */
        div.stButton > button {
            width: 100%;
            border-radius: 25px;
            height: 55px;
            background-color: #ffffff !important;
            color: #008B8B !important;
            border: 2px solid #87CEFA !important;
            font-weight: 700 !important;
            font-size: 1.1rem !important;
            transition: all 0.3s ease;
            margin-bottom: 10px;
        }

        div.stButton > button:hover {
            background-color: #87CEFA !important;
            color: #ffffff !important;
            border-color: #87CEFA !important;
            box-shadow: 0 4px 12px rgba(135, 206, 250, 0.4);
        }

        /* كود الخصم */
        .promo-box {
            background: #ffffff !important;
            border: 2px dashed #00BFFF;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            margin-top: 20px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


inject_custom_css()

# --- 2. بنك الأسئلة ---
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
]

# --- 3. إدارة الجلسة ---
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "current_q_idx" not in st.session_state:
    st.session_state.current_q_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "used_questions" not in st.session_state:
    st.session_state.used_questions = []

# --- 4. الهيدر ---
st.markdown(
    """
    <div class="drip-header">
        <h1>DRIP SPECIALTY COFFEE</h1>
        <p style="margin: 5px 0 0 0; opacity: 0.9;">No Sleep, Just Drip ☕</p>
    </div>
""",
    unsafe_allow_html=True,
)

# --- 5. الشاشات ---
if not st.session_state.game_started:
    st.markdown(
        """
        <div style="text-align: center; padding: 20px;">
            <h3 style="color: #333;">جاهز تتحدى معلوماتك وتكسب خصمك؟ 🎯</h3>
            <p style="color: #666;">عندك 15 ثانية لكل سؤال.. جاوب صح واكسب عرض كرايف فوراً!</p>
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

        # حساب الوقت المتبقي
        elapsed = time.time() - st.session_state.get("start_time", time.time())
        remaining = max(0, int(15 - elapsed))

        # عرض التايمر
        timer_placeholder = st.empty()
        timer_placeholder.progress(
            remaining / 15, text=f"⏱️ الوقت المتبقي: {remaining} ثانية"
        )

        # عرض السؤال والخيارات
        st.markdown(
            f"""
            <div class="question-card">
                <h4>السؤال {q_idx + 1} من 3:</h4>
                <p>{current_q['q']}</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

        # التعامل مع الإجابات
        for opt in current_q["options"]:
            if st.button(opt, key=f"btn_{q_idx}_{opt}"):
                if opt == current_q["answer"]:
                    st.session_state.score += 1
                st.session_state.current_q_idx += 1
                st.session_state.start_time = time.time()
                st.rerun()

        # تحديث التايمر لايف كل ثانية
        if remaining > 0:
            time.sleep(1)
            st.rerun()
        else:
            st.warning("⏰ انتهى الوقت!")
            st.session_state.current_q_idx += 1
            st.session_state.start_time = time.time()
            time.sleep(1)
            st.rerun()

    else:
        # الشاشة النهائية
        score = st.session_state.score
        st.balloons()

        st.markdown(
            f"""
            <div style="text-align: center;">
                <h2 style="color: #008B8B;">🎉 عاش جداً!</h2>
                <p style="font-size: 1.2rem; color: #333;">إجاباتك الصحيحة: <b>{score} من 3</b></p>
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
                <p style="font-size: 1.3rem; font-weight: bold; color: #111; margin: 10px 0;">{offer}</p>
                <p style="font-size: 1rem; color: #555;">ورّي الشاشة دي للكاشير واستمتع بعرضك!</p>
                <div style="background: #e6f7ff; padding: 10px; border-radius: 10px; display: inline-block; font-weight: bold; font-size: 1.2rem; color: #00BFFF;">
                    {promo_code}
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )

        if st.button("العب مرة ثانية 🔄"):
            st.session_state.game_started = False
            st.rerun()
