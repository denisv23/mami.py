import streamlit as st
import random

# Konfigurimi i faqes
st.set_page_config(page_title="Për Mamin", page_icon="❤️")

# CSS për të stiluar butonat si zemra të mëdha dhe për animacionin e zemrave që bien
st.markdown("""
    <style>
    /* Bën butonin të duket thjesht si një emoji i madh */
    .stButton>button {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        font-size: 120px !important; 
        padding: 0;
        display: flex;
        margin: auto;
        transition: transform 0.2s;
        line-height: 1;
    }
    .stButton>button:hover {
        transform: scale(1.1);
    }
    /* Shkrimi i fundit "TË DUA MAMI" */
    .te-dua-mami {
        font-size: 70px;
        color: #ff4b4b;
        text-align: center;
        font-weight: bold;
        margin-top: 50px;
        animation: fadeIn 2s ease-in;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    /* Animacioni i zemrave qe bien ne hapin e fundit */
    .falling-heart {
        position: fixed;
        top: -10%;
        font-size: 30px;
        animation: fall linear infinite;
        z-index: 999;
    }
    @keyframes fall {
        to {
            transform: translateY(110vh);
        }
    }
    </style>
""", unsafe_allow_html=True)

# Inicializojmë gjendjen e hapave
if 'hapi' not in st.session_state:
    st.session_state.hapi = 0

def kalo_ne_hapin_1():
    st.session_state.hapi = 1

def kalo_ne_hapin_2():
    st.session_state.hapi = 2

# ----------------------------------------
# HAPI 0: Vetëm zemra e madhe në qendër
# ----------------------------------------
if st.session_state.hapi == 0:
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.button("❤️", key="zemer_madhe", on_click=kalo_ne_hapin_1)
    st.markdown("<p style='text-align: center; color: gray; font-size: 20px;'>Kliko zemrën</p>", unsafe_allow_html=True)

# ----------------------------------------
# HAPI 1: Fjalimi i bukur dhe zemra në fund
# ----------------------------------------
elif st.session_state.hapi == 1:
    st.markdown("<h1 style='text-align: center; color: #d63384;'>Gëzuar 8 Marsin! 🌸</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Fjalimi për mamin
    st.markdown("""
    <div style='font-size: 22px; text-align: center; line-height: 1.6;'>
    E dashur Mami,<br><br>
    Sot është dita jote, por për mua ti je e veçantë çdo ditë të vitit. <br>
    Faleminderit për dashurinë e pakushtëzuar, për durimin tënd të pafund, 
    dhe për çdo sakrificë që ke bërë për të më parë të lumtur.<br><br>
    Ti je forca ime, mbështetja ime më e madhe dhe drita që më udhëheq në çdo hap. 
    Asnjë fjalë nuk mund ta përshkruajë sa shumë të dua dhe sa me fat jam që të kam.<br><br>
    Të uroj një ditë sa më të bukur, ashtu siç e ke shpirtin tënd!
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # Butoni i dytë në formë zemre
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("❤️", key="zemer_e_vogel", on_click=kalo_ne_hapin_2)
    st.markdown("<p style='text-align: center; color: gray;'>Kliko sërish</p>", unsafe_allow_html=True)

# ----------------------------------------
# HAPI 2: Zemrat që bien dhe mesazhi i madh
# ----------------------------------------
elif st.session_state.hapi == 2:
    # Krijojmë efektin e zemrave që bien me HTML/CSS
    zemrat_html = ""
    for _ in range(40): # 40 zemra në ekran
        left_pos = random.randint(0, 100)
        kohëzgjatja = random.uniform(3, 6)
        vonesa = random.uniform(0, 4)
        zemrat_html += f"<div class='falling-heart' style='left: {left_pos}%; animation-duration: {kohëzgjatja}s; animation-delay: {vonesa}s;'>❤️</div>"
    
    st.markdown(zemrat_html, unsafe_allow_html=True)
    
    # Shkrimi i madh
    st.markdown("<div class='te-dua-mami'>TË DUA MAMI!</div>", unsafe_allow_html=True)
    
    # Shtojmë edhe tullumbacet e Streamlit për ekstra atmosferë
    st.balloons()
