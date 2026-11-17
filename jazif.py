
import streamlit as st

st.set_page_config(
    page_title="JAZIF | Take the step",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# JAZIF — CREATIVE SPACE
# =========================================================

COMMUNITIES = {
    "Draw": {
        "ar": "الفنون والرسم",
        "icon": "🎨",
        "desc": "مساحة نترك فيها الأفكار تتحول إلى ألوان، ونجرب بدون خوف من النتيجة.",
        "image": "https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=1400&q=85",
        "ideas": [
            "جلسة رسم جماعية في الحديقة",
            "Art & Coffee",
            "تبادل اللوحات والأعمال"
        ],
    },
    "Walk": {
        "ar": "المشي والاستكشاف",
        "icon": "🥾",
        "desc": "نطلع من الروتين، نكتشف أماكن جديدة، ونصنع لحظات بسيطة مع أشخاص جدد.",
        "image": "https://images.unsplash.com/photo-1472396961693-142e6e269027?auto=format&fit=crop&w=1400&q=85",
        "ideas": [
            "Sunset Walk",
            "جولة تصوير في الطبيعة",
            "Walk & Talk"
        ],
    },
    "Bikes": {
        "ar": "الدراجات",
        "icon": "🚲",
        "desc": "مجتمع للحركة والتجربة ومشاركة الطرق الجديدة، مهما كان مستواك.",
        "image": "https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=1400&q=85",
        "ideas": [
            "جولة دراجات للمبتدئين",
            "Morning Ride",
            "تحدي مسافة جماعي"
        ],
    },
    "Music": {
        "ar": "الموسيقى",
        "icon": "🎧",
        "desc": "نجتمع حول الأصوات والإيقاعات، نكتشف موسيقى جديدة ونتشارك ما نحب.",
        "image": "https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=1400&q=85",
        "ideas": [
            "جلسة استماع في الحديقة",
            "Open Mic Night",
            "اصنع قائمة موسيقية جماعية"
        ],
    },
    "Yoga": {
        "ar": "اليوغا",
        "icon": "🧘🏻‍♀️",
        "desc": "وقت نبطئ فيه الإيقاع، نتحرك، ونعطي أنفسنا مساحة للتوازن.",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=1400&q=85",
        "ideas": [
            "Sunset Yoga",
            "Yoga & Coffee",
            "جلسة تنفس وتأمل"
        ],
    },
}

EVENTS = [
    {
        "title": "Sunset Sketch Club",
        "community": "Draw",
        "date": "قريباً",
        "place": "الحديقة الخارجية",
        "image": COMMUNITIES["Draw"]["image"],
    },
    {
        "title": "Walk & Talk",
        "community": "Walk",
        "date": "قريباً",
        "place": "نقطة التجمع",
        "image": COMMUNITIES["Walk"]["image"],
    },
    {
        "title": "Listening Session",
        "community": "Music",
        "date": "قريباً",
        "place": "المساحة الداخلية",
        "image": COMMUNITIES["Music"]["image"],
    },
]

# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "page": "الرئيسية",
    "community": "Music",
    "ideas": [],
    "votes": {},
    "interests": [],
    "cohosts": [],
    "new_community_requests": [],
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# DESIGN / CSS
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');

:root {
    --ink: #14251f;
    --forest: #203b31;
    --mint: #c8e2d2;
    --cream: #f4f1e8;
    --line: rgba(32,59,49,.16);
}

html, body, [class*="css"], button, input, textarea {
    font-family: 'IBM Plex Sans Arabic', 'DM Sans', sans-serif !important;
}

.stApp {
    background: var(--cream);
    color: var(--ink);
}

#MainMenu, footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1240px;
    padding: 150px 2rem 3rem !important;
}

/* FIXED NAVIGATION */

