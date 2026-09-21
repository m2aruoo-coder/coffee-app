import streamlit as st
import time
import random

# --- 1. إعدادات الهوية البصرية (Drip Branding & CSS) ---
st.set_page_config(page_title="Drip Trivia Challenge", page_icon="☕")

def local_css():
    st.markdown(
        """
        <style>
        /* استيراد خط مودرن شبه اللوجو */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

        /* تصفير الهامش وتحديد الخط الرئيسي */
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Poppins', sans-serif;
            color: #1a1a1a;
        }

        /* الخلفية العامة: دمج بين الأبيض وتموجات الأزرق السماوي Drip */
        [data-testid="stAppViewContainer"] {
            background-color: #f8fbff;
            background-image: 
                radial-gradient(at 0% 0%, rgba(135, 206, 250, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(255, 255, 255, 1) 0px, transparent 50%);
        }

        /* الهيدر والعنوان */
        .header-container {
            text-align: center;
            padding: 20px 0 40px 0;
            background: linear-gradient(135deg, rgba(135, 206, 250, 0.2) 0%, rgba(255, 255, 255, 0) 100%);
            border-bottom-left-radius: 50px;
            border-bottom-right-radius: 50px;
        }

        .main-title {
            font-size: 3rem !important;
            font-weight: 700;
            color: #333;
            letter-spacing: -1px;
            margin-bottom: 0px;
        }
        .main-title span {
            color: #87CEFA; /* Drip Blue */
            text-shadow: 0 0 10px rgba(135, 206, 250, 0.5);
        }
        
        /* مربع السؤال */
        .question-box {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 20px;
            border-left: 8px solid #87CEFA;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }
        .question-text {
            font-size: 1.5rem;
            font-weight: 500;
            color: #333;
        }

        /* أزرار الإجابات (تعديل الـ Widget الافتراضي) */
        div.stButton > button {
            width: 100%;
            height: 60px;
            background-color: #f0f8ff; /* Lightest Drip Blue */
            color: #1E90FF; /* Drip Darker Blue */
            border-radius: 30px; /* مستديرة بالكامل */
            border: 2px solid transparent;
            font-weight: 500;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
            margin-bottom: 15px;
        }
        div.stButton > button:hover {
            background-color: #87CEFA; /* Drip Blue */
            color: #ffffff;
            border-color: #87CEFA;
            box-shadow: 0 0 15px rgba(135, 206, 250, 0.6); /* تأثير نيون hover */
            transform: translateY(-2px);
        }

        /* تنسيق رسائل النتيجة */
        .result-box-correct {
            padding: 20px;
            border-radius: 15px;
            background-color: #d4edda;
            color: #155724;
            text-align: center;
            font-weight: 700;
            font-size: 1.2rem;
            margin-bottom: 20px;
        }
        .result-box-wrong {
            padding: 20px;
            border-radius: 15px;
            background-color: #f8d7da;
            color: #721c24;
            text-align: center;
            font-weight: 700;
            font-size: 1.2rem;
            margin-bottom: 20px;
        }
        
        /* التايمر */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #FFD700 0%, #FF8C00 100%); /* نيون أصفر */
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
        }
        
        </style>
        """,
        unsafe_allow_stdio=True,
    )

local_css()

# --- 2. بنك الأسئلة (100 سؤال متنوع وغير متكرر عن القهوة والبارستا) ---
def get_all_questions():
    # بنك أسئلة Drip: قهوة، تاريخ، ثقافة، معلومات بارستا
    raw_questions = [
        ("ما هي الدولة التي تعتبر الموطن الأصلي للقهوة؟", ["إثيوبيا", "اليمن", "البرازيل", "كولومبيا"], "إثيوبيا"),
        ("ماذا تعني كلمة 'إسبريسو' بالإيطالية؟", ["السريع", "المضغوط", "المُعَد لحظياً", "القوي"], "المُعَد لحظياً"),
        ("ما هو نوع القهوة الأكثر استهلاكاً في العالم؟", ["أرابيكا", "روبوستا", "ليبيريكا", "إكسيلسا"], "أرابيكا"),
        ("أي من هذه المشروبات يحتوي على أكبر كمية حليب؟", ["فلات وايت", "كابتشينو", "لاتيه", "كورتادو"], "لاتيه"),
        ("كم تبلغ نسبة الكافيين تقريباً في كوب قهوة إسبريسو واحد؟", ["30-50 ملغ", "60-80 ملغ", "100-120 ملغ", "20-40 ملغ"], "60-80 ملغ"),
        ("ما اسم الأداة التي تستخدم لضغط القهوة المطحونة في الـ Portafilter؟", ["Tamper", "Distributor", "Pitcher", "Grinder"], "Tamper"),
        ("في أي بلد تم اختراع أول آلة إسبريسو؟", ["فرنسا", "ألمانيا", "إيطاليا", "سويسرا"], "إيطاليا"),
        ("ما هي القهوة 'المنزوعة الكافيين' بشكل طبيعي تقريباً؟", ["عربيا", "ليبيريكاعاش يا مروان، التفكير في إنك تمنع التكرار (Anti-cheat) وتحط وقت استجابة (Timer) مع توحيد الهوية البصرية (Branding) ده اللي هينقل الفكرة من مجرد مشروع تجريبي لمنتج احترافي جاهز للبيع! 

عشان نعمل **أسئلة لا نهائية ومختلفة لكل زبون** مع **مؤقت 15 ثانية** وتصميم احترافي:

---

### 1. إزاي نخلي الأسئلة لا نهائية ومختلفة؟ (Infinite Dynamic Questions)

عندك طريقتين ممتازين:

* **الطريقة الأولى (الذكاء الاصطناعي - AI-Generated Queries):**
  نربط الكود بـ **Gemini API**؛ مع كل دخول للزبون، الكود بيبعت طلب للـ API يولد 3 أسئلة جديدة تماماً عن القهوة، الثقافة العامة، أو الأفلام، بأسلوب مشوق ومعاهم الاختيارات والإجابة الصحيحة. وبكده مفيش زبون هيشوف نفس السؤال مرتين إطلاقاً.
* **الطريقة الثانية (Dynamic Randomization):**
  نعمل بنك أسئلة كبير (مثلاً 100+ سؤال) والكود يختار عشوائياً بدون تكرار لنفس الجهاز.

---

### 2. التايمر (15 ثانية لكل سؤال)

في Streamlit تقدر تضيف تايمر بـ JavaScript أو باستخدام `st.empty()` مع كاونتر بايثون يعيد تنشيط الصفحة تلقائياً لو الـ 15 ثانية خلصوا، والزبون يتنقل للسؤال اللي بعده أو يخسر التحدي.

---

### 3. التصميم الاحترافي والـ Branding (Custom CSS)

عشان نخلي الـ Web App شبه المكان كافيه كرايف ومودرن، بنستخدم **Custom CSS** جوة Streamlit لتغيير:
* الألوان والألوان الخلفية (Background & Theme colors).
* نوع الخط وحجمه (Typography).
* شكل الأزرار والمربعات والأنيميشن الخاص بالتايمر والنتيجة.

---

### 📸 ابعت صورة المكان!

ابعت صورة الكافيه أو اللوجو/الهوية البصرية عشان أطلعلك ألوان الـ Hex Codes الدقيقة وأصمملك الـ UI بـ CSS يطابق المكان تماماً. أول ما تبعت الصورة، هكتبلك الكود الكامل المطور بالتايمر والـ AI!
