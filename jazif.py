import streamlit as st
import qrcode
from io import BytesIO

# =========================================================
# JAZIF COMMUNITY SPACE — MOBILE-FIRST DEMO
# =========================================================

st.set_page_config(
    page_title="JAZIF | Community Space",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------------- COLORS -------------------------

DARK = "#263D32"
GREEN = "#496653"
SOFT_GREEN = "#E7EDE5"
BG = "#F7F7F2"
WHITE = "#FFFFFF"
MUTED = "#66766A"
BORDER = "#E2E8DF"

# ---------------------- SESSION STATE ---------------------

defaults = {
    "page": "الرئيسية",
    "community": "اليوغا",
    "ideas": [],
    "votes": {},
    "interests": [],
    "messages": {},
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ----------------------------- CSS -------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap');

    :root {
        --dark: #263D32;
        --green: #496653;
        --soft: #E7EDE5;
        --bg: #F7F7F2;
        --white: #FFFFFF;
        --muted: #66766A;
        --border: #E2E8DF;
    }

    html, body, [class*="css"], button, input, textarea {
        font-family: 'IBM Plex Sans Arabic', sans-serif !important;
    }

    .stApp {
        background: var(--bg) !important;
        color: var(--dark) !important;
    }

    /* Hide Streamlit's default chrome, but keep the app usable */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    #MainMenu, footer {
        visibility: hidden;
    }

    /* Main page spacing: reserve room for the fixed site header */
    .block-container {
        max-width: 1100px;
        padding: 158px 1.2rem 3rem !important;
    }

    .stApp p, .stApp li, .stApp label, .stMarkdown {
        color: var(--dark);
    }

    h1, h2, h3, h4 {
        color: var(--dark) !important;
        font-weight: 700 !important;
        line-height: 1.5 !important;
    }

    p { line-height: 1.8; }

    /* FIXED HEADER: logo + navigation stay together */
    .st-key-site_header {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        z-index: 999999 !important;
        box-sizing: border-box !important;
        background: var(--bg) !important;
        padding: 12px max(14px, calc((100vw - 1060px) / 2)) 10px !important;
        border-bottom: 1px solid var(--border) !important;
        box-shadow: 0 4px 14px rgba(38, 61, 50, 0.08) !important;
    }

    .brand {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 4px 0 9px;
    }

    .brand-name {
        color: var(--dark);
        font-size: 27px;
        font-weight: 700;
        letter-spacing: 1px;
    }

    .brand-sub {
        color: var(--muted);
        font-size: 12px;
        margin-right: 6px;
    }

    .brand-icon { font-size: 25px; }

    /* Navigation radio group */
    .st-key-site_header div[data-testid="stRadio"] {
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        background: transparent !important;
    }

    .st-key-site_header div[data-testid="stRadio"] > label {
        display: none !important;
    }

    .st-key-site_header div[data-testid="stRadio"] > div {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 7px !important;
        width: 100% !important;
    }

    .st-key-site_header div[data-testid="stRadio"] label {
        flex: 1 1 0 !important;
        min-width: 0 !important;
        justify-content: center !important;
        background: var(--white) !important;
        border: 1px solid var(--border) !important;
        border-radius: 12px !important;
        padding: 8px 3px !important;
        margin: 0 !important;
    }

    .st-key-site_header div[data-testid="stRadio"] label p,
    .st-key-site_header div[data-testid="stRadio"] label span {
        color: var(--dark) !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        white-space: nowrap !important;
        opacity: 1 !important;
    }

    .st-key-site_header div[data-testid="stRadio"] label:has(input:checked) {
        background: var(--dark) !important;
        border-color: var(--dark) !important;
    }

    .st-key-site_header div[data-testid="stRadio"] label:has(input:checked) p,
    .st-key-site_header div[data-testid="stRadio"] label:has(input:checked) span {
        color: #FFFFFF !important;
    }

    .st-key-site_header div[data-testid="stRadio"] label > div:first-child,
    .st-key-site_header div[data-testid="stRadio"] div[role="radio"] > div:first-child {
        display: none !important;
    }

    /* Hero */
    .hero {
        background: var(--dark);
        color: #FFFFFF;
        padding: 30px 24px;
        border-radius: 22px;
        margin: 12px 0 28px;
    }

    .hero h1 {
        color: #FFFFFF !important;
        font-size: 30px;
        margin-top: 14px;
    }

    .hero p {
        color: #E7EDE5 !important;
        font-size: 15px;
    }

    .hero-tag {
        display: inline-block;
        background: var(--soft);
        color: var(--dark) !important;
        padding: 7px 13px;
        border-radius: 30px;
        font-size: 12px;
        font-weight: 600;
    }

    .section-title {
        font-size: 23px;
        font-weight: 700;
        color: var(--dark);
        margin: 28px 0 8px;
    }

    .section-description {
        color: var(--muted);
        font-size: 14px;
        margin-bottom: 16px;
    }

    .info-card, .community-card {
        background: var(--white);
        padding: 18px;
        border: 1px solid var(--border);
        border-radius: 18px;
        margin-bottom: 12px;
        color: var(--dark);
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

    .area {
        background: var(--soft);
        padding: 20px 10px;
        border-radius: 17px;
        text-align: center;
        border: 1px solid #D5E0D4;
        min-height: 140px;
    }

    .area.outdoor { background: #E0E9DD; }

    .area h2 {
        color: var(--dark) !important;
        font-size: 25px;
    }

    .stButton button {
        background: var(--dark) !important;
        color: #FFFFFF !important;
        border: 1px solid var(--dark) !important;
        border-radius: 12px !important;
        min-height: 43px;
        font-weight: 600 !important;
    }

    .stButton button p, .stButton button span {
        color: #FFFFFF !important;
    }

    .stButton button:hover {
        background: var(--green) !important;
        border-color: var(--green) !important;
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

    .stTextInput input, .stTextArea textarea {
        background: var(--white) !important;
        color: var(--dark) !important;
        border: 1px solid #C9D5C9 !important;
        border-radius: 12px !important;
    }

    .stTextInput input::placeholder, .stTextArea textarea::placeholder {
        color: #829087 !important;
    }

    .stCheckbox label p { color: var(--dark) !important; }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: var(--white);
        border: 1px solid var(--border) !important;
        border-radius: 17px !important;
    }

    div[data-testid="stMetric"] {
        background: var(--white);
        padding: 12px;
        border: 1px solid var(--border);
        border-radius: 14px;
    }

    div[data-testid="stMetricLabel"],
    div[data-testid="stCaptionContainer"] p {
        color: var(--muted) !important;
    }

    div[data-testid="stMetricValue"] { color: var(--dark) !important; }

    .footer {
        text-align: center;
        padding: 24px 10px;
        color: var(--muted);
        font-size: 13px;
        margin-top: 28px;
    }

    @media (max-width: 600px) {
        .block-container {
            padding: 145px 0.85rem 2.5rem !important;
        }

        .st-key-site_header {
            padding: 9px 9px 9px !important;
        }

        .brand {
            padding: 2px 3px 7px;
        }

        .brand-name { font-size: 24px; }
        .brand-sub { font-size: 10px; }
        .brand-icon { font-size: 23px; }

        .st-key-site_header div[data-testid="stRadio"] > div {
            gap: 5px !important;
        }

        .st-key-site_header div[data-testid="stRadio"] label {
            padding: 8px 2px !important;
            border-radius: 10px !important;
        }

        .st-key-site_header div[data-testid="stRadio"] label p {
            font-size: 11px !important;
        }

        .hero {
            padding: 23px 17px;
            border-radius: 18px;
            margin-top: 10px;
        }

        .hero h1 { font-size: 24px; }
        .hero p { font-size: 14px; }
        .section-title { font-size: 21px; }
        .community-card { padding: 15px; }
        .area { min-height: 130px; padding: 15px 6px; }
        .area h2 { font-size: 21px; }

        div[data-testid="stTabs"] button {
            font-size: 11px !important;
            padding: 7px 4px !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------- DATA ---------------------------

communities = {
    "اليوغا": {
        "icon": "🧘🏻‍♀️",
        "description": "مساحة للحركة والهدوء والتوازن.",
        "bring": ["ملابس مريحة", "قارورة ماء", "حصيرة يوغا إن توفرت"],
        "ideas": [
            "Sunset Yoga",
            "جلسة تأمل وتنفس",
            "Yoga & Coffee",
        ],
    },
    "الفنون": {
        "icon": "🎨",
        "description": "مساحة للإبداع والتعبير الفني.",
        "bring": ["ملابس مناسبة للرسم", "دفتر رسم", "أدواتك الفنية"],
        "ideas": [
            "Art Jamming",
            "جلسة رسم جماعية",
            "تبادل الأعمال الفنية",
        ],
    },
    "الفخار": {
        "icon": "🏺",
        "description": "تجربة تشكيل الطين وصناعة قطعك الخاصة.",
        "bring": ["ملابس مريحة", "مريلة", "حماس للتجربة"],
        "ideas": [
            "Pottery for Beginners",
            "اصنع كوبك الخاص",
            "جلسة تلوين الفخار",
        ],
    },
    "الخيول": {
        "icon": "🐎",
        "description": "تجربة للتعرف على الخيل والتواصل معها.",
        "bring": ["حذاء مغلق", "ملابس مريحة", "قارورة ماء"],
        "ideas": [
            "Meet the Horses",
            "جلسة عناية بالخيل",
            "مبادئ الفروسية",
        ],
    },
    "الورش": {
        "icon": "💡",
        "description": "نتعلم ونشارك المهارات والأفكار.",
        "bring": ["دفتر وقلم", "حاسوب عند الحاجة", "استعداد للمشاركة"],
        "ideas": [
            "Creative Thinking",
            "AI for Everyone",
            "جلسة تبادل مهارات",
        ],
    },
}

events = [
    {
        "name": "Sunset Yoga",
        "type": "اليوغا",
        "date": "قريباً",
        "place": "الحديقة الخارجية",
        "seats": 8,
        "total": 15,
    },
    {
        "name": "Art Jamming",
        "type": "الفنون",
        "date": "قريباً",
        "place": "المساحة الداخلية",
        "seats": 12,
        "total": 20,
    },
    {
        "name": "Pottery for Beginners",
        "type": "الفخار",
        "date": "قريباً",
        "place": "المساحة الداخلية",
        "seats": 6,
        "total": 12,
    },
    {
        "name": "Meet the Horses",
        "type": "الخيول",
        "date": "قريباً",
        "place": "الحديقة الخارجية",
        "seats": 5,
        "total": 10,
    },
    {
        "name": "AI for Everyone",
        "type": "الورش",
        "date": "قريباً",
        "place": "المساحة الداخلية",
        "seats": 14,
        "total": 18,
    },
]

# ------------------------- HEADER -------------------------

with st.container(key="site_header"):
    st.markdown(
        """
        <div class="brand">
            <div>
                <span class="brand-name">JAZIF</span>
                <span class="brand-sub">COMMUNITY SPACE</span>
            </div>
            <div class="brand-icon">🌿</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    pages = ["الرئيسية", "المجتمعات", "تذاكري", "حسابي"]

    selected_page = st.radio(
        "التنقل",
        pages,
        index=pages.index(st.session_state.page),
        horizontal=True,
        label_visibility="collapsed",
        key="main_navigation",
    )

    st.session_state.page = selected_page

# -------------------------- HOME --------------------------

if st.session_state.page == "الرئيسية":
    st.markdown(
        """
        <div class="hero">
            <span class="hero-tag">A SPACE TO CONNECT & CREATE</span>
            <h1>مساحة تجمعنا، وتجارب تصنع ذكرياتنا</h1>
            <p>
                جازف مساحة مجتمعية تجمع الأشخاص حول الاهتمامات المشتركة،
                وتمنحهم فرصة للتجربة والتعلم والتواصل.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">أهلاً بك في جازف</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-description">مساحة صممت لتكون نقطة بداية لتجارب وصداقات وأفكار جديدة.</div>',
        unsafe_allow_html=True,
    )

    

    st.markdown('<div class="section-title">تجارب ومساحات جازف</div>', unsafe_allow_html=True)

    feature_cols = st.columns(3)
    features = [
        ("🌿", "Community", "مساحات تجمع أصحاب الاهتمامات المشتركة."),
        ("✨", "Experiences", "تجارب وفعاليات نصنعها معاً."),
        ("💡", "Ideas", "أفكار الأعضاء تتحول إلى تجارب حقيقية."),
    ]

    for col, (icon, title, desc) in zip(feature_cols, features):
        with col:
            st.markdown(
                f"""
                <div class="info-card">
                    <div style="font-size:29px;">{icon}</div>
                    <b>{title}</b>
                    <div class="card-description">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown('<div class="section-title">خريطة المساحة</div>', unsafe_allow_html=True)
    st.caption("اكتشف مناطق جازف والتجارب التي تقام فيها.")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="area">
                <div style="font-size:28px;">🏡</div>
                <b>المساحة الداخلية</b>
                <h2>105 m²</h2>
                <small>ورش واجتماعات وتجارب داخلية</small>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="area outdoor">
                <div style="font-size:28px;">🌳</div>
                <b>الحديقة الخارجية</b>
                <h2>533 m²</h2>
                <small>يوغا وفعاليات وتجارب خارجية</small>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-title">التجارب القادمة</div>', unsafe_allow_html=True)

    for event in events:
        with st.container(border=True):
            st.markdown(f"### {event['name']}")
            st.caption(f"{event['type']} · {event['date']} · {event['place']}")
            st.write(f"🪑 المقاعد المتبقية: {event['seats']} من {event['total']}")
            if st.button("استكشف التجربة", key=f"event_{event['name']}", use_container_width=True):
                st.session_state.community = event["type"]
                st.session_state.page = "المجتمعات"
                st.rerun()

    if st.button("اكتشف جميع المجتمعات ←", use_container_width=True):
        st.session_state.page = "المجتمعات"
        st.rerun()

# ---------------------- COMMUNITIES PAGE ------------------

elif st.session_state.page == "المجتمعات":
    st.title("مجتمعات جازف 🌿")
    st.write("كل مجتمع يبدأ باهتمام، وينمو بالأشخاص الذين يجمعهم.")
    st.markdown('<div class="section-title">اكتشف مجتمعاتنا</div>', unsafe_allow_html=True)

    for name, data in communities.items():
        with st.container(border=True):
            st.markdown(f"### {data['icon']} {name}")
            st.caption(data["description"])
            if st.button(f"اكتشف مجتمع {name}", key=f"open_{name}", use_container_width=True):
                st.session_state.community = name
                st.rerun()

    st.divider()

    name = st.session_state.community
    data = communities[name]

    st.markdown(f"## {data['icon']} مجتمع {name}")
    st.write(data["description"])

    tab1, tab2, tab3 = st.tabs(["نظرة عامة", "مختبر الأفكار", "مساحة المجتمع"])

    with tab1:
        st.subheader("عن المجتمع")
        st.write(data["description"])
        st.markdown("### من تجاربنا السابقة")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                '<div class="info-card">📸<br><b>تجربة سابقة 01</b><div class="card-description">تضاف الصور لاحقاً</div></div>',
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                '<div class="info-card">📸<br><b>تجربة سابقة 02</b><div class="card-description">تضاف الصور لاحقاً</div></div>',
                unsafe_allow_html=True,
            )

        st.markdown("### What to Bring 🎒")
        st.caption(f"الأشياء المقترحة لمجتمع {name}")
        for item in data["bring"]:
            st.checkbox(item, key=f"bring_{name}_{item}")

        if st.button("سجل اهتمامك بالمجتمع", key=f"interest_{name}", use_container_width=True):
            if name not in st.session_state.interests:
                st.session_state.interests.append(name)
            st.success("تم تسجيل اهتمامك بنجاح! 🌿")

    with tab2:
        st.subheader("Idea Lab 💡")
        st.write("شارك أفكارك وصوّت على التجارب التي ترغب برؤيتها.")

        with st.form(f"idea_form_{name}"):
            new_idea = st.text_input("ما الفكرة التي تقترحها؟", placeholder="اكتب فكرتك هنا...")
            submitted = st.form_submit_button("＋ أضف اقتراحك", use_container_width=True)
            if submitted and new_idea.strip():
                st.session_state.ideas.append({"community": name, "idea": new_idea.strip()})
                st.success("تمت إضافة فكرتك!")

        st.divider()
        st.markdown("### أفكار المجتمع")
        st.markdown(
            """
            <div style="
                background:#E7EDE5;
                color:#263D32;
                border:1px solid #D5E0D4;
                border-radius:14px;
                padding:13px 15px;
                margin:8px 0 16px;
                text-align:center;
                font-weight:700;
                font-size:15px;">
                💚 We love it, we support it!
                <div style="font-size:12px;font-weight:400;margin-top:4px;">
                    صوتك يدعم الفكرة ويساعدها تكبر.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Combine suggested ideas and member-submitted ideas so both can receive support.
        community_ideas = [
            {"text": idea, "key": f"{name}_suggested_{i}"}
            for i, idea in enumerate(data["ideas"])
        ]
        community_ideas += [
            {"text": idea["idea"], "key": f"{name}_member_{i}"}
            for i, idea in enumerate(st.session_state.ideas)
            if idea["community"] == name
        ]

        for idea in community_ideas:
            vote_key = idea["key"]
            with st.container(border=True):
                st.write(f"💡 {idea['text']}")
                votes = st.session_state.votes.get(vote_key, 0)
                st.caption(f"💚 {votes} دعم")
                if st.button(
                    "💚 We love it, we support it",
                    key=f"vote_{vote_key}",
                    use_container_width=True,
                ):
                    st.session_state.votes[vote_key] = votes + 1
                    st.rerun()

        st.divider()
        st.subheader("Find a Co-host 🤝")
        st.write("هل عندك فكرة وتبحث عن شخص يشاركك تنظيمها؟")
        if st.button("ابحث عن شريك لتنظيم الفكرة", use_container_width=True):
            st.info("سيتم تطوير نظام البحث عن Co-host لاحقاً.")

    with tab3:
        st.subheader("Community Space 🔒")
        st.write("مساحة خاصة للتواصل بين أعضاء المجتمع.")

        accepted = st.toggle("محاكاة: تم قبول تسجيلي في المجتمع", key=f"accepted_{name}")

        if accepted:
            st.success("مرحباً بك في مساحة المجتمع!")
            st.markdown("### Community Chat")
            message = st.text_area("اكتب رسالتك", placeholder="شاركنا أفكارك...", key=f"message_{name}")

            if st.button("إرسال الرسالة", key=f"send_{name}", use_container_width=True):
                if message.strip():
                    st.session_state.messages.setdefault(name, [])
                    st.session_state.messages[name].append(message.strip())
                    st.success("تم إرسال الرسالة التجريبية.")

            for msg in st.session_state.messages.get(name, []):
                st.info(msg)

            st.divider()
            st.markdown("### قنوات التواصل")
            st.markdown("- 💬 مجموعة WhatsApp (رابط تجريبي)\n- ✉️ البريد الإلكتروني للمجتمع")
        else:
            st.info("🔒 هذه المساحة متاحة للأعضاء المقبولين فقط.")

# ------------------------- DIGITAL PASS -------------------

elif st.session_state.page == "تذاكري":
    st.title("Digital Pass 🎟️")
    st.write("تذكرتك الرقمية للدخول إلى جازف.")

    qr_image = qrcode.make("JAZIF-DEMO-MEMBER-001")
    qr_buffer = BytesIO()
    qr_image.save(qr_buffer, format="PNG")

    with st.container(border=True):
        st.markdown(
            "<h2 style='text-align:center;color:#263D32'>JAZIF 🌿</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='text-align:center;color:#66766A'>MEMBER DIGITAL PASS</p>",
            unsafe_allow_html=True,
        )
        st.image(qr_buffer.getvalue(), width=190)
        st.markdown(
            "<h3 style='text-align:center;color:#263D32'>Noura Member</h3>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='text-align:center;color:#66766A'>Member ID: JZ-001-DEMO</p>",
            unsafe_allow_html=True,
        )
        st.success("Active Member · Demo")

    st.caption("هذا QR تجريبي للتوضيح فقط، وليس تصريح دخول حقيقي.")

# --------------------------- ACCOUNT ----------------------

elif st.session_state.page == "حسابي":
    st.title("حسابي 👤")

    with st.container(border=True):
        st.markdown("## 👩🏻")
        st.subheader("Noura Member")
        st.caption("Jazif Community Member")
        st.markdown('<span class="tag">Active Member</span>', unsafe_allow_html=True)

    st.markdown("### Badges 🏅")
    b1, b2, b3 = st.columns(3)
    b1.metric("Explorer", "01")
    b2.metric("Ideas", "03")
    b3.metric("Events", "02")

    st.markdown("### مجتمعاتي")
    if st.session_state.interests:
        for community in st.session_state.interests:
            st.write(f"{communities[community]['icon']} {community}")
    else:
        st.caption("لم تسجلي اهتمامك بأي مجتمع حتى الآن.")

    st.divider()

    if st.button("🎟️ عرض التذاكر الرقمية", use_container_width=True):
        st.session_state.page = "تذاكري"
        st.rerun()

    if st.button("🌿 تصفح المجتمعات", use_container_width=True):
        st.session_state.page = "المجتمعات"
        st.rerun()

# ---------------------------- FOOTER ---------------------

st.markdown(
    """
    <div class="footer">
        <b style="color:#263D32;">JAZIF COMMUNITY SPACE 🌿</b>
        <br>
        A place to connect, create & belong.
    </div>
    """,
    unsafe_allow_html=True,
)