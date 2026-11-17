
import streamlit as st

# =====================================================
# JAZIF | COMMUNITY SPACE
# =====================================================

st.set_page_config(
    page_title="JAZIF | Creative Space",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------- COLORS --------------------

DARK = "#203A30"
GREEN = "#315545"
CREAM = "#F5F1E6"
CARD = "#E5E6D8"
WHITE = "#FFFCF5"
MUTED = "#78847A"
BORDER = "#D9D8CB"

# -------------------- SESSION STATE --------------------

defaults = {
    "page": "الرئيسية",
    "nav_choice": "الرئيسية",
    "last_nav": "الرئيسية",
    "community": "الفخار",
    "joined": [],
    "ideas": {},
    "votes": {},
    "cohosts": {},
    "interests": [],
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -------------------- COMMUNITY DATA --------------------

communities = {
    "الفخار": {
        "en": "POTTERY COMMUNITY",
        "icon": "🏺",
        "description": "مساحة تجمع محبي الفخار والتشكيل بالطين. نتعلم، نجرب، ونصنع قطعاً تحمل بصمتنا الخاصة.",
        "members": 94,
        "image": "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=1200",
        "events": [
            ("Pottery for Beginners", "قريباً", "المساحة الداخلية"),
            ("Make Your Own Cup", "قريباً", "المساحة الداخلية"),
        ],
    },
    "اليوغا": {
        "en": "YOGA COMMUNITY",
        "icon": "🧘🏻‍♀️",
        "description": "مساحة للحركة والهدوء والتوازن، نلتقي فيها لنمنح أنفسنا وقتاً للحضور والاسترخاء.",
        "members": 76,
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200",
        "events": [
            ("Sunset Yoga", "قريباً", "الحديقة الخارجية"),
            ("Yoga & Coffee", "قريباً", "الحديقة الخارجية"),
        ],
    },
    "الفنون": {
        "en": "ART COMMUNITY",
        "icon": "🎨",
        "description": "مجتمع للإبداع والتعبير الفني، نتشارك الأفكار ونجرب أساليب جديدة ونحتفي باختلاف أعمالنا.",
        "members": 112,
        "image": "https://images.unsplash.com/photo-1513364776144-60967b0f800f?w=1200",
        "events": [
            ("Art Jamming", "قريباً", "المساحة الداخلية"),
            ("Creative Painting", "قريباً", "المساحة الداخلية"),
        ],
    },
    "الورش": {
        "en": "WORKSHOPS COMMUNITY",
        "icon": "💡",
        "description": "مساحة للتعلم وتبادل المهارات والأفكار، وتحويل المعرفة إلى تجارب عملية.",
        "members": 88,
        "image": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=1200",
        "events": [
            ("AI for Everyone", "قريباً", "المساحة الداخلية"),
            ("Creative Thinking", "قريباً", "المساحة الداخلية"),
        ],
    },
}

# -------------------- CSS --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap');

:root {
    --dark: #203A30;
    --green: #315545;
    --cream: #F5F1E6;
    --card: #E5E6D8;
}

html, body, [class*="css"], button, input, textarea {
    font-family: 'IBM Plex Sans Arabic', sans-serif !important;
}

.stApp {
    background: var(--cream);
    color: var(--dark);
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 1250px;
    padding: 165px 1.3rem 3rem !important;
}

h1, h2, h3, h4 {
    color: var(--dark) !important;
    font-weight: 700 !important;
}

p {
    line-height: 1.9;
}

/* FIXED HEADER */

.st-key-jazif_header {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    z-index: 999999 !important;
    background: rgba(245,241,230,0.98) !important;
    padding: 13px max(16px, calc((100vw - 1180px)/2)) 10px !important;
    border-bottom: 1px solid #D9D8CB;
    box-shadow: 0 5px 18px rgba(32,58,48,0.06);
}

.brand {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.brand-name {
    font-family: Arial, sans-serif;
    font-size: 34px;
    font-weight: 800;
    letter-spacing: 6px;
    color: var(--dark);
}

.brand-sub {
    font-size: 11px;
    letter-spacing: 4px;
    color: #78847A;
}

.brand-star {
    font-size: 34px;
    color: var(--dark);
}

.st-key-jazif_header div[data-testid="stRadio"] > label {
    display: none;
}

.st-key-jazif_header div[data-testid="stRadio"] > div {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    gap: 7px;
}

.st-key-jazif_header div[data-testid="stRadio"] label {
    flex: 1;
    min-width: 0;
    justify-content: center;
    border: 1px solid #D9D8CB;
    border-radius: 40px;
    padding: 7px 4px;
    background: #FFFCF5;
    margin: 0;
}

.st-key-jazif_header div[data-testid="stRadio"] label p {
    font-size: 13px;
    font-weight: 600;
    color: var(--dark);
    white-space: nowrap;
}

.st-key-jazif_header div[data-testid="stRadio"] label:has(input:checked) {
    background: var(--dark);
    border-color: var(--dark);
}

.st-key-jazif_header div[data-testid="stRadio"] label:has(input:checked) p {
    color: white !important;
}

.st-key-jazif_header div[data-testid="stRadio"] label > div:first-child {
    display: none;
}

/* HERO */

.hero {
    min-height: 650px;
    border-radius: 0 0 30px 30px;
    background:
    linear-gradient(180deg, rgba(12,34,27,0.15), rgba(12,34,27,0.85)),
    url("https://images.unsplash.com/photo-1448375240586-882707db888b?w=1800");
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 35px;
    color: white;
    margin-bottom: 45px;
}

.hero-kicker {
    font-size: 12px;
    letter-spacing: 4px;
    color: #D9E2D5;
}

.hero h1 {
    color: white !important;
    font-size: clamp(36px, 6vw, 65px);
    line-height: 1.3;
    max-width: 750px;
}

.hero p {
    color: #F1F0E8;
    font-size: 17px;
    max-width: 580px;
}

/* GENERAL */

.eyebrow {
    color: #829087;
    letter-spacing: 5px;
    font-size: 12px;
    font-weight: 600;
}

.section-title {
    font-size: 30px;
    margin: 5px 0;
}

.section-desc {
    color: #78847A;
    margin-bottom: 25px;
}

.stButton button {
    background: var(--dark) !important;
    color: white !important;
    border: 1px solid var(--dark) !important;
    border-radius: 40px !important;
    min-height: 48px;
    font-weight: 600 !important;
}

.stButton button:hover {
    background: var(--green) !important;
    border-color: var(--green) !important;
}

.stButton button p,
.stButton button span {
    color: white !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 20px !important;
    border-color: var(--border) !important;
    background: var(--white);
}

.stTextInput input, .stTextArea textarea {
    background: #FFFCF5 !important;
    border: 1px solid #C9D0C4 !important;
    border-radius: 13px !important;
    color: var(--dark) !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #87938A !important;
}

/* COMMUNITY IMAGE CARDS */

.community-card-title {
    font-size: 20px;
    font-weight: 700;
    color: var(--dark);
    margin-top: 8px;
}

.community-card-sub {
    color: #78847A;
    font-size: 11px;
    letter-spacing: 2px;
}

div[data-testid="stImage"] img {
    border-radius: 15px;
}

/* COMMUNITY DETAIL */

.detail-cover {
    min-height: 350px;
    border-radius: 22px;
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 28px;
    color: white;
    margin-bottom: 20px;
}

.detail-cover h1 {
    color: white !important;
    font-size: 42px;
}

.detail-cover p {
    color: white;
}

.detail-box {
    background: #E5E6D8;
    border: 1px solid #D4D7C9;
    border-radius: 20px;
    padding: 20px;
    margin: 15px 0;
}

.stat-number {
    font-size: 30px;
    font-weight: 700;
    color: var(--dark);
}

.event-box {
    background: #FFFCF5;
    border: 1px solid #D9D8CB;
    border-radius: 17px;
    padding: 17px;
    margin-bottom: 12px;
}

.idea-box {
    background: #E5E6D8;
    border: 1px solid #D4D7C9;
    border-radius: 18px;
    padding: 18px;
    margin: 12px 0;
}

.footer {
    text-align: center;
    color: #78847A;
    padding: 35px 10px;
    margin-top: 50px;
    border-top: 1px solid #D9D8CB;
}

@media(max-width:600px) {
    .block-container {
        padding: 155px 0.85rem 2rem !important;
    }

    .st-key-jazif_header {
        padding: 10px 9px !important;
    }

    .brand-name {
        font-size: 29px;
    }

    .brand-sub {
        font-size: 9px;
        letter-spacing: 3px;
    }

    .st-key-jazif_header div[data-testid="stRadio"] > div {
        gap: 5px;
    }

    .st-key-jazif_header div[data-testid="stRadio"] label {
        padding: 8px 2px;
    }

    .st-key-jazif_header div[data-testid="stRadio"] label p {
        font-size: 11px;
    }

    .hero {
        min-height: 580px;
        padding: 22px;
        border-radius: 0 0 22px 22px;
    }

    .hero h1 {
        font-size: 37px;
    }

    .hero p {
        font-size: 14px;
    }

    .detail-cover {
        min-height: 290px;
        padding: 20px;
    }

    .detail-cover h1 {
        font-size: 32px;
    }
}
</style>
""", unsafe_allow_html=True)


# -------------------- HEADER --------------------

with st.container(key="jazif_header"):
    st.markdown("""
    <div class="brand">
        <div>
            <div class="brand-name">JAZIF</div>
            <div class="brand-sub">CREATIVE SPACE · RIYADH</div>
        </div>
        <div class="brand-star">✦</div>
    </div>
    """, unsafe_allow_html=True)

    pages = ["الرئيسية", "المجتمعات", "التجارب", "خريطة المساحة"]

    selected = st.radio(
        "Navigation",
        pages,
        horizontal=True,
        key="nav_choice",
        label_visibility="collapsed"
    )

    if selected != st.session_state.last_nav:
        st.session_state.page = selected
        st.session_state.last_nav = selected


# -------------------- HOME PAGE --------------------

if st.session_state.page == "الرئيسية":

    st.markdown("""
    <div class="hero">
        <div class="hero-kicker">
            A SPACE TO CONNECT · CREATE · EXPERIENCE
        </div>
        <h1>Take the step.<br>Be you.</h1>
        <p dir="rtl">
            جازف، مساحة تبدأ فيها خطوة صغيرة،
            وتكتشف من خلالها أشياء جديدة عن نفسك والعالم حولك.
        </p>
        <div style="margin-top:25px;font-size:13px;letter-spacing:3px;">
            JAZIF · RIYADH
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="eyebrow">WELCOME TO JAZIF</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-title">مساحة تشبهك.</div>',
                unsafe_allow_html=True)
    st.markdown(
        '<div class="section-desc">مساحة تجمع الأشخاص حول اهتماماتهم، '
        'وتمنحهم فرصة للتجربة والتواصل وصناعة ذكريات جديدة.</div>',
        unsafe_allow_html=True
    )

    a, b, c = st.columns(3)
    a.metric("Communities", "04")
    b.metric("Indoor Space", "105 m²")
    c.metric("Outdoor Space", "533 m²")

    st.markdown("---")

    st.markdown('<div class="eyebrow">DISCOVER YOUR COMMUNITY</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-title">اعثر على مجتمعك</div>',
                unsafe_allow_html=True)

    if st.button("اكتشف المجتمعات ←", use_container_width=True):
        st.session_state.page = "المجتمعات"
        st.session_state.nav_choice = "المجتمعات"
        st.session_state.last_nav = "المجتمعات"
        st.rerun()

    st.markdown("---")
    st.markdown('<div class="eyebrow">UPCOMING EXPERIENCES</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-title">تجارب قادمة</div>',
                unsafe_allow_html=True)

    for name, data in communities.items():
        for event in data["events"][:1]:
            with st.container(border=True):
                st.markdown(f"### {event[0]}")
                st.caption(f"{name} · {event[1]} · {event[2]}")

    st.markdown("""
    <div class="footer">
        <b>JAZIF · CREATIVE SPACE</b><br>
        A place to connect, create & belong.
    </div>
    """, unsafe_allow_html=True)


# -------------------- COMMUNITIES PAGE --------------------

elif st.session_state.page == "المجتمعات":

    st.markdown('<div class="eyebrow">THE COMMUNITIES</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-title">اختر مجتمعك</div>',
                unsafe_allow_html=True)
    st.markdown(
        '<div class="section-desc">كل مجتمع له اهتمامه، ناسه، '
        'وتجارب تصنعونها مع بعض.</div>',
        unsafe_allow_html=True
    )

    names = list(communities.keys())

    # Two equal columns, including on mobile
    for i in range(0, len(names), 2):
        cols = st.columns(2, gap="medium")

        for j, col in enumerate(cols):
            index = i + j

            if index >= len(names):
                continue

            name = names[index]
            data = communities[name]

            with col:
                with st.container(border=True):
                    st.image(data["image"], use_container_width=True)
                    st.markdown(
                        f'<div class="community-card-title">'
                        f'{data["icon"]} {name}</div>'
                        f'<div class="community-card-sub">'
                        f'{data["en"]}</div>',
                        unsafe_allow_html=True
                    )
                    st.caption(f"👥 {data['members']} عضو")

                    if st.button(
                        "اكتشف المجتمع ←",
                        key=f"open_{name}",
                        use_container_width=True
                    ):
                        st.session_state.community = name
                        st.session_state.page = "تفاصيل المجتمع"
                        st.rerun()

    st.markdown("""
    <div class="footer">
        JAZIF · FIND YOUR PEOPLE
    </div>
    """, unsafe_allow_html=True)


# -------------------- COMMUNITY DETAIL PAGE --------------------

elif st.session_state.page == "تفاصيل المجتمع":

    name = st.session_state.community
    data = communities[name]

    if st.button("← العودة إلى المجتمعات"):
        st.session_state.page = "المجتمعات"
        st.rerun()

    st.markdown(f"""
    <div class="detail-cover"
         style="background-image:linear-gradient(
         0deg,rgba(17,40,30,.9),rgba(17,40,30,.05)),
         url('{data["image"]}');">
        <div style="font-size:14px;letter-spacing:3px;">
            {data["en"]}
        </div>
        <h1>{data["icon"]} {name}</h1>
        <p>Find your people. Share your passion.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="eyebrow">ABOUT THE COMMUNITY</div>',
                unsafe_allow_html=True)
    st.markdown(f"## عن مجتمع {name}")
    st.write(data["description"])

    st.markdown("---")

    # MEMBERS
    st.markdown("### مجتمعنا بالأرقام")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(f"""
        <div class="detail-box">
            <div class="stat-number">{data["members"]}</div>
            <div>عضو في المجتمع 👥</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="detail-box">
            <div class="stat-number">02</div>
            <div>تجارب قادمة ✨</div>
        </div>
        """, unsafe_allow_html=True)

    # EVENTS
    st.markdown("---")
    st.markdown("### الفعاليات القادمة")

    for event in data["events"]:
        st.markdown(f"""
        <div class="event-box">
            <b>✨ {event[0]}</b><br>
            <span style="color:#78847A;font-size:13px;">
                {event[1]} · {event[2]}
            </span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # REGISTRATION
    st.markdown('<div class="eyebrow">BECOME A MEMBER</div>',
                unsafe_allow_html=True)
    st.markdown("### انضم إلى المجتمع")

    if name in st.session_state.joined:

        st.success("أنت عضو في هذا المجتمع! 🌿")

    else:

        st.write("سجل اهتمامك وانضم إلى الأشخاص الذين يشاركونك هذا الشغف.")

        member_name = st.text_input(
            "اسمك",
            key=f"member_name_{name}",
            placeholder="اكتب اسمك"
        )

        if st.button(
            "انضم إلى المجتمع +",
            key=f"join_{name}",
            use_container_width=True
        ):

            if member_name.strip():

                st.session_state.joined.append(name)
                st.session_state.interests.append(name)

                st.success("تم تسجيل انضمامك بنجاح!")
                st.rerun()

            else:
                st.warning("اكتب اسمك أولاً.")

    # IDEA LAB ONLY AFTER JOINING
    if name in st.session_state.joined:

        st.markdown("---")

        st.markdown(
            '<div class="eyebrow">IDEA LAB · COMMUNITY VOICE</div>',
            unsafe_allow_html=True
        )

        st.markdown("## مختبر الأفكار 💡")
        st.write(
            "هنا تبدأ الأفكار من الأعضاء، "
            "وتتحول إلى تجارب يصنعها المجتمع معاً."
        )

        # Add idea
        with st.container(border=True):

            st.markdown("### اقترح تجربة جديدة")
            idea = st.text_input(
                "فكرتك",
                key=f"new_idea_{name}",
                placeholder="مثال: جلسة فخار مع موسيقى هادئة..."
            )

            if st.button(
                "＋ اطرح فكرتك",
                key=f"add_idea_{name}",
                use_container_width=True
            ):

                if idea.strip():

                    st.session_state.ideas.setdefault(name, [])

                    st.session_state.ideas[name].append({
                        "text": idea.strip(),
                        "love": 0,
                        "support": 0,
                        "cohost": 0
                    })

                    st.success("تمت إضافة فكرتك!")
                    st.rerun()

                else:
                    st.warning("اكتب فكرتك أولاً.")

        # Suggested ideas
        default_ideas = {
            "الفخار": [
                "معرض مصغر لأعمال أعضاء المجتمع",
                "اصنع كوبك الخاص",
            ],
            "اليوغا": [
                "Sunset Yoga & Coffee",
                "جلسة تأمل في الحديقة",
            ],
            "الفنون": [
                "Art Jamming Night",
                "تبادل اللوحات الفنية",
            ],
            "الورش": [
                "AI for Everyone",
                "Creative Thinking Session",
            ],
        }

        ideas = [
            {
                "text": item,
                "love": 0,
                "support": 0,
                "cohost": 0
            }
            for item in default_ideas[name]
        ]

        ideas += st.session_state.ideas.get(name, [])

        st.markdown("### أفكار المجتمع")

        for index, item in enumerate(ideas):

            with st.container(border=True):

                st.markdown(f"#### 💡 {item['text']}")

                st.caption("شارك رأيك وساعد الفكرة تكبر.")

                v1, v2 = st.columns(2)

                with v1:
                    if st.button(
                        f"❤️ We Love It ({item['love']})",
                        key=f"love_{name}_{index}",
                        use_container_width=True
                    ):
                        item["love"] += 1
                        st.rerun()

                with v2:
                    if st.button(
                        f"🙌 We Support It ({item['support']})",
                        key=f"support_{name}_{index}",
                        use_container_width=True
                    ):
                        item["support"] += 1
                        st.rerun()

                if st.button(
                    f"🤝 Be a Co-host ({item['cohost']})",
                    key=f"cohost_{name}_{index}",
                    use_container_width=True
                ):
                    item["cohost"] += 1
                    st.success("تم تسجيل اهتمامك بالمشاركة!")
                    st.rerun()

    else:

        st.markdown("""
        <div class="detail-box" style="text-align:center;">
            <div style="font-size:30px;">🔒</div>
            <h3>Idea Lab</h3>
            <p>انضم إلى المجتمع أولاً لتشارك أفكارك
            وتصوت على التجارب القادمة.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        JAZIF · YOUR COMMUNITY, YOUR IDEAS
    </div>
    """, unsafe_allow_html=True)


# -------------------- EXPERIENCES PAGE --------------------

elif st.session_state.page == "التجارب":

    st.markdown('<div class="eyebrow">THE EXPERIENCES</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-title">جرّب شيئاً جديداً.</div>',
                unsafe_allow_html=True)
    st.write("تجارب جازف تبدأ باهتمام وتنمو بمشاركة المجتمع.")

    for name, data in communities.items():

        for event in data["events"]:

            with st.container(border=True):
                st.markdown(f"### ✨ {event[0]}")
                st.caption(f"{name} · {event[1]} · {event[2]}")

                if st.button(
                    "اكتشف المجتمع",
                    key=f"event_community_{name}_{event[0]}",
                    use_container_width=True
                ):
                    st.session_state.community = name
                    st.session_state.page = "تفاصيل المجتمع"
                    st.rerun()


# -------------------- SPACE MAP PAGE --------------------

elif st.session_state.page == "خريطة المساحة":

    st.markdown('<div class="eyebrow">JAZIF · SPACE MAP</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-title">اكتشف المساحة</div>',
                unsafe_allow_html=True)
    st.write("كل زاوية في جازف صممت لتمنحك تجربة مختلفة.")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="detail-box" style="text-align:center;min-height:210px;">
            <div style="font-size:42px;">🏡</div>
            <h3>المساحة الداخلية</h3>
            <div class="stat-number">105 m²</div>
            <p>ورش · لقاءات · تجارب إبداعية</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="detail-box" style="text-align:center;min-height:210px;">
            <div style="font-size:42px;">🌳</div>
            <h3>الحديقة الخارجية</h3>
            <div class="stat-number">533 m²</div>
            <p>تجارب خارجية · يوغا · لقاءات</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### مساحة للجميع")
    st.write("اكتشف المناطق والتجارب المتاحة داخل جازف.")


# -------------------- END --------------------
