#!/usr/bin/env python3
"""
Improve UI contrast for navigation, history, and about boxes
"""

import re

def improve_ui_contrast():
    # Read the current app.py
    with open('app.py', 'r') as f:
        content = f.read()
    
    # Enhanced CSS for better contrast and visibility
    enhanced_css = '''
    .main > div {
        padding-top: 2rem;
    }
    .stApp {
        background: #F8F9FA;
    }
    .stSidebar {
        background: linear-gradient(180deg, #E3F2FD 0%, #BBDEFB 100%) !important;
        color: #1A237E !important;
        border-right: 3px solid #2196F3;
    }
    .stSidebar .stSelectbox > div > div {
        background-color: rgba(255,255,255,0.95);
        border-radius: 12px;
        border: 2px solid #2196F3;
        box-shadow: 0 2px 8px rgba(33,150,243,0.2);
    }
    .stSidebar .stSelectbox label {
        color: #1A237E !important;
        font-weight: 600;
    }
    .stSidebar .stTextInput label {
        color: #1A237E !important;
        font-weight: 600;
    }
    .stSidebar .stTextArea label {
        color: #1A237E !important;
        font-weight: 600;
    }
    .stSidebar .stNumberInput label {
        color: #1A237E !important;
        font-weight: 600;
    }
    .stSidebar .stSlider label {
        color: #1A237E !important;
        font-weight: 600;
    }
    .stSidebar .stCheckbox label {
        color: #1A237E !important;
        font-weight: 600;
    }
    .stSidebar .stRadio label {
        color: #1A237E !important;
        font-weight: 600;
    }
    .stSidebar .stMultiSelect label {
        color: #1A237E !important;
        font-weight: 600;
    }
    .stSidebar .stSelectbox > div > div > div {
        color: #1A237E !important;
    }
    .stFileUploader > div {
        background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
        border-radius: 20px;
        padding: 1.5rem;
        color: #1A237E;
        box-shadow: 0 8px 25px rgba(33,150,243,0.3);
        border: 2px solid #2196F3;
        transition: all 0.3s ease;
    }
    .stFileUploader > div:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(33,150,243,0.4);
    }
    .stButton > button {
        background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        box-shadow: 0 6px 20px rgba(33,150,243,0.3);
        transition: all 0.3s ease;
        border: 1px solid #1565C0;
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(33,150,243,0.4);
        background: linear-gradient(135deg, #1976D2 0%, #2196F3 100%);
    }
    .stSidebar .stButton > button {
        background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 1rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 6px 20px rgba(33,150,243,0.3);
        transition: all 0.3s ease;
        width: 100%;
        border: 1px solid #1565C0;
    }
    .stSidebar .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(33,150,243,0.4);
        background: linear-gradient(135deg, #1976D2 0%, #2196F3 100%);
    }
    .stSidebar .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #FF5722 0%, #E64A19 100%);
        box-shadow: 0 6px 20px rgba(255,87,34,0.4);
        border: 1px solid #D84315;
    }
    .stSidebar .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #E64A19 0%, #FF5722 100%);
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(255,87,34,0.5);
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
        color: #1A237E !important;
    }
    .stSidebar .stMarkdown h1,
    .stSidebar .stMarkdown h2,
    .stSidebar .stMarkdown h3,
    .stSidebar .stMarkdown h4,
    .stSidebar .stMarkdown h5,
    .stSidebar .stMarkdown h6 {
        color: #1A237E !important;
        font-weight: 700;
    }
    .stSidebar .stMarkdown p {
        color: #283593 !important;
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
    new_css = f'<style>{enhanced_css}</style>'
    content = re.sub(css_pattern, new_css, content, flags=re.DOTALL)
    
    # Write the updated content back to app.py
    with open('app.py', 'w') as f:
        f.write(content)
    
    print("✅ Enhanced UI contrast and visibility!")
    print("🎨 Navigation sidebar: Light blue gradient with dark blue text")
    print("📚 History containers: Purple gradient with better contrast")
    print("ℹ️ Info boxes: Green gradient with dark green text")
    print("✅ Success boxes: Green gradient with dark green text")
    print("⚠️ Warning boxes: Orange gradient with dark orange text")
    print("❌ Error boxes: Red gradient with dark red text")

if __name__ == "__main__":
    improve_ui_contrast()
