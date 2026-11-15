
import streamlit as st
import qrcode
from io import BytesIO

# ==================================================
# CONFIG
# ==================================================

st.set_page_config(
    page_title="JAZIF | Community Space",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# JAZIF BRAND COLORS
# ==================================================

DARK = "#263D32"
GREEN = "#496653"
SOFT_GREEN = "#E7EDE5"
BG = "#F7F7F2"
WHITE = "#FFFFFF"
TEXT = "#263D32"
MUTED = "#66766A"
BORDER = "#E2E8DF"
ACCENT = "#B6C5B5"

# ==================================================
# COMPLETE MOBILE-FIRST CSS
# ==================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap');

:root {
    --dark: #263D32;
    --green: #496653;
    --soft: #E7EDE5;
    --bg: #F7F7F2;
    --white: #FFFFFF;
    --text: #263D32;
    --muted: #66766A;
    --border: #E2E8DF;
}

html, body, [class*="css"], button, input, textarea {
    font-family: 'IBM Plex Sans Arabic', sans-serif !important;
}

.stApp {
    background: var(--bg) !important;
    color: var(--text) !important;
}

.block-container {
    max-width: 1100px;
    padding: 1rem 1.2rem 3rem;
}

header, footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

/* GLOBAL TEXT */

.stApp p,
.stApp li,
.stApp label,
.stApp span,
.stMarkdown,
.stText,
.stCaption {
    color: var(--text);
}

h1, h2, h3, h4, h5 {
    color: var(--dark) !important;
    font-weight: 700 !important;
    line-height: 1.5 !important;
}

p {
    line-height: 1.8;
}

/* HEADER */

.brand {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0 18px;
}

.brand-name {
    color: var(--dark);
    font-size: 29px;
    font-weight: 700;
    letter-spacing: 1px;
}

.brand-sub {
    color: var(--muted);
    font-size: 12px;
    margin-right: 6px;
}

.brand-icon {
    font-size: 27px;
}

/* NAVIGATION */

div[data-testid="stRadio"] {
    width: 100%;
}

div[data-testid="stRadio"] > label {
    display: none;
}

div[data-testid="stRadio"] > div {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    width: 100%;
}

div[data-testid="stRadio"] label {
    background: #FFFFFF !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 8px 13px !important;
    flex: 1 1 auto;
    justify-content: center;
    min-width: 0;
    margin: 0 !important;
}

div[data-testid="stRadio"] label p,
div[data-testid="stRadio"] label span {
    color: var(--dark) !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    opacity: 1 !important;
}

div[data-testid="stRadio"] label:has(input:checked) {
    background: var(--dark) !important;
    border-color: var(--dark) !important;
}

div[data-testid="stRadio"] label:has(input:checked) p,
div[data-testid="stRadio"] label:has(input:checked) span {
    color: #FFFFFF !important;
}

/* Hide radio circles */
div[data-testid="stRadio"] label > div:first-child {
    display: none !important;
}

/* HERO */

.hero {
    background: var(--dark);
    color: #FFFFFF;
    padding: 34px 27px;
    border-radius: 24px;
    margin: 22px 0 30px;
}

.hero h1 {
    color: #FFFFFF !important;
    font-size: 32px;
    margin-top: 16px;
}

.hero p {
    color: #E7EDE5 !important;
    font-size: 16px;
}

.hero-tag {
    display: inline-block;
    background: #E7EDE5;
    color: #263D32 !important;
    padding: 7px 14px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 600;
}

/* SECTION TITLES */

.section-title {
    font-size: 24px;
    font-weight: 700;
    color: var(--dark);
    margin: 30px 0 10px;
}

.section-description {
    color: var(--muted);
    font-size: 14px;
    margin-bottom: 18px;
}

/* CARDS */

.info-card {
    background: #FFFFFF;
    padding: 20px;
    border: 1px solid var(--border);
    border-radius: 19px;
    margin-bottom: 12px;
    color: var(--dark);
}

.community-card {
    background: #FFFFFF;
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 19px;
    margin-bottom: 12px;
}

.community-icon {
    font-size: 32px;
}

.card-description {
    color: var(--muted);
    font-size: 13px;
}

.tag {
    display: inline-block;
    background: var(--soft);
    color: var(--dark);
    padding: 6px 12px;
    border-radius: 30px;
    font-size: 12px;
}

/* MAP */

.area {
    background: #E7EDE5;
    padding: 22px 12px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid #D5E0D4;
    min-height: 145px;
}

.area.outdoor {
    background: #E0E9DD;
}

.area h2 {
    color: var(--dark) !important;
    font-size: 27px;
}

/* EVENTS */

.event-card {
    background: #FFFFFF;
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 17px;
    margin-bottom: 12px;
}

/* BUTTONS */

.stButton button {
    background: var(--dark) !important;
    color: #FFFFFF !important;
    border: 1px solid var(--dark) !important;
    border-radius: 13px !important;
    min-height: 43px;
    font-weight: 600 !important;
    transition: 0.2s ease;
}

.stButton button p,
.stButton button span {
    color: #FFFFFF !important;
}

.stButton button:hover {
    background: var(--green) !important;
    border-color: var(--green) !important;
}

/* TABS */

div[data-testid="stTabs"] {
    margin-top: 12px;
}

div[data-testid="stTabs"] button {
    color: var(--muted) !important;
    font-weight: 600 !important;
    font-size: 13px !important;
}

div[data-testid="stTabs"] button[aria-selected="true"] {
    color: var(--dark) !important;
}

div[data-testid="stTabs"] [data-baseweb="tab-highlight"] {
    background-color: var(--green) !important;
}

/* INPUTS */

.stTextInput input,
.stTextArea textarea {
    background: #FFFFFF !important;
    color: var(--dark) !important;
    border: 1px solid #C9D5C9 !important;
    border-radius: 12px !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #829087 !important;
}

.stCheckbox label p {
    color: var(--dark) !important;
}

/* CONTAINERS */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFFFF;
    border: 1px solid var(--border) !important;
    border-radius: 18px !important;
}

