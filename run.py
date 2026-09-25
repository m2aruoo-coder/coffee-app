import random
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="DRIP | Coffee Challenge",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# --- Custom DRIP Branding UI CSS ---
def inject_drip_theme():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@600;700;800;900&family=Montserrat:wght@800;900&display=swap');

        /* Light Clean Canvas like DRIP Website */
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Cairo', 'Montserrat', sans-serif;
            background-color: #f4f9fd !important;
            color: #0f172a !important;
        }

        #MainMenu, footer, header {visibility: hidden;}

        /* Top Marquee Banner */
        .marquee-banner {
            background-color: #0f172a;
            color: #ffffff;
            padding: 8px 0;
            text-align: center;
            font-family: 'Montserrat', sans-serif;
            font-size: 0.8rem;
            font-weight: 800;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin: -60px -20px 25px -20px;
        }
        .marquee-banner span {
            color: #38bdf8;
        }

        /* Header UI matching DRIP Logo */
        .brand-header {
            text-align: center;
            padding: 10px 0 20px 0;
        }

        .brand-title {
            font-family: 'Montserrat', sans-serif;
            font-size: 3.5rem;
            font-weight: 900;
            color: #38bdf8;
            letter-spacing: -1px;
            line-height: 0.9;
            text-transform: uppercase;
            margin: 0;
            text-shadow: 3px 3px 0px #f472b6;
        }

        .brand-subtitle {
            font-family: 'Montserrat', sans-serif;
            font-size: 0.9rem;
            letter-spacing: 4px;
            color: #0f172a;
            margin-top: 8px;
            font-weight: 800;
            text-transform: uppercase;
        }

        .slogan-tag {
            background-color: #e0f2fe;
            color: #0284c7;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 800;
            display: inline-block;
            margin-top: 10px;
        }

        /* Quiz Card */
        .drip-card {
            background: #ffffff !important;
            padding: 30px 25px;
            border-radius: 24px;
            box-shadow: 0 10px 30px rgba(56, 189, 248, 0.15);
            border: 2px solid #bae6fd;
            margin-bottom: 25px;
            text-align: center;
            direction: rtl;
        }

        .drip-card h4 {
            font-family: 'Montserrat', sans-serif;
            color: #f472b6 !important;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin: 0 0 12px 0;
            font-weight: 900;
        }

        .drip-card p {
            font-family: 'Cairo', sans-serif;
            color: #0f172a !important;
            font-size: 1.35rem !important;
            font-weight: 800 !important;
            line-height: 1.6;
            margin: 0;
        }

        /* DRIP Styled Buttons */
        div.stButton > button {
            width: 100%;
            border-radius: 16px;
            height: 58px;
            background-color: #ffffff !important;
            color: #0f172a !important;
            border: 2px solid #e2e8f0 !important;
            font-family: 'Cairo', sans-serif !important;
            font-weight: 800 !important;
            font-size: 1.1rem !important;
            transition: all 0.25s ease;
            margin-bottom: 10px;
            direction: rtl;
            box-shadow: 0 4px 10px rgba(0,0,0,0.03);
        }

        div.stButton > button:hover {
            background-color: #38bdf8 !important;
            color: #ffffff !important;
            border-color: #38bdf8 !important;
            box-shadow: 0 8px 20px rgba(56, 189, 248, 0.35);
            transform: translateY(-2px);
        }

        /* Reward & Result Cards */
        .reward-card {
            background: #ffffff !important;
            border: 3px solid #38bdf8;
            padding: 35px 25px;
            border-radius: 28px;
            text-align: center;
            margin-top: 15px;
            box-shadow: 0 15px 35px rgba(56, 189, 248, 0.2);
        }

        .promo-badge {
            background: linear-gradient(135deg, #38bdf8 0%, #f472b6 100%);
            padding: 14px 32px;
            border-radius: 16px;
            display: inline-block;
            font-weight: 900;
            font-size: 1.6rem;
            color: #ffffff;
            letter-spacing: 3px;
            margin-top: 18px;
            box-shadow: 0 8px 20px rgba(244, 114, 182, 0.3);
            font-family: 'Montserrat', sans-serif;
        }

        .status-card {
            background: #ffffff !important;
            border: 3px solid #f472b6;
            padding: 35px 25px;
            border-radius: 28px;
            text-align: center;
            margin-top: 15px;
            box-shadow: 0 15px 35px rgba(244, 114, 182, 0.15);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


inject_drip_theme()

# --- Arabic 60 Questions Bank ---
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

# --- Top Banner ---
st.markdown(
    """
    <div class="marquee-banner">
        RESPECT THE BEAN • TRUST THE DRIP • <span>100% ARABICA</span>
    </div>
""",
    unsafe_allow_html=True,
)

# --- Header ---
st.markdown(
    """
    <div class="brand-header">
        <div class="brand-title">DRIP</div>
        <div class="brand-subtitle">Specialty Coffee</div>
        <div class="slogan-tag">NO SLEEP, JUST DRIP ☕</div>
    </div>
""",
    unsafe_allow_html=True,
)

# --- Session State Initializations ---
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "current_q_idx" not in st.session_state:
    st.session_state.current_q_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "used_questions" not in st.session_state:
    st.session_state.used_questions = []

# --- Landing Screen ---
if not st.session_state.game_started:
    st.markdown(
        """
        <div class="drip-card">
            <h3 style="color: #0f172a; margin-top: 0; font-weight: 900;">جاهز تتحدى معلوماتك وتكسب خصمك؟ 🎯</h3>
            <p style="font-size: 1.05rem !important; color: #64748b !important; font-weight: 600 !important;">جاوب 3 أسئلة صح واكسب كود خصم فوري عند طلبك القادم من DRIP Coffee!</p>
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
        st.rerun()

# --- Quiz Screen ---
else:
    q_idx = st.session_state.current_q_idx

    if q_idx < len(st.session_state.used_questions):
        current_q = st.session_state.used_questions[q_idx]

        # Display Question Card
        st.markdown(
            f"""
            <div class="drip-card">
                <h4>السؤال {q_idx + 1} من 3</h4>
                <p>{current_q['q']}</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

        # Options Buttons
        for opt in current_q["options"]:
            if st.button(opt, key=f"btn_{q_idx}_{opt}"):
                if opt == current_q["answer"]:
                    st.session_state.score += 1
                st.session_state.current_q_idx += 1
                st.rerun()

    # --- Results & Voucher Screen ---
    else:
        score = st.session_state.score

        if score == 3:
            st.balloons()
            promo_code = f"DRIP-{random.randint(1000, 9999)}"

            st.markdown(
                f"""
                <div class="reward-card">
                    <h2 style="color: #38bdf8; margin: 0; font-family: 'Montserrat', sans-serif; font-size: 2rem;">مبروك! النتيجة كاملة (3/3) 🎉</h2>
                    <p style="font-size: 1.2rem; font-weight: 800; color: #0f172a; margin: 15px 0;">خصم 20% على مشروبك المفضل من DRIP</p>
                    <p style="font-size: 0.9rem; color: #64748b;">قّم الكود التالي للبارستا أو استخدمه عند الطلب:</p>
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
                    <h2 style="color: #f472b6; margin: 0; font-family: 'Montserrat', sans-serif; font-size: 1.8rem;">محاولة جيدة! ☕</h2>
                    <p style="font-size: 1.2rem; color: #0f172a; margin-top: 15px;">نيجتك: <b>{score} من 3</b></p>
                    <p style="font-size: 0.95rem; color: #64748b;">تحتاج للإجابة على جميع الأسئلة 3/3 بشكل صحيح للحصول على كود الخصم.</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

        st.markdown(
            "<div style='margin-top: 25px;'></div>", unsafe_allow_html=True
        )
        if st.button("جرب مرة أخرى 🔄"):
            st.session_state.game_started = False
            st.rerun()
