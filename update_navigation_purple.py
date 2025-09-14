#!/usr/bin/env python3
"""
Update navigation sidebar to purple-magenta gradient matching the image
"""

import re

def update_navigation_purple():
    # Read the current app.py
    with open('app.py', 'r') as f:
        content = f.read()
    
    # Purple-magenta gradient CSS for navigation
    purple_css = '''
    .main > div {
        padding-top: 2rem;
    }
    .stApp {
        background: #F8F9FA;
    }
    .stSidebar {
        background: linear-gradient(180deg, #8B5CF6 0%, #A855F7 50%, #C084FC 100%) !important;
        color: white !important;
        border-right: 3px solid #7C3AED;
    }
    .stSidebar .stSelectbox > div > div {
        background-color: rgba(255,255,255,0.95);
        border-radius: 12px;
        border: 2px solid #7C3AED;
        box-shadow: 0 2px 8px rgba(124,58,237,0.3);
    }
    .stSidebar .stSelectbox label {
        color: white !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    .stSidebar .stTextInput label {
        color: white !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    .stSidebar .stTextArea label {
        color: white !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    .stSidebar .stNumberInput label {
        color: white !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    .stSidebar .stSlider label {
        color: white !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    .stSidebar .stCheckbox label {
        color: white !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    .stSidebar .stRadio label {
        color: white !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    .stSidebar .stMultiSelect label {
        color: white !important;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    .stSidebar .stSelectbox > div > div > div {
        color: #4C1D95 !important;
    }
    .stFileUploader > div {
        background: linear-gradient(135deg, #8B5CF6 0%, #A855F7 100%);
        border-radius: 20px;
        padding: 1.5rem;
        color: white;
        box-shadow: 0 8px 25px rgba(139,92,246,0.4);
        border: 2px solid #7C3AED;
        transition: all 0.3s ease;
    }
    .stFileUploader > div:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(139,92,246,0.5);
    }
    .stButton > button {
        background: linear-gradient(135deg, #8B5CF6 0%, #A855F7 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        box-shadow: 0 6px 20px rgba(139,92,246,0.4);
        transition: all 0.3s ease;
        border: 1px solid #7C3AED;
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(139,92,246,0.5);
        background: linear-gradient(135deg, #A855F7 0%, #8B5CF6 100%);
    }
    .stSidebar .stButton > button {
        background: linear-gradient(135deg, #8B5CF6 0%, #A855F7 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 1rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 6px 20px rgba(139,92,246,0.4);
        transition: all 0.3s ease;
        width: 100%;
        border: 1px solid #7C3AED;
    }
    .stSidebar .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(139,92,246,0.5);
        background: linear-gradient(135deg, #A855F7 0%, #8B5CF6 100%);
    }
    .stSidebar .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%);
        box-shadow: 0 6px 20px rgba(236,72,153,0.4);
        border: 1px solid #BE185D;
    }
    .stSidebar .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #DB2777 0%, #EC4899 100%);
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(236,72,153,0.5);
    }
    .stInfo {
        background: linear-gradient(135deg, #E8F5E8 0%, #C8E6C9 100%);
        border-radius: 20px;
        border: 2px solid #4CAF50;
        color: #1B5E20;
        box-shadow: 0 8px 25px rgba(76,175,80,0.3);
        padding: 1rem;
    }
    .stSuccess {
        background: linear-gradient(135deg, #E8F5E8 0%, #C8E6C9 100%);
        border-radius: 20px;
        border: 2px solid #4CAF50;
        color: #1B5E20;
        box-shadow: 0 8px 25px rgba(76,175,80,0.3);
        padding: 1rem;
    }
    .stWarning {
        background: linear-gradient(135deg, #FFF3E0 0%, #FFE0B2 100%);
        border-radius: 20px;
        border: 2px solid #FF9800;
        color: #E65100;
        box-shadow: 0 8px 25px rgba(255,152,0,0.3);
        padding: 1rem;
    }
    .stError {
        background: linear-gradient(135deg, #FFEBEE 0%, #FFCDD2 100%);
        border-radius: 20px;
        border: 2px solid #F44336;
        color: #B71C1C;
        box-shadow: 0 8px 25px rgba(244,67,54,0.3);
        padding: 1rem;
    }
    .stSidebar .stMarkdown {
        color: white !important;
    }
    .stSidebar .stMarkdown h1,
    .stSidebar .stMarkdown h2,
    .stSidebar .stMarkdown h3,
    .stSidebar .stMarkdown h4,
    .stSidebar .stMarkdown h5,
    .stSidebar .stMarkdown h6 {
        color: white !important;
        font-weight: 700;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    .stSidebar .stMarkdown p {
        color: #F3E8FF !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    .stMarkdown h1,
    .stMarkdown h2,
    .stMarkdown h3,
    .stMarkdown h4,
    .stMarkdown h5,
    .stMarkdown h6 {
        color: #1A237E !important;
        font-weight: 600;
    }
    .stMarkdown p {
        color: #283593 !important;
    }
    /* Enhanced container styling for history and about sections */
    .stContainer {
        background: linear-gradient(135deg, #F3E5F5 0%, #E1BEE7 100%);
        border-radius: 20px;
        border: 2px solid #9C27B0;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(156,39,176,0.2);
    }
    /* Enhanced caption styling */
    .stCaption {
        background: rgba(255,255,255,0.9);
        border-radius: 8px;
        padding: 0.5rem;
        border: 1px solid #E0E0E0;
        color: #424242;
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
    new_css = f'<style>{purple_css}</style>'
    content = re.sub(css_pattern, new_css, content, flags=re.DOTALL)
    
    # Write the updated content back to app.py
    with open('app.py', 'w') as f:
        f.write(content)
    
    print("✅ Updated navigation sidebar to beautiful purple-magenta gradient!")
    print("🎨 Navigation: Purple gradient (#8B5CF6 → #A855F7 → #C084FC)")
    print("💜 Primary buttons: Pink gradient (#EC4899 → #DB2777)")
    print("✨ White text with subtle shadows for better readability")

if __name__ == "__main__":
    update_navigation_purple()
