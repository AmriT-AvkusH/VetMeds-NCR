import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time

# --- HELPER FUNCTION TO LOAD LOTTIE ANIMATIONS ---
# This function fetches the animation JSON from a URL dynamically.
@st.cache_data # Cache data to prevent reloading on every interaction
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def show_dashboard():
    # --- LOAD ANIMATIONS ASSETS (Professional 3D Style) ---
    # These URLs are premium-style, clean 3D animations
    lottie_dog = load_lottieurl("https://lottie.host/a189b40d-5913-4787-982e-815310665165/9G9G9G9G9G.json") # Placeholder UUID for a clean 3D dog
    # Using generic high quality ones for demonstration:
    lottie_dog_real = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_xhzgplj6.json") # Cute 3D dog
    lottie_cat = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_zyu0q7qb.json") # Playful 3D cat
    lottie_cow = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_k08g3m1c.json") # Friendly 3D cow
    lottie_goat = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_syj3y3.json") # Farm animal/Goat style

    # --- SIDEBAR LOGIN (Kept identical to before) ---
    with st.sidebar:
        st.header("👤 User Login")
        if 'user' not in st.session_state:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                if username and password == "admin": # Simple demo password
                    st.session_state.user = username
                    st.toast(f"Welcome back, {username}!", icon="🎉")
                    time.sleep(1)
                    st.rerun()
                elif username:
                     st.error("Invalid password (Try 'admin')")
        else:
            st.success(f"Hi, {st.session_state.user}!")
            if st.button("Logout", type="primary"):
                del st.session_state.user
                st.rerun()

    # --- MAIN CONTENT ---
    st.title("VetMeds NCR 🐾")
    st.markdown("### The Complete Pet Healthcare Superapp")

    # --- THE 3D ANIMATION HERO SECTION ---
    # This creates the professional, moving banner
    with st.container():
        anim_col1, anim_col2, anim_col3, anim_col4 = st.columns(4)
        
        with anim_col1:
             if lottie_dog_real:
                 st_lottie(lottie_dog_real, height=150, key="dog")
             else: st.write("🐕") # Fallback

        with anim_col2:
             if lottie_cat:
                 st_lottie(lottie_cat, height=150, key="cat")
             else: st.write("🐈")

        with anim_col3:
             if lottie_cow:
                st_lottie(lottie_cow, height=150, key="cow")
             else: st.write("🐄")

        with anim_col4:
             if lottie_goat:
                 st_lottie(lottie_goat, height=150, key="goat")
             else: st.write("🐐")
            
    st.divider()
    
    # Emergency Banner
    st.error("🚑 **Emergency?** Call 24/7 Animal Ambulance: **1962**")

    # Quick Action Grid (Tata 1mg Style)
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        with st.container(border=True):
            st.markdown("### 💊 Pharmacy")
            st.caption("Flat 20% off on Medicines")
            if st.button("Order Now", use_container_width=True):
                st.switch_page("pages/buy.py")

    with c2:
        with st.container(border=True):
            st.markdown("### 📹 Consult Vet")
            st.caption("Video Call in 5 mins")
            if st.button("Book Doctor", use_container_width=True):
                st.switch_page("pages/consult.py")

    with c3:
        with st.container(border=True):
            st.markdown("### 🐕 Pet Profile")
            st.caption("Manage Dosages & Diet")
            if st.button("View Profile", use_container_width=True):
                st.switch_page("pages/pet.py")
    
    with c4:
        with st.container(border=True):
            st.markdown("### 📍 Find Vet")
            st.caption("Govt & Pvt Hospitals")
            if st.button("Open Map", use_container_width=True):
                st.switch_page("pages/map.py")

    st.divider()
    # Using a cleaner, professional footer image
    st.image("https://img.freepik.com/free-vector/veterinarians-taking-care-pets_23-2148533585.jpg?w=1380&t=st=1715528000~exp=1715528600~hmac=10c23729950928617437620327171439", caption="Trusted by 10,000+ Pet Parents in NCR | Professional Care", use_container_width=True)

show_dashboard()
