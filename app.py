import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import Image
import io, base64, os, sqlite3, time, pandas as pd, numpy as np
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Spot the Shade", 
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🎨"
)

# Beautiful title and styling

# Add custom CSS for better styling

# Add Google Fonts import


st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@300;400;500;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)


st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stSidebar {
        background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
    }
    .stSidebar .stSelectbox > div > div {
        background-color: rgba(255,255,255,0.9);
        border-radius: 10px;
    }
    .stFileUploader > div {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        border-radius: 20px;
        padding: 1.2rem;
        color: white;
        box-shadow: 0 6px 15px rgba(0,0,0,0.2);
        border: 1px solid rgba(255,255,255,0.1);
    }
    .stButton > button {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.6rem 1.2rem;
        font-weight: bold;
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
    }
    .stSidebar .stButton > button {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.8rem 1.2rem;
        font-weight: bold;
        font-size: 1rem;
        margin: 0.3rem 0;
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        width: 100%;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .stSidebar .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        background: linear-gradient(135deg, #34495e 0%, #2c3e50 100%);
    }
    .stSidebar .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        box-shadow: 0 6px 12px rgba(255,107,107,0.3);
    }
    .stSidebar .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #ee5a24 0%, #ff6b6b 100%);
        transform: translateY(-3px);
        box-shadow: 0 8px 16px rgba(255,107,107,0.4);
    }
    .stInfo {
        background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.2);
        color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .stSuccess {
        background: linear-gradient(135deg, #96ceb4 0%, #feca57 100%);
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.2);
        color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }

    .blinking {
        animation: blink 1.5s infinite;
    }
    
    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0.3; }
    }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div style="background: linear-gradient(45deg, #e74c3c, #f39c12, #27ae60, #8e44ad, #2c3e50); 
            background-size: 400% 400%; 
            animation: gradient 15s ease infinite;
            padding: 1.5rem; 
            border-radius: 20px; 
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
            border: 1px solid rgba(255,255,255,0.1);">
    <h2 style="color: white; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); font-family: 'Playfair Display', 'Georgia', serif; font-weight: 400; letter-spacing: 0.8px; font-size: 1.8rem;">
        Every pixel tells a color story
    </h2>
    <p style="color: white; margin: 0.5rem 0 0 0; font-size: 1.1rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
        Detect, analyze, and save colors from any image with precision
    </p>
</div>

