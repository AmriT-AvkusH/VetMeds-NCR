import streamlit as st

def show_dashboard():
    # --- SIDEBAR LOGIN SIMULATION ---
    with st.sidebar:
        st.header("👤 User Login")
        if 'user' not in st.session_state:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                if username:  # Simple check
                    st.session_state.user = username
                    st.success(f"Logged in as {username}")
                    st.rerun()
        else:
            st.success(f"Welcome, {st.session_state.user}!")
            if st.button("Logout"):
                del st.session_state.user
                st.rerun()

    # --- MAIN CONTENT ---
    st.title("VetMeds NCR 🐾")
    st.markdown("### Your Complete Pet Healthcare Superapp")
    
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
    st.image("https://img.freepik.com/free-vector/veterinary-clinic-concept-illustration_114360-3023.jpg?w=1380", caption="Trusted by 10,000+ Pet Parents in NCR", use_container_width=True)

show_dashboard()
