import streamlit as st

# 1. SETUP PAGE CONFIGURATION
st.set_page_config(page_title="VetMeds NCR", page_icon="🐾", layout="wide")

# 2. DEFINE PAGES
# User Services
dashboard = st.Page("pages/dashboard.py", title="Home & Login", icon="🏠", default=True)
buy_page = st.Page("pages/buy.py", title="Buy Medicines", icon="🛒")
consult_page = st.Page("pages/consult.py", title="Video Consultation", icon="📹")
pet_page = st.Page("pages/pet.py", title="Pet Health Profile", icon="🐕")

# Admin/Partner Side
map_page = st.Page("pages/map.py", title="Hospital Network Map", icon="📍")
partner_page = st.Page("pages/partners.py", title="Partner Registration", icon="🤝")
delivery_page = st.Page("pages/delivery.py", title="Rider Logistics", icon="🛵")

# 3. NAVIGATION STRUCTURE
pg = st.navigation({
    "User Services": [dashboard, buy_page, consult_page, pet_page],
    "Network & Partners": [map_page, partner_page, delivery_page]
})

# 4. RUN NAVIGATION
pg.run()