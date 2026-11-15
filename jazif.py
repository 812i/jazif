import streamlit as st

# إعدادات الصفحة لتكون عريضة ومنظمة
st.set_page_config(
    page_title="جازف - JAZIF Communities", page_icon="✨", layout="wide"
)

# تنسيق CSS إضافي لتحسين المظهر وتثبيت القائمة العلوية
st.markdown(
    """
    <style>
    /* تثبيت القائمة العلوية */
    .stMainBlockContainer {
        padding-top: 2rem;
    }
    .profile-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e9ecef;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# القائمة العلوية الثابتة (Sticky Navbar عبر أعمدة Streamlit)
# ---------------------------------------------------------
nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns(
    [1.5, 1, 1, 1, 1.5]
)

with nav_col1:
    st.markdown("### **جـازف | JAZIF**")

# الروابط الرئيسية في المنتصف
selected_tab = st.radio(
    "القائمة",
    ["الرئيسية", "المجتمعات", "تسجيل مجتمع جديد", "تسجيل للشركات"],
    horizontal=True,
    label_visibility="collapsed",
)

with nav_col5:
    # زر الحساب الجانبي (على اليمين)
    if st.button("👤 حسابي / الشارات"):
        st.session_state["show_profile"] = (
            not st.session_state.get("show_profile", False)
        )

st.markdown("---")

# ---------------------------------------------------------
# لوحة الملف الشخصي الجانبية (لو تم الضغط على زر الحساب)
# ---------------------------------------------------------
if st.session_state.get("show_profile", False):
    with st.sidebar:
        st.markdown("### 👤 تفاصيل الحساب")
        st.image(
            "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150",
            width=80,
        )
        st.write("**سارة أحمد**")
        st.text("عضو في مجتمع اليوغا والقيمنق")

        st.markdown("---")
        st.markdown("#### 🏅 الشارات (Badges)")
        st.success("🌟 منظم فعالية نشط")
        st.info("🧘‍♀️ رائدة يوغا جازف")

        st.markdown("#### 🎟️ تذاكري والـ Digital Pass")
        st.code("JAZIF-PASS-9821", language="text")
        st.button("إغلاق القائمة", on_click=lambda: st.session_state.update({"show_profile": False}))

# ---------------------------------------------------------
# 1. الصفحة الرئيسية (Home 1)
# ---------------------------------------------------------
if selected_tab == "الرئيسية":
    # القسم الأول: التعريف بمبادرة جازف
    st.markdown(
        "<h1 style='text-align: center;'>مساحة تبدأ من فكرتك.</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center; color: gray;'>في وادي حنيفة بالرياض، تتكيف المساحة لتمنحك أجواء تجمع بين هدوء الطبيعة وخصوصية المكان.</p>",
        unsafe_allow_html=True,
    )

    st.write("---")

    # القسم الثاني: صور مرونة المساحة
    st.subheader("✨ مرونة المساحة (نفس المكان .. تجارب مختلفة)")
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)

    with m_col1:
        st.image(
            "https://images.unsplash.com/photo-1545205597-3d9d02c29597?w=300",
            caption="يوغا واسترخاء",
        )
    with m_col2:
        st.image(
            "https://images.unsplash.com/photo-1513364776144-60967b0f800f?w=300",
            caption="ورش فخار ورسم",
        )
    with m_col3:
        st.image(
            "https://images.unsplash.com/photo-1511578314322-379afb476865?w=300",
            caption="تجمعات وفعاليات",
        )
    with m_col4:
        st.image(
            "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=300",
            caption="لقاءات واجتماعات",
        )

    st.write("---")

    # القسم الثالث: خريطة المساحة (Map) والتجارب القريبة والبعيدة
    st.subheader("🗺️ خريطة الفعاليات والتجارب الحية في جازف")

    map_col1, map_col2 = st.columns([2, 1])

    with map_col1:
        # صورة تمثيلية للخريطة أو قسم المساحة (الداخلية والخارجية)
        st.image(
            "https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=600",
            caption="خريطة مساحة جازف (وادي حنيفة - داخلي وخارجي)",
        )

    with map_col2:
        st.markdown("### 📍 التجارب القادمة")
        # تجارب وقتها قريب (تظهر باللون الأزرق)
        st.info("🔵 **جلسة يوغا صباحية**\n- **متى:** غداً، 6:00 صباحاً\n- **مكانها:** الحديقة الخلفية الخارجية")
        # تجارب وقتها بعيد (تظهر باللون الرمادي)
        st.warning(
            "⚪ **بطولة القيمنق الودية**\n- **متى:** الخميس القادم\n- **مكانها:** القاعة الداخلية المكيفة"
        )

    st.write("---")
    # تواصل معنا والحسابات في نهاية الصفحة
    st.markdown("### 📞 تواصل معنا")
    f_col1, f_col2 = st.columns(2)
    with f_col1:
        st.write("📍 وادي حنيفة - حي الرفيعة - الرياض")
        st.write("📞 0536656051")
    with f_col2:
        st.write("🌐 انستغرام / تويتر: @Jazifspace")
        st.write("✨ خذ الخطوة .. كن أنت")

# ---------------------------------------------------------
# 2. صفحة المجتمعات
# ---------------------------------------------------------
elif selected_tab == "المجتمعات":
    st.markdown("<h2>👥 مجتمعات جازف الإبداعية</h2>", unsafe_allow_html=True)
    st.write("اختر المجتمع الذي يعبر عن اهتمامك وانضم لرحلتنا:")

    # أيقونات المجتمعات
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        if st.button("🧘‍♀️ يوغا وصحة"):
            st.session_state["active_community"] = "يوغا"
    with c2:
        if st.button("🐎 خيول وفروسية"):
            st.session_state["active_community"] = "خيول"
    with c3:
        if st.button("🎮 قيمنق وألعاب"):
            st.session_state["active_community"] = "قيمنق"
    with c4:
        if st.button("🎨 ورش وفنون"):
            st.session_state["active_community"] = "فنون"

    # عرض محتوى المجتمع المختار
    current_comm = st.session_state.get("active_community", "يوغا")
    st.write("---")
    st.markdown(f"### تفاصيل مجتمع: {current_comm}")

    tab_p1, tab_p2, tab_p3 = st.tabs(
        ["صور وفعاليات", "مختبر الأفكار والتصويت", "مساحة المجتمع والشات"]
    )

    with tab_p1:
        st.write("صور من الفعاليات السابقة والقادمة:")
        st.image(
            "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=500",
            width=400,
        )
        if st.button("سجل اهتمامك بالانضمام لهذا المجتمع"):
            st.success("تم تسجيل اهتمامك بنجاح! سيتم مراجعة طلبك.")

    with tab_p2:
        st.markdown("#### 💡 اقترح فكرة جديدة لتطوير هذا المجتمع")
        idea_text = st.text_input("اكتب فكرتك هنا:")
        if st.button("إرسال الفكرة للتصويت"):
            st.success("تم طرح فكرتك لتصويت الأعضاء!")

        st.markdown("---")
        st.markdown("##### الأفكار المقترحة الحالية:")
        st.write(
            "📌 **جلسة يوغا تحت ضوء القمر** - التصويت: 👍 We love it (14) | 🤝 We support it (8)"
        )
        # خيار البحث عن Co-host
        if st.button("🤝 ابحث عن مشرف مشارك (Find a Co-host)"):
            st.info(
                "تم تفعيل طلبك للبحث عن Co-host لمساعدتك في إدارة الفكرة!"
            )

    with tab_p3:
        st.markdown("🔒 **مساحة النقاش الخاصة بأعضاء المجتمع**")
        st.info(
            "الشات مغلق ولا يفتح إلا قبل الفعالية بـ 24 ساعة لضمان الجدية والإشراف."
        )
        st.text_input("أرسل رسالة للإدارة أو المشرفين:", placeholder="اكتب هنا...")

# ---------------------------------------------------------
# 3. تسجيل مجتمع جديد
# ---------------------------------------------------------
elif selected_tab == "تسجيل مجتمع جديد":
    st.markdown("<h2>🚀 اقترح مجتمعك الخاص في جازف</h2>", unsafe_allow_html=True)
    st.write(
        "لديك اهتمام غير موجود؟ املأ النموذج وسندعمك بالمساحة والتجهيزات:"
    )

    with st.form("new_community_form"):
        comm_name = st.text_input("اسم المجتمع المقترح (مثل: نادي الكتاب، التصوير الفوتوغرافي...)")
        comm_desc = st.text_area("نبذة عن نشاطات المجتمع وأهداف غير الربحية")
        expected_people = st.slider("العدد المتوقع للحضور:", 5, 30, 10)
        submitted = st.form_submit_button("إرسال طلب تأسيس المجتمع")
        if submitted:
            st.success(
                f"شكراً لك! تم استلام طلب تأسيس مجتمع '{comm_name}' وسيتواصل معك فريق جازف قريباً."
            )

# ---------------------------------------------------------
# 4. تسجيل للشركات والتعاونات
# ---------------------------------------------------------
elif selected_tab == "تسجيل للشركات":
    st.markdown("<h2>🏢 الشركات، الجهات، والتعاونات</h2>", unsafe_allow_html=True)
    st.write(
        "مساحة جازف ترحب بالشراكات المجتمعية غير الربحية ورعاية الفعاليات في وادي حنيفة."
    )

    with st.form("corporate_form"):
        org_name = st.text_input("اسم الجهة / الشركة / المبادرة")
        collab_type = st.selectbox(
            "نوع التعاون المطلوب:",
            [
                "رعاية فعالية مجتمعية",
                "استضافة لقاء فريق عمل",
                "شراكة استراتيجية غير ربحية",
            ],
        )
        message = st.text_area("تفاصيل الطلب أو المبادرة:")
        corp_submitted = st.form_submit_button("إرسال طلب التعاون")
        if corp_submitted:
            st.success(
                "تم إرسال طلب الشراكة بنجاح، يسعدنا التعاون معكم في جازف!"
            )
