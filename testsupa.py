import streamlit as st
from st_supabase_connection import SupabaseConnection

st.set_page_config(page_title="Supabase Viewer...")

# Initialize connection
conn = st.connection("supabase", type=SupabaseConnection)

def main():
    st.title("📋 Supabase Table Records:")
    
    try:
        # Use conn.table() directly if the library version supports it, 
        # or use conn.client for the standard Supabase syntax.
        # This is the most reliable way to fetch all rows:
        response = conn.table("test").select("*").execute()

        if response.data:
            st.success(f"Found {len(response.data)} rows in the 'test' table.")
            st.dataframe(response.data, use_container_width=True)
        else:
            st.info("The 'test' table is empty...")

    except AttributeError:
        # Fallback if the wrapper structure is different in your environment
        st.error("Connection attribute error. Trying fallback method...")
        try:
            response = conn.client.table("test").select("*").execute()
            st.dataframe(response.data)
        except Exception as e:
            st.error(f"Fallback failed: {e}")
            
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
