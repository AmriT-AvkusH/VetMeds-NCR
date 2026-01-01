import streamlit as st

st.title("🤝 Partner Registration")

tab1, tab2 = st.tabs(["👨‍⚕️ Vet Registration", "🏥 Pharmacist Registration"])

with tab1:
    st.header("Join as a Doctor")
    with st.form("vet_form"):
        c1, c2 = st.columns(2)
        c1.text_input("Dr. Name")
        c2.text_input("Experience (Years)")
        st.text_input("Clinic Address")
        st.file_uploader("Upload Degree Certificate")
        if st.form_submit_button("Register Vet"):
            st.success("Application Submitted for Verification.")

with tab2:
    st.header("Register your Pharmacy")
    with st.form("pharma_form"):
        c1, c2 = st.columns(2)
        c1.text_input("Shop Name")
        c2.text_input("Drug License No (Form 20/21)")
        st.file_uploader("Upload Drug License")
        if st.form_submit_button("Register Pharmacy"):
            st.success("Pharmacy Application Submitted.")