.st-key-jazif_nav {
    position: fixed !important;
    top: 0;
    left: 0;
    right: 0;
    z-index: 999999;
    background: rgba(244,241,232,.96);
    backdrop-filter: blur(14px);
    padding: 12px max(18px, calc((100vw - 1180px) / 2)) 10px !important;
    border-bottom: 1px solid var(--line);
}

.brand {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 4px 10px;
}

.brand strong {
    font-family: 'DM Sans', sans-serif;
    font-size: 25px;
    letter-spacing: 3px;
    color: var(--forest);
}

.brand small {
    display: block;
    font-size: 9px;
    letter-spacing: 3px;
    color: #68766d;
}

.brand-mark {
    font-size: 25px;
}

.st-key-jazif_nav [data-testid="stRadio"] > label {
    display: none;
}

.st-key-jazif_nav [data-testid="stRadio"] > div {
    display: flex;
    flex-wrap: nowrap;
    gap: 8px;
}

.st-key-jazif_nav [data-testid="stRadio"] label {
    background: #fffaf0;
    border: 1px solid var(--line);
    border-radius: 30px;
    padding: 6px 13px;
    margin: 0;
    white-space: nowrap;
}

.st-key-jazif_nav [data-testid="stRadio"] label p {
    font-size: 13px;
    color: var(--forest);
    font-weight: 600;
}

.st-key-jazif_nav [data-testid="stRadio"] label:has(input:checked) {
    background: var(--forest);
    border-color: var(--forest);
}

.st-key-jazif_nav [data-testid="stRadio"] label:has(input:checked) p {
    color: white;
}

/* HERO */

.hero-wrap {
    position: relative;
    border-radius: 26px;
    overflow: hidden;
    min-height: 590px;
    background: #203b31;
    margin: 0 0 48px;
}

.hero-img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(.60);
}

.hero-overlay {
    position: absolute;
    inset: 0;
    background:
        linear-gradient(90deg, rgba(12,28,22,.75), rgba(12,28,22,.08)),
        linear-gradient(0deg, rgba(12,28,22,.45), transparent 60%);
}

.hero-content {
    position: absolute;
    left: 7%;
    right: 7%;
    bottom: 12%;
    color: white;
}

.hero-kicker {
    font: 600 11px 'DM Sans';
    letter-spacing: 4px;
    color: #d9e9dd;
}

.hero-content h1 {
    font-size: clamp(38px,6vw,76px);
    line-height: 1.15;
    color: white !important;
    margin: 18px 0;
    font-weight: 700;
}

.hero-content p {
    color: #f1f2e9;
    font-size: 18px;
    max-width: 520px;
}

.hero-foot {
    position: absolute;
    bottom: 25px;
    left: 7%;
    right: 7%;
    display: flex;
    justify-content: space-between;
    color: white;
    font: 11px 'DM Sans';
    letter-spacing: 3px;
    border-top: 1px solid #ffffff70;
    padding-top: 13px;
}

/* SECTIONS */

.section-kicker {
    font: 600 10px 'DM Sans';
    letter-spacing: 4px;
    color: #7c897e;
    margin: 38px 0 8px;
}

.section-heading {
    font-size: 34px;
    font-weight: 700;
    color: var(--forest);
    margin: 0 0 8px;
}

.section-sub {
    color: #69776d;
    font-size: 15px;
    margin-bottom: 22px;
}

/* COMMUNITY IMAGES */

.photo-card {
    position: relative;
    border-radius: 20px;
    overflow: hidden;
    height: 300px;
    margin-bottom: 10px;
    background: #d8dfd5;
}

.photo-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(.76);
}

.photo-card .photo-label {
    position: absolute;
    left: 18px;
    right: 18px;
    bottom: 17px;
    color: white;
}

.photo-label b {
    font-size: 25px;
    display: block;
}

.photo-label span {
    font-size: 12px;
    letter-spacing: 2px;
}

/* EVENTS */

