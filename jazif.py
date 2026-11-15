import streamlit as st
import qrcode
from io import BytesIO

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="JAZIF | Community",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- STYLE ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap');

* {
    font-family: 'IBM Plex Sans Arabic', sans-serif;
}

html, body, [class*="css"] {
    direction: rtl;
}

.stApp {
    background: #F7F7F3;
    color: #26382F;
}

.block-container {
    max-width: 1100px;
    padding: 1rem 1.2rem 4rem;
}

header {visibility: hidden;}
footer {visibility: hidden;}

.hero {
    background: #263D32;
    color: white;
    padding: 30px 24px;
    border-radius: 22px;
    margin: 15px 0;
}

.hero h1 {
    font-size: 32px;
    font-weight: 700;
}

.hero p {
    color: #D6E2D8;
    font-size: 15px;
}

.section-title {
    font-size: 23px;
    font-weight: 700;
    margin-top: 28px;
    margin-bottom: 12px;
    color: #263D32;
}

.info-card {
    background: white;
    padding: 18px;
    border-radius: 18px;
    border: 1px solid #E8EAE4;
    margin-bottom: 12px;
}

.community-card {
    background: white;
    border: 1px solid #E5E9E2;
    border-radius: 18px;
    padding: 18px;
    min-height: 155px;
    margin-bottom: 10px;
}

.community-icon {
    font-size: 32px;
}

.muted {
    color: #78857C;
    font-size: 13px;
}

.tag {
    background: #E9F0E9;
    color: #365744;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 12px;
    display: inline-block;
}

.area {
    background: #E8EEE7;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    min-height: 120px;
    border: 1px dashed #9AAA9B;
}

.area.outdoor {
    background: #E5EBDD;
}

button[kind="primary"] {
    background: #365744 !important;
    border-radius: 12px !important;
}

div[data-testid="stTabs"] button {
    font-size: 13px;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 12px;
    border-radius: 14px;
}

