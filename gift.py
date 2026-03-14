import streamlit as st
import time

# 1. إعدادات الصفحة (العنوان والأيقونة التي تظهر في المتصفح)
st.set_page_config(page_title="هدية خاصة 🎁", page_icon="❤️")

# 2. إضافة خلفية قلوب (باستخدام CSS بسيط)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.onlygfx.com/wp-content/uploads/2018/10/4-heart-confetti-background-2.png");
        background-size: cover;
    }
    
    /* هذا الجزء سيغير لون كل أنواع الكتابة في الصفحة */
    h1, h2, h3, p, span, div {
        color: #FFFFFF !important; /* الأسود، يمكنك تغييره لأي لون غامق */
        font-weight: bold !important; /* لجعل الخط عريض وواضح */
        text-shadow: 1px 1px 2px white; /* إضافة ظل أبيض خفيف خلف الكلام ليفصله عن الخلفية */
    }
    
    /* إذا أردت تغيير لون النص الموجود على الزر أيضاً */
    .stButton>button {
        color: #ffffff; /* لون نص الزر أبيض */
        background-color: #ff4b4b; /* لون الزر نفسه أحمر */
        border-radius: 20px; /* جعل زوايا الزر دائرية */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. منطق "فتح الظرف"
if 'opened' not in st.session_state:
    st.session_state.opened = False

st.write("#") # مسافة فارغة

if not st.session_state.opened:
    # عرض صورة ظرف مغلق (يمكنك استبدال الرابط بصورة من جهازك لاحقاً)
    st.image("https://png.pngtree.com/png-clipart/20230927/original/pngtree-closed-white-envelope-png-image_13148675.png", width=300)
    
    if st.button('اضغط لفتح الظرف ✉️'):
        st.session_state.opened = True
        st.balloons() # تأثير البالونات
        st.rerun()
else:
    # ما يحدث بعد الفتح
    st.write("## 🎉 مسمووسه  كل عام وأنت بخير! 🎉")
    st.image("https://img.pikbest.com/png-images/blue-envelope-mother-s-day-floral-gift_5850325.png!bw700", width=200) # صورة ظرف مفتوح
    
    # رسالتك هنا
    st.error("يا مسمس يا اجمل و احلى مساري فيكي يا دنيا يارب سنة خير و مسرات و راحة بال  و هاي هدية بسيطه الج تستاهلين اكثرر يا اعظم انسانه في حياتي ")
    
    # تأثير "تطشر الورود" (سنستخدم الثلج كبديل للورود البيضاء) 
# كود الورود الكبيرة والكثيرة 🌸🌹
st.markdown(
    """
    <style>
    @keyframes fall {
        0% { top: -10%; transform: translateX(0) rotate(0deg); opacity: 1; }
        100% { top: 100%; transform: translateX(100px) rotate(360deg); opacity: 0.3; }
    }
    .flower {
        position: fixed;
        z-index: 9999;
        font-size: 40px; /* هنا نكبر الحجم */
        user-select: none;
        animation: fall 8s linear infinite;
    }
    </style>
    
    <div class="flower" style="left:5%;  animation-delay:0s">🌸</div>
    <div class="flower" style="left:15%; animation-delay:2s">🌹</div>
    <div class="flower" style="left:25%; animation-delay:4s">🌷</div>
    <div class="flower" style="left:35%; animation-delay:1s">🌺</div>
    <div class="flower" style="left:45%; animation-delay:5s">🌸</div>
    <div class="flower" style="left:55%; animation-delay:3s">🌹</div>
    <div class="flower" style="left:65%; animation-delay:6s">🌷</div>
    <div class="flower" style="left:75%; animation-delay:2s">🌻</div>
    <div class="flower" style="left:85%; animation-delay:4s">🌸</div>
    <div class="flower" style="left:95%; animation-delay:1s">🌹</div>
    """, 
    unsafe_allow_html=True
)


if st.button('إغلاق الظرف ↩️'):
        st.session_state.opened = False
        st.rerun()
