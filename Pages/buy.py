import streamlit as st
import time
import random

st.set_page_config(page_title="Shop", page_icon="🛒", layout="wide")

# --- LOGIN CHECK ---
if 'user' not in st.session_state:
    st.error("🔒 Please Login on the Home Page first.")
    if st.button("Go to Login"):
        st.switch_page("pages/dashboard.py")
    st.stop()

# --- INITIALIZE CART ---
if 'cart' not in st.session_state:
    st.session_state.cart = []

# --- 50+ REAL PRODUCTS DATABASE (INDIA MARKET) ---
products = [
    # === MEDICINES (DOGS & CATS) ===
    {"id": 101, "name": "Bravecto Chewable (20-40kg)", "cat": "Medicine", "price": 2150, "mrp": 2400, "rx": True, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Kills ticks & fleas for 12 weeks. Single Dose."},
    {"id": 102, "name": "NexGard Spectra (15-30kg)", "cat": "Medicine", "price": 1850, "mrp": 2100, "rx": True, "img": "https://m.media-amazon.com/images/I/71Yy+e7t+nL._AC_UF1000,1000_QL80_.jpg", "desc": "Tick, Flea & Deworming Tablet."},
    {"id": 103, "name": "Drontal Plus (Dewormer)", "cat": "Medicine", "price": 140, "mrp": 160, "rx": False, "img": "https://m.media-amazon.com/images/I/61f5X3+l-cL._AC_UF1000,1000_QL80_.jpg", "desc": "Effective against tapeworms & roundworms."},
    {"id": 104, "name": "Meloxicam Oral Suspension", "cat": "Medicine", "price": 85, "mrp": 120, "rx": True, "img": "https://5.imimg.com/data5/SELLER/Default/2023/7/326444837/OI/QW/SR/3496338/meloxicam-oral-suspension-bp-500x500.jpg", "desc": "Pain relief for arthritis/injury."},
    {"id": 105, "name": "CiproVet Eye Drops", "cat": "Medicine", "price": 70, "mrp": 95, "rx": True, "img": "https://m.media-amazon.com/images/I/51pT2zO+m4L._AC_UF1000,1000_QL80_.jpg", "desc": "Antibiotic eye drops for infections."},
    {"id": 106, "name": "Himalaya Immunol Liquid", "cat": "Medicine", "price": 142, "mrp": 160, "rx": False, "img": "https://m.media-amazon.com/images/I/61X-wB+3VIL._AC_UF1000,1000_QL80_.jpg", "desc": "Immunity booster for dogs & cats."},
    {"id": 107, "name": "Digyton Drops (30ml)", "cat": "Medicine", "price": 110, "mrp": 130, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Digestive stimulant for puppies."},
    {"id": 108, "name": "Savavet Safeheart 5mg", "cat": "Medicine", "price": 645, "mrp": 700, "rx": True, "img": "https://m.media-amazon.com/images/I/51+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Cardiac support medicine."},
    {"id": 109, "name": "Candid Ear Drops", "cat": "Medicine", "price": 150, "mrp": 180, "rx": False, "img": "https://m.media-amazon.com/images/I/41+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Anti-fungal ear drops."},
    {"id": 110, "name": "Betadine Solution (100ml)", "cat": "Medicine", "price": 120, "mrp": 140, "rx": False, "img": "https://m.media-amazon.com/images/I/51+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Antiseptic for minor wounds."},
    {"id": 111, "name": "Vetoquinol Samfur Powder", "cat": "Medicine", "price": 188, "mrp": 214, "rx": False, "img": "https://m.media-amazon.com/images/I/51+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Skin & coat supplement."},
    {"id": 112, "name": "ClearKill Spot On (10-20kg)", "cat": "Medicine", "price": 582, "mrp": 647, "rx": True, "img": "https://m.media-amazon.com/images/I/51+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Topical flea & tick remover."},

    # === DOG FOOD ===
    {"id": 201, "name": "Royal Canin Puppy (3kg)", "cat": "Dog Food", "price": 2150, "mrp": 2800, "rx": False, "img": "https://m.media-amazon.com/images/I/71I2P-2dFQL._AC_UF1000,1000_QL80_.jpg", "desc": "Starter food for small breed puppies."},
    {"id": 202, "name": "Royal Canin Maxi Adult (4kg)", "cat": "Dog Food", "price": 3100, "mrp": 3400, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "For large dogs (German Shepherd/Lab)."},
    {"id": 203, "name": "Drools Chicken & Egg (3kg)", "cat": "Dog Food", "price": 782, "mrp": 849, "rx": False, "img": "https://m.media-amazon.com/images/I/71w+e8w+GEL._AC_UF1000,1000_QL80_.jpg", "desc": "Adult dog food, high protein."},
    {"id": 204, "name": "Pedigree Adult Chicken (10kg)", "cat": "Dog Food", "price": 1984, "mrp": 2390, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Complete balanced diet."},
    {"id": 205, "name": "Farmina N&D Grain Free (800g)", "cat": "Dog Food", "price": 1600, "mrp": 1800, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Premium grain-free pumpkin & chicken."},
    {"id": 206, "name": "Chappi Adult Dog Food (3kg)", "cat": "Dog Food", "price": 450, "mrp": 500, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Economical complete food."},
    {"id": 207, "name": "Drools Vet Pro Obesity (3kg)", "cat": "Dog Food", "price": 1499, "mrp": 1600, "rx": True, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Prescription diet for weight loss."},
    {"id": 208, "name": "Himalaya Healthy Pet Food (1.2kg)", "cat": "Dog Food", "price": 350, "mrp": 400, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Meat & Rice formula."},
    {"id": 209, "name": "Pedigree Wet Gravy Pouch (12pk)", "cat": "Dog Food", "price": 540, "mrp": 600, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Chicken chunks in gravy."},
    {"id": 210, "name": "Canine Creek Starter (4kg)", "cat": "Dog Food", "price": 2150, "mrp": 2300, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Ultra premium starter."},

    # === CAT FOOD ===
    {"id": 301, "name": "Whiskas Tuna Adult (1.2kg)", "cat": "Cat Food", "price": 428, "mrp": 450, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Dry food for cats 1+ years."},
    {"id": 302, "name": "Whiskas Wet Jelly (12 Pack)", "cat": "Cat Food", "price": 510, "mrp": 600, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Tuna in Jelly wet food."},
    {"id": 303, "name": "Me-O Persian Cat Food (1.1kg)", "cat": "Cat Food", "price": 440, "mrp": 500, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Anti-hairball formula."},
    {"id": 304, "name": "Royal Canin Persian Adult (2kg)", "cat": "Cat Food", "price": 1800, "mrp": 2100, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Special kibble for flat faces."},
    {"id": 305, "name": "Sheba Rich Wet Food (12pk)", "cat": "Cat Food", "price": 582, "mrp": 600, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Maguro & Bream premium wet food."},
    {"id": 306, "name": "PurePet Ocean Fish (7kg)", "cat": "Cat Food", "price": 999, "mrp": 1200, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Economical dry cat food."},
    {"id": 307, "name": "Whiskas Kitten Mackerel (1.1kg)", "cat": "Cat Food", "price": 404, "mrp": 425, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "For kittens 2-12 months."},
    
    # === TREATS ===
    {"id": 401, "name": "Pedigree Dentastix (Medium)", "cat": "Treats", "price": 199, "mrp": 210, "rx": False, "img": "https://m.media-amazon.com/images/I/61w+3+7+GEL._AC_UF1000,1000_QL80_.jpg", "desc": "Daily oral care chews."},
    {"id": 402, "name": "Drools Calcium Bones (190g)", "cat": "Treats", "price": 199, "mrp": 220, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Calcium supplement treats."},
    {"id": 403, "name": "Chip Chops Chicken Diced", "cat": "Treats", "price": 210, "mrp": 245, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "High value training treats."},
    {"id": 404, "name": "Gnawlers Calcium Stick", "cat": "Treats", "price": 150, "mrp": 180, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Long lasting chew stick."},
    {"id": 405, "name": "JerHigh Strawberry Stick", "cat": "Treats", "price": 230, "mrp": 250, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Soft fruity treat."},
    {"id": 406, "name": "Temptations Cat Treat (Tuna)", "cat": "Treats", "price": 130, "mrp": 150, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Crunchy outside, soft inside."},
    {"id": 407, "name": "Himalaya Dog Biscuits", "cat": "Treats", "price": 120, "mrp": 140, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Healthy digestive biscuits."},
    {"id": 408, "name": "HUFT Yakies Chew Bone (L)", "cat": "Treats", "price": 255, "mrp": 269, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Hard cheese chew (Churpi)."},
    {"id": 409, "name": "Goodies Spiral Stick", "cat": "Treats", "price": 180, "mrp": 200, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Dental spiral chew."},
    {"id": 410, "name": "Kennel Kitchen Chicken Jerky", "cat": "Treats", "price": 299, "mrp": 350, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Real dried chicken strips."},

    # === ACCESSORIES ===
    {"id": 501, "name": "Nylon Leash (Red, 1 Inch)", "cat": "Accessories", "price": 373, "mrp": 450, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Durable nylon leash."},
    {"id": 502, "name": "Padded Dog Harness (L)", "cat": "Accessories", "price": 1125, "mrp": 1500, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Reflective padded harness."},
    {"id": 503, "name": "E-Collar (Cone) Size 1", "cat": "Accessories", "price": 440, "mrp": 550, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Prevent scratching after surgery."},
    {"id": 504, "name": "Steel Feeding Bowl (Non-Tip)", "cat": "Accessories", "price": 250, "mrp": 350, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Anti-skid rubber base."},
    {"id": 505, "name": "Slicker Brush (Grooming)", "cat": "Accessories", "price": 300, "mrp": 450, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Removes loose fur."},
    {"id": 506, "name": "Pet Wipes (80 pcs)", "cat": "Accessories", "price": 399, "mrp": 500, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Alcohol free cleaning wipes."},
    {"id": 507, "name": "Retractable Leash (5M)", "cat": "Accessories", "price": 1800, "mrp": 2000, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Freedom leash for walking."},
    {"id": 508, "name": "Anti-Tick Shampoo (200ml)", "cat": "Accessories", "price": 250, "mrp": 300, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Kills ticks during bath."},
    {"id": 509, "name": "Nail Clipper", "cat": "Accessories", "price": 200, "mrp": 350, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Safety clipper for pets."},
    {"id": 510, "name": "Chew Rope Toy", "cat": "Accessories", "price": 150, "mrp": 250, "rx": False, "img": "https://m.media-amazon.com/images/I/61+y+Uo-cIL._AC_UF1000,1000_QL80_.jpg", "desc": "Cotton rope for dental health."},
]

st.title("🛒 Buy Medicines & Supplies")
st.markdown(f"**{len(products)} Quality Products Available** | Flat 20% Discount applied.")

# --- SIDEBAR FILTERS ---
with st.sidebar:
    st.header("Filters")
    cat_filter = st.radio("Category", ["All", "Medicine", "Dog Food", "Cat Food", "Treats", "Accessories"])
    search_query = st.text_input("🔍 Search", placeholder="e.g. Royal Canin, Tick...")

# --- MAIN SHOPPING GRID ---
col1, col2 = st.columns([3, 1])

with col1:
    found_items = 0
    # Loop through products and filter
    for item in products:
        # Filter Logic
        if cat_filter != "All" and item['cat'] != cat_filter:
            continue
        if search_query and search_query.lower() not in item['name'].lower():
            continue
        
        found_items += 1
        
        # DISPLAY CARD
        with st.container(border=True):
            c1, c2, c3 = st.columns([1, 2, 1])
            with c1:
                st.image(item['img'], use_container_width=True)
            with c2:
                st.subheader(item['name'])
                st.write(item['desc'])
                if item['rx']:
                    st.caption("🔴 **Prescription Required**")
                else:
                    st.caption("🟢 **No Rx Needed**")
            with c3:
                st.markdown(f"### ₹{item['price']}")
                st.caption(f"MRP: ~~₹{item['mrp']}~~")
                
                # Add Button
                if st.button("ADD +", key=f"add_{item['id']}", type="primary"):
                    st.session_state.cart.append(item)
                    st.toast(f"Added {item['name']}")

    if found_items == 0:
        st.warning("No products found matching your search.")

# --- CART SECTION (RIGHT COLUMN) ---
with col2:
    with st.container(border=True):
        st.header(f"🛍️ Cart ({len(st.session_state.cart)})")
        
        if not st.session_state.cart:
            st.info("Your cart is empty.")
        else:
            total = 0
            rx_needed = False
            
            for cart_item in st.session_state.cart:
                st.write(f"• {cart_item['name']}")
                st.caption(f"₹{cart_item['price']}")
                total += cart_item['price']
                if cart_item['rx']:
                    rx_needed = True
            
            st.divider()
            st.markdown(f"**Total: ₹{total}**")
            
            if rx_needed:
                st.warning("⚠️ Rx Upload Required")
                st.file_uploader("Upload Prescription", type=["jpg", "pdf"], key="rx_upload")
            
            if st.button("Proceed to Pay", use_container_width=True):
                with st.spinner("Processing Payment..."):
                    time.sleep(2)
                st.balloons()
                st.success(f"Order Placed! ID: #{random.randint(10000,99999)}")
                st.session_state.cart = [] # Clear cart
                time.sleep(2)
                st.rerun()