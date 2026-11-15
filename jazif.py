import streamlit as st

# 1. إعدادات الصفحة لتناسب الجوال
st.set_page_config(
    page_title="مساحة جازف | JAZEF",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. تنسيقات CSS مخصصة للجوال والهوية البصرية (عربي RTL)
st.markdown("""
<style>
    /* ضبط الاتجاه العربي وتقليل الهوامش للجوال */
    .main .block-container {
        max-width: 480px;
        padding-top: 1rem;
        padding-bottom: 3rem;
        direction: rtl;
        text-align: right;
    }
    
    /* تنسيق الهيدر العلوي */
    .mobile-header {
        background-color: #1E293B;
        color: white;
        padding: 12px 16px;
        border-radius: 14px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
    }
    
    /* بطاقات التجارب والخريطة */
    .exp-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
    }
    .badge-soon {
        background-color: #DCFCE7;
        color: #166534;
        padding: 3px 8px;
        border-radius: 8px;
        font-size: 12px;
        font-weight: bold;
    }
    .badge-later {
        background-color: #FEF3C7;
        color: #92400E;
        padding: 3px 8px;
        border-radius: 8px;
        font-size: 12px;
        font-weight: bold;
    }
    
    /* بطاقة التذكرة الرقمية QR */
    .digital-pass {
        background: linear-gradient(135deg, #0F172A, #334155);
        color: white;
        padding: 18px;
        border-radius: 16px;
        text-align: center;
        margin: 10px 0;
    }
    
    /* تحسين أزرار ستريملت للجوال */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 3. بيانات تجريبية للمجتمعات (لتكون ديناميكية)
COMMUNITIES = {
    "يوغا وتأمل 🧘‍♀️": {
        "desc": "جلسات صباحية ومسائية في الحديقة الخارجية لتصفية الذهن واستعادة التوازن.",
        "checklist": ["سجادة يوغا (Mat)", "ملابس رياضية مريحة", "مطارة ماء شخصية", "منشفة صغيرة"],
        "member_approved": True,
        "past_images": ["🌅 يوغا الشروق", "🌿 تأمل الحديقة"]
    },
    "فنون وفخار 🎨": {
        "desc": "ورش عمل حرة لتشكيل الفخار والرسم على الكانفس في المساحة الداخلية المكيفة.",
        "checklist": ["مريلة رسم (أو ملابس لا تمانع اتساخها)", "دفتر سكتش لأفكارك", "كل الأدوات الفنية متوفرة لدينا!"],
        "member_approved": False,
        "past_images": ["🏺 ورشة الفخار", "🖌️ ليلة الرسم الحر"]
    },
    "فروسية وخيول 🐎": {
        "desc": "لقاءات لعشاق الخيل وتجارب ركوب وتعلم أساسيات التعامل مع الخيول.",
        "checklist": ["حذاء مغلق ومناسب (Boots)", "بنطال مريح", "قفازات ركوب (اختياري)"],
        "member_approved": True,
        "past_images": ["🐎 جولة المساء", "🌾 العناية بالخيل"]
    }
}

# 4. الهيدر الثابت (Sticky Header) + زر الملف الشخصي والتذكرة
st.markdown("""
<div class="mobile-header">
    <div>
        <strong style="font-size:18px;">🌿 مساحة جازف</strong><br>
        <span style="font-size:11px; color:#CBD5E1;">مجتمعات، تجارب، ومساحة حرة</span>
    </div>
    <div style="text-align:left;">
        <span style="background:#334155; padding:6px 10px; border-radius:20px; font-size:13px;">👤 حسابي</span>
    </div>
</div>
""", unsafe_allow_html=True)

# قائمة الحساب المنسدلة (Badges + المجتمعات + الـ Digital Pass)
with st.expander("👤 قائمة حسابي & التذكرة الرقمية (Digital Pass)"):
    col_p1, col_p2 = st.columns([2, 1])
    with col_p1:
        st.markdown("**أهلاً بك في جازف 👋**")
        st.caption("🏅 الأوسمة: مؤسس مجتمع • حاضر 3 تجارب")
        st.caption("📌 مجتمعاتي: اليوغا، الفروسية")
    with col_p2:
        show_qr = st.toggle("تذكرتي 🎟️", value=False)
    
    if show_qr:
        st.markdown("""
        <div class="digital-pass">
            <div style="font-size:13px; color:#94A3B8;">JAZEF DIGITAL PASS</div>
            <h3 style="margin:5px 0; color:white;">#JZF-2026-88</h3>
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=JAZEF-PASS-88" style="border-radius:8px; margin:8px 0; background:white; padding:5px;">
            <div style="font-size:12px; color:#38BDF8;">✅ صالح للدخول عند البوابة</div>
        </div>
        """, unsafe_allow_html=True)

# 5. شريط التنقل الرئيسي للجوال (بديل روابط الهيدر)
page = st.radio(
    "التنقل",
    ["🏠 الرئيسية", "🤝 المجتمعات", "📝 تسجيل / شركات"],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()

# ==========================================
# الصفحة 1: الرئيسية (Home 1)
# ==========================================
if page == "🏠 الرئيسية":
    # أ) التعريف بالمبادرة
    st.subheader("فكرة تتجاوز جدران المكان ✨")
    st.write("في **جازف**، نهيئ لك مساحة مرنة تجمع بين الهدوء والحيوية لتبني مجتمعك، تطلق ورشتك، أو تعيش تجربة جديدة.")
    
    # ب) مرونة المساحة (صور سريعة)
    st.markdown("#### 🔄 مرونة المساحة")
    c1, c2, c3 = st.columns(3)
    c1.info("🧘‍♀️ **يوغا**\n\nصباحية")
    c2.success("🎶 **حفل**\n\nموسيقي")
    c3.warning("🎨 **ورش**\n\nإبداعية")
    
    st.divider()
    
    # ج) خريطة التجارب التفاعلية (Map) مقسمة: داخلية 105م² وخارجية 533م²
    st.subheader("🗺️ خريطة المساحة والتجارب")
    
    zone = st.segmented_control(
        "اختر القسم في الخريطة:",
        ["🌳 الحديقة الخارجية (533 م²)", "🏠 المساحة الداخلية (105 م²)"],
        default="🌳 الحديقة الخارجية (533 م²)"
    )
    
    if zone == "🌳 الحديقة الخارجية (533 م²)":
        st.markdown("""
        <div class="exp-card">
            <span class="badge-soon">🟢 قريباً - اليوم 6:00 م</span>
            <h4 style="margin:6px 0;">جلسة يوغا الغروب</h4>
            <p style="font-size:13px; margin:2px 0;">📍 الحديقة الخارجية • ⏳ باقي <b>4 مقاعد</b> من 12</p>
        </div>
        <div class="exp-card">
            <span class="badge-later">🟡 الأسبوع القادم - الجمعة 8:00 م</span>
            <h4 style="margin:6px 0;">أمسية موسيقية مفتوحة</h4>
            <p style="font-size:13px; margin:2px 0;">📍 المسرح الخارجي • ⏳ باقي <b>11 مقعد</b> من 30</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="exp-card">
            <span class="badge-soon">🟢 غداً - 5:30 م</span>
            <h4 style="margin:6px 0;">ورشة تشكيل الفخار للمبتدئين</h4>
            <p style="font-size:13px; margin:2px 0;">📍 الاستوديو الداخلي • ⏳ باقي <b>2 مقعد</b> من 8</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# الصفحة 2: المجتمعات (Communities)
# ==========================================
elif page == "🤝 المجتمعات":
    st.subheader("اختر مجتمعك واستكشف التفاصيل")
    
    # اختيار المجتمع (يحاكي الضغط على بطاقة المجتمع والانتقال لصفحته)
    selected_comm = st.selectbox("المجتمعات المتاحة:", list(COMMUNITIES.keys()))
    comm_data = COMMUNITIES[selected_comm]
    
    st.markdown(f"### {selected_comm}")
    
    # التبويبات الثلاثة النظيفة داخل صفحة المجتمع
    tab1, tab2, tab3 = st.tabs(["📌 نظرة عامة", "💡 مختبر الأفكار", "💬 مساحة المجتمع"])
    
    # تبويب 1: نظرة عامة + قائمة ماذا تحضر معك الديناميكية
    with tab1:
        st.write(comm_data["desc"])
        
        # قائمة What to Bring الديناميكية حسب المجتمع
        with st.container(border=True):
            st.markdown("**🎒 ماذا تحضر معك؟ (What to Bring)**")
            for item in comm_data["checklist"]:
                st.checkbox(item, key=f"{selected_comm}_{item}")
                
        st.markdown("**📸 من لقاءاتنا السابقة:**")
        img_cols = st.columns(2)
        for idx, img_label in enumerate(comm_data["past_images"]):
            img_cols[idx].info(img_label)
            
        if st.button("✨ سجل اهتمامك بهذا المجتمع", type="primary"):
            st.toast("تم إرسال طلب انضمامك! سيصلك إشعار عند القبول.")

    # تبويب 2: مختبر الأفكار (اقتراح + تصويت + Find a Co-host)
    with tab2:
        st.markdown("**أفكار مقترحة من الأعضاء للتجربة القادمة:**")
        with st.container(border=True):
            st.write("💡 **تجربة دمج الرسم مع الموسيقى الحية**")
            col_v1, col_v2 = st.columns(2)
            col_v1.button("👍 تصويت (18)", key="vote1")
            col_v2.button("🤝 Find a Co-host", key="cohost1")
            
        with st.expander("➕ اقترح فكرة جديدة"):
            st.text_input("عنوان التجربة")
            st.checkbox("أبحث عن شريك تنظيم (Co-host)")
            st.button("نشر الفكرة للتصويت")

    # تبويب 3: مساحة المجتمع (مقفلة إلا للمقبولين)
    with tab3:
        if comm_data["member_approved"]:
            st.success("✅ أنت عضو مقبول في هذا المجتمع")
            st.link_button("📲 دخول قروب الواتساب الرسمي", "https://whatsapp.com")
            st.markdown("---")
            st.markdown("**💬 شات المجتمع (تحت إشراف الأدمن):**")
            st.chat_message("assistant").write("أهلاً بالجميع! تذكير: لقاءنا القادم الساعة 6 مساءً 🌿")
            st.chat_message("user").write("متحمسين جداً! هل المواقف متوفرة عند البوابة؟")
            st.chat_input("اكتب رسالتك للمجتمع...")
        else:
            st.warning("🔒 هذه المساحة (الشات وقروب الواتساب) تظهر فقط للأعضاء المقبولين في المجتمع.")
            st.caption("سجّل اهتمامك من تبويب (نظرة عامة) ليتم تفعيل الوصول لك.")

# ==========================================
# الصفحة 3: تسجيل جديد / تسجيل شركات
# ==========================================
elif page == "📝 تسجيل / شركات":
    reg_type = st.segmented_control("نوع التسجيل:", ["👤 تسجيل أفراد", "🏢 تسجيل شركات / جهات"], default="👤 تسجيل أفراد")
    
    with st.form("reg_form"):
        if reg_type == "👤 تسجيل أفراد":
            st.text_input("الاسم الكامل")
            st.text_input("رقم الجوال (واتساب)")
            st.multiselect("المجتمعات التي تهمك", list(COMMUNITIES.keys()))
        else:
            st.text_input("اسم الشركة / الجهة")
            st.selectbox("نوع التعاون", ["حجز المساحة لفعالية خاصة", "رعاية مجتمع", "ورشة عمل لموظفي الشركة"])
            st.text_input("البريد الإلكتروني الرسمي")
            
        if st.form_submit_button("إرسال الطلب 🚀", type="primary"):
            st.success("تم استلام بياناتك بنجاح! فريق جازف سيتواصل معك قريباً.")