/* METRICS */

div[data-testid="stMetric"] {
    background: #FFFFFF;
    padding: 13px;
    border: 1px solid var(--border);
    border-radius: 15px;
}

div[data-testid="stMetricLabel"] {
    color: var(--muted) !important;
}

div[data-testid="stMetricValue"] {
    color: var(--dark) !important;
}

/* CAPTIONS */

div[data-testid="stCaptionContainer"] p {
    color: var(--muted) !important;
    font-size: 12px;
}

/* ALERTS */

div[data-testid="stAlert"] {
    border-radius: 14px;
}

/* FOOTER */

.footer {
    text-align: center;
    padding: 24px 10px;
    color: var(--muted);
    font-size: 13px;
    margin-top: 30px;
}

/* MOBILE */

@media (max-width: 600px) {
    .block-container {
        padding: 0.6rem 0.85rem 2.5rem;
    }

    .brand-name {
        font-size: 25px;
    }

    .hero {
        padding: 24px 18px;
        border-radius: 19px;
        margin-top: 15px;
    }

    .hero h1 {
        font-size: 25px;
    }

    .hero p {
        font-size: 14px;
    }

    .section-title {
        font-size: 21px;
    }

    div[data-testid="stRadio"] > div {
        gap: 5px;
    }

    div[data-testid="stRadio"] label {
        padding: 9px 5px !important;
        border-radius: 10px !important;
    }

    div[data-testid="stRadio"] label p {
        font-size: 11px !important;
    }

    .community-card {
        padding: 15px;
    }

    .area {
        min-height: 135px;
        padding: 16px 7px;
    }

    .area h2 {
        font-size: 22px;
    }

    div[data-testid="stTabs"] button {
        font-size: 11px !important;
        padding: 8px 5px !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ==================================================
# DATA
# ==================================================

communities = {
    "اليوغا": {
        "icon": "🧘🏻‍♀️",
        "description": "مساحة للحركة والهدوء والتوازن.",
        "bring": ["ملابس مريحة", "حصيرة يوغا", "قارورة ماء"],
        "ideas": [
            "جلسة يوغا عند الغروب",
            "Morning Yoga",
            "يوغا وتأمل"
        ]
    },
    "الفنون": {
        "icon": "🎨",
        "description": "مجتمع يجمع محبي الفن والتجارب الإبداعية.",
        "bring": ["ملابس مناسبة للتلوين", "دفتر رسم", "أدواتك الفنية"],
        "ideas": [
            "رسم جماعي",
            "Art & Coffee",
            "ورشة ألوان مائية"
        ]
    },
    "الفخار": {
        "icon": "🏺",
        "description": "اكتشف متعة صناعة الأشياء بيديك.",
        "bring": ["ملابس مريحة", "مريلة", "روح إبداعية"],
        "ideas": [
            "صناعة أكواب",
            "ورشة تشكيل الطين",
            "Pottery & Coffee"
        ]
    },
    "الخيول": {
        "icon": "🐎",
        "description": "مجتمع لمحبي الخيل والتجارب الخارجية.",
        "bring": ["ملابس مناسبة", "حذاء مغلق", "قارورة ماء"],
        "ideas": [
            "لقاء لمحبي الخيل",
            "جلسة تعريفية",
            "تجربة ركوب"
        ]
    },
    "الورش": {
        "icon": "🛠️",
        "description": "نتعلم أشياء جديدة ونتشارك المهارات.",
        "bring": ["دفتر ملاحظات", "قلم", "حاسوب عند الحاجة"],
        "ideas": [
            "ورشة ابتكار",
            "تبادل المهارات",
            "لقاء تعليمي"
        ]
    }
}

events = [
    {
        "name": "Morning Yoga",
        "type": "اليوغا",
        "date": "20 نوفمبر",
        "place": "الحديقة الخارجية",
        "seats": 4,
        "total": 12
    },
    {
        "name": "Art & Coffee",
        "type": "الفنون",
        "date": "22 نوفمبر",
        "place": "المساحة الداخلية",
        "seats": 7,
        "total": 15
    },
    {
        "name": "Pottery Workshop",
        "type": "الفخار",
        "date": "25 نوفمبر",
        "place": "المساحة الداخلية",
        "seats": 3,
        "total": 10
    }
]


# ==================================================
# SESSION STATE
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "الرئيسية"

if "community" not in st.session_state:
    st.session_state.community = "اليوغا"

if "ideas" not in st.session_state:
    st.session_state.ideas = []

if "votes" not in st.session_state:
    st.session_state.votes = {}

if "interests" not in st.session_state:
    st.session_state.interests = []

if "accepted" not in st.session_state:
    st.session_state.accepted = False


# ==================================================
# HEADER
# ==================================================

st.markdown("""
<div class="brand">
    <div>
        <span class="brand-name">JAZIF</span>
        <span class="brand-sub">COMMUNITY SPACE</span>
    </div>
    <div class="brand-icon">🌿</div>
</div>
""", unsafe_allow_html=True)

pages = ["الرئيسية", "المجتمعات", "تذاكري", "حسابي"]

selected_page = st.radio(
    "Navigation",
    pages,
    index=pages.index(st.session_state.page),
    horizontal=True,
    label_visibility="collapsed",
    key="navigation"
)

st.session_state.page = selected_page

st.divider()


# ==================================================
# HOME PAGE
# ==================================================

if st.session_state.page == "الرئيسية":

    st.markdown("""
    <div class="hero">
        <span class="hero-tag">A SPACE TO CONNECT</span>
        <h1>🌿 أهلاً بك في جازف</h1>
        <p>
        مساحة تجمع الناس والأفكار والتجارب.
        مكان نلتقي فيه، نتعلم، ونصنع ذكريات جديدة.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">اكتشف جازف</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'مساحة مرنة تتغير بتغير الأشخاص والأنشطة والمجتمعات.'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="info-card">
            <div style="font-size:30px;">🧘🏻‍♀️</div>
            <b>Yoga</b>
            <div class="card-description">حركة وهدوء</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="info-card">
            <div style="font-size:30px;">🎨</div>
            <b>Art</b>
            <div class="card-description">فن وإبداع</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="info-card">
            <div style="font-size:30px;">🛠️</div>
            <b>Workshops</b>
            <div class="card-description">تعلم وتجربة</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">خريطة المساحة</div>',
        unsafe_allow_html=True
    )

    st.caption("اكتشف مناطق جازف والتجارب التي تقام فيها.")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="area">
            <div style="font-size:28px;">🏡</div>
            <b>المساحة الداخلية</b>
            <h2>105 m²</h2>
            <small>ورش واجتماعات وتجارب داخلية</small>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="area outdoor">
            <div style="font-size:28px;">🌳</div>
            <b>الحديقة الخارجية</b>
            <h2>533 m²</h2>
            <small>يوغا وفعاليات وتجارب خارجية</small>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">التجارب القادمة</div>',
        unsafe_allow_html=True
    )

    for event in events:

        with st.container(border=True):

            st.markdown(f"### {event['name']}")

            st.caption(
                f"{event['type']}  ·  {event['date']}  ·  {event['place']}"
            )

            st.write(
                f"🪑 المقاعد المتبقية: "
                f"{event['seats']} من {event['total']}"
            )

            if st.button(
                "استكشف التجربة",
                key=f"event_{event['name']}",
                use_container_width=True
            ):
                st.session_state.community = event["type"]
                st.session_state.page = "المجتمعات"
                st.rerun()

    if st.button(
        "اكتشف جميع المجتمعات ←",
        use_container_width=True
    ):
        st.session_state.page = "المجتمعات"
        st.rerun()


# ==================================================
# COMMUNITIES PAGE
# ==================================================

elif st.session_state.page == "المجتمعات":

    st.title("مجتمعات جازف 🌿")

    st.write(
        "كل مجتمع يبدأ باهتمام، وينمو بالأشخاص الذين يجمعهم."
    )

    st.markdown(
        '<div class="section-title">اكتشف مجتمعاتنا</div>',
        unsafe_allow_html=True
    )

    for name, data in communities.items():

        with st.container(border=True):

            st.markdown(
                f"### {data['icon']} {name}"
            )

            st.caption(data["description"])

            if st.button(
                f"اكتشف مجتمع {name}",
                key=f"open_{name}",
                use_container_width=True
            ):
                st.session_state.community = name
                st.rerun()

    st.divider()

    name = st.session_state.community
    data = communities[name]

    st.markdown(f"## {data['icon']} مجتمع {name}")
    st.write(data["description"])

    tab1, tab2, tab3 = st.tabs([
        "نظرة عامة",
        "مختبر الأفكار",
        "مساحة المجتمع"
    ])

    # ----------------------------------------------
    # OVERVIEW
    # ----------------------------------------------

    with tab1:

        st.subheader("عن المجتمع")

        st.write(data["description"])

        st.markdown("### من تجاربنا السابقة")

        c1, c2 = st.columns(2)

        with c1:
            st.markdown("""
            <div class="info-card">
                <div style="font-size:28px;">📸</div>
                <b>تجربة سابقة 01</b>
                <div class="card-description">تضاف الصور لاحقاً</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="info-card">
                <div style="font-size:28px;">📸</div>
                <b>تجربة سابقة 02</b>
                <div class="card-description">تضاف الصور لاحقاً</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### What to Bring 🎒")

        st.caption(
            f"الأشياء المقترحة لمجتمع {name}"
        )

        for item in data["bring"]:
            st.checkbox(
                item,
                key=f"bring_{name}_{item}"
            )

        st.divider()

        if st.button(
            "سجل اهتمامك بالمجتمع",
            key=f"interest_{name}",
            use_container_width=True
        ):

            if name not in st.session_state.interests:
                st.session_state.interests.append(name)

            st.success("تم تسجيل اهتمامك بنجاح! 🌿")

    # ----------------------------------------------
    # IDEA LAB
    # ----------------------------------------------

    with tab2:

        st.subheader("Idea Lab 💡")

        st.write(
            "شارك أفكارك وصوّت على التجارب التي ترغب برؤيتها."
        )

        with st.form(f"idea_form_{name}"):

            new_idea = st.text_input(
                "ما الفكرة التي تقترحها؟",
                placeholder="اكتب فكرتك هنا..."
            )

            submitted = st.form_submit_button(
                "＋ أضف اقتراحك",
                use_container_width=True
            )

            if submitted and new_idea.strip():

                st.session_state.ideas.append({
                    "community": name,
                    "idea": new_idea.strip()
                })

                st.success("تمت إضافة فكرتك!")

        st.divider()

        st.markdown("### أفكار المجتمع")

        for i, idea in enumerate(data["ideas"]):

            key = f"{name}_{i}"

            with st.container(border=True):

                st.write(f"💡 {idea}")

                votes = st.session_state.votes.get(key, 0)

                st.caption(f"الأصوات: {votes}")

                if st.button(
                    "👍 صوّت",
                    key=f"vote_{key}"
                ):

                    st.session_state.votes[key] = votes + 1
                    st.rerun()

        for i, idea in enumerate(st.session_state.ideas):

            if idea["community"] == name:

                with st.container(border=True):
                    st.write("💡 " + idea["idea"])

        st.divider()

        st.subheader("Find a Co-host 🤝")

        st.write(
            "هل عندك فكرة وتبحث عن شخص يشاركك تنظيمها؟"
        )

        if st.button(
            "ابحث عن شريك لتنظيم الفكرة",
            use_container_width=True
        ):
            st.info(
                "سيتم تطوير نظام البحث عن Co-host لاحقاً."
            )

    # ----------------------------------------------
    # COMMUNITY SPACE
    # ----------------------------------------------

    with tab3:

        st.subheader("Community Space 🔒")

        st.write(
            "مساحة خاصة للتواصل بين أعضاء المجتمع."
        )

        accepted = st.toggle(
            "محاكاة: تم قبول تسجيلي في المجتمع",
            value=st.session_state.accepted,
            key=f"accepted_{name}"
        )

        if accepted:

            st.success("مرحباً بك في مساحة المجتمع!")

            st.markdown("### Community Chat")

            message = st.text_area(
                "اكتب رسالتك",
                placeholder="شاركنا أفكارك..."
            )

            if st.button(
                "إرسال الرسالة",
                use_container_width=True
            ):

                if message.strip():
                    st.success("تم إرسال الرسالة التجريبية.")

            st.divider()

            st.markdown("### قنوات التواصل")

            st.markdown("""
            - 💬 مجموعة WhatsApp (رابط تجريبي)
            - ✉️ البريد الإلكتروني للمجتمع
            """)

        else:

            st.info(
                "🔒 هذه المساحة متاحة للأعضاء المقبولين فقط."
            )


# ==================================================
# DIGITAL PASS
# ==================================================

elif st.session_state.page == "تذاكري":

    st.title("Digital Pass 🎟️")

    st.write("تذكرتك الرقمية للدخول إلى جازف.")

    qr = qrcode.make("JAZIF-DEMO-MEMBER-001")

    buffer = BytesIO()

    qr.save(buffer, format="PNG")

    with st.container(border=True):

        st.markdown(
            "<h2 style='text-align:center;color:#263D32'>JAZIF 🌿</h2>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<p style='text-align:center;color:#66766A'>"
            "MEMBER DIGITAL PASS</p>",
            unsafe_allow_html=True
        )

        st.image(
            buffer.getvalue(),
            width=190
        )

        st.markdown(
            "<h3 style='text-align:center;color:#263D32'>"
            "Noura Member</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<p style='text-align:center;color:#66766A'>"
            "Member ID: JZ-001-DEMO</p>",
            unsafe_allow_html=True
        )

        st.success("Active Member · Demo")

    st.caption(
        "هذا QR تجريبي للتوضيح فقط، وليس تصريح دخول حقيقي."
    )


# ==================================================
# ACCOUNT
# ==================================================

elif st.session_state.page == "حسابي":

    st.title("حسابي 👤")

    with st.container(border=True):

        st.markdown("## 👩🏻")

        st.subheader("Noura Member")

        st.caption("Jazif Community Member")

        st.markdown(
            '<span class="tag">Active Member</span>',
            unsafe_allow_html=True
        )

    st.markdown("### Badges 🏅")

    b1, b2, b3 = st.columns(3)

    b1.metric("Explorer", "01")
    b2.metric("Ideas", "03")
    b3.metric("Events", "02")

    st.markdown("### مجتمعاتي")

    if st.session_state.interests:

        for community in st.session_state.interests:
            st.write(
                communities[community]["icon"] + " " + community
            )

    else:
        st.caption("لم تسجلي اهتمامك بأي مجتمع حتى الآن.")

    st.divider()

    if st.button(
        "🎟️ عرض التذاكر الرقمية",
        use_container_width=True
    ):

        st.session_state.page = "تذاكري"
        st.rerun()

    if st.button(
        "🌿 تصفح المجتمعات",
        use_container_width=True
    ):

        st.session_state.page = "المجتمعات"
        st.rerun()


# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<div class="footer">
    <b style="color:#263D32;">JAZIF COMMUNITY SPACE 🌿</b>
    <br>
    A place to connect, create & belong.
</div>
""", unsafe_allow_html=True)