.event-card {
    background: #fffaf0;
    border: 1px solid var(--line);
    border-radius: 18px;
    overflow: hidden;
    margin-bottom: 14px;
}

.event-card img {
    width: 100%;
    height: 165px;
    object-fit: cover;
}

.event-copy {
    padding: 14px;
}

.event-copy small {
    color: #77847a;
}

/* COMMUNITY PAGE */

.community-hero {
    position: relative;
    border-radius: 24px;
    overflow: hidden;
    height: 390px;
    margin-bottom: 24px;
}

.community-hero img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(.55);
}

.community-hero div {
    position: absolute;
    bottom: 28px;
    left: 28px;
    right: 28px;
    color: white;
}

.community-hero h1 {
    color: white !important;
    font-size: 46px;
    margin: 8px 0;
}

/* IDEA LAB */

.idea-card {
    background: #fffaf0;
    border: 1px solid var(--line);
    padding: 20px;
    border-radius: 18px;
    margin: 12px 0;
}

.idea-card h4 {
    margin: 0 0 7px;
    color: var(--forest);
}

/* MAP */

.map-panel {
    background: #e2e8d9;
    border-radius: 24px;
    padding: 24px;
    min-height: 420px;
    position: relative;
    overflow: hidden;
}

.map-zone {
    background: #f9f6ed;
    border: 2px solid #b8c7b6;
    border-radius: 18px;
    padding: 22px;
    text-align: center;
    margin: 10px;
    min-height: 120px;
}

/* BUTTONS AND INPUTS */

.stButton button {
    background: var(--forest) !important;
    color: white !important;
    border: 1px solid var(--forest) !important;
    border-radius: 30px !important;
    min-height: 44px;
    font-weight: 600 !important;
}

.stButton button:hover {
    background: #3e6654 !important;
    border-color: #3e6654 !important;
}

.stTextInput input,
.stTextArea textarea {
    background: #fffaf0 !important;
    border: 1px solid #c8d2c6 !important;
    border-radius: 12px !important;
    color: var(--ink) !important;
}

div[data-testid="stTabs"] button {
    color: #68776d !important;
    font-weight: 600 !important;
}

div[data-testid="stTabs"] button[aria-selected="true"] {
    color: var(--forest) !important;
}

div[data-testid="stTabs"] [data-baseweb="tab-highlight"] {
    background: var(--forest) !important;
}

.footer {
    text-align: center;
    color: #7a867c;
    padding: 35px 0 10px;
    font: 10px 'DM Sans';
    letter-spacing: 3px;
}

/* MOBILE */

