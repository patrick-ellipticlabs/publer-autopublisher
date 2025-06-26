
import streamlit as st
import requests
import json
from datetime import datetime

st.set_page_config(page_title="Publer AutoPublisher", layout="wide")
st.title("📣 Publer AutoPublisher")

st.markdown("Upload your content and schedule posts to Publer for multiple platforms.")

api_key = st.secrets.get("PUBLER_API_KEY") or st.text_input("🔐 Enter your Publer API Key", type="password")

uploaded_file = st.file_uploader("📁 Upload JSON Content File", type="json")

if uploaded_file and api_key:
    content = json.load(uploaded_file)
    st.success(f"Loaded {len(content)} post(s) from file.")

    for idx, post in enumerate(content):
        st.subheader(f"📝 Post {idx + 1}: {post['title']}")
        st.write(f"📅 Schedule: {post['schedule']}")
        st.write("🖼️ Media:", post.get("media", "None"))
        for platform in post["platforms"]:
            caption = post["captions"].get(platform, "")
            st.markdown(f"**{platform}**: {caption}")

        if st.button(f"🚀 Publish Post {idx + 1} to Publer", key=idx):
            for platform in post["platforms"]:
                payload = {
                    "account_id": f"PLACEHOLDER_{platform.upper()}_ID",  # Replace with real IDs
                    "caption": post["captions"].get(platform, ""),
                    "media": [post["media"]],
                    "scheduled_time": post["schedule"],
                    "status": "scheduled"
                }
                response = requests.post(
                    "https://publer.io/api/posts",
                    headers={"Authorization": f"Bearer {api_key}"},
                    json=payload
                )
                if response.status_code == 200:
                    st.success(f"{platform} post scheduled successfully.")
                else:
                    st.error(f"{platform} post failed: {response.text}")
else:
    st.info("Please upload a JSON file and enter a valid API key.")
