import streamlit as st

st.set_page_config(
    page_title="JAZIF | Community Space",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Demo content uses curated stock-photo URLs so the prototype looks complete
# without requiring the user to upload images. Replace these with real Jazif
# photos when they become available.

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap');
:root { --forest:#203c2f; --forest2:#294b3a; --cream:#f6f7f1; --sage:#e5ece3; --muted:#758278; --coral:#e85c62; }
html, body, [class*="css"] { font-family:'DM Sans','IBM Plex Sans Arabic',sans-serif; }
.stApp { background:var(--cream); color:var(--forest); }
.block-container { max-width:1180px; padding-top:1.2rem; padding-bottom:4rem; }
header, footer {visibility:hidden;}
[data-testid="stToolbar"] {display:none;}
#MainMenu {visibility:hidden;}
.brand {display:flex; align-items:center; justify-content:space-between; padding:12px 0 18px; border-bottom:1px solid #dfe6dc; margin-bottom:18px;}
.brandname {font-size:29px; font-weight:800; letter-spacing:1px; color:var(--forest);}
.brandtag {font-size:12px; letter-spacing:1.5px; color:#7b887e; margin-left:9px;}
.leaf {font-size:27px;}
div[role="radiogroup"] {gap:9px; justify-content:flex-start; direction:rtl; flex-wrap:wrap;}
div[role="radiogroup"] label {background:#fff; border:1px solid #dce4da; border-radius:13px; padding:9px 17px; color:var(--forest)!important; font-weight:600;}
div[role="radiogroup"] label[data-checked="true"] {background:var(--forest)!important; color:#fff!important; border-color:var(--forest)!important;}
div[role="radiogroup"] label p {font-size:14px;}
.hero {background:linear-gradient(90deg,rgba(20,49,37,.91),rgba(20,49,37,.48)),url('https://images.unsplash.com/photo-1519331379826-f10be5486c6f?auto=format&fit=crop&w=1800&q=85') center/cover; border-radius:26px; padding:54px 48px; color:white; min-height:390px; display:flex; flex-direction:column; justify-content:center; margin:18px 0 42px;}
.eyebrow {display:inline-block; background:#edf2e9; color:var(--forest); padding:9px 16px; border-radius:30px; font-size:12px; font-weight:700; letter-spacing:1px; width:max-content;}
.hero h1 {font-family:'IBM Plex Sans Arabic',sans-serif; font-size:clamp(32px,5vw,54px); line-height:1.35; max-width:700px; margin:22px 0 12px; color:white;}
.hero p {font-family:'IBM Plex Sans Arabic',sans-serif; font-size:17px; color:#edf2e9; max-width:620px; line-height:1.9;}
.hero .smallnote {font-size:11px; opacity:.75; margin-top:20px;}
.section-head {display:flex; align-items:end; justify-content:space-between; margin:38px 0 17px; direction:rtl;}
.section-head h2 {font-family:'IBM Plex Sans Arabic',sans-serif; font-size:27px; margin:0; color:var(--forest);}
.section-head span {color:var(--muted); font-size:13px;}
.intro {font-family:'IBM Plex Sans Arabic',sans-serif; color:#758278; font-size:16px; line-height:1.9; direction:rtl; text-align:right; margin-top:-7px; margin-bottom:24px;}
.feature-card {background:white; border:1px solid #e1e8df; border-radius:20px; overflow:hidden; height:100%; box-shadow:0 5px 18px rgba(32,60,47,.035);}
.feature-card img {width:100%; height:185px; object-fit:cover; display:block;}
.feature-body {padding:19px 20px 21px; direction:rtl; text-align:right;}
.feature-body h3 {font-family:'IBM Plex Sans Arabic',sans-serif; font-size:21px; margin:0 0 8px; color:var(--forest);}
.feature-body p {font-family:'IBM Plex Sans Arabic',sans-serif; color:#758278; line-height:1.8; margin:0 0 14px; font-size:14px;}
.pill {display:inline-block; background:#edf2e9; color:var(--forest); padding:6px 11px; border-radius:30px; font-size:11px; margin:2px;}
.event {background:white; border:1px solid #e1e8df; border-radius:18px; padding:13px; display:flex; gap:16px; align-items:center; margin-bottom:12px;}
.event img {width:118px; height:112px; object-fit:cover; border-radius:13px;}
.event h3 {font-size:19px; margin:0 0 6px; color:var(--forest);}
.event p {margin:0; color:var(--muted); font-size:13px; line-height:1.7;}
.event .meta {margin-top:8px; color:var(--forest); font-weight:600; font-size:12px;}
.stat {background:#e7eee5; border-radius:18px; padding:23px; text-align:center;}
.stat strong {display:block; font-size:31px; color:var(--forest);}
.stat span {font-family:'IBM Plex Sans Arabic',sans-serif; color:#758278; font-size:13px;}
.mapbox {background:#e5ece3; border:1px solid #d5e0d4; border-radius:22px; padding:18px; overflow:hidden;}
.mapgrid {display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-top:15px;}
.mapspot {background:#f8faf5; border:1px solid #d6e1d4; border-radius:14px; padding:16px; text-align:center; color:var(--forest);}
.mapspot b {display:block; font-size:15px; margin:5px 0;}
.mapspot small {color:#7b887e;}
.cta {background:var(--forest); border-radius:22px; padding:30px; color:white; text-align:right; direction:rtl; margin:35px 0;}
.cta h2 {font-family:'IBM Plex Sans Arabic',sans-serif; color:white; margin:0 0 8px;}
.cta p {font-family:'IBM Plex Sans Arabic',sans-serif; color:#dce7dc; margin:0; line-height:1.8;}
.footer {border-top:1px solid #dfe6dc; padding:25px 0; margin-top:45px; color:#7b887e; display:flex; justify-content:space-between; font-size:12px;}
[dir="rtl"] {text-align:right;}
@media(max-width:700px) {
 .block-container {padding-left:1rem; padding-right:1rem;}
 .hero {padding:30px 23px; min-height:360px;}
 .hero p {font-size:15px;}
 .section-head h2 {font-size:23px;}
 .event img {width:92px;height:100px;}
 .mapgrid {grid-template-columns:1fr 1fr;}
 .footer {display:block; line-height:2;}
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="brand">
  <div><span class="brandname">JAZIF</span><span class="brandtag">COMMUNITY SPACE</span></div>
  <div class="leaf">🌿</div>
</div>
""", unsafe_allow_html=True)

page = st.radio(
    "التنقل",
    ["الرئيسية", "المجتمعات", "التجارب", "خريطة المساحة", "عن جازف"],
    horizontal=True,
    label_visibility="collapsed",
)

def section(title, subtitle=""):
    st.markdown(f'<div class="section-head"><h2>{title}</h2><span>{subtitle}</span></div>', unsafe_allow_html=True)

def card(image, title, desc, tag):
    st.markdown(f"""
    <div class="feature-card">
      <img src="{image}" />
      <div class="feature-body">
        <span class="pill">{tag}</span>
        <h3>{title}</h3><p>{desc}</p>
      </div>
    </div>""", unsafe_allow_html=True)

def event(image, title, place, date, seats, desc):
    st.markdown(f"""
    <div class="event">
      <img src="{image}"/>
      <div style="flex:1">
        <h3>{title}</h3><p>{desc}</p>
        <p class="meta">📍 {place} &nbsp; · &nbsp; {date} &nbsp; · &nbsp; {seats}</p>
      </div>
    </div>""", unsafe_allow_html=True)

if page == "الرئيسية":
    st.markdown("""
    <div class="hero">
      <span class="eyebrow">A SPACE TO CONNECT & CREATE</span>
      <h1>مساحة تجمعنا، وتجارب تصنع ذكرياتنا</h1>
      <p>جازف مساحة مجتمعية تجمع الأشخاص حول الاهتمامات المشتركة، وتمنحهم فرصة للتجربة والتعلّم والتواصل.</p>
      <div class="smallnote">COMMUNITY · CREATIVITY · EXPERIENCES</div>
    </div>
    """, unsafe_allow_html=True)

    section("أهلاً بك في جازف", "مكان تبدأ فيه فكرة، وتتحول إلى تجربة")
    st.markdown('<div class="intro">مساحة صُممت لتكون نقطة بداية لتجارب وصداقات وأفكار جديدة. اختر مجتمعك، اكتشف ما يحدث، وكن جزءاً من التجربة.</div>', unsafe_allow_html=True)

    section("اكتشف مساحات جازف", "مساحات تجمع الاهتمامات")
    a,b,c = st.columns(3)
    with a: card("https://images.unsplash.com/photo-1511988617509-a57c8a288659?auto=format&fit=crop&w=900&q=85","المجتمعات","مساحات تجمع أصحاب الاهتمامات المشتركة وتفتح باب التواصل.","COMMUNITY")
    with b: card("https://images.unsplash.com/photo-1528605248644-14dd04022da1?auto=format&fit=crop&w=900&q=85","التجارب","ورش وفعاليات وأنشطة نصنعها ونعيشها معاً.","EXPERIENCES")
    with c: card("https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=900&q=85","الأفكار","أفكار الأعضاء تتحول إلى تجارب حقيقية داخل جازف.","IDEAS")

    section("التجارب القادمة", "اختر تجربتك القادمة")
    event("https://images.unsplash.com/photo-1506126613408-2?auto=format&fit=crop&w=500&q=80","Sunset Yoga","الحديقة الخارجية","قريباً","8 من 15 مقعداً","جلسة يوغا هادئة مع أجواء الغروب.")
    event("https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=500&q=85","Art Jamming","المساحة الداخلية","قريباً","12 من 20 مقعداً","مساحة مفتوحة للرسم والتعبير الفني.")
    event("https://images.unsplash.com/photo-1565193298595-6c1f5a7f6f7b?auto=format&fit=crop&w=500&q=85","Pottery for Beginners","المساحة الداخلية","قريباً","أماكن محدودة","تجربة تشكيل الطين وصناعة قطعتك الخاصة.")

    section("خريطة المساحة", "اعرف المكان قبل زيارتك")
    st.markdown("""
    <div class="mapbox">
      <div style="height:185px;border-radius:15px;background:linear-gradient(135deg,#dce8d8,#b8ceb6);display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;">
        <div style="font-size:48px;">🌳　📍　🌿</div>
        <div style="position:absolute;bottom:12px;right:15px;background:#fff;padding:8px 13px;border-radius:20px;font-size:12px;">خريطة جازف التجريبية</div>
      </div>
      <div class="mapgrid">
        <div class="mapspot">🏡<b>المساحة الداخلية</b><small>105 م² · ورش واجتماعات</small></div>
        <div class="mapspot">🌳<b>الحديقة الخارجية</b><small>533 م² · يوغا وفعاليات</small></div>
        <div class="mapspot">🎨<b>منطقة الإبداع</b><small>ورش وتجارب فنية</small></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cta"><h2>عندك فكرة؟ مكانها هنا.</h2><p>شاركنا فكرتك، وصوّت لأفكار المجتمع. يمكن فكرتك تكون التجربة القادمة في جازف.</p></div>
    """, unsafe_allow_html=True)

elif page == "المجتمعات":
    st.markdown('<div class="hero" style="min-height:260px"><span class="eyebrow">FIND YOUR PEOPLE</span><h1>مجتمعك يبدأ من اهتمامك</h1><p>اكتشف مجتمعات جازف، وتعرّف على أشخاص يشاركونك الشغف.</p></div>', unsafe_allow_html=True)
    section("اكتشف مجتمعاتنا", "مساحة لكل اهتمام")
    a,b,c = st.columns(3)
    with a: card("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=900&q=85","مجتمع اليوغا","مساحة للحركة والهدوء والتوازن.","WELLNESS")
    with b: card("https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=900&q=85","مجتمع الفنون","مساحة للإبداع والتعبير الفني وتجربة أشياء جديدة.","ART")
    with c: card("https://images.unsplash.com/photo-1565193298595-6c1f5a7f6f7b?auto=format&fit=crop&w=900&q=85","مجتمع الفخار","تجربة تشكيل الطين وصناعة قطعك الخاصة.","CRAFT")
    st.markdown('<div class="cta"><h2>ما لقيت مجتمعك؟</h2><p>اقترح اهتماماً جديداً، ودعنا نبني له مساحة في جازف.</p></div>', unsafe_allow_html=True)

elif page == "التجارب":
    st.markdown('<div class="hero" style="min-height:260px"><span class="eyebrow">MAKE IT A MEMORY</span><h1>تجارب تستحق أن تعاش</h1><p>من لحظات الهدوء إلى التجارب الإبداعية؛ اختر ما يشبهك.</p></div>', unsafe_allow_html=True)
    section("التجارب القادمة", "فعاليات جازف")
    event("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=500&q=85","Sunset Yoga","الحديقة الخارجية","قريباً","8 من 15 مقعداً","جلسة يوغا هادئة مع أجواء الغروب.")
    event("https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=500&q=85","Art Jamming","المساحة الداخلية","قريباً","12 من 20 مقعداً","مساحة مفتوحة للرسم والتعبير الفني.")
    event("https://images.unsplash.com/photo-1565193298595-6c1f5a7f6f7b?auto=format&fit=crop&w=500&q=85","Pottery for Beginners","المساحة الداخلية","قريباً","أماكن محدودة","تجربة تشكيل الطين وصناعة قطعتك الخاصة.")

elif page == "خريطة المساحة":
    st.markdown('<div class="hero" style="min-height:260px"><span class="eyebrow">EXPLORE THE SPACE</span><h1>كل زاوية لها تجربة</h1><p>استكشف مرافق جازف وتعرّف على المساحات التي تنتظرك.</p></div>', unsafe_allow_html=True)
    section("خريطة جازف", "تصور مبدئي للمواقع")
    st.markdown("""
    <div class="mapbox">
      <div style="height:300px;border-radius:16px;background:linear-gradient(135deg,#dce8d8,#b8ceb6);display:flex;align-items:center;justify-content:center;">
        <div style="text-align:center;color:#203c2f"><div style="font-size:70px">🌳　📍　🏡</div><b style="font-size:22px">JAZIF SPACE MAP</b><br/><small>تصور تجريبي — تُستبدل بالخريطة الفعلية لاحقاً</small></div>
      </div>
      <div class="mapgrid">
        <div class="mapspot">🏡<b>المساحة الداخلية</b><small>105 م² · ورش واجتماعات</small></div>
        <div class="mapspot">🌳<b>الحديقة الخارجية</b><small>533 م² · يوغا وفعاليات</small></div>
        <div class="mapspot">🎨<b>منطقة الإبداع</b><small>ورش وتجارب فنية</small></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "عن جازف":
    st.markdown('<div class="hero" style="min-height:260px"><span class="eyebrow">A COMMUNITY WITH ROOM TO GROW</span><h1>مساحة تبدأ بالناس</h1><p>جازف ليس مجرد مكان؛ هو مساحة تجمع الاهتمامات وتحول الأفكار إلى تجارب مشتركة.</p></div>', unsafe_allow_html=True)
    section("لماذا جازف؟", "الفكرة وراء المساحة")
    st.markdown('<div class="intro">نؤمن أن التجارب الجميلة تبدأ عندما يلتقي أشخاص لديهم اهتمامات مشتركة. لذلك صُممت جازف لتكون مساحة للتواصل والتعلّم والتجربة وصناعة الذكريات.</div>', unsafe_allow_html=True)
    x,y,z = st.columns(3)
    with x: st.markdown('<div class="stat"><strong>01</strong><span>نتواصل</span></div>',unsafe_allow_html=True)
    with y: st.markdown('<div class="stat"><strong>02</strong><span>نجرب</span></div>',unsafe_allow_html=True)
    with z: st.markdown('<div class="stat"><strong>03</strong><span>نبتكر</span></div>',unsafe_allow_html=True)

st.markdown("""
<div class="footer"><span><b style="color:#203c2f">JAZIF 🌿</b> &nbsp; COMMUNITY SPACE</span><span>مساحة تجمعنا، وتجارب تصنع ذكرياتنا</span><span>DEMO CONCEPT · 2026</span></div>
""", unsafe_allow_html=True)
