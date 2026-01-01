import streamlit as st
import time

st.title("📹 Video Consultation")
st.markdown("Connect with top Vets in Delhi NCR instantly.")

# --- DOCTOR LIST ---
doctors = [
    {"name": "Dr. Sharma", "spec": "General Surgeon", "exp": "15 Yrs", "status": "Available", "fee": 500},
    {"name": "Dr. Anjali Gupta", "spec": "Dermatology (Skin)", "exp": "8 Yrs", "status": "Busy", "fee": 700},
]

col1, col2 = st.columns(2)

for doc in doctors:
    with col1 if doctors.index(doc) % 2 == 0 else col2:
        with st.container(border=True):
            st.subheader(doc['name'])
            st.write(f"**Speciality:** {doc['spec']}")
            st.write(f"**Experience:** {doc['exp']}")
            st.write(f"**Consultation Fee:** ₹{doc['fee']}")
            
            if doc['status'] == "Available":
                st.success("🟢 Available Now")
                if st.button(f"Call {doc['name']}", key=doc['name']):
                    with st.spinner("Connecting to secure video line..."):
                        time.sleep(2)
                    st.image("https://media.istockphoto.com/id/1226848601/photo/medical-webinar.jpg?s=612x612&w=0&k=20&c=L_dGqQWqgLioRdb046wTfsnC4Uo1M7wPzN17a1W6w3o=", caption="Connected")
                    st.info("Microphone and Camera active.")
            else:
                st.warning("🔴 Busy (On another call)")
