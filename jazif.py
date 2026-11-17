import streamlit as st
from pathlib import Path
import base64, html

st.set_page_config(page_title="JAZIF | Creative Space", page_icon="✦", layout="wide", initial_sidebar_state="collapsed")
ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

def b64(name):
    p = ASSETS / name
    return base64.b64encode(p.read_bytes()).decode() if p.exists() else ""

HERO1 = b64("jazif_hero_1.jpeg")
HERO2 = b64("jazif_hero_2.jpeg")

COMMUNITIES = [
    {"key":"draw","name":"مجتمع الفن والفخار","en":"DRAW","desc":"مساحة للرسم والفخار والتجريب الفني، مهما كان مستواك.","members":94,"emoji":"🎨","img":"https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=1800&q=90"},
    {"key":"walk","name":"مجتمع المشي","en":"WALK","desc":"نكتشف المدينة وتفاصيلها الصغيرة خطوة بخطوة.","members":68,"emoji":"🚶","img":"https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1800&q=90"},
    {"key":"bikes","name":"مجتمع الدراجات","en":"BIKES","desc":"جولات بالدراجات، حركة، وهواء جديد ووجوه جديدة.","members":52,"emoji":"🚲","img":"https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=1800&q=90"},
    {"key":"music","name":"مجتمع الموسيقى","en":"MUSIC","desc":"نجتمع حول الموسيقى؛ نسمع، نشارك، ونجرب أصواتاً وأفكاراً جديدة.","members":124,"emoji":"🎙️","img":"https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=1800&q=90"},
    {"key":"yoga","name":"مجتمع اليوغا","en":"YOGA","desc":"وقت للحركة الهادئة والتنفس والتواصل مع الجسد.","members":43,"emoji":"🧘","img":"https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1800&q=90"},
]

if "page" not in st.session_state: st.session_state.page = "home"
if "community" not in st.session_state: st.session_state.community = "music"
if "ideas" not in st.session_state:
    st.session_state.ideas = {
        "music":[
            {"title":"معرض مصغر لأعمال أعضاء المجتمع في حديقة جازف","by":"لمي الدوسري","detail":"مساحة نعرض فيها أعمال ومواهب أعضاء المجتمع، مع موسيقى وأجواء مفتوحة.","love":31,"support":20,"hosts":0},
            {"title":"جلسة رسم على الفخار مع موسيقى هادئة","by":"عضو من المجتمع","detail":"تجربة تجمع الفن والموسيقى في لقاء واحد.","love":18,"support":14,"hosts":0}
        ]
    }
if "my_votes" not in st.session_state: st.session_state.my_votes = set()
if "proposals" not in st.session_state: st.session_state.proposals = []
if "interest" not in st.session_state: st.session_state.interest = set()
if "active_tab" not in st.session_state: st.session_state.active_tab = "ideas"

def go(page, key=None):
    st.session_state.page = page
    if key: st.session_state.community = key
    st.rerun()

