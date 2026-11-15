import streamlit as st
import qrcode

from io import BytesIO


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="JAZIF Community Space",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# SESSION STATE
# =========================================================

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

if "messages" not in st.session_state:
    st.session_state.messages = {}


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    :root {
        --dark: #263D32;
        --green: #496653;
        --soft: #E7EDE5;
        --background: #F7F7F2;
        --white: #FFFFFF;
        --muted: #66766A;
        --border: #E2E8DF;
    }

    .stApp {
        background-color: var(--background);
        color: var(--dark);
    }

    .block-container {
        padding-top: 158px;
        padding-bottom: 2rem;
        max-width: 1100px;
    }

    .st-key-site_header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999999;
        background: #F7F7F2;
        padding: 15px 25px 10px;
        border-bottom: 1px solid #E2E8DF;
    }

    .brand {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 8px;
    }

    .brand-name {
        font-size: 28px;
        font-weight: 800;
        color: #263D32;
        letter-spacing: 2px;
    }

    .brand-sub {
        display: block;
        font-size: 11px;
        color: #66766A;
        letter-spacing: 2px;
    }

    .brand-icon {
        font-size: 25px;
    }

    .hero {
        background: linear-gradient(135deg, #263D32, #496653);
        padding: 35px;
        border-radius: 22px;
        color: white;
        margin-bottom: 25px;
    }

    .hero h1 {
        color: white !important;
        font-size: 30px;
    }

    .hero p {
        color: #E7EDE5;
        font-size: 15px;
    }

    .hero-tag {
        color: #E7EDE5;
        font-size: 11px;
        letter-spacing: 2px;
    }

    .section-title {
        font-size: 23px;
        font-weight: 750;
        color: #263D32;
        margin-top: 28px;
        margin-bottom: 7px;
    }

    .section-subtitle {
        color: #66766A;
        font-size: 14px;
        margin-bottom: 18px;
    }

    .card {
        background: white;
        border: 1px solid #E2E8DF;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 14px;
    }

    .card-title {
        color: #263D32;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 7px;
    }

    .muted {
        color: #66766A;
        font-size: 13px;
    }

    .tag {
        display: inline-block;
        background: #E7EDE5;
        color: #263D32;
        border-radius: 30px;
        padding: 5px 11px;
        font-size: 12px;
        margin: 3px;
    }

    .stat-card {
        background: white;
        border: 1px solid #E2E8DF;
        border-radius: 16px;
        padding: 18px;
        text-align: center;
    }

    .stat-number {
        font-size: 26px;
        color: #263D32;
        font-weight: 700;
    }

    .stat-label {
        color: #66766A;
        font-size: 12px;
    }

    .idea-card {
        background: white;
        border: 1px solid #E2E8DF;
        border-radius: 16px;
        padding: 18px;
        margin: 12px 0;
    }

    .idea-voting-banner {
        background: #E7EDE5;
        border: 1px solid #E2E8DF;
        border-radius: 16px;
        padding: 17px 18px;
        margin: 14px 0 18px;
        text-align: center;
    }

    .idea-voting-banner .banner-title {
        color: #263D32;
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .idea-voting-banner .banner-subtitle {
        color: #66766A;
        font-size: 13px;
    }

    .idea-vote-count {
        color: #496653;
        font-size: 13px;
        font-weight: 600;
        margin-top: 8px;
    }

    .community-cover {
        background: linear-gradient(135deg, #263D32, #496653);
        color: white;
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 18px;
    }

    .community-cover h2 {
        color: white !important;
    }

    .community-cover p {
        color: #E7EDE5 !important;
    }

    .space-box {
        background: white;
        border: 1px solid #E2E8DF;
        border-radius: 16px;
        padding: 18px;
        text-align: center;
    }

    .space-number {
        font-size: 25px;
        font-weight: 700;
        color: #263D32;
    }

    .space-label {
        font-size: 13px;
        color: #66766A;
    }

    .ticket {
        background: white;
        border: 1px dashed #496653;
        border-radius: 18px;
        padding: 22px;
        margin: 14px 0;
    }

    .stButton > button {
        background: #263D32 !important;
        color: white !important;
        border: 1px solid #263D32 !important;
        border-radius: 12px !important;
        padding: 9px 17px !important;
        font-weight: 600 !important;
        min-height: 42px;
        width: 100%;
    }

    .stButton > button:hover {
        background: #496653 !important;
        border-color: #496653 !important;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 145px 0.85rem 2rem !important;
        }

        .st-key-site_header {
            padding: 9px 12px;
        }

        .brand-name {
            font-size: 23px;
        }

        .brand-sub {
            font-size: 10px;
        }

        .hero {
            padding: 24px 18px;
        }

        .hero h1 {
            font-size: 24px;
        }

        .section-title {
            font-size: 20px;
        }

        .card {
            padding: 16px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)
```python
    .section-subtitle {
        color: var(--muted);
        font-size: 14px;
        margin-bottom: 18px;
    }

    .card {
        background: var(--white);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 14px;
    }

    .card-title {
        color: var(--dark);
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 7px;
    }

    .muted {
        color: var(--muted);
        font-size: 13px;
    }

    .tag {
        display: inline-block;
        background: var(--soft);
        color: var(--dark);
        border-radius: 30px;
        padding: 5px 11px;
        font-size: 12px;
        margin: 3px 3px 3px 0;
    }

    .stat-card {
        background: var(--white);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 18px;
        text-align: center;
    }

    .stat-number {
        font-size: 26px;
        color: var(--dark);
        font-weight: 700;
    }

    .stat-label {
        color: var(--muted);
        font-size: 12px;
    }

    .idea-card {
        background: var(--white);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 18px;
        margin: 12px 0;
    }

    .idea-voting-banner {
        background: var(--soft);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 17px 18px;
        margin: 14px 0 18px;
        text-align: center;
    }

    .idea-voting-banner .banner-title {
        color: var(--dark);
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .idea-voting-banner .banner-subtitle {
        color: var(--muted);
        font-size: 13px;
    }

    .idea-vote-count {
        color: var(--green);
        font-size: 13px;
        font-weight: 600;
        margin-top: 8px;
    }

    .community-cover {
        background: linear-gradient(135deg, #263D32, #496653);
        color: white;
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 18px;
    }

    .community-cover h2 {
        color: white !important;
        margin-bottom: 5px;
    }

    .community-cover p {
        color: #E7EDE5 !important;
    }

    .space-box {
        background: var(--white);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 18px;
        text-align: center;
    }

    .space-number {
        font-size: 25px;
        font-weight: 700;
        color: var(--dark);
    }

    .space-label {
        font-size: 13px;
        color: var(--muted);
    }

    .event-date {
        background: var(--soft);
        color: var(--dark);
        padding: 9px 12px;
        border-radius: 12px;
        text-align: center;
        min-width: 65px;
        font-weight: 700;
    }

    .ticket {
        background: white;
        border: 1px dashed var(--green);
        border-radius: 18px;
        padding: 22px;
        margin: 14px 0;
    }

    .badge {
        display: inline-block;
        background: var(--soft);
        border: 1px solid var(--border);
        border-radius: 30px;
        padding: 7px 12px;
        color: var(--dark);
        font-size: 12px;
        margin: 4px;
    }

    /* Buttons */
    .stButton > button {
        background: var(--dark) !important;
        color: white !important;
        border: 1px solid var(--dark) !important;
        border-radius: 12px !important;
        padding: 9px 17px !important;
        font-weight: 600 !important;
        min-height: 42px;
        width: 100%;
    }

    .stButton > button:hover {
        background: var(--green) !important;
        border-color: var(--green) !important;
        color: white !important;
    }

    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"] {
        background: white !important;
        border-radius: 10px !important;
    }

    div[data-testid="stTabs"] button {
        color: var(--dark) !important;
        font-weight: 600 !important;
    }

    div[data-testid="stTabs"] button[aria-selected="true"] {
        color: var(--green) !important;
    }

    .stAlert {
        border-radius: 12px !important;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 145px 0.85rem 2rem !important;
        }

        .st-key-site_header {
            padding: 9px 12px 9px !important;
        }

        .brand-name {
            font-size: 23px;
        }

        .brand-sub {
            font-size: 10px;
        }

        .st-key-site_header div[data-testid="stRadio"] > div {
            gap: 4px !important;
        }

        .st-key-site_header div[data-testid="stRadio"] label {
            padding: 7px 1px !important;
            border-radius: 9px !important;
        }

        .st-key-site_header div[data-testid="stRadio"] label p,
        .st-key-site_header div[data-testid="stRadio"] label span {
            font-size: 11px !important;
        }

        .hero {
            padding: 24px 18px;
        }

        .hero h1 {
            font-size: 24px;
        }

        .section-title {
            font-size: 20px;
        }

        .card {
            padding: 16px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# DATA
# =========================================================

COMMUNITIES = {
    "اليوغا": {
        "emoji": "🧘‍♀️",
        "description": "مساحة للتوازن والهدوء والحركة الواعية.",
        "intro": "نلتقي لنمنح أجسادنا وعقولنا مساحة للتنفس والاسترخاء.",
        "bring": [
            "ملابس مريحة للحركة",
            "قارورة ماء",
            "حصيرة يوغا إن توفرت",
            "منشفة صغيرة",
        ],
        "activities": ["جلسات يوغا", "تأمل", "تمارين تنفس"],
        "badge": "Mindful Soul",
    },
    "الفنون": {
        "emoji": "🎨",
        "description": "مجتمع يجمع محبي الفن والتجربة والإبداع.",
        "intro": "جرّب أفكاراً فنية جديدة وشارك إبداعك مع الآخرين.",
        "bring": [
            "ملابس مناسبة للتلوين",
            "دفتر رسم إن توفر",
            "أدواتك الفنية المفضلة",
        ],
        "activities": ["رسم", "تلوين", "تجارب فنية"],
        "badge": "Creative Mind",
    },
    "الفخار": {
        "emoji": "🏺",
        "description": "من الفكرة إلى قطعة تصنعها بيديك.",
        "intro": "اكتشف متعة تشكيل الطين وصناعة قطعك الخاصة.",
        "bring": [
            "ملابس مريحة",
            "مريلة أو ملابس قابلة للاتساخ",
            "حماس للتجربة",
        ],
        "activities": ["تشكيل الطين", "التلوين", "صناعة القطع"],
        "badge": "Clay Artist",
    },
    "الخيول": {
        "emoji": "🐎",
        "description": "تجربة تجمع بين التعلم والتواصل مع الخيل.",
        "intro": "اقترب من عالم الخيل وتعرّف على أساسيات التعامل معها.",
        "bring": [
            "حذاء مغلق ومريح",
            "ملابس مناسبة للنشاط",
            "قارورة ماء",
        ],
        "activities": ["التعرف على الخيل", "العناية", "التجربة"],
        "badge": "Horse Friend",
    },
    "الورش": {
        "emoji": "💡",
        "description": "نتعلم معاً ونحوّل الأفكار إلى تجارب.",
        "intro": "ورش متنوعة تفتح لك أبواباً لمهارات وأفكار جديدة.",
        "bring": [
            "دفتر وقلم",
            "حاسوب محمول عند الحاجة",
            "استعداد للمشاركة",
        ],
        "activities": ["ورش إبداعية", "جلسات تعلم", "عصف ذهني"],
        "badge": "Curious Learner",
    },
}

EVENTS = [
    {
        "title": "Morning Yoga",
        "community": "اليوغا",
        "date": "قريباً",
        "time": "9:00 AM",
        "place": "المساحة الداخلية",
        "seats": 12,
        "description": "ابدأ يومك بجلسة يوغا هادئة.",
    },
    {
        "title": "Creative Art Session",
        "community": "الفنون",
        "date": "قريباً",
        "time": "5:00 PM",
        "place": "المساحة الداخلية",
        "seats": 8,
        "description": "مساحة مفتوحة للتجربة الفنية.",
    },
    {
        "title": "Pottery Workshop",
        "community": "الفخار",
        "date": "قريباً",
        "time": "4:00 PM",
        "place": "المساحة الداخلية",
        "seats": 10,
        "description": "اصنع قطعتك الخاصة من الطين.",
    },
    {
        "title": "Horse Experience",
        "community": "الخيول",
        "date": "قريباً",
        "time": "6:00 PM",
        "place": "الحديقة الخارجية",
        "seats": 6,
        "description": "تجربة للتعرف على الخيل.",
    },
    {
        "title": "Ideas & Innovation",
        "community": "الورش",
        "date": "قريباً",
        "time": "7:00 PM",
        "place": "المساحة الداخلية",
        "seats": 15,
        "description": "شارك أفكارك وناقشها مع المجتمع.",
    },
]

DEFAULT_IDEAS = [
    {
        "id": "idea_1",
        "title": "ليلة أفلام في الحديقة",
        "description": "نجتمع في الهواء الطلق لمشاهدة فيلم وتجربة أجواء مختلفة.",
        "author": "JAZIF Team",
        "community": "عام",
    },
    {
        "id": "idea_2",
        "title": "تبادل الكتب",
        "description": "كل شخص يحضر كتاباً ويستبدله بكتاب جديد.",
        "author": "JAZIF Team",
        "community": "عام",
    },
    {
        "id": "idea_3",
        "title": "جلسة قهوة ومواهب",
        "description": "مساحة بسيطة يشارك فيها الأعضاء مواهبهم واهتماماتهم.",
        "author": "JAZIF Team",
        "community": "عام",
    },
]
# =========================================================
# HELPER FUNCTIONS
# =========================================================

def section_title(title, subtitle=None):
    st.markdown(
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True,
    )
    if subtitle:
        st.markdown(
            f'<div class="section-subtitle">{subtitle}</div>',
            unsafe_allow_html=True,
        )


def card(title, description="", extra=""):
    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">{title}</div>
            <div>{description}</div>
            {extra}
        </div>
        """,
        unsafe_allow_html=True,
    )


def get_ideas():
    return DEFAULT_IDEAS + st.session_state.ideas


def get_vote_count(idea_id):
    return st.session_state.votes.get(idea_id, 0)


def vote_for_idea(idea_id):
    st.session_state.votes[idea_id] = get_vote_count(idea_id) + 1


def add_idea(title, description, community):
    new_idea = {
        "id": f"member_idea_{len(st.session_state.ideas) + 1}",
        "title": title,
        "description": description,
        "author": "Community Member",
        "community": community,
    }
    st.session_state.ideas.append(new_idea)


def show_idea_voting_banner():
    st.markdown(
        """
        <div class="idea-voting-banner">
            <div class="banner-title">
                💚 We love it, we support it
            </div>
            <div class="banner-subtitle">
                صوتك يدعم الفكرة ويساعدها تكبر
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_ideas(community_filter=None):
    ideas = get_ideas()

    if community_filter and community_filter != "عام":
        ideas = [
            idea for idea in ideas
            if idea["community"] in [community_filter, "عام"]
        ]

    show_idea_voting_banner()

    if not ideas:
        st.info("ما فيه أفكار حالياً، كن أول شخص يشارك فكرته!")
        return

    for idea in ideas:
        idea_id = idea["id"]
        votes = get_vote_count(idea_id)

        st.markdown(
            f"""
            <div class="idea-card">
                <div class="card-title">{idea["title"]}</div>
                <p>{idea["description"]}</p>
                <span class="tag">{idea["community"]}</span>
                <div class="muted">By {idea["author"]}</div>
                <div class="idea-vote-count">
                    💚 {votes} support votes
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "💚 We love it, we support it",
            key=f"vote_{idea_id}",
            use_container_width=True,
        ):
            vote_for_idea(idea_id)
            st.rerun()


def create_qr(data):
    qr = qrcode.QRCode(
        version=1,
        box_size=8,
        border=3,
    )
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color="#263D32",
        back_color="white",
    )

    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer


# =========================================================
# FIXED HEADER / NAVIGATION
# =========================================================

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


# =========================================================
# HOME PAGE
# =========================================================

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

    section_title(
        "أهلاً بك في جازف",
        "مساحة صممت لتكون نقطة بداية لتجارب وصداقات وأفكار جديدة.",
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">5</div>
                <div class="stat-label">مجتمعات متنوعة</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">∞</div>
                <div class="stat-label">أفكار وتجارب</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">1</div>
                <div class="stat-label">مجتمع واحد يجمعنا</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    section_title(
        "اكتشف المساحة",
        "مكان يجمع بين المساحات الداخلية والخارجية.",
    )

    space1, space2 = st.columns(2)

    with space1:
        st.markdown(
            """
            <div class="space-box">
                <div class="space-number">105 m²</div>
                <div class="space-label">المساحة الداخلية</div>
                <p class="muted">للفعاليات والورش واللقاءات.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with space2:
        st.markdown(
            """
            <div class="space-box">
                <div class="space-number">533 m²</div>
                <div class="space-label">الحديقة الخارجية</div>
                <p class="muted">للتجارب والأنشطة في الهواء الطلق.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    section_title(
        "مجتمعات جازف",
        "اختر المجتمع الأقرب لاهتماماتك.",
    )

    community_columns = st.columns(2)

    for index, (name, info) in enumerate(COMMUNITIES.items()):
        with community_columns[index % 2]:
            st.markdown(
                f"""
                <div class="card">
                    <div class="card-title">
                        {info["emoji"]} {name}
                    </div>
                    <p>{info["description"]}</p>
                    <span class="tag">Explore Community</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(
                f"استكشف مجتمع {name}",
                key=f"home_community_{name}",
            ):
                st.session_state.community = name
                st.session_state.page = "المجتمعات"
                st.rerun()

    section_title(
        "الفعاليات القادمة",
        "تجارب قادمة بانتظارك.",
    )

    for event in EVENTS:
        with st.container():
            st.markdown(
                f"""
                <div class="card">
                    <div class="card-title">{event["title"]}</div>
                    <p>{event["description"]}</p>
                    <span class="tag">{event["community"]}</span>
                    <span class="tag">📅 {event["date"]}</span>
                    <span class="tag">🕒 {event["time"]}</span>
                    <span class="tag">📍 {event["place"]}</span>
                    <div class="muted">
                        المقاعد المتبقية: {event["seats"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
# =========================================================
# COMMUNITIES PAGE
# =========================================================

elif st.session_state.page == "المجتمعات":

    section_title(
        "مجتمعات جازف",
        "كل مجتمع مساحة تجمع أشخاصاً يشتركون في الاهتمام نفسه.",
    )

    selected_community = st.selectbox(
        "اختر المجتمع",
        list(COMMUNITIES.keys()),
        index=list(COMMUNITIES.keys()).index(
            st.session_state.community
        ),
        key="community_selector",
    )

    st.session_state.community = selected_community
    info = COMMUNITIES[selected_community]

    st.markdown(
        f"""
        <div class="community-cover">
            <h2>{info["emoji"]} {selected_community}</h2>
            <p>{info["description"]}</p>
            <p>{info["intro"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    overview_tab, gallery_tab, ideas_tab, members_tab = st.tabs(
        [
            "نظرة عامة",
            "صور سابقة",
            "مختبر الأفكار",
            "مساحة الأعضاء",
        ]
    )

    # ---------------- OVERVIEW TAB ----------------

    with overview_tab:

        section_title(
            "عن المجتمع",
            "اكتشف الأنشطة والتجارب التي يقدمها هذا المجتمع.",
        )

        card(
            "وش بنسوي؟",
            info["intro"],
        )

        section_title("الأنشطة")

        activity_columns = st.columns(2)

        for index, activity in enumerate(info["activities"]):
            with activity_columns[index % 2]:
                st.markdown(
                    f"""
                    <div class="card">
                        <div class="card-title">✨ {activity}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        section_title(
            "What to Bring",
            "قائمة بسيطة تساعدك تستعد للتجربة.",
        )

        checklist_key = f"checklist_{selected_community}"

        if checklist_key not in st.session_state:
            st.session_state[checklist_key] = []

        for index, item in enumerate(info["bring"]):
            checked = item in st.session_state[checklist_key]

            if st.checkbox(
                item,
                value=checked,
                key=f"{checklist_key}_{index}",
            ):
                if item not in st.session_state[checklist_key]:
                    st.session_state[checklist_key].append(item)
            else:
                if item in st.session_state[checklist_key]:
                    st.session_state[checklist_key].remove(item)

        completed = len(st.session_state[checklist_key])
        total = len(info["bring"])

        st.progress(completed / total if total else 0)
        st.caption(f"أنجزت {completed} من {total}")

        section_title("فعاليات المجتمع")

        community_events = [
            event for event in EVENTS
            if event["community"] == selected_community
        ]

        if community_events:
            for event in community_events:
                st.markdown(
                    f"""
                    <div class="card">
                        <div class="card-title">{event["title"]}</div>
                        <p>{event["description"]}</p>
                        <span class="tag">📅 {event["date"]}</span>
                        <span class="tag">🕒 {event["time"]}</span>
                        <span class="tag">📍 {event["place"]}</span>
                        <div class="muted">
                            المقاعد المتبقية: {event["seats"]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        if st.button(
            "💚 سجّل اهتمامك بالمجتمع",
            key=f"interest_{selected_community}",
        ):
            if selected_community not in st.session_state.interests:
                st.session_state.interests.append(selected_community)
                st.success("تم تسجيل اهتمامك بنجاح!")
            else:
                st.info("أنت مسجل اهتمامك بهذا المجتمع بالفعل.")

    # ---------------- GALLERY TAB ----------------

    with gallery_tab:

        section_title(
            "لحظات من مجتمعنا",
            "مساحة لعرض الصور والذكريات من التجارب السابقة.",
        )

        st.markdown(
            """
            <div class="card">
                <div class="card-title">📸 Coming Soon</div>
                <p>
                    قريباً بنشارك هنا صور ولقطات من فعاليات المجتمع
                    وتجارب أعضائه.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.caption(
            "يمكن إضافة الصور لاحقاً من ملفات المشروع أو روابط الصور."
        )

    # ---------------- IDEAS TAB ----------------

    with ideas_tab:

        section_title(
            "مختبر الأفكار",
            "عندك فكرة؟ شاركها مع المجتمع وخلي الآخرين يدعمونها.",
        )

        show_ideas(selected_community)

        st.markdown("---")

        section_title(
            "شاركنا فكرتك",
            "كل فكرة ممكن تكون بداية تجربة جديدة.",
        )

        with st.form(
            key=f"idea_form_{selected_community}",
            clear_on_submit=True,
        ):

            idea_title = st.text_input(
                "عنوان الفكرة",
                placeholder="مثلاً: جلسة رسم في الحديقة",
            )

            idea_description = st.text_area(
                "اشرح فكرتك",
                placeholder="اكتب تفاصيل بسيطة عن فكرتك...",
            )

            submitted = st.form_submit_button(
                "إرسال الفكرة",
                use_container_width=True,
            )

            if submitted:
                if idea_title.strip() and idea_description.strip():
                    add_idea(
                        idea_title.strip(),
                        idea_description.strip(),
                        selected_community,
                    )
                    st.success("وصلتنا فكرتك! شكراً لمشاركتك 💚")
                    st.rerun()
                else:
                    st.warning("فضلاً اكتب عنوان الفكرة ووصفها.")

    # ---------------- MEMBERS TAB ----------------

    with members_tab:

        section_title(
            "مساحة الأعضاء",
            "مساحة خاصة للتواصل ومشاركة التحديثات بين أعضاء المجتمع.",
        )

        st.markdown(
            """
            <div class="card">
                <div class="card-title">🔒 Members Only</div>
                <p>
                    هذه المساحة مخصصة للأعضاء المقبولين في المجتمع.
                    يمكن تطوير تسجيل الدخول والتحقق من العضوية لاحقاً.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        member_message = st.text_area(
            "اكتب رسالة للمجتمع",
            placeholder="شارك تحديثاً أو فكرة مع الأعضاء...",
            key=f"member_message_{selected_community}",
        )

        if st.button(
            "نشر الرسالة",
            key=f"send_message_{selected_community}",
        ):
            if member_message.strip():
                if selected_community not in st.session_state.messages:
                    st.session_state.messages[selected_community] = []

                st.session_state.messages[selected_community].append(
                    member_message.strip()
                )

                st.success("تم نشر رسالتك.")
                st.rerun()
            else:
                st.warning("اكتب رسالة أولاً.")

        messages = st.session_state.messages.get(
            selected_community,
            [],
        )

        if messages:
            section_title("رسائل الأعضاء")

            for message in reversed(messages):
                st.markdown(
                    f"""
                    <div class="card">
                        <p>{message}</p>
                        <div class="muted">Community Member</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.info("لا توجد رسائل حتى الآن.")


# =========================================================
# MY TICKETS PAGE
# =========================================================

elif st.session_state.page == "تذاكري":

    section_title(
        "تذاكري",
        "كل تجاربك وحجوزاتك في مكان واحد.",
    )

    st.markdown(
        """
        <div class="card">
            <div class="card-title">🎟️ Your JAZIF Pass</div>
            <p>
                هنا تظهر التذاكر التي حصلت عليها للفعاليات
                والتجارب في مساحة جازف.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    ticket_event = st.selectbox(
        "اختر فعالية لعرض تذكرتها التجريبية",
        [event["title"] for event in EVENTS],
        key="ticket_event",
    )

    selected_event = next(
        event for event in EVENTS
        if event["title"] == ticket_event
    )

    st.markdown(
        f"""
        <div class="ticket">
            <div class="card-title">JAZIF COMMUNITY SPACE</div>
            <h3>{selected_event["title"]}</h3>
            <p>{selected_event["description"]}</p>
            <span class="tag">{selected_event["community"]}</span>
            <span class="tag">📅 {selected_event["date"]}</span>
            <span class="tag">🕒 {selected_event["time"]}</span>
            <span class="tag">📍 {selected_event["place"]}</span>
            <hr>
            <div class="muted">DEMO TICKET — NOT A REAL BOOKING</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    qr_data = (
        f"JAZIF DEMO TICKET | {selected_event['title']} | "
        f"{selected_event['community']}"
    )

    qr_image = create_qr(qr_data)

    qr_col1, qr_col2, qr_col3 = st.columns([1, 2, 1])

    with qr_col2:
        st.image(
            qr_image,
            caption="QR Code — Demo",
            use_container_width=True,
        )

    st.info(
        "هذه تذكرة تجريبية للعرض فقط، وليست حجزاً فعلياً."
    )
    
# =========================================================
# MY ACCOUNT PAGE
# =========================================================

elif st.session_state.page == "حسابي":

    section_title(
        "حسابي",
        "مساحتك الشخصية في مجتمع جازف.",
    )

    st.markdown(
        """
        <div class="community-cover">
            <h2>مرحباً بك في جازف 🌿</h2>
            <p>كل تجربة تبدأ باهتمام، وكل مجتمع يبدأ بأشخاص مثلك.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_title("ملفي الشخصي")

    with st.container():
        st.markdown(
            """
            <div class="card">
                <div class="card-title">Community Member</div>
                <p class="muted">JAZIF Community Space</p>
                <span class="tag">🌱 New Member</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    section_title("مجتمعاتي")

    if st.session_state.interests:
        for community in st.session_state.interests:
            info = COMMUNITIES[community]

            st.markdown(
                f"""
                <div class="card">
                    <div class="card-title">
                        {info["emoji"]} {community}
                    </div>
                    <p>{info["description"]}</p>
                    <span class="tag">Joined Interest</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.info(
            "ما سجلت اهتمامك بأي مجتمع حتى الآن. "
            "استكشف المجتمعات واختر اللي يناسبك."
        )

    section_title("إنجازاتي وشاراتي")

    badges = [
        ("🌱", "First Step", "أول خطوة في جازف"),
        ("💡", "Idea Starter", "شاركت فكرة مع المجتمع"),
        ("💚", "Community Supporter", "دعمت أفكار الآخرين"),
        ("✨", "Explorer", "استكشفت المجتمعات"),
    ]

    badge_columns = st.columns(2)

    for index, (emoji, title, description) in enumerate(badges):
        with badge_columns[index % 2]:
            st.markdown(
                f"""
                <div class="card">
                    <div style="font-size:25px;">{emoji}</div>
                    <div class="card-title">{title}</div>
                    <div class="muted">{description}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    section_title("نشاطي في جازف")

    total_ideas = len(st.session_state.ideas)
    total_votes = sum(st.session_state.votes.values())
    total_interests = len(st.session_state.interests)

    activity_col1, activity_col2, activity_col3 = st.columns(3)

    with activity_col1:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{total_interests}</div>
                <div class="stat-label">اهتماماتي</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with activity_col2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{total_ideas}</div>
                <div class="stat-label">أفكاري</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with activity_col3:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{total_votes}</div>
                <div class="stat-label">تصويتاتي</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div style="
        text-align:center;
        padding:35px 10px 15px;
        margin-top:35px;
        border-top:1px solid #E2E8DF;
    ">
        <div style="
            color:#263D32;
            font-size:20px;
            font-weight:700;
            letter-spacing:1px;
        ">
            JAZIF 🌿
        </div>
        <div style="
            color:#66766A;
            font-size:12px;
            margin-top:5px;
        ">
            A SPACE TO CONNECT, CREATE & GROW
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)