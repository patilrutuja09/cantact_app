import requests
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Contact Info", page_icon="🐙")

st.title("Contact Info")

if st.button("Get Contact Info"):
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        user_info = []

        for user in data:
            user_info.append({
                "ID": user["id"],
                "Name": user["name"],
                "Email": user["email"],
                "Website": user["website"]
            })

        df = pd.DataFrame(user_info)

        st.subheader("User Contact Information")
        st.dataframe(df, use_container_width=True)

    else:
        st.error("Failed to retrieve data.")




# def main():
#     url = "https://jsonplaceholder.typicode.com/users"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         for user in data:
#             print(f"id:{user['id']} Name: {user['name']}, Email: {user['email']}, ")
#     else:
#         print("Failed to retrieve data from GitHub API.")
# if __name__ == "__main__":9
#     main()

  
