import streamlit as st

st.set_page_config(page_title="Partner Login", page_icon="👨‍⚕️")

st.title("👨‍⚕️ Partner Dashboard")
st.write("Join the VetMeds network to increase your sales.")

tabs = st.tabs(["Login", "New Registration", "Data Collection"])

with tabs[0]:
    st.text_input("License ID / Mobile")
    st.text_input("Password", type="password")
    st.button("Login")

with tabs[1]:
    st.markdown("### Register New Pharmacy")
    with st.form("reg_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Shop Name")
            st.text_input("Owner Name")
            st.text_input("Mobile Number")
        with col2:
            st.text_input("Drug License No (Form 20/21)")
            st.text_input("GST Number")
            st.text_input("Shop Area (e.g., Lajpat Nagar)")
        
        st.file_uploader("Upload Drug License Copy")
        submitted = st.form_submit_button("Submit for Verification")
        if submitted:
            st.success("Application received! Our compliance team will visit you shortly.")

with tabs[2]:
    st.info("ADMIN USE ONLY: Manufacturer Data Entry")
    # This is where your team would manually enter data collected from the web
    st.text_area("Paste Data (JSON/CSV format)")
    st.button("Parse & Upload to DB")