@media(max-width:650px) {
    .block-container {
        padding: 140px .8rem 2rem !important;
    }

    .st-key-jazif_nav {
        padding: 8px 8px 9px !important;
    }

    .brand strong {
        font-size: 22px;
    }

    .st-key-jazif_nav [data-testid="stRadio"] > div {
        gap: 4px;
    }

    .st-key-jazif_nav [data-testid="stRadio"] label {
        padding: 6px 7px;
    }

    .st-key-jazif_nav [data-testid="stRadio"] label p {
        font-size: 10px;
    }

    .hero-wrap {
        min-height: 590px;
        border-radius: 18px;
    }

    .hero-content {
        left: 7%;
        right: 7%;
        bottom: 15%;
    }

    .hero-content h1 {
        font-size: 42px;
    }

    .hero-content p {
        font-size: 15px;
    }

    .hero-foot {
        font-size: 8px;
        letter-spacing: 1px;
    }

    .section-heading {
        font-size: 27px;
    }

    .photo-card {
        height: 260px;
    }

    .community-hero {
        height: 330px;
    }

    .community-hero h1 {
        font-size: 36px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# NAVIGATION
# =========================================================

with st.container(key="jazif_nav"):

    st.markdown("""
    <div class="brand">
        <div>
            <strong>JAZIF</strong>
            <small>CREATIVE SPACE · RIYADH</small>
        </div>
        <div class="brand-mark">✦</div>
    </div>
    """, unsafe_allow_html=True)

    nav = [
        "الرئيسية",
        "المجتمعات",
        "التجارب",
        "خريطة المساحة"
    ]

    current = st.radio(
        "Navigation",
        nav,
        index=nav.index(st.session_state.page)
        if st.session_state.page in nav else 0,
        horizontal=True,
        label_visibility="collapsed",
        key="jazif_navigation"
    )

    st.session_state.page = current


def heading(kicker, title, subtitle=""):
    st.markdown(
        f"""
        <div class="section-kicker">{kicker}</div>
        <div class="section-heading">{title}</div>
        <div class="section-sub">{subtitle}</div>
        """,
        unsafe_allow_html=True
    )


def go(page):
    st.session_state.page = page
    st.rerun()


# =========================================================
# HOME PAGE
# =========================================================

if st.session_state.page == "الرئيسية":

    st.markdown("""
    <div class="hero-wrap">

      <img class="hero-img"
      src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=2200&q=90">

      <div class="hero-overlay"></div>

      <div class="hero-content">

        <div class="hero-kicker">
        A SPACE TO CONNECT · CREATE · EXPERIENCE
        </div>

        <h1>
        Take the step.<br>
        Be you.
        </h1>

        <p>
        جازف. مساحة تبدأ فيها خطوة صغيرة،
        وتكتشف من خلالها أشياء جديدة عن نفسك
        والعالم حولك.
        </p>

      </div>

      <div class="hero-foot">
        <span>JAZIF · RIYADH</span>
        <span>خُذ الخطوة… كن أنت</span>
      </div>

    </div>
    """, unsafe_allow_html=True)

    heading(
        "FIND YOUR PEOPLE",
        "مجتمعات جازف",
        "اهتم بشيء؟ أو ودك تجرب شيء جديد؟ مكانك هنا."
    )

    cols = st.columns(2)

    for i, (name, data) in enumerate(COMMUNITIES.items()):

        with cols[i % 2]:

            st.markdown(f"""
            <div class="photo-card">
                <img src="{data['image']}">
                <div class="photo-label">
                    <span>{name.upper()} · COMMUNITY</span>
                    <b>{data['ar']} {data['icon']}</b>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(
                f"اكتشف مجتمع {data['ar']} ←",
                key=f"home_{name}",
                use_container_width=True
            ):
                st.session_state.community = name
                go("المجتمعات")

    if st.button(
        "SEE ALL COMMUNITIES ↗",
        use_container_width=True
    ):
        go("المجتمعات")

    heading(
        "MAKE IT HAPPEN",
        "مو لاقي مجتمعك؟",
        "كل اهتمام يستحق مساحة. اقترح مجتمعك وخله يبدأ من هنا."
    )

    with st.container(border=True):

        st.markdown("### Make your own community ✳")

        st.write(
            "شاركنا الفكرة، وفريق جازف يراجع الطلب قبل إضافته."
        )

        with st.form("home_new_community"):

            proposed = st.text_input(
                "اسم المجتمع أو الهواية"
            )

            reason = st.text_area(
                "وش الفكرة؟ وليه ودك يكون لها مجتمع؟"
            )

            submitted = st.form_submit_button(
                "إرسال الاقتراح",
                use_container_width=True
            )

            if submitted:

                if proposed.strip():

                    st.session_state.new_community_requests.append({
                        "name": proposed.strip(),
                        "reason": reason.strip()
                    })

                    st.success(
                        "وصلنا اقتراحك! بنراجعه مع فريق جازف."
                    )

                else:
                    st.warning("اكتب اسم المجتمع أولاً.")

    heading(
        "UP NEXT",
        "تجارب قريبة",
        "مساحات صغيرة، تجارب جديدة، وناس ممكن تصير جزء من رحلتك."
    )

    cols = st.columns(3)

    for col, event in zip(cols, EVENTS):

        with col:

            st.markdown(f"""
            <div class="event-card">
                <img src="{event['image']}">
                <div class="event-copy">
                    <small>
                    {event['community'].upper()} · {event['date']}
                    </small>
                    <h4>{event['title']}</h4>
                    <small>{event['place']}</small>
                </div>
            </div>
            """, unsafe_allow_html=True)


# =========================================================
# COMMUNITIES PAGE
# =========================================================

elif st.session_state.page == "المجتمعات":

    heading(
        "THE COMMUNITIES",
        "اختر مجتمعك",
        "كل مجتمع له اهتمامه، ناسه، وتجارب تصنعونها مع بعض."
    )

    names = list(COMMUNITIES.keys())

    selected = st.selectbox(
        "اختاري مجتمع",
        names,
        index=names.index(st.session_state.community)
    )

    st.session_state.community = selected

    data = COMMUNITIES[selected]

    st.markdown(f"""
    <div class="community-hero">

        <img src="{data['image']}">

        <div>
            <div class="hero-kicker">
            {selected.upper()} COMMUNITY
            </div>

            <h1>{data['icon']} {data['ar']}</h1>

            <p>{data['desc']}</p>
        </div>

    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        "عن المجتمع",
        "IDEA LAB 💡",
        "مساحة المجتمع"
    ])

    # ABOUT

    with tab1:

        heading(
            "ABOUT THE COMMUNITY",
            f"أهلاً بك في {data['ar']}",
            data["desc"]
        )

        st.markdown("#### What's coming")

        matching = [
            event for event in EVENTS
            if event["community"] == selected
        ]

        if matching:

            for event in matching:

                st.markdown(
                    f"""
                    **{event['title']}**

                    {event['date']} · {event['place']}
                    """
                )

        else:
            st.info(
                "نعمل على تجهيز التجارب القادمة لهذا المجتمع."
            )

        st.markdown("#### Ready to try?")

        if st.button(
            "＋ طلب انضمام / تسجيل اهتمام",
            key=f"join_{selected}",
            use_container_width=True
        ):

            if selected not in st.session_state.interests:
                st.session_state.interests.append(selected)

            st.success("تم تسجيل اهتمامك! 🌿")

    # IDEA LAB

    with tab2:

        heading(
            "YOUR IDEA MATTERS",
            "Idea Lab",
            "اقترح تجربة أو فعالية لهذا المجتمع. الفكرة تكبر بمشاركة الجميع."
        )

        with st.form(f"idea_form_{selected}"):

            idea_text = st.text_area(
                "وش ودك نسوي؟",
                placeholder="مثلاً: جلسة موسيقى هادئة وقت الغروب..."
            )

            idea_submit = st.form_submit_button(
                "＋ أرسل فكرتك",
                use_container_width=True
            )

            if idea_submit:

                if idea_text.strip():

                    st.session_state.ideas.append({
                        "community": selected,
                        "text": idea_text.strip()
                    })

                    st.success(
                        "فكرتك صارت ضمن أفكار المجتمع!"
                    )

                else:
                    st.warning("اكتب فكرتك أولاً.")

        st.markdown("### أفكار المجتمع")

        all_ideas = [
            {
                "id": f"seed_{selected}_{i}",
                "text": idea
            }
            for i, idea in enumerate(data["ideas"])
        ]

        all_ideas += [
            {
                "id": f"member_{i}",
                "text": idea["text"]
            }
            for i, idea in enumerate(st.session_state.ideas)
            if idea["community"] == selected
        ]

        for item in all_ideas:

            st.markdown(f"""
            <div class="idea-card">
                <h4>💡 {item['text']}</h4>
                <small>
                صوتك ممكن يساعد الفكرة تصير تجربة حقيقية.
                </small>
            </div>
            """, unsafe_allow_html=True)

            a, b, c = st.columns(3)

            options = [
                (a, "❤️ We Love It", "love"),
                (b, "🙌 We Support It", "support"),
                (c, "🤝 Be a Co-host", "host")
            ]

            for col, label, keypart in options:

                vote_key = f"{item['id']}_{keypart}"

                with col:

                    if st.button(
                        label,
                        key=f"vote_{vote_key}",
                        use_container_width=True
                    ):

                        st.session_state.votes[vote_key] = (
                            st.session_state.votes.get(vote_key, 0) + 1
                        )

                        if keypart == "host":

                            st.session_state.cohosts.append({
                                "community": selected,
                                "idea": item["text"]
                            })

                        st.rerun()

                    st.caption(
                        str(st.session_state.votes.get(vote_key, 0))
                    )

        st.caption(
            "التصويت هنا نموذج تجريبي؛ الأصوات لا تُحفظ بشكل دائم بعد إعادة تشغيل التطبيق."
        )

    # COMMUNITY SPACE

    with tab3:

        st.markdown("### Community Space")

        st.write(
            "مساحة للتواصل بين أعضاء المجتمع."
        )

        st.info(
            "🔒 هذه المساحة حالياً واجهة تجريبية. "
            "سيتم تطوير العضويات والمحادثات لاحقاً."
        )


# =========================================================
# EXPERIENCES PAGE
# =========================================================

elif st.session_state.page == "التجارب":

    heading(
        "JAZIF EXPERIENCES",
        "التجارب القادمة",
        "مو لازم تعرف كل شيء من البداية. يكفي إنك تجرب."
    )

    for event in EVENTS:

        c1, c2 = st.columns([1, 1.5])

        with c1:

            st.image(
                event["image"],
                use_container_width=True
            )

        with c2:

            st.markdown(f"### {event['title']}")

            st.caption(
                f"{event['community']} · "
                f"{event['date']} · "
                f"{event['place']}"
            )

            st.write(
                "تجربة مجتمعية مفتوحة للتعرف على أشخاص جدد وتجربة شيء مختلف."
            )

            if st.button(
                "سجل اهتمامك",
                key=f"event_interest_{event['title']}"
            ):

                if event["community"] not in st.session_state.interests:
                    st.session_state.interests.append(event["community"])

                st.success("تم تسجيل اهتمامك.")


# =========================================================
# JAZIF MAP
# =========================================================

elif st.session_state.page == "خريطة المساحة":

    heading(
        "EXPLORE JAZIF",
        "خريطة المساحة",
        "تصور أولي للمكان — نقدر نضيف تفاصيل وتجارب تفاعلية لاحقاً."
    )

    st.markdown("""
    <div class="map-panel">

        <div style="
            text-align:center;
            font-weight:700;
            letter-spacing:4px;
            color:#526b57;
        ">
            J A Z I F · SPACE MAP
        </div>

        <div class="map-zone">

            <div style="font-size:30px">🏡</div>

            <b>المساحة الداخلية</b>

            <br>

            <small>
            ورش · لقاءات · تجارب إبداعية
            </small>

        </div>

        <div style="
            display:flex;
            justify-content:center;
            font-size:26px;
            color:#66866b;
        ">
            ↓ ✦ ↓
        </div>

        <div class="map-zone" style="background:#d5e3ce">

            <div style="font-size:30px">🌳</div>

            <b>الحديقة الخارجية</b>

            <br>

            <small>
            جلسات · يوغا · فعاليات خارجية
            </small>

        </div>

        <div style="
            text-align:center;
            color:#657c67;
            font-size:12px;
            margin-top:12px;
        ">
            TAKE THE STEP · BE YOU
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.caption(
        "الخريطة الحالية تصور بصري تجريبي وليست مخططاً هندسياً للموقع."
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    JAZIF · CREATIVE SPACE · RIYADH
    <br>
    TAKE THE STEP · BE YOU
</div>
""", unsafe_allow_html=True)
