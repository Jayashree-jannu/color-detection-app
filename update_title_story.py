#!/usr/bin/env python3
"""
Update main title to 'Every pixel tells a colour story' and match running colors
"""

import re

def update_title_story():
    # Read the current app.py
    with open('app.py', 'r') as f:
        content = f.read()
    
    # Update the main title section with new text and matching blue running colors
    title_pattern = r'<div style="background: linear-gradient\(135deg, #B3E5FC 0%, #E1F5FE 50%, #F3E5F5 100\);.*?</div>'
    new_title = '''<div style="background: linear-gradient(45deg, #B3E5FC, #E1F5FE, #81D4FA, #4FC3F7, #29B6F6, #03A9F4); 
            background-size: 400% 400%; 
            animation: gradient 15s ease infinite;
            padding: 1.5rem; 
            border-radius: 20px; 
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 8px 25px rgba(21,101,192,0.3);
            border: 1px solid rgba(21,101,192,0.2);">
    <h2 style="color: #1565C0; margin: 0; text-shadow: 2px 2px 4px rgba(255,255,255,0.5); font-family: 'Playfair Display', 'Georgia', serif; font-weight: 400; letter-spacing: 0.8px; font-size: 1.8rem;">
        Every pixel tells a colour story
    </h2>
    <p style="color: #1976D2; margin: 0.5rem 0 0 0; font-size: 1.1rem; text-shadow: 1px 1px 2px rgba(255,255,255,0.3); font-family: 'Crimson Text', 'Georgia', serif; font-style: italic;">
        Discover colors with precision and beauty
    </p>
</div>'''
    content = re.sub(title_pattern, new_title, content, flags=re.DOTALL)
    
    # Add the gradient animation keyframes to the CSS
    css_pattern = r'(@keyframes blink {.*?})'
    new_css_animation = '''@keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0.3; }
    }'''
    content = re.sub(css_pattern, new_css_animation, content, flags=re.DOTALL)
    
    # Write the updated content back to app.py
    with open('app.py', 'w') as f:
        f.write(content)
    
    print("✅ Updated main title to 'Every pixel tells a colour story'!")
    print("🎨 Running colors: Beautiful blue gradient animation")
    print("💙 Colors: #B3E5FC → #E1F5FE → #81D4FA → #4FC3F7 → #29B6F6 → #03A9F4")
    print("✨ Smooth 15-second gradient animation cycle")

if __name__ == "__main__":
    update_title_story()