<style>
@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; padding: 2.5rem 0; background: linear-gradient(135deg, #2c3e50 0%, #34495e 50%, #1a1a1a 100%); border-radius: 25px; margin-bottom: 2rem; box-shadow: 0 15px 35px rgba(0,0,0,0.4); border: 1px solid rgba(255,255,255,0.1);">
    <h1 style="color: white; font-size: 3.5rem; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
        <span class="blinking">✨</span> Spot the Shade
    </h1>
    <p style="color: #f0f0f0; font-size: 1.5rem; margin: 0.5rem 0 0 0; font-family: 'Playfair Display', 'Georgia', serif; font-weight: 300; font-style: italic; text-shadow: 2px 2px 4px rgba(0,0,0,0.4); letter-spacing: 1.2px; line-height: 1.3;">
        Every pixel tells a color story
    </p>
</div>
""", unsafe_allow_html=True)

# Setup directories
os.makedirs("uploads", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Database setup
def init_db():
    conn = sqlite3.connect("color_history.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS captures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            image_path TEXT,
            x INTEGER, y INTEGER,
            r INTEGER, g INTEGER, b INTEGER,
            hex TEXT, color_name TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_db_conn():
    return sqlite3.connect("color_history.db")

# Load colors data
@st.cache_data
def load_colors():
    try:
        df = pd.read_csv("data/colors.csv")
        return df
    except:
        # Create sample colors if file doesn't exist
        colors = [
            {"name": "Red", "hex": "#FF0000", "r": 255, "g": 0, "b": 0},
            {"name": "Green", "hex": "#008000", "r": 0, "g": 128, "b": 0},
            {"name": "Blue", "hex": "#0000FF", "r": 0, "g": 0, "b": 255},
            {"name": "Yellow", "hex": "#FFFF00", "r": 255, "g": 255, "b": 0},
            {"name": "Orange", "hex": "#FFA500", "r": 255, "g": 165, "b": 0},
            {"name": "Purple", "hex": "#800080", "r": 128, "g": 0, "b": 128},
            {"name": "Pink", "hex": "#FFC0CB", "r": 255, "g": 192, "b": 203},
            {"name": "Brown", "hex": "#A52A2A", "r": 165, "g": 42, "b": 42},
            {"name": "Gray", "hex": "#808080", "r": 128, "g": 128, "b": 128},
            {"name": "Black", "hex": "#000000", "r": 0, "g": 0, "b": 0},
            {"name": "White", "hex": "#FFFFFF", "r": 255, "g": 255, "b": 255}
        ]
        return pd.DataFrame(colors)

# Helper functions
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def find_closest_color(rgb, colors_df):
    colors_array = colors_df[["r", "g", "b"]].values
    distances = np.sqrt(np.sum((colors_array - np.array(rgb))**2, axis=1))
    closest_idx = np.argmin(distances)
    return colors_df.iloc[closest_idx]
def resize_image_for_display(image, max_width=1600, max_height=1200):
    """Resize image for display while maintaining aspect ratio"""
    width, height = image.size
    if width <= max_width and height <= max_height:
        return image, 1.0  # No resize needed, scale factor = 1
    
    # Calculate scale factor
    width_scale = max_width / width
    height_scale = max_height / height
    scale_factor = min(width_scale, height_scale)
    
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    
    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return resized_image, scale_factor


# Initialize database
init_db()
colors_df = load_colors()

# Sidebar navigation with static buttons
st.sidebar.markdown("### 🧭 Navigation")
st.sidebar.markdown("---")

# Navigation buttons
if st.sidebar.button("🎯 Color Picker", use_container_width=True, type="primary"):
    st.session_state.current_page = "color_picker"
if st.sidebar.button("📚 History", use_container_width=True):
    st.session_state.current_page = "history"
if st.sidebar.button("🎨 About", use_container_width=True):
    st.session_state.current_page = "about"

# Initialize session state
if "current_page" not in st.session_state:
    st.session_state.current_page = "color_picker"

# Set page based on session state
page = st.session_state.current_page

# Map session state to page names
if page == "color_picker":
    page = "🎯 Color Picker"
elif page == "history":
    page = "📚 History"
elif page == "about":
    page = "🎨 About"

if page == "🎯 Color Picker":
    st.header("Upload an image and click to detect colors")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file:
        # Load and display image
        original_image = Image.open(uploaded_file).convert("RGB")
        
        # Resize image for display
        display_image, scale_factor = resize_image_for_display(original_image)
        
        # Save both original and display images
        timestamp = int(time.time())
        original_path = f"uploads/original_{timestamp}.png"
        display_path = f"uploads/display_{timestamp}.png"
        original_image.save(original_path)
        display_image.save(display_path)
        
        # Show image dimensions info
        col1, col2 = st.columns([2, 1])
        with col1:
            st.info("👆 Click anywhere on the image to detect the color")
        with col2:
            st.caption(f"Original: {original_image.size[0]}×{original_image.size[1]}")
            if scale_factor < 1.0:
                st.caption(f"Display: {display_image.size[0]}×{display_image.size[1]} ({scale_factor:.2f}x)")
        
        # Display resized image with click coordinates
        coords = streamlit_image_coordinates(display_path)
        
        if coords:
            # Get coordinates and scale back to original image
            display_x = coords.get("x", 0)
            display_y = coords.get("y", 0)
            
            # Scale coordinates back to original image
            original_x = int(display_x / scale_factor)
            original_y = int(display_y / scale_factor)
            
            # Clamp coordinates to original image bounds
            original_x = max(0, min(original_x, original_image.width - 1))
            original_y = max(0, min(original_y, original_image.height - 1))
            
            # Get pixel color from original image
            r, g, b = original_image.getpixel((original_x, original_y))
            hex_color = rgb_to_hex((r, g, b))
            
            # Find closest named color
            closest = find_closest_color((r, g, b), colors_df)
            
            # Display results in columns
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.markdown("**Detected Color**")
                st.markdown(f'<div style="width:100px; height:100px; background-color:{hex_color}; border-radius:10px; border:2px solid #ddd;"></div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown("**Color Information**")
                st.write(f"**RGB:** ({r}, {g}, {b})")
                st.write(f"**HEX:** {hex_color}")
                st.write(f"**Closest Name:** {closest['name']}")
                st.write(f"**Coordinates:** ({original_x}, {original_y})")
            
            # Save button
            if st.button("💾 Save to History", type="primary"):
                conn = get_db_conn()
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO captures (timestamp, image_path, x, y, r, g, b, hex, color_name)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (datetime.now().isoformat(), original_path, original_x, original_y, r, g, b, hex_color, closest['name']))
                conn.commit()
                conn.close()
                st.success("✅ Color saved to history!")

elif page == "📚 History":
    st.header("Saved Color History")
    
    conn = get_db_conn()
    df = pd.read_sql_query("SELECT * FROM captures ORDER BY id DESC", conn)
    conn.close()
    
    if df.empty:
        st.info("No colors saved yet. Go to Color Picker to start detecting colors!")
    else:
        for _, row in df.iterrows():
            with st.container():
                col1, col2, col3 = st.columns([1, 3, 1])
                
                with col1:
                    st.markdown(f'<div style="width:60px; height:60px; background-color:{row["hex"]}; border-radius:8px; border:1px solid #ddd;"></div>', unsafe_allow_html=True)
                
                with col2:
                    st.write(f"**{row['color_name']}** - {row['hex']}")
                    st.write(f"RGB: ({row['r']}, {row['g']}, {row['b']}) | Position: ({row['x']}, {row['y']})")
                    st.caption(f"Saved: {row['timestamp']}")
                
                with col3:
                    if st.button("🗑️", key=f"delete_{row['id']}", help="Delete this color"):
                        conn = get_db_conn()
                        cur = conn.cursor()
                        cur.execute("DELETE FROM captures WHERE id = ?", (row['id'],))
                        conn.commit()
                        conn.close()
                        st.rerun()

elif page == "🎨 About":
    st.header("About Spot the Shade")
    
    st.markdown("""
    ### How to Use
    1. **Upload an image** - PNG, JPG, or JPEG formats supported
    2. **Click anywhere** on the image to detect the color at that pixel
    3. **View results** - Get RGB, HEX values and closest color name
    4. **Save colors** - Build your personal color palette
    
    ### Tips for Best Results
    - Use high-resolution images for better accuracy
    - Avoid heavily compressed images
    - Click on solid color areas for most accurate results
    
    ### Features
    - 🎯 **Precise Color Detection** - Click any pixel to get exact color values
    - 📚 **Color History** - Save and organize your favorite colors
    - 🎨 **Color Matching** - Find the closest named color from our database
    - 💾 **Local Storage** - All data stored locally on your device
    
    ### Technical Details
    - Built with Streamlit and Python
    - Uses PIL (Pillow) for image processing
    - SQLite database for local storage
    - Euclidean distance algorithm for color matching
    """)
    
    st.markdown("---")
    st.markdown("*Made with ❤️ for designers and color enthusiasts*")

# Beautiful footer
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #2c3e50 0%, #34495e 50%, #1a1a1a 100%); 
            border-radius: 20px; margin-top: 2rem; box-shadow: 0 8px 25px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1);">
    <h3 style="color: white; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
        ✨ Spot the Shade
    </h3>
    <p style="color: #f0f0f0; margin: 0.5rem 0 0 0; font-size: 1.1rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
        colour detecting tool
    </p>
    <p style="color: #e0e0e0; margin: 0.5rem 0 0 0; font-size: 0.9rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
        Made with ❤️ for designers and color enthusiasts
    </p>
</div>
""", unsafe_allow_html=True)
