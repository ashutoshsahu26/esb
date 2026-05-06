import streamlit as st
from st_supabase_connection import SupabaseConnection

# Page configuration
st.set_page_config(page_title="Data Portal", layout="wide")

# Initialize connection
# On Render, this will automatically look for SUPABASE_URL and SUPABASE_KEY 
# in the Environment Variables you set in the dashboard.
conn = st.connection("supabase", type=SupabaseConnection)

def main():
    st.title("📊 Database Management Portal")
    st.markdown("---")

    # Sidebar for navigation or status
    st.sidebar.header("Connection Status")
    st.sidebar.success("Connected to Supabase")

    # Main area: Data Retrieval
    try:
        # Replace 'your_table_name' with the actual table name in your Supabase DB
        # ttl="0" ensures you see fresh data without caching during testing
        res = conn.query("*", table="your_table_name", ttl="0").execute()
        
        st.subheader("📋 Table Records")
        if res.data:
            st.dataframe(res.data, use_container_width=True)
        else:
            st.info("Connected, but no records found in this table.")

    except Exception as e:
        st.error(f"Error fetching data: {e}")
        st.info("Check if your table name is correct and permissions (RLS) are set.")

    # Data Entry Section
    st.markdown("---")
    st.subheader("➕ Add New Record")
    
    with st.form("entry_form", clear_on_submit=True):
        # Change these fields to match your table columns
        item_name = st.text_input("Entry Name")
        item_description = st.text_area("Description")
        
        submitted = st.form_submit_button("Save to Database")
        
        if submitted:
            if item_name:
                try:
                    new_row = {"name": item_name, "description": item_description}
                    conn.table("your_table_name").insert(new_row).execute()
                    st.success("Successfully saved!")
                    st.rerun() # Refresh to show the new data in the table
                except Exception as e:
                    st.error(f"Error saving data: {e}")
            else:
                st.warning("Please enter a name.")

if __name__ == "__main__":
    main()
