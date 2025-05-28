import streamlit as st
import pandas as pd
import random

# Mock address generator
def generate_mock_addresses(zip_code, count=10):
    streets = ["Orange Ave", "Colonial Dr", "Kirkman Rd", "Conroy Rd", "Semoran Blvd"]
    types = ["Residential", "Commercial"]
    addresses = []
    for i in range(count):
        number = random.randint(100, 9999)
        street = random.choice(streets)
        address = f"{number} {street}, Orlando, FL {zip_code}"
        addr_type = random.choice(types)
        addresses.append({"address": address, "type": addr_type})
    return addresses

# Mock property owner name generator
def generate_mock_owner_name():
    first_names = ["John", "Maria", "James", "Patricia", "David", "Linda"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Mock reverse phone lookup (placeholder for real API)
def mock_lookup_phone(address):
    return f"({random.randint(200, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}"

# Full lead generator with mock phone lookup
def generate_leads_with_phone(zip_code, count=10):
    addresses = generate_mock_addresses(zip_code, count)
    leads = []
    for entry in addresses:
        owner_name = generate_mock_owner_name()
        phone = mock_lookup_phone(entry['address'])
        leads.append({
            "ZIP Code": zip_code,
            "Owner Name": owner_name,
            "Property Address": entry['address'],
            "Property Type": entry['type'],
            "Phone": phone
        })
    return pd.DataFrame(leads)

# Streamlit UI
st.title("📞 Orlando Cold Call Lead Generator")

zip_code = st.selectbox("Select ZIP Code", ["32801", "32803", "32804", "32805", "32806", "32808", "32809", "32811", "32812", "32819", "32822", "32824"])
count = st.slider("Number of Leads to Generate", 1, 100, 10)

if st.button("Generate Leads"):
    leads_df = generate_leads_with_phone(zip_code, count)
    st.write("### 📋 Generated Leads")
    st.dataframe(leads_df)

    csv = leads_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="orlando_leads.csv",
        mime="text/csv"
    )
