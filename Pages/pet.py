import streamlit as st

st.title("🐕 Pet Health Profile")

with st.form("profile"):
    name = st.text_input("Pet Name")
    weight = st.number_input("Weight (kg)", min_value=1.0)
    breed = st.selectbox("Breed", ["Labrador", "German Shepherd", "Pug", "Indie", "Other"])
    
    if st.form_submit_button("Get Recommendations"):
        st.divider()
        st.subheader(f"Results for {name}")
        
        # Dosage Logic
        deworm_dose = weight / 10
        st.info(f"💊 **Dewormer Dose:** {deworm_dose:.1f} Tablets (Drontal Plus)")
        
        food = weight * 25
        st.success(f"🍖 **Food Intake:** Approx {food} grams/day")
        
        st.caption("Disclaimer: AI suggestions. Consult a vet for critical issues.")