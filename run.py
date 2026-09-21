import random
import time
import streamlit as st

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

# --- Arabic Question Bank (60 Questions) ---
QUESTIONS_BANK = [
    {
        "q": "ما هي الدولة التي تـُعتبر الموطن الأصلي التاريخي لشجرة القهوة (الأرابيكا)؟",
        "options": ["إثيوبيا", "اليمن", "البرازيل", "كولومبيا"],
        "answer": "إثيوبيا",
    },
    {
        "q": "ما هو أول ميناء عربي أُطلقت تسميته على أحد أشهر أنواع القهوة عالمياً؟",
        "options": ["المخا", "عدن", "جدة", "الإسكندرية"],
        "answer": "المخا",
    },
    {
        "q": "ماذا يعني مصطلح 'إسبريسو' حرفياً في اللغة الإيطالية؟",
        "options": ["المعصور طازجاً", "السريع جداً", "المركز القوي", "القهوة الداكنة"],
        "answer": "المعصور طازجاً",
    },
    {
        "q": "ما هي أكبر دولة منتجة ومصدرة لحبوب القهوة في العالم حالياً؟",
        "options": ["البرازيل", "فيتنام", "كولومبيا", "إندونيسيا"],
        "answer": "البرازيل",
    },
    {
        "q": "في أي قرن بدأت المقاهي بالتوسع والانتشار في الشرق الأوسط والعالم العربي؟",
        "options": [
            "القرن الـ 16",
            "القرن الـ 12",
            "القرن الـ 18",
            "القرن الـ 20",
        ],
        "answer": "القرن الـ 16",
    },
    {
        "q": "ما هي اسم الثمرة التي تُستخرج منها حبوب القهوة؟",
        "options": [
            "كرز القهوة",
            "توت القهوة",
            "عنب القهوة",
            "زيتون القهوة",
        ],
        "answer": "كرز القهوة",
    },
    {
        "q": "ما هي القارة الأولى من حيث معدل استهلاك القهوة للفرد؟",
        "options": ["أوروبا", "أمريكا الشمالية", "آسيا", "أمريكا الجنوبية"],
        "answer": "أوروبا",
    },
    {
        "q": "ما هي القهوة الشهيرة عالمياً المستخرجة من ثمار القهوة بعد أن يأكلها حيوان زباد النخل؟",
        "options": ["كوبي لواك", "جيشا", "جاميكا بلو ماونتن", "ماراغوجيبي"],
        "answer": "كوبي لواك",
    },
    {
        "q": "أي دولة تُعرف بتحضير قهوة 'الفلات وايت' لأول مرة في التاريخ؟",
        "options": ["أستراليا", "إيطاليا", "أمريكا", "إنجلترا"],
        "answer": "أستراليا",
    },
    {
        "q": "ما هو الاسم الشعبي الذي يُطلق على مشروب القهوة التركية التقليدية في اليمن؟",
        "options": ["القشر", "الشوذق", "العسلية", "المرّة"],
        "answer": "القشر",
    },
    {
        "q": "أي من سلالات حبوب القهوة التالية تحتوي على نسبة كافيين أعلى وطعم أكثر حدة؟",
        "options": ["روبوستا", "أرابيكا", "ليبيريكا", "إكسيلسا"],
        "answer": "روبوستا",
    },
    {
        "q": "ما هي السلالة الأكثر انتشاراً واستخداماً في القهوة المختصة لتميز إيحاءاتها؟",
        "options": ["أرابيكا", "روبوستا", "ليبيريكا", "كاتيمور"],
        "answer": "أرابيكا",
    },
    {
        "q": "سلالة 'جيشا' (Geisha) الفاخرة تشتهر بنكهاتها وإيحاءاتها الزهرية، ما أصلها؟",
        "options": ["إثيوبيا", "بنما", "كولومبيا", "اليابان"],
        "answer": "إثيوبيا",
    },
    {
        "q": "ما هي السلالة التي تُعرف باسم 'حبوب القهوة العملاقة' لكبر حجم حبتها؟",
        "options": ["ماراغوجيبي", "بوربون", "تيبيكا", "كاتورا"],
        "answer": "ماراغوجيبي",
    },
    {
        "q": "كم تبلغ نسبة الكافيين تقريباً في حبوب الأرابيكا مقارنة بالروبوستا؟",
        "options": ["النصف تقريباً", "الضعف", "المتساوية تماماً", "الربع"],
        "answer": "النصف تقريباً",
    },
    {
        "q": "تُعرف حبوب القهوة القادمة من جامايكا بأسعارها المرتفعة جداً وتنمو في جبال:",
        "options": [
            "البلو ماونتن",
            "الأنديز",
            "كليمنجارو",
            "الألب",
        ],
        "answer": "البلو ماونتن",
    },
    {
        "q": "ما السلالة التي تفرعت منها أغلب سلالات الأرابيكا الحديثة إلى جانب سلالة تيبيكا؟",
        "options": ["بوربون", "روبوستا", "باكاس", "سلا 28"],
        "answer": "بوربون",
    },
    {
        "q": "ما هي أكبر دولة منتجة لحبوب 'الروبوستا' في العالم؟",
        "options": ["فيتنام", "البرازيل", "الهند", "أوغندا"],
        "answer": "فيتنام",
    },
    {
        "q": "ماذا تُسمى الطفرة الجينية الطبيعية حيث تحتوي كرزة القهوة على حبة دائرية واحدة بدلاً من حبتين؟",
        "options": ["بيبيري (Peaberry)", "جيشا", "بوربون", "ماراغوجيبي"],
        "answer": "بيبيري (Peaberry)",
    },
    {
        "q": "أي لون تكون عليه حبة القهوة النيئة قبل إجراء عملية التحميص؟",
        "options": ["أخضر", "بني فاتح", "أصفر", "أسود"],
        "answer": "أخضر",
    },
    {
        "q": "أي من أدوات القهوة التالية تتبع أسلوب التقطير بالفلتر الورقي؟",
        "options": ["V60", "French Press", "Moka Pot", "Ibrik"],
        "answer": "V60",
    },
    {
        "q": "ما هي النسبة الذهبية (Ratio) القياسية الموصى بها عند تحضير V60؟",
        "options": ["1:15", "1:5", "1:30", "1:50"],
        "answer": "1:15",
    },
    {
        "q": "ما هي الأداة التي تستخدم ضغط الهواء اليدوي لاستخلاص القهوة خلال وقت قياسي؟",
        "options": ["Aeropress", "Chemex", "Syphon", "Kalita Wave"],
        "answer": "Aeropress",
    },
    {
        "q": "ما هي أداة التقطير التي تتميز بزجاجها السميك وفلترها السميك جداً لمنع أي زيوت؟",
        "options": ["Chemex", "V60", "Kalita", "Origami"],
        "answer": "Chemex",
    },
    {
        "q": "أداة 'الفرنش بريس' (French Press) تعتمد في تحضير القهوة على أسلوب:",
        "options": ["النقع الكلي", "التقطير بالتنقيط", "الضغط بالبخار", "الغلي المباشر"],
        "answer": "النقع الكلي",
    },
    {
        "q": "ما هو الاسم الشهير لوعاء إبريق تحضير القهوة التركية/العربية المكبوس بالحرارة؟",
        "options": ["الركوة (الكنكة)", "السيفون", "الموكابوت", "الفرنش بريس"],
        "answer": "الركوة (الكنكة)",
    },
    {
        "q": "أداة 'الموكابوت' (Moka Pot) تستخدم أي من العناصر التالية للتحضير على النار؟",
        "options": [
            "ضغط بخار الماء",
            "التقطير البطيء",
            "النقع في الماء البارد",
            "الكبس اليدوي",
        ],
        "answer": "ضغط بخار الماء",
    },
    {
        "q": "ما هو مشروب القهوة المستخلص بالماء البارد لفترة تنقع تمتد من 12 إلى 24 ساعة؟",
        "options": ["كولد برو (Cold Brew)", "أيس لاتيه", "أيس أمريكانو", "افوجاتو"],
        "answer": "كولد برو (Cold Brew)",
    },
    {
        "q": "أداة 'السيفون' (Syphon) تعتمد على فيزياء تمدد وانكماش الغازات وخصائص:",
        "options": [
            "تفريغ الهواء والضغط السلبي",
            "الضغط الهيدروليكي",
            "التصفية بالجاذبية فقط",
            "التجميد المباشر",
        ],
        "answer": "تفريغ الهواء والضغط السلبي",
    },
    {
        "q": "ما هي درجة الحرارة المثالية بالسيليزيوس لماء تحضير القهوة المقطرة عادة؟",
        "options": ["90 - 96 درجة", "100 درجة غليان", "70 - 75 درجة", "60 درجة"],
        "answer": "90 - 96 درجة",
    },
    {
        "q": "ما هو العنصر الأساسي الذي يميّز الفلات وايت عن الكابتشينو؟",
        "options": [
            "كثافة ورغوة الحليب (Microfoam)",
            "درجة تحميص البن",
            "درجة حرارة الماء",
            "نوع كوب التقديم",
        ],
        "answer": "كثافة ورغوة الحليب (Microfoam)",
    },
    {
        "q": "ما هو المشروب الكلاسيكي الذي يتكون فقط من شوط إسبريسو مع ماء ساخن؟",
        "options": ["أمريكانو", "لاتيه", "ماكياتو", "فلات وايت"],
        "answer": "أمريكانو",
    },
    {
        "q": "ماذا تُسمى الطبقة الذهبية الرغوية القادمة على سطح شوط الإسبريسو الطازج؟",
        "options": ["الكريما (Crema)", "الميكروفوم", "الماكياتو", "اللاتيه"],
        "answer": "الكريما (Crema)",
    },
    {
        "q": "مشروب 'الماكياتو' (Macchiato) الإيطالي تعني كلمة ماكياتو فيه:",
        "options": ["المُبقع / المتبوع بلمسة", "المثلج", "المعزز", "المحلى"],
        "answer": "المُبقع / المتبوع بلمسة",
    },
    {
        "q": "مشروب يتكون من شوط إسبريسو يُصب فوق كرة من آيس كريم الفانيليا:",
        "options": ["أفوجاتو", "موكاتشينو", "فرابوتشينو", "كون بانا"],
        "answer": "أفوجاتو",
    },
    {
        "q": "ما اسم شوط الإسبريسو القصير جداً والمركز الذي يُستخلص في نصف الوقت تقريباً؟",
        "options": ["ريستريتو (Ristretto)", "لونجو", "أمريكانو", "دوبليو"],
        "answer": "ريستريتو (Ristretto)",
    },
    {
        "q": "ما اسم شوط الإسبريسو المستخلص بكمية ماء أكثر ووقت أطول من المعتاد؟",
        "options": ["لونجو (Lungo)", "ريستريتو", "كورتادو", "ماكياتو"],
        "answer": "لونجو (Lungo)",
    },
    {
        "q": "ما اسم المقبض المعدني الذي يُوضع فيه البن المطحون ويُركب في ماكينة الإسبريسو؟",
        "options": ["بورتافلتر (Portafilter)", "الباسكت", "التامبر", "الدوزينج رينج"],
        "answer": "بورتافلتر (Portafilter)",
    },
    {
        "q": "ما هو الوزن التقريبي للجرعة المزدوجة (Double Shot) من البن المطحون للإسبريسو؟",
        "options": ["18 - 20 جرام", "5 - 8 جرام", "35 - 40 جرام", "50 جرام"],
        "answer": "18 - 20 جرام",
    },
    {
        "q": "كم يبلغ الضغط القياسي بالبار (Bar) لاستخلاص شوط الإسبريسو المثالي؟",
        "options": ["9 بار", "2 بار", "20 بار", "15 بار"],
        "answer": "9 بار",
    },
    {
        "q": "في معالجة القهوة 'المجففة' (Natural)، أين تُترك ثمرة الكرز لكي تجف؟",
        "options": [
            "على أسرّة تجفيف تحت الشمس بقلفتها",
            "داخل أحواض ماء",
            "في أفران حرارية",
            "تُدفن تحت الأرض",
        ],
        "answer": "على أسرّة تجفيف تحت الشمس بقلفتها",
    },
    {
        "q": "ما هي المعالجة التي يتم فيها إزالة القشرة الخارجية وغسل القهوة بالماء قبل التجفيف؟",
        "options": ["المغسولة (Washed)", "المجففة", "العسلية", "التخمير اللاهوائي"],
        "answer": "المغسولة (Washed)",
    },
    {
        "q": "ماذا يُطلق على صوت الفرقعة الأول لحبوب القهوة أثناء عملية التحميص؟",
        "options": [
            "الفرقعة الأولى (First Crack)",
            "الانفجار",
            "التكرمل",
            "الاستخلاص",
        ],
        "answer": "الفرقعة الأولى (First Crack)",
    },
    {
        "q": "أي درجـات التحميص التالية تُبرز حمضية القهوة وإيجاءاتها الفاكهية والزهرية بشكل أكبر؟",
        "options": [
            "التحميص الفاتح (Light Roast)",
            "التحميص الداكن",
            "التحميص المتوسط الداكن",
            "التحميص الإيطالي",
        ],
        "answer": "التحميص الفاتح (Light Roast)",
    },
    {
        "q": "التفاعل الكيميائي المسند لتحول سكريات القهوة للون البني وتغير طعمها في المحمصة يُسمى:",
        "options": [
            "تفاعل مايلارد (Maillard)",
            "الأكسدة",
            "التستر",
            "التخمر المائي",
        ],
        "answer": "تفاعل مايلارد (Maillard)",
    },
    {
        "q": "ما هي معالجة القهوة التي تجمع بين جزء من حلاوة المجففة ونظافة المغسولة؟",
        "options": ["العسلية (Honey)", "المغسولة بالكامل", "التجميد", "التجفيف السريع"],
        "answer": "العسلية (Honey)",
    },
    {
        "q": "ما العملية المتقدمة التي يُمنع فيها الأكسجين عن حبوب القهوة أثناء التخمر لإبراز النكهات؟",
        "options": [
            "التخمير اللاهوائي (Anaerobic)",
            "التجفيف الشمسي",
            "الغسيل الرغوي",
            "التحميص السريع",
        ],
        "answer": "التخمير اللاهوائي (Anaerobic)",
    },
    {
        "q": "ما اسم الغاز الأساسي الذي تنبعث منه حبوب القهوة بعد التحميص وتتطلب تريحها (Degassing)؟",
        "options": [
            "ثاني أكسيد الكربون (CO2)",
            "الأكسجين",
            "النيتروجين",
            "الهيدروجين",
        ],
        "answer": "ثاني أكسيد الكربون (CO2)",
    },
    {
        "q": "ماذا يحدث لحجم ونسبة مرارة حبة القهوة كلما زادت درجة تحميصها للداكن؟",
        "options": [
            "يكبر حجمها وتزيد مرارتها",
            "يصغر حجمها وتزيد حمضيتها",
            "لا يتغير حجمها",
            "تقل مرارتها وتزيد حلاوتها",
        ],
        "answer": "يكبر حجمها وتزيد مرارتها",
    },
    {
        "q": "ما هي المادة المسؤولة بشكل رئيسي عن الإحساس بالمرارة القوية في القهوة المحمصة؟",
        "options": ["مركبات الكافيين وحمض الكلوجنيك", "السكريات", "الماء", "الزيوت"],
        "answer": "مركبات الكافيين وحمض الكلوجنيك",
    },
    {
        "q": "ما اسم جلسة التذوق والتقييم المعيارية التي يعتمدها خبراء القهوة المختصة لتذوق العينات؟",
        "options": ["الرشف / الكابينج (Cupping)", "البارستا شو", "الفلترة", "التنقيط"],
        "answer": "الرشف / الكابينج (Cupping)",
    },
    {
        "q": "ما هي المنظمة العالمية المسؤولة عن وضع معايير القهوة المختصة وتصنيف الدرجات؟",
        "options": ["SCA", "FIFA", "ISO Coffee", "WBC"],
        "answer": "SCA",
    },
    {
        "q": "لتصنيف القهوة على أنها 'قهوة مختصة'، يجب أن تحصل على تقييم لا يقل عن كم درجة من 100؟",
        "options": ["80 درجة", "60 درجة", "90 درجة", "70 درجة"],
        "answer": "80 درجة",
    },
    {
        "q": "ما العجلة الشهيرة التي تُستخدم لتحديد وتوصيف إيحاءات ونكهات القهوة المختلفة؟",
        "options": [
            "عجلة نكهات القهوة (Flavor Wheel)",
            "دائرة الإسبريسو",
            "مخطط الفلترة",
            "بوصلة التحميص",
        ],
        "answer": "عجلة نكهات القهوة (Flavor Wheel)",
    },
    {
        "q": "ما الأداة التي تُستخدم لقياس نسبة المواد الصلبة الذائبة (TDS) في القهوة؟",
        "options": ["الرفراكتومتر (Refractometer)", "الجرام ميزان", "الترمومتر", "البارومتر"],
        "answer": "الرفراكتومتر (Refractometer)",
    },
    {
        "q": "ما هي المادة الناتجة عن تبخير الحليب والتي تمنحه الطعم السكري الحلو دون إضافة سكر؟",
        "options": ["سعادة اللاكتوز الكيميائية", "الكرياتين", "الكافيين", "الجلوكوز"],
        "answer": "سعادة اللاكتوز الكيميائية",
    },
    {
        "q": "ماذا يُقصد بمصطلح 'القوام' (Body) عند تذوق القهوة؟",
        "options": [
            "الشعور بوزن القهوة وملمسها في الفم",
            "درجة حرارة الفنجان",
            "رائحة البن قبل التحضير",
            "لون القهوة النهائي",
        ],
        "answer": "الشعور بوزن القهوة وملمسها في الفم",
    },
    {
        "q": "ما هو التأثير الكيميائي لغاز النيتروجين عندما يُحقن في القهوة (Nitro Cold Brew)؟",
        "options": [
            "يمنحها قواماً كريمياً ورغوة ناعمة جداً",
            "يجعلها تسخن تلقائياً",
            "يزيد مرارتها",
            "يلغي الكافيين تماماً",
        ],
        "answer": "يمنحها قواماً كريمياً ورغوة ناعمة جداً",
    },
    {
        "q": "ما اسم الاداة التي تُستخدم لضغط ودك البن المطحون داخل البورتافلتر بانتظام؟",
        "options": ["التامبر (Tamper)", "الموزع", "النيدل", "الباسكت"],
        "answer": "التامبر (Tamper)",
    },
    {
        "q": "ماذا يُطلق على ظاهرة مرور الماء من قنوات واسعة دون استخلاص القهوة بالتساوي؟",
        "options": ["القنواتية (Channeling)", "التشبع", "التنقيب", "التكتل"],
        "answer": "القنواتية (Channeling)",
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
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

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
                </div>
            """,
                unsafe_allow_html=True,
            )

        st.markdown(
            "<div style='margin-top: 25px;'></div>", unsafe_allow_html=True
        )
        if st.button("PLAY AGAIN 🔄"):
            st.session_state.game_started = False
            st.rerun()
