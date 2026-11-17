import streamlit as st
from pathlib import Path
import base64
import html

st.set_page_config(page_title="JAZIF | Creative Space", page_icon="✦", layout="wide", initial_sidebar_state="collapsed")

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

COMMUNITIES = [
    {"key":"draw","name":"DRAW","arabic":"ارسم","desc":"مساحة للرسم، التجريب، وتبادل الإلهام مهما كان مستواك.","tag":"MAKE SOMETHING","img":"https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=1200&q=85"},
    {"key":"walk","name":"WALK","arabic":"امشِ","desc":"نكتشف المدينة وتفاصيلها الصغيرة خطوة بخطوة.","tag":"FIND YOUR PACE","img":"https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1200&q=85"},
    {"key":"bikes","name":"BIKES","arabic":"انطلق","desc":"جولات بالدراجات، حركة، وهواء جديد ووجوه جديدة.","tag":"MOVE TOGETHER","img":"https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=1200&q=85"},
    {"key":"music","name":"MUSIC","arabic":"اسمع","desc":"نجتمع حول الموسيقى؛ نسمع، نشارك، ونجرب أصواتاً وأفكاراً جديدة.","tag":"FEEL THE SOUND","img":"https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=1200&q=85"},
    {"key":"yoga","name":"YOGA","arabic":"اتّزن","desc":"وقت للحركة الهادئة والتنفس والتواصل مع الجسد.","tag":"SLOW DOWN","img":"https://images.unsplash.com/photo- yoga-placeholder?auto=format&fit=crop&w=1200&q=85"},
]
# Replace the yoga placeholder with a stable public image URL.
COMMUNITIES[-1]["img"] = "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1200&q=85"

if "page" not in st.session_state: st.session_state.page = "home"
if "community" not in st.session_state: st.session_state.community = "music"
if "ideas" not in st.session_state:
    st.session_state.ideas = {
        "music": [
            {"title":"Listening picnic","detail":"جلسة استماع مفتوحة في الهواء الطلق، كل شخص يشارك أغنية لها ذكرى.","votes":12},
            {"title":"Bring your instrument","detail":"لقاء عفوي نجرب فيه العزف مع بعض بدون اشتراط الاحتراف.","votes":8},
        ]
    }
if "proposals" not in st.session_state: st.session_state.proposals = []
if "votes" not in st.session_state: st.session_state.votes = set()

def go(page, community=None):
    st.session_state.page = page
    if community: st.session_state.community = community
    st.rerun()

def image_url(url):
    return f'<div class="photo" style="background-image:linear-gradient(180deg,rgba(0,0,0,.03),rgba(0,0,0,.50)),url(&quot;{url}&quot;)"></div>'

def local_b64(path):
    try:
        return base64.b64encode(path.read_bytes()).decode()
    except Exception:
        return ""

# Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap');
:root{--ink:#f4f0e9;--muted:#aaa49a;--bg:#171715;--panel:#22221f;--line:rgba(255,255,255,.15);--lime:#d5e4a1}
html,body,[class*="css"]{font-family:'DM Sans','IBM Plex Sans Arabic',sans-serif}
.stApp{background:#171715;color:var(--ink)}
.block-container{max-width:1440px;padding:1rem 4vw 5rem}
header[data-testid="stHeader"]{background:transparent}
footer{visibility:hidden}
div[data-testid="stToolbar"]{visibility:hidden}
.navline{position:sticky;top:0;z-index:99;background:rgba(23,23,21,.94);backdrop-filter:blur(14px);border-bottom:1px solid var(--line);padding:14px 0;margin-bottom:24px}
.brand{font-size:25px;font-weight:700;letter-spacing:2px;color:#fff}
.brand small{font-size:9px;letter-spacing:4px;color:#aaa;display:block;margin-top:-4px}
.eyebrow{font-size:11px;letter-spacing:4px;color:var(--muted);text-transform:uppercase}
h1,h2,h3,p{color:var(--ink)}
.hero{position:relative;min-height:560px;border-radius:5px;overflow:hidden;background-size:cover;background-position:center;display:flex;align-items:flex-end;padding:5vw;background-image:linear-gradient(0deg,rgba(0,0,0,.78),rgba(0,0,0,.05)),url('assets/jazif_hero_1.jpeg')}
.hero:after{content:'';position:absolute;inset:0;background-image:url('assets/jazif_hero_2.jpeg');background-size:cover;background-position:center;opacity:0;animation:shift 12s infinite}
@keyframes shift{0%,42%{opacity:0}50%,90%{opacity:.28}100%{opacity:0}}
.hero-content{position:relative;z-index:2;max-width:760px}
.hero h1{font-size:clamp(42px,7vw,90px);line-height:.98;letter-spacing:-3px;margin:15px 0}
.hero p{font-size:15px;letter-spacing:3px;color:#e9e5dc}
.rule{border-top:1px solid var(--line);margin:30px 0}
.section-title{font-size:clamp(32px,5vw,58px);letter-spacing:-2px;margin:4px 0 18px}
.photo{height:230px;background-size:cover;background-position:center;border-radius:4px}
.card-title{font-size:26px;font-weight:700;margin:12px 0 3px}
.muted{color:var(--muted);font-size:14px;line-height:1.8}
.pill{display:inline-block;border:1px solid var(--line);padding:6px 11px;border-radius:30px;font-size:10px;letter-spacing:2px;color:var(--lime)}
.idea{border:1px solid var(--line);padding:20px;border-radius:4px;background:#20201d;margin:10px 0}
.idea h4{margin:0 0 8px;font-size:20px}
.big-quote{font-size:clamp(27px,4vw,48px);line-height:1.35;max-width:850px}
.footer{padding:35px 0;border-top:1px solid var(--line);margin-top:60px;color:#aaa;font-size:11px;letter-spacing:3px}
div.stButton>button{border:1px solid #d5e4a1;background:transparent;color:#f4f0e9;border-radius:2px;padding:10px 18px;min-height:42px}
div.stButton>button:hover{background:#d5e4a1;color:#171715;border-color:#d5e4a1}
.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb="select"]{background:#252521;color:#fff;border:1px solid #555}
label{color:#d9d4ca!important}
@media(max-width:700px){.block-container{padding:0.6rem 5vw 3rem}.hero{min-height:500px;padding:8vw}.photo{height:190px}.hero h1{letter-spacing:-1px}}
</style>
""", unsafe_allow_html=True)

# Fixed-feeling navigation bar
st.markdown('<div class="navline"><span class="brand">جازف <small>JAZIF · CREATIVE SPACE</small></span></div>', unsafe_allow_html=True)
nav = st.columns([1,1,1,1,1.2])
for col, label, page in zip(nav, ["الرئيسية","المجتمعات","التجارب","خريطة المساحة","عن جازف"], ["home","communities","experiences","map","about"]):
    with col:
        if st.button(label, key="nav_"+page, use_container_width=True):
            go(page)

def section(kicker, title, desc=None):
    st.markdown(f'<div class="eyebrow">{kicker}</div><div class="section-title">{title}</div>', unsafe_allow_html=True)
    if desc: st.markdown(f'<p class="muted">{desc}</p>', unsafe_allow_html=True)

def community_cards(items):
    cols = st.columns(3, gap="large")
    for i, c in enumerate(items):
        with cols[i%3]:
            st.markdown(image_url(c["img"]), unsafe_allow_html=True)
            st.markdown(f'<div class="eyebrow" style="margin-top:16px">{c["tag"]}</div><div class="card-title">{c["name"]} <span style="font-size:16px;color:#aaa">{c["arabic"]}</span></div><p class="muted">{c["desc"]}</p>', unsafe_allow_html=True)
            if st.button("EXPLORE COMMUNITY ↗", key="open_"+c["key"], use_container_width=True):
                go("community", c["key"])

page = st.session_state.page

if page == "home":
    st.markdown("""
    <div class="hero"><div class="hero-content">
    <div class="eyebrow">A CREATIVE SPACE · RIYADH</div>
    <h1>TAKE THE STEP.<br>BE YOU.</h1>
    <p>خُذ الخطوة... كن أنت</p>
    <span class="pill">CREATE · MEET · EXPERIENCE · MOVE</span>
    </div></div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
    section("A SPACE TO BEGIN", "وش ودّك تجرّب؟", "جازف مساحة تجمع أشخاصاً عندهم فضول يجربون أشياء جديدة، يتعلمون من بعض، ويصنعون تجاربهم سوا.")
    community_cards(COMMUNITIES[:3])
    st.markdown("<br>", unsafe_allow_html=True)
    community_cards(COMMUNITIES[3:])
    c1,c2 = st.columns(2)
    with c1:
        if st.button("SEE ALL COMMUNITIES ↗", use_container_width=True): go("communities")
    with c2:
        if st.button("MAKE YOUR OWN COMMUNITY +", use_container_width=True): go("make")
    st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
    section("NOT JUST A HOBBY", "الفكرة تبدأ بخطوة.", "مو لازم تكون محترف. يكفي إن عندك رغبة تبدأ.")
    st.markdown('<div class="big-quote">“You don’t have to be good at something to start. You just have to start.”</div>', unsafe_allow_html=True)

elif page == "communities":
    section("FIND YOUR PEOPLE", "المجتمعات", "كل مجتمع مساحة صغيرة لهواية كبيرة. اختَر اللي يشبه فضولك.")
    community_cards(COMMUNITIES)
    st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
    section("GOT YOUR OWN THING?", "Make your own.")
    st.markdown('<p class="muted">ما لقيت مجتمع لهوايتك؟ اقترح مجتمعك، وخلّنا نبدأه مع بعض.</p>', unsafe_allow_html=True)
    if st.button("PROPOSE A COMMUNITY +", use_container_width=True): go("make")

elif page == "make":
    section("START SOMETHING", "Make your own community.", "اقترح هواية أو اهتمام ودّك تجمع الناس حوله. بنراجع الاقتراح قبل إضافته.")
    with st.form("community_form"):
        name = st.text_input("اسم المجتمع", placeholder="مثلاً: pottery club")
        about = st.text_area("وش فكرة المجتمع؟", placeholder="اكتب لنا وش ممكن نسوي فيه...")
        who = st.text_input("اسمك (اختياري)")
        submitted = st.form_submit_button("SEND PROPOSAL ↗")
    if submitted:
        if name.strip() and about.strip():
            st.session_state.proposals.append({"name":name.strip(),"about":about.strip(),"who":who.strip(),"votes":0})
            st.success("وصلنا اقتراحك! بنراجعه قبل اعتماده.")
        else: st.warning("اكتب اسم المجتمع وفكرته أولاً.")
    if st.session_state.proposals:
        section("COMMUNITY IDEAS", "اقتراحات وصلت")
        for p in st.session_state.proposals:
            st.markdown(f'<div class="idea"><h4>{html.escape(p["name"])}</h4><p class="muted">{html.escape(p["about"])}</p><span class="pill">UNDER REVIEW</span></div>', unsafe_allow_html=True)

elif page == "community":
    c = next((x for x in COMMUNITIES if x["key"] == st.session_state.community), COMMUNITIES[3])
    st.markdown(image_url(c["img"]), unsafe_allow_html=True)
    st.markdown(f'<div class="eyebrow" style="margin-top:24px">{c["tag"]} · JAZIF COMMUNITY</div><div class="section-title">{c["name"]}</div><div class="big-quote">{c["desc"]}</div>', unsafe_allow_html=True)
    st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
    section("COMING UP", "التجارب القادمة", "فعاليات مقترحة للتجربة — التفاصيل والمواعيد قابلة للتحديث.")
    if c["key"] == "music":
        events = [("01","Listening picnic","جلسة استماع ومشاركة أغاني في أجواء مفتوحة","قريباً · الرياض"),("02","Open jam night","ليلة موسيقية تجريبية؛ شارك بصوتك أو آلتك أو حضورك","قريباً · الرياض")]
    else:
        events = [("01",f"{c['name']} meetup","لقاء تعارف وتجربة مفتوحة لجميع المستويات","قريباً · الرياض"),("02","Try something new","تجربة بسيطة نبدأها مع بعض","قريباً · الرياض")]
    for n,t,d,when in events:
        st.markdown(f'<div class="idea"><span class="eyebrow">{n} / UPCOMING</span><h4>{t}</h4><p class="muted">{d}</p><span class="pill">{when}</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
    section("IDEA LAB", "We love it… we support it.", "عندك فكرة لفعالية تخص هذا المجتمع؟ شاركها. وصوّت للأفكار اللي ودّك نشوفها على أرض الواقع.")
    with st.form("idea_form_"+c["key"]):
        idea_title = st.text_input("عنوان الفكرة", placeholder="Give your idea a name")
        idea_detail = st.text_area("احكِ لنا عنها", placeholder="وش بنسوي؟ وكيف ممكن تكون التجربة؟")
        add = st.form_submit_button("SUBMIT YOUR IDEA +")
    if add:
        if idea_title.strip() and idea_detail.strip():
            st.session_state.ideas.setdefault(c["key"], []).append({"title":idea_title.strip(),"detail":idea_detail.strip(),"votes":0})
            st.success("فكرتك وصلت إلى Idea Lab!")
        else: st.warning("اكتب عنوان الفكرة ووصفها.")
    ideas = st.session_state.ideas.get(c["key"], [])
    if ideas:
        for i, idea in enumerate(ideas):
            st.markdown(f'<div class="idea"><span class="eyebrow">COMMUNITY IDEA</span><h4>{html.escape(idea["title"])}</h4><p class="muted">{html.escape(idea["detail"])}</p></div>', unsafe_allow_html=True)
            vote_key = f'{c["key"]}_{i}'
            cols = st.columns([1,3])
            with cols[0]:
                if st.button(f"♡ SUPPORT · {idea['votes']}", key="vote_"+vote_key):
                    if vote_key not in st.session_state.votes:
                        idea["votes"] += 1
                        st.session_state.votes.add(vote_key)
                        st.rerun()
                    else: st.info("صوّتِ لهذه الفكرة من قبل في هذه الجلسة.")
    else:
        st.info("لسه ما فيه أفكار. كوني أول من يقترح!")
    if st.button("← BACK TO COMMUNITIES"): go("communities")

elif page == "experiences":
    section("DO IT, DON'T JUST THINK IT", "التجارب", "مساحة للفعاليات واللقاءات والتجارب اللي تخليك تطلع من روتينك.")
    pics = [
        ("A LITTLE DIFFERENT","تجارب قصيرة تكسر الروتين","https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=1200&q=85"),
        ("MEET YOUR PEOPLE","لقاءات تجمع أشخاصاً باهتمامات مشتركة","https://images.unsplash.com/photo-1511632765486-a01980e01a18?auto=format&fit=crop&w=1200&q=85"),
        ("TRY THE UNKNOWN","جرّب شيئاً ما قد جرّبته من قبل","https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=85")]
    cols=st.columns(3)
    for col,(tag,title,url) in zip(cols,pics):
        with col:
            st.markdown(image_url(url),unsafe_allow_html=True)
            st.markdown(f'<div class="eyebrow" style="margin-top:14px">{tag}</div><h3>{title}</h3>',unsafe_allow_html=True)
    st.markdown('<div class="rule"></div>',unsafe_allow_html=True)
    section("YOUR NEXT STEP", "وش التجربة اللي تنتظرك؟")
    st.markdown('<p class="muted">قريباً بنضيف تقويم الفعاليات والتسجيل في كل تجربة. حالياً تقدر تستكشف المجتمعات وتقترح فعاليتك.</p>',unsafe_allow_html=True)
    if st.button("EXPLORE COMMUNITIES ↗"): go("communities")

elif page == "map":
    section("FIND YOUR WAY", "خريطة جازف", "المساحة مو بس مكان؛ هي نقاط تلتقي فيها الاهتمامات والناس والتجارب.")
    map_path = ASSETS / "jazif_map_reference.jpeg"
    if map_path.exists(): st.image(str(map_path), use_container_width=True)
    st.markdown('<div class="idea"><h4>THE JAZIF MAP</h4><p class="muted">هذه مساحة مبدئية للخريطة. لاحقاً نقدر نحولها إلى خريطة تفاعلية فيها مناطق المجتمعات، أماكن الفعاليات، ونقاط التجمع.</p><span class="pill">MORE TO DISCOVER</span></div>',unsafe_allow_html=True)

elif page == "about":
    section("WHAT IS JAZIF?", "جازف. خذ الخطوة… كن أنت.", "جازف مبادرة تشجّع الإنسان يبدأ، يجرّب، يلتقي بناس جدد، ويكتشف أشياء يمكن ما كان يعرف إنه يحبها.")
    st.markdown('<div class="big-quote">أربع أفعال. مساحة واحدة.<br>اصنع · اجتمع · جرّب · تحرّك</div>',unsafe_allow_html=True)
    st.markdown('<div class="rule"></div>',unsafe_allow_html=True)
    st.markdown('<p class="muted">JAZIF — CREATIVE SPACE · RIYADH</p>',unsafe_allow_html=True)

st.markdown('<div class="footer">JAZIF · TAKE THE STEP … BE YOU · RIYADH</div>', unsafe_allow_html=True)
