import streamlit as st

# =====================================================
# JAZIF — CREATIVE SPACE | RIYADH
# =====================================================

st.set_page_config(
    page_title="JAZIF | Creative Space",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------- COLORS -------------------------

DARK = "#20382F"
GREEN = "#496653"
CREAM = "#F4F1E7"
WHITE = "#FFFCF5"
MUTED = "#7C887F"
BORDER = "#DEDCCF"
RED = "#C94F59"

# ------------------- SESSION STATE --------------------

defaults = {
    "page": "الرئيسية",
    "community": "Music",
    "votes": {},
    "ideas": [],
    "cohosts": [],
    "interests": [],
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ----------------------- DATA -------------------------

communities = {
    "Music": {
        "icon": "🎧",
        "arabic": "الموسيقى",
        "description": "اكتشف موسيقى جديدة وشارك ما تحب.",
        "color": "#DCE5D9",
        "ideas": ["Music Night", "Vinyl Listening", "Music Exchange"]
    },
    "Art": {
        "icon": "🎨",
        "arabic": "الفنون",
        "description": "مساحة للإبداع والتجربة الفنية.",
        "color": "#EADDD1",
        "ideas": ["Art Jamming", "Paint & Coffee", "Creative Workshop"]
    },
    "Pottery": {
        "icon": "🏺",
        "arabic": "الفخار",
        "description": "اصنع شيئاً بيديك واكتشف عالم الفخار.",
        "color": "#E9DFCC",
        "ideas": ["Pottery for Beginners", "Clay & Coffee"]
    },
    "Yoga": {
        "icon": "🧘🏻‍♀️",
        "arabic": "اليوغا",
        "description": "الحركة والهدوء والتوازن.",
        "color": "#DDE6E0",
        "ideas": ["Sunset Yoga", "Yoga & Coffee"]
    },
    "Horses": {
        "icon": "🐎",
        "arabic": "الخيول",
        "description": "تجارب للتعرف على الخيل والتواصل معها.",
        "color": "#E8E0D5",
        "ideas": ["Meet the Horses", "Horse Care"]
    },
    "Workshops": {
        "icon": "💡",
        "arabic": "الورش",
        "description": "تعلم مهارات جديدة وشارك خبراتك.",
        "color": "#E4E4D7",
        "ideas": ["AI for Everyone", "Creative Thinking"]
    }
}

experiences = [
    {
        "name": "Walk & Talk",
        "category": "Community",
        "location": "الحديقة الخارجية",
        "description": "لقاء مفتوح للتعارف والمشي ومشاركة الأحاديث.",
        "image": "https://images.unsplash.com/photo-1472396961693-142e6e269027?w=1200"
    },
    {
        "name": "Art Jamming",
        "category": "Art",
        "location": "المساحة الداخلية",
        "description": "تجربة رسم جماعية بدون قواعد أو توقعات.",
        "image": "https://images.unsplash.com/photo-1513364776144-60967b0f800f?w=1200"
    },
    {
        "name": "Pottery Time",
        "category": "Pottery",
        "location": "المساحة الداخلية",
        "description": "اكتشف متعة تشكيل الطين وصناعة قطعتك الخاصة.",
        "image": "https://images.unsplash.com/photo-1565193298595-6b5b9e5a3b11?w=1200"
    }
]

# ------------------------- CSS -------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');

:root {
    --dark: #20382F;
    --green: #496653;
    --cream: #F4F1E7;
    --white: #FFFCF5;
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
    max-width: 1200px;
    padding: 150px 1.3rem 3rem !important;
}

h1, h2, h3, h4 {
    color: var(--dark) !important;
    font-weight: 700 !important;
}

p {
    line-height: 1.9;
}

/* FIXED NAVIGATION */

.st-key-site_header {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    z-index: 999999 !important;
    width: 100% !important;
    box-sizing: border-box !important;
    background: var(--cream) !important;
    padding: 12px max(16px, calc((100vw - 1100px)/2)) 10px !important;
    border-bottom: 1px solid var(--border);
    box-shadow: 0 3px 15px rgba(32,56,47,.07);
}

.brand {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 3px 10px;
}

.brand-name {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 34px;
    font-weight: 700;
    letter-spacing: 5px;
    color: var(--dark);
}

.brand-sub {
    display: block;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 10px;
    letter-spacing: 4px;
    color: #7D8980;
}

.brand-star {
    font-size: 31px;
    color: var(--dark);
}

.st-key-site_header div[data-testid="stRadio"] > label {
    display: none !important;
}

.st-key-site_header div[data-testid="stRadio"] > div {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    gap: 7px !important;
    width: 100%;
}

.st-key-site_header div[data-testid="stRadio"] label {
    flex: 1 1 0 !important;
    min-width: 0 !important;
    justify-content: center !important;
    background: var(--white) !important;
    border: 1px solid #DAD8CD !important;
    border-radius: 30px !important;
    padding: 8px 3px !important;
    margin: 0 !important;
}

.st-key-site_header div[data-testid="stRadio"] label p {
    font-size: 12px !important;
    color: var(--dark) !important;
    font-weight: 600 !important;
    white-space: nowrap !important;
}

.st-key-site_header label:has(input:checked) {
    background: var(--dark) !important;
    border-color: var(--dark) !important;
}

.st-key-site_header label:has(input:checked) p {
    color: white !important;
}

.st-key-site_header label > div:first-child {
    display: none !important;
}

/* HERO */

.hero {
    height: 590px;
    width: 100%;
    border-radius: 0 0 30px 30px;
    overflow: hidden;
    position: relative;
    background-image:
        linear-gradient(0deg, rgba(15,35,27,.82), rgba(15,35,27,.08)),
        url('https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1800');
    background-position: center;
    background-size: cover;
    display: flex;
    align-items: flex-end;
    box-sizing: border-box;
    padding: 45px;
    margin-bottom: 65px;
}

.hero-content {
    color: white;
    max-width: 650px;
}

.hero-kicker {
    font-family: 'DM Sans', sans-serif;
    letter-spacing: 3px;
    font-size: 12px;
    color: #E5E9DF;
    margin-bottom: 20px;
}

.hero-title {
    color: white !important;
    font-size: clamp(38px, 6vw, 72px);
    line-height: 1.2;
    font-weight: 700;
    margin: 0 0 15px;
}

.hero-description {
    color: #F0F0E8;
    font-size: 17px;
    max-width: 470px;
    line-height: 2;
}

/* SECTIONS */

.eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    letter-spacing: 5px;
    color: #89958A;
    margin-bottom: 12px;
}

.section-heading {
    font-size: 32px;
    margin-bottom: 8px;
    font-weight: 700;
}

.section-desc {
    color: var(--muted);
    font-size: 15px;
    margin-bottom: 28px;
}

.section-space {
    height: 45px;
}

/* COMMUNITY SQUARES */

.community-square {
    aspect-ratio: 1 / 1;
    width: 100%;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 18px;
    box-sizing: border-box;
    border: 1px solid rgba(32,56,47,.10);
    margin-bottom: 10px;
    transition: .2s;
}

.community-icon {
    font-size: 38px;
}

.community-name {
    font-size: 19px;
    font-weight: 700;
    color: var(--dark);
}

.community-en {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    letter-spacing: 2px;
    color: #68776C;
}

.stButton button {
    background: var(--dark) !important;
    color: white !important;
    border: 1px solid var(--dark) !important;
    border-radius: 30px !important;
    min-height: 44px;
    font-weight: 600 !important;
}

.stButton button p {
    color: white !important;
}

.stButton button:hover {
    background: var(--green) !important;
    border-color: var(--green) !important;
}

/* EXPERIENCE CARDS */

.experience-image {
    width: 100%;
    height: 330px;
    object-fit: cover;
    border-radius: 20px;
}

.experience-name {
    font-size: 25px;
    font-weight: 700;
    margin-top: 13px;
}

.experience-meta {
    color: var(--muted);
    font-size: 13px;
}

/* COMMUNITY DETAILS */

.detail-hero {
    padding: 30px;
    border-radius: 24px;
    background: #E5E8DC;
    margin: 20px 0;
}

.idea-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 20px;
    margin: 12px 0;
}

