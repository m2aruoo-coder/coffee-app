import random
import time
import streamlit as st

# ضبط إعدادات الصفحة للموبايل
st.set_page_config(
    page_title="تحدي الكافيه ☕", page_icon="🎯", layout="centered"
)

# بنك الأسئلة (يمكنك تعديله أو زيادته بسهولة)
QUESTIONS = [
    {
        "question": "ما هي الدولة الأكثر إنتاجاً للقهوة في العالم؟ 🌍",
        "options": ["إثيوبيا", "البرازيل", "كولومبيا", "إيطاليا"],
        "answer": "البرازيل",
    },
    {
        "question": "أي من المشروبات التالية يحتوي على أعلى نسبة رغوة حليب؟ 🥛",
        "options": ["الفلات وايت", "الكابتشينو", "اللاتيه", "الأمريكانو"],
        "answer": "الكابتشينو",
    },
    {
        "question": "ما هي المادة المسؤولة عن الشعور باليقظة عند شرب القهوة؟ ⚡",
        "options": ["السيروتونين", "الجلوكوز", "الكافيين", "المغنيسيوم"],
        "answer": "الكافيين",
    },
]

# تهيئة متغيرات الجلسة (Session State)
if "score" not in st.session_state:
    st.session_state.score = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# واجهة التطبيق
st.title("🎯 تحدي الـ 60 ثانية!")
st.subheader("جاوب صح واكسب خصم حصري على طلبك دلوقتي ☕🍰")
st.write("---")

if not st.session_state.game_over:
    current_q = QUESTIONS[st.session_state.q_index]

    st.markdown(
        f"### السؤال ({st.session_state.q_index + 1}/{len(QUESTIONS)}):"
    )
    st.write(f"**{current_q['question']}**")

    # خيارات الإجابة
    user_choice = st.radio(
        "اختر الإجابة الصحيحة:",
        current_q["options"],
        key=f"q_{st.session_state.q_index}",
    )

    if st.button("تأكيد الإجابة 🚀"):
        if user_choice == current_q["answer"]:
            st.session_state.score += 1
            st.success("إجابة صحيحة! 🎉")
        else:
            st.error(f"إجابة خاطئة! الإجابة الصحيحة هي: {current_q['answer']}")

        time.sleep(1)

        # الانتقال للسؤال التالي أو إنهاء اللعبة
        if st.session_state.q_index + 1 < len(QUESTIONS):
            st.session_state.q_index += 1
            st.rerun()
        else:
            st.session_state.game_over = True
            st.rerun()

else:
    # شاشة النتيجة النهائية
    st.balloons()
    st.markdown("## 🏆 انتهاء التحدي!")
    st.write(
        f"نتيجة الاختبار: **{st.session_state.score} من {len(QUESTIONS)}**"
    )

    if st.session_state.score == len(QUESTIONS):
        promo_code = f"WINNER-{random.randint(1000, 9999)}"
        st.success("🎉 مبروك! جاوبت على كل الأسئلة صح!")
        st.markdown(f"""
        ### 🎁 هديتك: خصم 15% على أي نوع حلو!
        * **كود الخصم:** `{promo_code}`
        * **طريقة الاستخدام:** ورّي الشاشة دي للكاشير فوراً واستمتع بعرضك.
        *(الكود صالح لمدة 15 دقيقة فقط)*
        """)
    else:
        st.info(
            "حاولت كويس! تقدر تلف العجلة أو تجارب التحدي تاني المرة الجاية."
        )

    if st.button("إعادة اللعبة 🔄"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.game_over = False
        st.rerun()