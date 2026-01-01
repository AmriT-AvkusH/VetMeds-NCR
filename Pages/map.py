import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("📍 Vet Network Map")

# --- DATA ---
data = pd.DataFrame({
    'lat': [28.6139, 28.5355, 28.7041],
    'lon': [77.2090, 77.3910, 77.1025],
    'name': ['Govt Vet Hospital (Delhi)', 'Noida Pet Clinic (Pvt)', 'Pitampura Doggy World'],
    'type': ['Govt', 'Private', 'Private']
})

# --- FILTERS ---
choice = st.radio("Filter:", ["All", "Govt Only", "Private Only"], horizontal=True)

# --- MAP LOGIC ---
m = folium.Map(location=[28.61, 77.23], zoom_start=11)

for i, row in data.iterrows():
    if choice == "Govt Only" and row['type'] != 'Govt': continue
    if choice == "Private Only" and row['type'] != 'Private': continue
    
    color = "blue" if row['type'] == 'Govt' else "green"
    folium.Marker(
        [row['lat'], row['lon']], 
        popup=row['name'],
        icon=folium.Icon(color=color)
    ).add_to(m)

st_folium(m, width=800, height=500)