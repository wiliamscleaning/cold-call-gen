
import streamlit as st
import pandas as pd
import random

# Mock address generator
def generate_mock_addresses(zip_code, count=10):
    streets = ["Main St", "First Ave", "Maple Dr", "Elm St", "Oak Rd"]
    types = ["residential", "commercial"]
    addresses = []
    for i in range(count):
        number = random.randint(100, 999)
        street = random.choice(streets)
        address = f"{number} {street}, ZIP {zip_code}"
        addr_type = random.choice(types)
        addresses.append({"address": address, "type": addr_type})
    return addresses

# Mock reverse lookup
def mock_reverse_lookup(address):
    first_names = ["John", "Jane", "Alex", "Chris", "Sam"]
    last_names = ["Doe", "Smith", "Brown", "Taylor", "Lee"]
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    phone = f"({random.randint(200, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}"
    return {"name": name, "phone": phone}

# Lead generator
def generate_mock_leads(zip_code, count=10):
    addresses = generate_mock_addresses(zip_code, count)
    leads = []
    for entry in addresses:
        info = mock_reverse_lookup(entry['address'])
        leads.append({
            "Address": entry['address'],
            "Type": entry['type'],
            "Name": info['name'],
            "Phone": info['phone']
        })
    return pd.DataFrame(leads)

# Streamlit UI
st.title("📞 Cold Call Lead Generator")

zip_code = st.text_input("Enter ZIP Code", "90210")
count = st.slider("Number of Leads to Generate", 1, 100, 10)

if st.button("Generate Leads"):
    leads_df = generate_mock_leads(zip_code, count)
    st.write("### 📋 Generated Leads")
    st.dataframe(leads_df)

    csv = leads_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="cold_call_leads.csv",
        mime="text/csv"
    )
