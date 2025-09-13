# db_init.py
"""
Database initialization script for Spot the Shade color detection app.
Creates the SQLite database and captures table if they don't exist.
"""

import sqlite3
import os

def init_database():
    """Initialize SQLite database with captures table"""
    # Create database connection
    conn = sqlite3.connect("color_history.db")
    cur = conn.cursor()
    
    # Create captures table with all required fields
    cur.execute("""
    CREATE TABLE IF NOT EXISTS captures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        image_path TEXT,
        x INTEGER,
        y INTEGER,
        r INTEGER, g INTEGER, b INTEGER,
        hex TEXT,
        color_name TEXT
    )
    """)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")
    print("📊 Table 'captures' created with fields: id, timestamp, image_path, x, y, r, g, b, hex, color_name")

if __name__ == "__main__":
    print("🎨 Spot the Shade - Database Initialization")
    print("=" * 50)
    init_database()
    print("=" * 50)
    print("🚀 Ready to run: streamlit run app.py")
