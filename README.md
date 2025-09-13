# Spot the Shade — Color Detection App

## Features
- Upload image, click anywhere to detect color (RGB & HEX).
- Closest named color from `data/colors.csv`.
- Save picks to local SQLite history, export palettes.

## Run locally
1. python -m venv .venv && source .venv/bin/activate
2. pip install -r requirements.txt
3. python db_init.py
4. streamlit run app.py

## Deploy
Push your repository to GitHub, then deploy to Streamlit Community Cloud following:
https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app

## Project Structure
```
spot-the-shade/
├── app.py                 # Main Streamlit application
├── db_init.py            # Database initialization
├── requirements.txt      # Dependencies
├── data/
│   └── colors.csv       # 25 named colors database
└── uploads/             # Auto-created for image storage
```

## Dependencies
- streamlit
- streamlit-image-coordinates
- Pillow
- numpy
- pandas

## Inspiration
- [Coolors.co](https://coolors.co) - Professional palette presentation
- [Figma](https://figma.com) - Minimal color picker UI
- [ImageColorPicker.com](https://imagecolorpicker.com) - Upload → pick pixel workflow
- [streamlit-image-coordinates](https://github.com/blackary/streamlit-image-coordinates) - Click detection

---

*"Upload. Click. Know the Color."*
