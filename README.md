
# 📣 Publer AutoPublisher (v0.1)

This is a Streamlit-based app for Elliptic Labs’ marketing team to automate scheduling and posting content across multiple social media platforms using Publer.

## 🚀 Features

- Upload or input manually prepared content
- Schedule posts to LinkedIn, Facebook, Instagram, TikTok, and BlueSky
- Preview platform-specific captions
- Push to Publer via API
- Log posting activity

## ⚙️ Requirements

- Python 3.9+
- A valid Publer API key (Pro/Business tier)
- Streamlit account for hosted deployment (optional but recommended)

## 🧰 Tech Stack

- Frontend: [Streamlit](https://streamlit.io)
- Backend: Python (requests, json, datetime)
- Deployment: Streamlit Cloud or Hugging Face Spaces

## 📄 Input Format (JSON)

```json
[
  {
    "title": "Launch Day!",
    "platforms": ["LinkedIn", "Instagram", "Facebook", "TikTok", "BlueSky"],
    "media": "launch_video.mp4",
    "schedule": "2025-07-01T10:00:00Z",
    "captions": {
      "LinkedIn": "We’re live! Check out our latest innovation 🚀",
      "Instagram": "We made it! #launchday #tech",
      "Facebook": "We’re officially launched! 🔥 Watch this.",
      "TikTok": "Behind the scenes of our launch 💥",
      "BlueSky": "We're live 🚨 Come see what we’ve built!"
    }
  }
]
```

## 🧪 Setup Instructions

```bash
git clone https://github.com/ellipticlabs/publer-autopublisher.git
cd publer-autopublisher
pip install -r requirements.txt
streamlit run app.py
```

## 🔐 Environment Variables

- `PUBLER_API_KEY`: Your Publer API key