@media (max-width: 600px) {
    .block-container {
        padding: 0.6rem 0.8rem 3rem;
    }
    .hero {
        padding: 23px 17px;
        border-radius: 18px;
    }
    .hero h1 {
        font-size: 25px;
    }
    .section-title {
        font-size: 20px;
    }
    .community-card {
        min-height: 130px;
        padding: 13px;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------------- DATA ----------------
communities = {
    "اليوغا": {
        "icon": "🧘🏻‍♀️",
        "description": "مساحة للحركة والهدوء والتوازن.",
        "bring": ["ملابس مريحة", "حصيرة يوغا", "قارورة ماء"],
        "ideas": ["جلسة يوغا عند الغروب", "Morning Yoga", "يوغا وتأمل"]
    },
    "الفنون": {
        "icon": "🎨",
        "description": "مجتمع يجمع محبي الفن والتجارب الإبداعية.",
        "bring": ["ملابس مناسبة للتلوين", "دفتر رسم", "أدواتك الفنية"],
        "ideas": ["رسم جماعي", "Art & Coffee", "ورشة ألوان مائية"]
    },
    "الفخار": {
        "icon": "🏺",
        "description": "اكتشف متعة صناعة الأشياء بيديك.",
        "bring": ["ملابس مريحة", "مريلة", "روح إبداعية"],
        "ideas": ["صناعة أكواب", "ورشة تشكيل الطين", "Pottery & Coffee"]
    },
    "الخيول": {
        "icon": "🐎",
        "description": "مجتمع لمحبي الخيل والتجارب الخارجية.",
        "bring": ["ملابس مناسبة", "حذاء مغلق", "ماء"],
        "ideas": ["لقاء لمحبي الخيل", "جلسة تعريفية", "تجربة ركوب"]
    },
    "الورش": {
        "icon": "🛠️",
        "description": "نتعلم أشياء جديدة ونتشارك المهارات.",
        "bring": ["دفتر ملاحظات", "قلم", "حاسوب عند الحاجة"],
        "ideas": ["ورشة ابتكار", "تبادل المهارات", "لقاء تعليمي"]
    }
}

events = [
    {"name": "Morning Yoga", "type": "اليوغا", "date": "20 نوفمبر",
     "place": "الحديقة الخارجية", "seats": 4, "total": 12},
    {"name": "Art & Coffee", "type": "الفنون", "date": "22 نوفمبر",
     "place": "المساحة الداخلية", "seats": 7, "total": 15},
    {"name": "Pottery Workshop", "type": "الفخار", "date": "25 نوفمبر",
     "place": "المساحة الداخلية", "seats": 3, "total": 10}
]

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "الرئيسية"

if "community" not in st.session_state:
    st.session_state.community = "اليوغا"

if "ideas" not in st.session_state:
    st.session_state.ideas = []

if "votes" not in st.session_state:
    st.session_state.votes = {}

if "registered" not in st.session_state:
    st.session_state.registered = False


# ---------------- HEADER ----------------
st.markdown("""
<div style="display:flex;justify-content:space-between;
align-items:center;padding:5px 0;">
    <div>
        <span style="font-size:27px;font-weight:700;color:#294333;">
        JAZIF</span>
        <span style="font-size:12px;color:#829087;"> COMMUNITY SPACE</span>
    </div>
    <div style="font-size:24px;">🌿</div>
</div>
""", unsafe_allow_html=True)

pages = ["الرئيسية", "المجتمعات", "تذاكري", "حسابي"]

selected_page = st.radio(
    "التنقل",
    pages,
    index=pages.index(st.session_state.page),
    horizontal=True,
    label_visibility="collapsed"
)

st.session_state.page = selected_page

st.divider()


# ================= HOME =================
if st.session_state.page == "الرئيسية":

    st.markdown("""
    <div class="hero">
        <span class="tag">A SPACE TO CONNECT</span>
        <h1>أهلاً بك في جازف 🌿</h1>
        <p>
        مساحة تجمع الناس والأفكار والتجارب.
        مكان نلتقي فيه، نتعلم، ونصنع ذكريات جديدة.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">اكتشف جازف</div>',
                unsafe_allow_html=True)

    st.write("مساحة مرنة تتغير بتغير الأشخاص والأنشطة والمجتمعات.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="info-card">🧘🏻‍♀️<br><b>Yoga</b><br><small>حركة وهدوء</small></div>',
                    unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="info-card">🎨<br><b>Art</b><br><small>فن وإبداع</small></div>',
                    unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="info-card">🛠️<br><b>Workshops</b><br><small>تعلم وتجربة</small></div>',
                    unsafe_allow_html=True)

    st.markdown('<div class="section-title">خريطة المساحة</div>',
                unsafe_allow_html=True)

    st.caption("اكتشف مناطق جازف والتجارب التي تقام فيها.")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="area">
        🏡<br><b>المساحة الداخلية</b><br>
        <h2>105 m²</h2>
        <small>ورش واجتماعات وتجارب داخلية</small>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="area outdoor">
        🌳<br><b>الحديقة الخارجية</b><br>
        <h2>533 m²</h2>
        <small>يوغا وفعاليات وتجارب خارجية</small>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">التجارب القادمة</div>',
                unsafe_allow_html=True)

    for event in events:
        with st.container(border=True):
            st.markdown(f"**{event['name']}**")
            st.caption(f"{event['type']} · {event['date']} · {event['place']}")
            st.write(f"🪑 المقاعد المتبقية: {event['seats']} من {event['total']}")
            if st.button("استكشف التجربة", key=f"event_{event['name']}",
                         use_container_width=True):
                st.session_state.community = event["type"]
                st.session_state.page = "المجتمعات"
                st.rerun()

    if st.button("اكتشف جميع المجتمعات ←", use_container_width=True):
        st.session_state.page = "المجتمعات"
        st.rerun()


# ================= COMMUNITIES =================
elif st.session_state.page == "المجتمعات":

    st.title("مجتمعات جازف")
    st.write("كل مجتمع يبدأ باهتمام، وينمو بالأشخاص الذين يجمعهم.")

    for name, data in communities.items():
        with st.container(border=True):
            st.markdown(f"### {data['icon']} {name}")
            st.caption(data["description"])

            if st.button(f"اكتشف مجتمع {name}", key=f"open_{name}",
                         use_container_width=True):
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

    # TAB 1
    with tab1:
        st.subheader("عن المجتمع")
        st.write(data["description"])

        st.markdown("**من تجاربنا السابقة**")

        p1, p2 = st.columns(2)
        with p1:
            st.markdown("🖼️ **تجربة سابقة 01**")
            st.caption("صورة تجريبية - تضاف الصور لاحقاً")
        with p2:
            st.markdown("🖼️ **تجربة سابقة 02**")
            st.caption("صورة تجريبية - تضاف الصور لاحقاً")

        st.subheader("What to Bring")
        for item in data["bring"]:
            st.checkbox(item, key=f"bring_{name}_{item}")

        if st.button("سجل اهتمامك بالمجتمع", key="interest",
                     use_container_width=True):
            st.session_state.registered = True
            st.success("تم تسجيل اهتمامك بنجاح!")

    # TAB 2
    with tab2:
        st.subheader("Idea Lab 💡")
        st.write("شارك أفكارك، وصوّت على التجارب التي ترغب برؤيتها.")

        with st.form("idea_form"):
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
        st.markdown("**أفكار مقترحة**")

        for i, idea in enumerate(data["ideas"]):
            key = f"{name}_{i}"
            with st.container(border=True):
                st.write(f"💡 {idea}")
                st.caption(f"الأصوات: {st.session_state.votes.get(key, 0)}")
                if st.button("👍 صوّت", key=f"vote_{key}"):
                    st.session_state.votes[key] = (
                        st.session_state.votes.get(key, 0) + 1
                    )
                    st.rerun()

        for idea in st.session_state.ideas:
            if idea["community"] == name:
                st.write("💡 " + idea["idea"])

        st.divider()
        st.subheader("Find a Co-host 🤝")
        st.write("هل عندك فكرة وتبحث عن شخص يشاركك تنظيمها؟")

        if st.button("ابحث عن شريك لتنظيم الفكرة",
                     use_container_width=True):
            st.info("سيتم تطوير نظام البحث عن Co-host لاحقاً.")

    # TAB 3
    with tab3:
        st.subheader("Community Space 🔒")

        accepted = st.toggle(
            "محاكاة: تم قبول تسجيلي في المجتمع",
            value=False
        )

        if accepted:
            st.success("مرحباً بك في مساحة المجتمع!")
            st.text_area(
                "Community Chat",
                placeholder="اكتب رسالة تجريبية..."
            )
            st.button("إرسال الرسالة", use_container_width=True)

            st.markdown("**قنوات التواصل**")
            st.markdown("- مجموعة WhatsApp (رابط تجريبي)")
            st.markdown("- البريد الإلكتروني للمجتمع")
            st.caption("المساحة الحقيقية تكون للأعضاء المقبولين فقط.")
        else:
            st.info("🔒 هذه المساحة متاحة للأعضاء المقبولين فقط.")


# ================= DIGITAL PASS =================
elif st.session_state.page == "تذاكري":

    st.title("Digital Pass 🎟️")
    st.write("تذكرتك الرقمية للدخول إلى جازف.")

    qr = qrcode.make("JAZIF-DEMO-MEMBER-001")
    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    with st.container(border=True):
        st.markdown("<h2 style='text-align:center'>JAZIF</h2>",
                    unsafe_allow_html=True)
        st.markdown("<p style='text-align:center'>MEMBER DIGITAL PASS</p>",
                    unsafe_allow_html=True)

        st.image(buffer.getvalue(), width=190)

        st.markdown("<h3 style='text-align:center'>Noura Member</h3>",
                    unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align:center;color:#78857C'>"
            "Member ID: JZ-001-DEMO</p>",
            unsafe_allow_html=True
        )

        st.success("Active Member · Demo")

    st.caption("هذا QR تجريبي للتوضيح فقط، وليس تصريح دخول حقيقي.")


# ================= ACCOUNT =================
elif st.session_state.page == "حسابي":

    st.title("حسابي 👤")

    with st.container(border=True):
        st.markdown("## 👩🏻")
        st.subheader("Noura Member")
        st.caption("Jazif Community Member")
        st.markdown('<span class="tag">Active Member</span>',
                    unsafe_allow_html=True)

    st.markdown("### Badges 🏅")
    b1, b2, b3 = st.columns(3)
    b1.metric("Explorer", "01")
    b2.metric("Ideas", "03")
    b3.metric("Events", "02")

    st.markdown("### مجتمعاتي")
    st.write("🧘🏻‍♀️ اليوغا")
    st.write("🎨 الفنون")

    if st.button("عرض التذاكر الرقمية", use_container_width=True):
        st.session_state.page = "تذاكري"
        st.rerun()

    if st.button("تصفح المجتمعات", use_container_width=True):
        st.session_state.page = "المجتمعات"
        st.rerun()


# ---------------- FOOTER ----------------
st.divider()
st.markdown("""
<div style="text-align:center;color:#8A958C;padding:15px;">
    JAZIF COMMUNITY SPACE 🌿<br>
    <small>A place to connect, create & belong.</small>
</div>
""", unsafe_allow_html=True)
