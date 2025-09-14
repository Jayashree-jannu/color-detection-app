#!/usr/bin/env python3
"""
Remove '✨ Spot the Shade' from the footer section
"""

import re

def remove_footer_title():
    # Read the current app.py
    with open('app.py', 'r') as f:
        content = f.read()
    
    # Update the footer section to remove the title
    footer_pattern = r'<div style="text-align: center; padding: 2rem; background: linear-gradient\(135deg, #B3E5FC 0%, #E1F5FE 50%, #F3E5F5 100\);.*?</div>'
    new_footer = '''<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #B3E5FC 0%, #E1F5FE 50%, #F3E5F5 100%); 
                   border-radius: 20px; margin-top: 2rem; box-shadow: 0 8px 25px rgba(21,101,192,0.3); border: 1px solid rgba(21,101,192,0.2);">
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
    
    print("✅ Removed '✨ Spot the Shade' from footer section!")
    print("🎨 Footer now shows only:")
    print("   • colour detecting tool")
    print("   • Made with ❤️ for designers and color enthusiasts")

if __name__ == "__main__":
    remove_footer_title()