def img_div(url, cls="photo"):
    return f'<div class="{cls}" style="background-image:linear-gradient(0deg,rgba(0,0,0,.62),rgba(0,0,0,.03)),url(&quot;{url}&quot;)"></div>'

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700;800&display=swap');
:root{{--bg:#101513;--panel:#18231f;--line:rgba(255,255,255,.16);--mint:#14b894;--mint2:#76e4c4;--cream:#f5f1e8}}
html,body,[class*="css"]{{font-family:'DM Sans','IBM Plex Sans Arabic',sans-serif}}
.stApp{{background:var(--bg);color:var(--cream)}}
.block-container{{max-width:1500px;padding:0 4vw 5rem}}
header[data-testid="stHeader"]{{background:transparent;height:0}}
footer{{visibility:hidden}} #MainMenu{{visibility:hidden}}
/* Fixed navigation: stays visible while scrolling */
.st-key-topnav{{position:fixed;top:0;left:0;right:0;z-index:9999;background:rgba(12,17,15,.91);backdrop-filter:blur(18px);border-bottom:1px solid var(--line);padding:12px 4vw 9px}}
.st-key-topnav [data-testid="stHorizontalBlock"]{{align-items:center;gap:8px}}
.st-key-topnav .stButton>button{{border:0;background:transparent;color:#f5f1e8;font-size:14px;padding:8px 5px;white-space:nowrap;min-height:38px}}
.st-key-topnav .stButton>button:hover{{color:var(--mint2);background:transparent}}
.nav-spacer{{height:68px}}
.brand{{font-size:24px;font-weight:800;letter-spacing:2px;line-height:1}}
.brand small{{display:block;font-size:8px;letter-spacing:3px;color:#aaa;margin-top:4px}}
.eyebrow{{font-size:10px;letter-spacing:4px;color:#b5b7ad;text-transform:uppercase}}
.hero{{height:calc(100svh - 72px);min-height:570px;max-height:920px;position:relative;overflow:hidden;border-radius:3px;background-image:linear-gradient(0deg,rgba(0,0,0,.72),rgba(0,0,0,.04)),url(data:image/jpeg;base64,{HERO1});background-size:cover;background-position:center;display:flex;align-items:flex-end;padding:clamp(25px,6vw,85px);margin-top:6px}}
.hero:before{{content:"";position:absolute;inset:0;background-image:linear-gradient(0deg,rgba(0,0,0,.68),rgba(0,0,0,.03)),url(data:image/jpeg;base64,{HERO2});background-size:cover;background-position:center;opacity:0;animation:heroShift 13s infinite}}
@keyframes heroShift{{0%,43%{{opacity:0}}50%,91%{{opacity:1}}100%{{opacity:0}}}}
.hero-copy{{position:relative;z-index:2;max-width:850px}}
.hero h1{{font-size:clamp(48px,8vw,112px);line-height:.9;letter-spacing:-4px;margin:20px 0;color:white;font-weight:800}}
.hero .arabic{{font-family:'IBM Plex Sans Arabic';font-size:clamp(19px,2vw,27px);letter-spacing:0}}
.hero-tag{{display:inline-block;border:1px solid rgba(255,255,255,.55);padding:9px 14px;border-radius:30px;font-size:10px;letter-spacing:3px;margin-top:18px}}
.section-kicker{{font-size:10px;letter-spacing:4px;color:var(--mint2);margin-bottom:7px}}
.section-title{{font-size:clamp(34px,5vw,64px);font-weight:800;letter-spacing:-2px;margin:0 0 8px;color:var(--cream)}}
.sub{{color:#b9c0b9;line-height:1.9;font-size:14px}}
.rule{{height:1px;background:var(--line);margin:38px 0}}
.photo{{height:270px;background-size:cover;background-position:center;border-radius:4px}}
.community-name{{font-size:24px;font-weight:800;margin:14px 0 4px}}
.pill{{display:inline-block;border:1px solid rgba(255,255,255,.3);border-radius:30px;padding:7px 12px;font-size:11px;letter-spacing:1px}}
.community-hero{{height:430px;background-size:cover;background-position:center;border-radius:4px;display:flex;flex-direction:column;justify-content:flex-end;padding:30px;margin:5px 0 0}}
.community-hero h1{{font-size:clamp(35px,6vw,70px);font-weight:800;margin:12px 0}}
.member-pill{{background:#0eaa7d;color:white;border-radius:30px;padding:10px 16px;font-weight:800;width:max-content}}
.joinbutton{{background:var(--mint);color:#06231c;border-radius:30px;padding:13px 20px;font-weight:800;display:inline-block;margin-top:16px}}
.idea-box{{background:#102b28;border:1px solid rgba(118,228,196,.25);padding:22px;border-radius:24px;margin:16px 0}}
.idea-title{{font-size:23px;font-weight:800;line-height:1.5;margin:10px 0}}
.idea-meta{{color:var(--mint2);font-size:14px;font-weight:700}}
.vote-row{{display:flex;gap:10px;flex-wrap:wrap;margin-top:20px}}
.vote-love{{background:#3a252c;border:1px solid #a54a62;color:#ffd5df;border-radius:28px;padding:10px 16px;font-weight:800}}
.vote-support{{background:#0d3443;border:1px solid #167a9c;color:#bdeaff;border-radius:28px;padding:10px 16px;font-weight:800}}
.vote-host{{background:#0eb78d;border:1px solid #0eb78d;color:#042a22;border-radius:28px;padding:10px 16px;font-weight:800}}
.footer{{border-top:1px solid var(--line);padding:30px 0;margin-top:60px;color:#929b93;font-size:10px;letter-spacing:3px}}
.stButton>button{{border:1px solid var(--mint);background:var(--mint);color:#06231c;border-radius:30px;font-weight:800;min-height:43px}}
.stButton>button:hover{{background:#72e2c2;border-color:#72e2c2;color:#06231c}}
.stTextInput input,.stTextArea textarea{{background:#132823;color:#fff;border:1px solid #176b63;border-radius:16px}}
label{{color:#e9eee9!important}}
@media(max-width:700px){{.block-container{{padding:0 4vw 3rem}}.st-key-topnav{{padding:8px 3vw}}.st-key-topnav .stButton>button{{font-size:11px;padding:6px 1px}}.nav-spacer{{height:58px}}.hero{{height:calc(90svh - 60px);min-height:530px;padding:25px 20px}}.hero h1{{letter-spacing:-2px}}.photo{{height:190px}}.community-hero{{height:380px;padding:20px}}.idea-box{{padding:17px}}}}
</style>
""", unsafe_allow_html=True)

# Persistent top menu
with st.container(key="topnav"):
    nav = st.columns([1.15,1,1,1,1])
    with nav[0]:
        st.markdown('<div class="brand">جازف<small>JAZIF · CREATIVE SPACE</small></div>',unsafe_allow_html=True)
    for col,label,page in zip(nav[1:],["الرئيسية","المجتمعات","التجارب","خريطة المساحة"],["home","communities","experiences","map"]):
        with col:
            if st.button(label,key="nav_"+page,use_container_width=True): go(page)
st.markdown('<div class="nav-spacer"></div>',unsafe_allow_html=True)

def section(kicker,title,desc=""):
    st.markdown(f'<div class="section-kicker">{kicker}</div><div class="section-title">{title}</div><p class="sub">{desc}</p>',unsafe_allow_html=True)

def cards(items):
    cols=st.columns(2 if len(items)>1 else 1,gap="large")
    for i,c in enumerate(items):
        with cols[i%len(cols)]:
            st.markdown(img_div(c["img"]),unsafe_allow_html=True)
            st.markdown(f'<div class="section-kicker" style="margin-top:15px">{c["en"]} COMMUNITY</div><div class="community-name">{c["name"]}</div><p class="sub">{c["desc"]}</p><span class="pill">{c["members"]} MEMBERS {c["emoji"]}</span>',unsafe_allow_html=True)
            if st.button("EXPLORE COMMUNITY ↗",key="community_"+c["key"],use_container_width=True): go("community",c["key"])

page=st.session_state.page

if page=="home":
    st.markdown('<div class="hero"><div class="hero-copy"><div class="eyebrow">A CREATIVE SPACE · RIYADH</div><h1>TAKE THE STEP.<br>BE YOU.</h1><div class="arabic">خُذ الخطوة... كن أنت</div><span class="hero-tag">CREATE · MEET · EXPERIENCE · MOVE</span></div></div>',unsafe_allow_html=True)
    st.markdown('<div class="rule"></div>',unsafe_allow_html=True)
    section("FIND YOUR PEOPLE","المجتمعات","هوايات مختلفة، أشخاص يشبهون فضولك، وتجارب تبدأ بخطوة.")
    cards(COMMUNITIES[:4])
    if st.button("SEE ALL COMMUNITIES ↗",use_container_width=True): go("communities")
    st.markdown('<div class="rule"></div>',unsafe_allow_html=True)
    section("YOUR NEXT STEP","مو لازم تعرف كل شيء… بس ابدأ.","جازف مساحة تجرب فيها شيئاً جديداً، وتلتقي بناس يشاركونك الاهتمام.")
    if st.button("MAKE YOUR OWN COMMUNITY +",use_container_width=True): go("make")

elif page=="communities":
    section("FIND YOUR COMMUNITY","المجتمعات","اختر مجتمعاً، شارك باهتمامك، أو ابدأ مجتمعاً جديداً.")
    cards(COMMUNITIES)
    st.markdown('<div class="rule"></div>',unsafe_allow_html=True)
    if st.button("MAKE YOUR OWN COMMUNITY +",use_container_width=True): go("make")

elif page=="community":
    c=next((x for x in COMMUNITIES if x["key"]==st.session_state.community),COMMUNITIES[0])
    st.markdown(f'<div class="community-hero" style="background-image:linear-gradient(0deg,rgba(0,0,0,.86),rgba(0,0,0,.08)),url(&quot;{c["img"]}&quot;)"><span class="member-pill">{c["members"]} عضو نشط {c["emoji"]}</span><h1>{c["name"]}</h1><div>{c["desc"]}</div></div>',unsafe_allow_html=True)
    if st.button("+ طلب اهتمام / انضمام للمجتمع",use_container_width=True):
        st.session_state.interest.add(c["key"])
        st.success("وصلنا اهتمامك! بنعلن لك عن الخطوات القادمة.")
    st.markdown('<div class="rule"></div>',unsafe_allow_html=True)
    tabs=st.columns(3)
    tab_names=[("events","الفعاليات القادمة"),("ideas","💡 اقترح فكرة والتصويت (Co-Host)"),("chat","💬 شات المجتمع")]
    for col,(key,label) in zip(tabs,tab_names):
        with col:
            if st.button(label,key="tab_"+key,use_container_width=True):
                st.session_state.active_tab=key
                st.rerun()
    active=st.session_state.active_tab
    st.markdown('<div class="rule"></div>',unsafe_allow_html=True)
    if active=="events":
        section("UP NEXT","الفعاليات القادمة","لقاءات وتجارب قريبة لهذا المجتمع.")
        for title,desc in [("Community Meetup","لقاء تعارف وتجربة مفتوحة لجميع المستويات."),("Try Something New","تجربة بسيطة نبدأها مع بعض.")]:
            st.markdown(f'<div class="idea-box"><div class="section-kicker">COMING SOON · RIYADH</div><div class="idea-title">{title}</div><p class="sub">{desc}</p></div>',unsafe_allow_html=True)
    elif active=="ideas":
        section("IDEA LAB","We love it… We support it.","اقترح تجربة أو لقاء لهذا المجتمع. المجتمع يصوّت، والمهتمون يقدرون ينضمون كـ Co-Host.")
        with st.form("new_idea"):
            title=st.text_input("اقترح تجربة أو لقاء جديد لهذا المجتمع:",placeholder="مثال: جلسة رسم على الفخار مع موسيقى هادئة")
            detail=st.text_area("تفاصيل الفكرة (اختياري)",placeholder="احكِ لنا كيف تتخيل التجربة...")
            submitted=st.form_submit_button("طرح للتصويت ↗")
        if submitted:
            if title.strip():
                st.session_state.ideas.setdefault(c["key"],[]).append({"title":title.strip(),"by":"عضو من المجتمع","detail":detail.strip(),"love":0,"support":0,"hosts":0})
                st.success("انضافت فكرتك إلى Idea Lab!")
            else: st.warning("اكتب عنوان الفكرة أولاً.")
        for i,idea in enumerate(st.session_state.ideas.get(c["key"],[])):
            st.markdown(f'<div class="idea-box"><div class="idea-meta">💡 مقترح من: {html.escape(idea["by"])}</div><div class="idea-title">{html.escape(idea["title"])}</div><p class="sub">{html.escape(idea["detail"])}</p></div>',unsafe_allow_html=True)
            cols=st.columns(3)
            vote_id=f'{c["key"]}_{i}'
            actions=[("❤️ We Love It", "love", "vote-love"),("🙌 We Support It","support","vote-support"),("🤝 Be a Co-Host","hosts","vote-host")]
            for col,(label,field,css) in zip(cols,actions):
                with col:
                    if st.button(f'{label} ({idea[field]})',key=f'{field}_{vote_id}',use_container_width=True):
                        unique=f"{field}_{vote_id}"
                        if unique not in st.session_state.my_votes:
                            idea[field]+=1
                            st.session_state.my_votes.add(unique)
                            st.rerun()
                        else: st.info("سبق وسجلت اختيارك لهذه الفكرة.")
    else:
        section("COMMUNITY CHAT","شات المجتمع","مساحة المحادثات والتعارف — نضيف نظام الحسابات والرسائل في مرحلة لاحقة.")
        st.info("واجهة الشات مبدئية، وتحتاج ربط قاعدة بيانات وتسجيل دخول لتفعيل المحادثات.")
    st.markdown('<div class="rule"></div>',unsafe_allow_html=True)
    if st.button("← العودة للمجتمعات"): go("communities")

elif page=="make":
    section("START SOMETHING","Make your own community","عندك هواية ودك تجمع الناس حولها؟ اقترح مجتمعك.")
    with st.form("community_suggestion"):
        name=st.text_input("اسم المجتمع")
        desc=st.text_area("فكرة المجتمع")
        if st.form_submit_button("SEND PROPOSAL ↗"):
            if name.strip() and desc.strip():
                st.session_state.proposals.append((name.strip(),desc.strip()))
                st.success("وصل اقتراحك للمراجعة!")
            else: st.warning("اكتب اسم المجتمع وفكرته.")
    for name,desc in st.session_state.proposals:
        st.markdown(f'<div class="idea-box"><div class="idea-title">{html.escape(name)}</div><p class="sub">{html.escape(desc)}</p><span class="pill">UNDER REVIEW</span></div>',unsafe_allow_html=True)

elif page=="experiences":
    section("MAKE IT HAPPEN","التجارب","فعاليات ولقاءات تفتح لك باب تجربة شيء جديد.")
    cards(COMMUNITIES[1:4])
    st.markdown('<div class="rule"></div>',unsafe_allow_html=True)
    st.info("قريباً: تقويم موحد للفعاليات، تفاصيل كل تجربة، والتسجيل المباشر.")

elif page=="map":
    section("EXPLORE THE SPACE","خريطة جازف","نبدأ برسم مبدئي للمساحة، ونطورها لاحقاً إلى خريطة تفاعلية.")
    p=ASSETS/"jazif_map_reference.jpeg"
    if p.exists(): st.image(str(p),use_container_width=True)
    st.markdown('<div class="idea-box"><div class="idea-title">THE JAZIF MAP</div><p class="sub">مناطق المجتمعات، أماكن الفعاليات، ونقاط التجمع — نحددها في المرحلة القادمة.</p></div>',unsafe_allow_html=True)

st.markdown('<div class="footer">JAZIF · TAKE THE STEP … BE YOU · RIYADH</div>',unsafe_allow_html=True)
