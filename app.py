import streamlit as st
import json
import os

# --- 1. Load the Data ---
# We use @st.cache_data so it only reads the JSON file once to save memory
@st.cache_data
def load_data():
    if not os.path.exists('reaction_data.json'):
        return []
    with open('reaction_data.json', 'r') as file:
        return json.load(file)

data = load_data()

# --- 2. Build the UI ---
st.set_page_config(page_title="Chemical Reaction Database", page_icon="🧪")
st.title("🧪 Chemical Reaction Database")

if not data:
    st.error("❌ 'reaction_data.json' not found. Please ensure it is in the same folder as this app.")
else:
    st.write("Select your chemical parameters below to predict the main product.")
    st.divider()

    # --- 3. Dynamically Extract Dropdown Options ---
    # This grabs all unique values from the JSON and capitalizes them nicely
    reactants = sorted(list(set([r['reactant'].title() for r in data])))
    
    # Capitalize acids/bases properly (e.g., hcl -> HCl)
    reagents = sorted(list(set([r['reagent'].upper() if len(r['reagent']) <= 5 else r['reagent'].title() for r in data])))
    
    concentrations = sorted(list(set([r['concentration'].title() for r in data])))
    temps = sorted(list(set([r['temp'].title() for r in data])))

    # --- 4. The Input Form (Using Columns for layout) ---
    col1, col2 = st.columns(2)
    
    with col1:
        u_react = st.selectbox("Reactant (Metal/Element):", options=reactants)
        u_reag = st.selectbox("Acid/Base (Reagent):", options=reagents)
        
    with col2:
        u_c = st.selectbox("Concentration:", options=concentrations)
        u_t = st.selectbox("Temperature:", options=temps)

    st.divider()

    # --- 5. The Search Logic ---
    if st.button("Check Reaction", type="primary", use_container_width=True):
        
        # Convert user selections back to lowercase to match the JSON database
        search_react = u_react.lower()
        search_reag = u_reag.lower()
        search_c = u_c.lower()
        search_t = u_t.lower()

        found = False
        
        # Scan the database for a match
        for reaction in data:
            if (reaction["reactant"] == search_react and 
                reaction["reagent"] == search_reag and 
                reaction["concentration"] == search_c and 
                reaction["temp"] == search_t):
                
                st.success(f"### Resulting Product: **{reaction['main_product']}**")
                found = True
                break # Stop searching once we find it
        
        # If the loop finishes and nothing was found
        if not found:
            st.warning("⚠️ No reaction found for these specific conditions in the database. Try adjusting the temperature or concentration.")