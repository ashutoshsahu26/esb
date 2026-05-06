import streamlit as st
from st_supabase_connection import SupabaseConnection

# Set up the page title
st.set_page_config(page_title="Supabase Viewer", page_icon="🔍")

# Initialize connection
# On Render, it uses the SUPABASE_URL and SUPABASE_KEY environment variables
conn = st.connection("supabase", type=SupabaseConnection)

def main():
    st.title("📋 Supabase Table Records")
    st.write("Fetching rows from the **test** table...")

    try:
        # Query all columns from the 'test' table
        # We set ttl=0 so that every refresh shows the most recent data
        res = conn.query("*", table="test", ttl=0).execute()

        # Check if data was returned
        if res.data:
            st.success(f"Successfully retrieved {len(res.data)} rows.")
            
            # Display the data in an interactive table
            st.dataframe(res.data, use_container_width=True)
        else:
            st.info("The 'test' table is currently empty.")

    except Exception as e:
        st.error("An error occurred while fetching data.")
        st.exception(e)

if __name__ == "__main__":
    main()