.vote-label {
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 13px;
}

.footer {
    border-top: 1px solid #D9D8CC;
    padding: 35px 10px;
    margin-top: 70px;
    text-align: center;
    color: #7A887E;
    font-size: 12px;
    letter-spacing: 2px;
}

/* MOBILE */

@media(max-width:600px) {
    .block-container {
        padding: 137px .85rem 2rem !important;
    }

    .st-key-site_header {
        padding: 10px 10px 9px !important;
    }

    .brand-name {
        font-size: 29px;
    }

    .brand-sub {
        font-size: 9px;
        letter-spacing: 3px;
    }

    .st-key-site_header div[data-testid="stRadio"] > div {
        gap: 5px !important;
    }

    .st-key-site_header div[data-testid="stRadio"] label {
        padding: 8px 1px !important;
    }

    .st-key-site_header div[data-testid="stRadio"] label p {
        font-size: 11px !important;
    }

    .hero {
        height: 590px;
        border-radius: 0 0 25px 25px;
        padding: 23px;
        margin-bottom: 45px;
    }

    .hero-title {
        font-size: 39px;
    }

    .hero-description {
        font-size: 14px;
    }

    .section-heading {
        font-size: 27px;
    }

    .community-square {
        padding: 13px;
        border-radius: 16px;
    }

    .community-icon {
        font-size: 30px;
    }

    .community-name {
        font-size: 16px;
    }

    .community-en {
        font-size: 9px;
    }

    .experience-image {
        height: 260px;
    }
}
</style>
""", unsafe_allow_html=True)


# ----------------------- HEADER -------------------------

with st.container(key="site_header"):

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
        index=pages.index(st.session_state.page),
        horizontal=True,
        label_visibility="collapsed",
        key="site_navigation"
    )

    st.session_state.page = selected


# =====================================================
# HOME
# =====================================================

if st.session_state.page == "الرئيسية":

    st.markdown("""
    <div class="hero">
        <div class="hero-content">
            <div class="hero-kicker">
                A SPACE TO CONNECT · CREATE · EXPERIENCE
            </div>
            <div class="hero-title">
                Take the step.<br>Be you.
            </div>
            <div class="hero-description" dir="rtl">
                جازف، مساحة تبدأ فيها خطوة صغيرة،
                وتكتشف من خلالها أشياء جديدة عن نفسك والعالم حولك.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="eyebrow">DISCOVER JAZIF</div>
    <div class="section-heading">مساحتك لاكتشاف شيء جديد</div>
    <div class="section-desc">
        مجتمعات، تجارب، وأشخاص تجمعهم الاهتمامات المشتركة.
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="idea-card">
            <div style="font-size:30px">🌿</div>
            <b>COMMUNITY</b>
            <p>اكتشف مجتمعاً يشبه اهتماماتك.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="idea-card">
            <div style="font-size:30px">✨</div>
            <b>EXPERIENCES</b>
            <p>جرّب أشياء جديدة واصنع ذكريات.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="idea-card">
            <div style="font-size:30px">💡</div>
            <b>IDEAS</b>
            <p>أفكارك قد تصبح تجربة للجميع.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="eyebrow">FIND YOUR PEOPLE</div>
    <div class="section-heading">مجتمعات جازف</div>
    <div class="section-desc">لكل اهتمام مساحة، ولكل مساحة أشخاص.</div>
    """, unsafe_allow_html=True)

    names = list(communities.keys())

    for start in range(0, len(names), 2):
        cols = st.columns(2)

        for col, name in zip(cols, names[start:start+2]):
            data = communities[name]

            with col:
                st.markdown(f"""
                <div class="community-square"
                     style="background:{data['color']}">
                    <div class="community-icon">{data['icon']}</div>
                    <div>
                        <div class="community-name">{data['arabic']}</div>
                        <div class="community-en">{name.upper()}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if st.button(
                    "اكتشف المجتمع ←",
                    key=f"home_{name}",
                    use_container_width=True
                ):
                    st.session_state.community = name
                    st.session_state.page = "المجتمعات"
                    st.rerun()

    st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="eyebrow">COME EXPERIENCE</div>
    <div class="section-heading">مساحة للتجربة</div>
    """, unsafe_allow_html=True)

    for event in experiences:
        st.image(event["image"], use_container_width=True)
        st.markdown(f"### {event['name']}")
        st.caption(event["location"])
        st.write(event["description"])
        st.divider()

    if st.button("استكشف جميع التجارب ←", use_container_width=True):
        st.session_state.page = "التجارب"
        st.rerun()


# =====================================================
# COMMUNITIES
# =====================================================

elif st.session_state.page == "المجتمعات":

    st.markdown("""
    <div class="eyebrow">THE COMMUNITIES</div>
    <div class="section-heading">اختر مجتمعك</div>
    <div class="section-desc">
        كل مجتمع له اهتمامه، ناسه، وتجارب تصنعونها مع بعض.
    </div>
    """, unsafe_allow_html=True)

    names = list(communities.keys())

    # Equal square cards: two columns on mobile

    for start in range(0, len(names), 2):
        cols = st.columns(2)

        for col, name in zip(cols, names[start:start+2]):
            data = communities[name]

            with col:
                st.markdown(f"""
                <div class="community-square"
                     style="background:{data['color']}">
                    <div class="community-icon">{data['icon']}</div>
                    <div>
                        <div class="community-name">{data['arabic']}</div>
                        <div class="community-en">{name.upper()}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if st.button(
                    "استكشف المجتمع",
                    key=f"community_{name}",
                    use_container_width=True
                ):
                    st.session_state.community = name
                    st.rerun()

    st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

    name = st.session_state.community
    data = communities[name]

    st.markdown("---")

    st.markdown(f"""
    <div class="eyebrow">{name.upper()} COMMUNITY</div>
    <div class="section-heading">
        {data['icon']} مجتمع {data['arabic']}
    </div>
    <div class="section-desc">{data['description']}</div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        "عن المجتمع",
        "مختبر الأفكار",
        "Community Space"
    ])

    # ABOUT

    with tab1:

        st.subheader("عن المجتمع")

        st.write(data["description"])

        st.markdown("### What to Bring 🎒")

        for item in ["الحماس للتجربة", "الاستعداد للتعرف على أشخاص جدد"]:
            st.checkbox(item, key=f"bring_{name}_{item}")

        if st.button("سجل اهتمامك بالمجتمع", use_container_width=True):
            if name not in st.session_state.interests:
                st.session_state.interests.append(name)
            st.success("تم تسجيل اهتمامك بنجاح 🌿")

    # IDEA LAB

    with tab2:

        st.subheader("Idea Lab 💡")

        st.write("شارك فكرة جديدة أو صوّت على فكرة تعجبك.")

        with st.form(f"idea_form_{name}"):

            new_idea = st.text_input(
                "اقترح تجربة أو لقاء جديد لهذا المجتمع:",
                placeholder="مثال: جلسة موسيقى مع غروب الشمس..."
            )

            submitted = st.form_submit_button(
                "＋ أرسل فكرتك",
                use_container_width=True
            )

            if submitted and new_idea.strip():

                st.session_state.ideas.append({
                    "community": name,
                    "text": new_idea.strip()
                })

                st.success("وصلتنا فكرتك! 💚")

        st.markdown("---")
        st.markdown("### أفكار المجتمع")

        all_ideas = [
            {"text": idea, "id": f"suggested_{name}_{i}"}
            for i, idea in enumerate(data["ideas"])
        ]

        all_ideas += [
            {
                "text": idea["text"],
                "id": f"member_{name}_{i}"
            }
            for i, idea in enumerate(st.session_state.ideas)
            if idea["community"] == name
        ]

        for idea in all_ideas:

            idea_id = idea["id"]

            st.markdown(f"""
            <div class="idea-card">
                <div class="eyebrow">COMMUNITY IDEA</div>
                <div style="font-size:19px;font-weight:700">
                    💡 {idea['text']}
                </div>
            </div>
            """, unsafe_allow_html=True)

            love, support = st.columns(2)

            current = st.session_state.votes.get(
                idea_id, {"love": 0, "support": 0}
            )

            with love:
                if st.button(
                    f"❤️ We Love It ({current['love']})",
                    key=f"love_{idea_id}",
                    use_container_width=True
                ):
                    current["love"] += 1
                    st.session_state.votes[idea_id] = current
                    st.rerun()

            with support:
                if st.button(
                    f"🙌 We Support It ({current['support']})",
                    key=f"support_{idea_id}",
                    use_container_width=True
                ):
                    current["support"] += 1
                    st.session_state.votes[idea_id] = current
                    st.rerun()

            if st.button(
                "🤝 Be a Co-host",
                key=f"host_{idea_id}",
                use_container_width=True
            ):
                if idea_id not in st.session_state.cohosts:
                    st.session_state.cohosts.append(idea_id)
                st.success("تم تسجيل اهتمامك بالمشاركة في تنظيم الفكرة!")

    # COMMUNITY SPACE

    with tab3:

        st.subheader("Community Space 🌿")

        st.write("مساحة للتواصل ومشاركة الاهتمامات بين الأعضاء.")

        st.info(
            "هذه نسخة تجريبية. سيتم ربط المساحة بنظام العضويات لاحقاً."
        )

        st.markdown("### انضم إلى المجتمع")

        if st.button("طلب الانضمام للمجتمع", use_container_width=True):
            if name not in st.session_state.interests:
                st.session_state.interests.append(name)
            st.success("تم إرسال طلب اهتمامك!")


# =====================================================
# EXPERIENCES
# =====================================================

elif st.session_state.page == "التجارب":

    st.markdown("""
    <div class="eyebrow">JAZIF EXPERIENCES</div>
    <div class="section-heading">تجارب تصنع ذكريات</div>
    <div class="section-desc">
        لا تحتاج أن تعرف كل شيء، فقط ابدأ بالتجربة.
    </div>
    """, unsafe_allow_html=True)

    for event in experiences:

        st.image(event["image"], use_container_width=True)

        st.markdown(f"""
        <div class="eyebrow">{event['category'].upper()}</div>
        <div class="section-heading">{event['name']}</div>
        <div class="section-desc">{event['description']}</div>
        """, unsafe_allow_html=True)

        st.caption(f"📍 {event['location']} · قريباً")

        if st.button(
            "أبغى أشارك بالتجربة",
            key=f"experience_{event['name']}",
            use_container_width=True
        ):
            st.success("تم تسجيل اهتمامك بالتجربة!")

        st.markdown("---")


# =====================================================
# SPACE MAP
# =====================================================

elif st.session_state.page == "خريطة المساحة":

    st.markdown("""
    <div class="eyebrow">EXPLORE THE PLACE</div>
    <div class="section-heading">خريطة مساحة جازف</div>
    <div class="section-desc">
        اكتشف المساحات المختلفة وما يمكن أن يحدث فيها.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="idea-card" style="background:#E4E9DE;padding:30px;text-align:center">
        <div style="font-size:50px">🏡</div>
        <div class="section-heading">المساحة الداخلية</div>
        <div style="font-size:34px;font-weight:700">105 m²</div>
        <p>ورش · لقاءات · تجارب إبداعية</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="idea-card" style="background:#DFE8D9;padding:30px;text-align:center">
        <div style="font-size:50px">🌳</div>
        <div class="section-heading">الحديقة الخارجية</div>
        <div style="font-size:34px;font-weight:700">533 m²</div>
        <p>لقاءات · يوغا · تجارب خارجية</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### مساحة واحدة، تجارب كثيرة")

    st.write(
        "تتغير المساحة بحسب التجربة والمجتمع، "
        "لتمنح كل لقاء أجواءه الخاصة."
    )


# ----------------------- FOOTER -------------------------

st.markdown("""
<div class="footer">
    <div style="font-size:25px;color:#20382F;font-weight:700">
        J A Z I F
    </div>
    CREATIVE SPACE · RIYADH
    <br><br>
    A place to connect, create & belong.
    <br>
    <span style="font-size:18px">✦</span>
</div>
""", unsafe_allow_html=True)
