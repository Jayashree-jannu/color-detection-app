#!/usr/bin/env python3
"""
Apply light blue and white theme matching the image with butterflies
"""

import re

def apply_blue_theme():
    # Read the current app.py
    with open('app.py', 'r') as f:
        content = f.read()
    
    # Light blue and white theme CSS
    blue_theme_css = '''
    .main > div {
        padding-top: 2rem;
    }
    .stApp {
        background: linear-gradient(135deg, #E3F2FD 0%, #F8F9FA 50%, #E1F5FE 100%);
    }
    .stSidebar {
        background: linear-gradient(180deg, #B3E5FC 0%, #E1F5FE 50%, #F3E5F5 100%) !important;
        color: #1565C0 !important;
        border-right: 1px solid rgba(21,101,192,0.2);
    }
    .stSidebar .stSelectbox > div > div {
        background-color: rgba(255,255,255,0.9);
        border-radius: 12px;
        border: 1px solid rgba(21,101,192,0.15);
        box-shadow: 0 2px 8px rgba(21,101,192,0.1);
    }
    .stSidebar .stSelectbox label {
        color: #1565C0 !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }
    .stSidebar .stTextInput label {
        color: #1565C0 !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }
    .stSidebar .stTextArea label {
        color: #1565C0 !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }
    .stSidebar .stNumberInput label {
        color: #1565C0 !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }
    .stSidebar .stSlider label {
        color: #1565C0 !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }
    .stSidebar .stCheckbox label {
        color: #1565C0 !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }
    .stSidebar .stRadio label {
        color: #1565C0 !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }
    .stSidebar .stMultiSelect label {
        color: #1565C0 !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }
    .stSidebar .stSelectbox > div > div > div {
        color: #0D47A1 !important;
    }
    .stFileUploader > div {
        background: linear-gradient(135deg, #B3E5FC 0%, #E1F5FE 100%);
        border-radius: 20px;
        padding: 1.5rem;
        color: #1565C0;
        box-shadow: 0 8px 25px rgba(21,101,192,0.2);
        border: 1px solid rgba(21,101,192,0.2);
        transition: all 0.3s ease;
    }
    .stFileUploader > div:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(21,101,192,0.3);
    }
    .stButton > button {
        background: linear-gradient(135deg, #42A5F5 0%, #1E88E5 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        box-shadow: 0 6px 20px rgba(66,165,245,0.3);
        transition: all 0.3s ease;
        border: 1px solid rgba(30,136,229,0.2);
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(66,165,245,0.4);
        background: linear-gradient(135deg, #1E88E5 0%, #42A5F5 100%);
    }
    .stSidebar .stButton > button {
        background: linear-gradient(135deg, #42A5F5 0%, #1E88E5 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 1rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 6px 20px rgba(66,165,245,0.3);
        transition: all 0.3s ease;
        width: 100%;
        border: 1px solid rgba(30,136,229,0.2);
    }
    .stSidebar .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(66,165,245,0.4);
        background: linear-gradient(135deg, #1E88E5 0%, #42A5F5 100%);
    }
    .stSidebar .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #29B6F6 0%, #0288D1 100%);
        box-shadow: 0 6px 20px rgba(41,182,246,0.4);
        border: 1px solid rgba(2,136,209,0.2);
    }
    .stSidebar .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #0288D1 0%, #29B6F6 100%);
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(41,182,246,0.5);
    }
    .stInfo {
        background: linear-gradient(135deg, #E8F5E8 0%, #C8E6C9 100%);
        border-radius: 20px;
        border: 1px solid rgba(76,175,80,0.3);
        color: #1B5E20;
        box-shadow: 0 8px 25px rgba(76,175,80,0.2);
        padding: 1rem;
    }
    .stSuccess {
        background: linear-gradient(135deg, #E8F5E8 0%, #C8E6C9 100%);
        border-radius: 20px;
        border: 1px solid rgba(76,175,80,0.3);
        color: #1B5E20;
        box-shadow: 0 8px 25px rgba(76,175,80,0.2);
        padding: 1rem;
    }
    .stWarning {
        background: linear-gradient(135deg, #FFF3E0 0%, #FFE0B2 100%);
        border-radius: 20px;
        border: 1px solid rgba(255,152,0,0.3);
        color: #E65100;
        box-shadow: 0 8px 25px rgba(255,152,0,0.2);
        padding: 1rem;
    }
    .stError {
        background: linear-gradient(135deg, #FFEBEE 0%, #FFCDD2 100%);
        border-radius: 20px;
        border: 1px solid rgba(244,67,54,0.3);
        color: #B71C1C;
        box-shadow: 0 8px 25px rgba(244,67,54,0.2);
        padding: 1rem;
    }
    .stSidebar .stMarkdown {
        color: #1565C0 !important;
    }
    .stSidebar .stMarkdown h1,
    .stSidebar .stMarkdown h2,
    .stSidebar .stMarkdown h3,
    .stSidebar .stMarkdown h4,
    .stSidebar .stMarkdown h5,
    .stSidebar .stMarkdown h6 {
        color: #1565C0 !important;
        font-weight: 700;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }
    .stSidebar .stMarkdown p {
        color: #1976D2 !important;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.3);
    }
    .stMarkdown h1,
    .stMarkdown h2,
    .stMarkdown h3,
    .stMarkdown h4,
    .stMarkdown h5,
    .stMarkdown h6 {
        color: #1565C0 !important;
        font-weight: 600;
    }
    .stMarkdown p {
        color: #1976D2 !important;
    }
    /* Enhanced container styling for history and about sections */
    .stContainer {
        background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
        border-radius: 20px;
        border: 1px solid rgba(21,101,192,0.2);
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(21,101,192,0.1);
    }
    /* Enhanced caption styling */
    .stCaption {
        background: rgba(255,255,255,0.9);
        border-radius: 8px;
        padding: 0.5rem;
        border: 1px solid rgba(21,101,192,0.1);
        color: #1565C0;
    }
    .blinking {
        animation: blink 1.5s infinite;
    }
    
    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0.3; }
    }'''
    
    # Replace the existing CSS
    css_pattern = r'<style>.*?</style>'
    new_css = f'<style>{blue_theme_css}</style>'
    content = re.sub(css_pattern, new_css, content, flags=re.DOTALL)
    
    # Update the main title section to match the blue theme
    title_pattern = r'<div style="background: linear-gradient\(45deg, #e74c3c, #f39c12, #27ae60, #8e44ad, #2c3e50\);.*?</div>'
    new_title = '''<div style="background: linear-gradient(135deg, #B3E5FC 0%, #E1F5FE 50%, #F3E5F5 100%); 
            background-size: 400% 400%; 
            animation: gradient 15s ease infinite;
            padding: 1.5rem; 
            border-radius: 20px; 
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 8px 25px rgba(21,101,192,0.3);
            border: 1px solid rgba(21,101,192,0.2);">
    <h2 style="color: #1565C0; margin: 0; text-shadow: 2px 2px 4px rgba(255,255,255,0.5); font-family: 'Playfair Display', 'Georgia', serif; font-weight: 400; letter-spacing: 0.8px; font-size: 1.8rem;">
        🎨 Spot the Shade
    </h2>
    <p style="color: #1976D2; margin: 0.5rem 0 0 0; font-size: 1.1rem; text-shadow: 1px 1px 2px rgba(255,255,255,0.3); font-family: 'Crimson Text', 'Georgia', serif; font-style: italic;">
        Discover colors with precision and beauty
    </p>
</div>'''
    content = re.sub(title_pattern, new_title, content, flags=re.DOTALL)
    
    # Update the footer section to match the blue theme
    footer_pattern = r'<div style="text-align: center; padding: 2rem; background: linear-gradient\(135deg, #6B46C1 0%, #8B5CF6 50%, #A855F7 100%\);.*?</div>'
    new_footer = '''<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #B3E5FC 0%, #E1F5FE 50%, #F3E5F5 100%); 
                   border-radius: 20px; margin-top: 2rem; box-shadow: 0 8px 25px rgba(21,101,192,0.3); border: 1px solid rgba(21,101,192,0.2);">
           <h3 style="color: #1565C0; margin: 0; text-shadow: 2px 2px 4px rgba(255,255,255,0.5);">
               ✨ Spot the Shade
           </h3>
           <p style="color: #1976D2; margin: 0.5rem 0 0 0; font-size: 1.1rem; text-shadow: 1px 1px 2px rgba(255,255,255,0.3);">
               colour detecting tool
           </p>
           <p style="color: #1976D2; margin: 0.5rem 0 0 0; font-size: 0.9rem; text-shadow: 1px 1px 2px rgba(255,255,255,0.3);">
               Made with ❤️ for designers and color enthusiasts
           </p>
       </div>'''
    content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL)
    
    # Write the updated content back to app.py
    with open('app.py', 'w') as f:
        f.write(content)
    
    print("✅ Applied beautiful light blue and white theme!")
    print("🎨 Navigation: Light blue gradient with subtle borders")
    print("💙 Main title: Light blue gradient matching navigation")
    print("🦋 Footer: Light blue gradient with matching colors")
    print("✨ Serene, ethereal appearance like the butterfly image")

if __name__ == "__main__":
    apply_blue_theme()
