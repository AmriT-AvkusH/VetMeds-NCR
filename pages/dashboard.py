import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time

# --- 1. SETUP LOTTIE LOADER ---
@st.cache_data
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def show_dashboard():
    # --- 2. INITIALIZE TIMER ---
    # We save the exact time the user opened the app
    if 'start_time' not in st.session_state:
        st.session_state.start_time = time.time()
    
    # Calculate how many seconds have passed
    elapsed_seconds = time.time() - st.session_state.start_time
    elapsed_minutes = elapsed_seconds / 60

    # --- 3. DEFINE ANIMATION URLs ---
    # These are high-quality 3D style assets
    url_cow = "https://lottie.host/233076c8-5459-4533-8991-8884659b819a/P83F97A4N8.json" 
    url_cat_dog = "https://lottie.host/64b58f89-c454-46c0-9d8a-84cb2f8f740f/1J84G69K33.json"
    url_goat = "https://lottie.host/80860456-12c8-4796-9810-72049d6387a2/7D93J67H92.json"

    # --- 4. SIDEBAR LOGIN (Standard) ---
    with st.sidebar:
        st.header("👤 User Login")
        if 'user' not in st.session_state:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                st.session_state.user = username
                st.rerun()
        else:
            st.success(f"Hi, {st.session_state.user}!")
            # Debug tool to test animations (Optional)
            st.divider()
            if st.button("⏩ Fast Forward Time (Test)", help="Click to skip 5 mins"):
                st.session_state.start_time -= 300 # Subtract 5 mins
                st.rerun()

    # --- 5. MAIN PAGE LAYOUT ---
    st.title("VetMeds NCR 🐾")
    
    # --- THE SMART ANIMATION SECTION ---
    # This container holds the classy greeting
    with st.container(border=True):
        col_anim, col_text = st.columns([1, 2])
        
        with col_anim:
            # LOGIC: CHANGE ANIMATION BASED ON TIME
            if elapsed_minutes < 5:
                # 0 to 5 Minutes: SHOW COW
                anim_data = load_lottieurl(url_cow)
                st_lottie(anim_data, height=180, key="cow_anim")
                greeting = "Moo! Welcome to VetMeds!"
                sub_text = "I'm here to help you get started."
                
            elif elapsed_minutes < 10:
                # 5 to 10 Minutes: SHOW CAT & DOG
                anim_data = load_lottieurl(url_cat_dog)
                st_lottie(anim_data, height=180, key="catdog_anim")
                greeting = "Woof & Meow! Still here?"
                sub_text = "Check out our Pet Profile section!"
                
            else:
                # 10+ Minutes: SHOW GOAT
                anim_data = load_lottieurl(url_goat)
                st_lottie(anim_data, height=180, key="goat_anim")
                greeting = "Baa! You are the G.O.A.T!"
                sub_text = "Don't forget to book a consultation."

        with col_text:
            st.markdown(f"## {greeting}")
            st.markdown(f"### *{sub_text}*")
            st.caption(f"Session Time: {int(elapsed_minutes)} mins")
            st.progress(min(elapsed_minutes/15, 1.0)) # Visual timer bar

    # --- 6. DASHBOARD ACTIONS ---
    st.divider()
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        if st.button("💊 Pharmacy", use_container_width=True):
            st.switch_page("pages/buy.py")
    with c2:
        if st.button("📹 Consult Vet", use_container_width=True):
            st.switch_page("pages/consult.py")
    with c3:
        if st.button("🐕 Pet Profile", use_container_width=True):
            st.switch_page("pages/pet.py")
    with c4:
        if st.button("📍 Find Vet", use_container_width=True):
            st.switch_page("pages/map.py")

    st.image("https://img.freepik.com/free-vector/veterinarians-taking-care-pets_23-2148533585.jpg?w=1380", use_container_width=True)

show_dashboard()
