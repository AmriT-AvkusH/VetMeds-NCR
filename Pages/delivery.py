import streamlit as st

st.title("🛵 Rider App (Logistics)")
st.info("This panel is for Delivery Partners only.")

st.markdown("### 🔔 Active Orders")

with st.container(border=True):
    st.write("Order #9982 - **Sector 18, Noida**")
    st.write("Item: Royal Canin (3kg)")
    st.write("Earning: ₹50")
    if st.button("Accept Delivery"):
        st.balloons()
        st.success("Job Assigned! GPS Navigation Starting...")