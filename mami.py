import streamlit as st
import time

# Konfigurimi i faqes
st.set_page_config(page_title="Për Mamin ❤️", page_icon="🌹")

# Stilimi me CSS për ta bërë pamjen më festive
st.markdown("""
    <style>
    .main {
        background-color: #fff5f5;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        height: 3em;
        width: 100%;
    }
    h1 {
        color: #d63384;
        text-align: center;
    }
    .stMarkdown {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Titulli kryesor
st.title("Gëzuar 8 Marsin, Mami! 🌸")

# Një imazh ose ilustrim (Mund të përdorësh një URL imazhi që të pëlqen)
st.image("https://img.freepik.com/free-vector/hand-painted-watercolor-floral-background_23-2148430134.jpg", use_column_width=True)

# Ndërveprimi
emri = st.text_input("Shkruaj emrin tënd këtu, Mami:", "")

if emri:
    st.balloons() # Efekti i tullumbaceve
    st.write(f"### Mirëseerdhe në hapësirën tënde dedikuar ty, {emri}! ✨")
    
    if st.button("Hap dhuratën tënde 🎁"):
        with st.spinner('Duke përgatitur diçka speciale...'):
            time.sleep(2)
        
        # Mesazhi Emocional
        st.success("Ti je mbretëresha e kësaj shtëpie!")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("💡 **Pse je e veçantë?**\n\n* Për durimin tënd pafund.\n* Për gatimet më të mira në botë.\n* Për përqafimin që shëron çdo gjë.")
        
        with col2:
            st.heart_box = st.markdown("## ❤️❤️❤️\n## ❤️❤️❤️")
        
        st.markdown("---")
        st.subheader("Poezi e vogël për ty:")
        st.write("""
        Në çdo hap që hedh në jetë,  
        Dritën tënde kam vërtet.  
        Me një fjalë e me një sy,  
        Bota bëhet parajsë me ty!
        """)
        
        # Një buton për t'i treguar sa shumë e do
        if st.button("Shtyp këtu për 1000 përqafime 🤗"):
            st.snow() # Efekti i dëborës/yjeve
            st.write("### U dërguan me sukses! 💌")