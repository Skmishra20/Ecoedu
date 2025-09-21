#!/usr/bin/env python3
"""
Simple HTTP server to run the EcoEdu Platform frontend
Run with: python serve.py
"""

import http.server
import socketserver
import os
import webbrowser
import threading
import time

PORT = 8080
DIRECTORY = "frontend"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def open_browser():
    """Open browser after a short delay"""
    time.sleep(1.5)
    webbrowser.open(f'http://localhost:{PORT}')

if __name__ == "__main__":
    # Change to the project root directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Check if frontend directory exists
    if not os.path.exists(DIRECTORY):
        print(f"Error: {DIRECTORY} directory not found!")
        print("Make sure you're running this from the eco-edu-platform root directory.")
        exit(1)
    
    # Start the server
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🌱 EcoEdu Platform Server Starting...")
        print(f"📁 Serving files from: {os.path.abspath(DIRECTORY)}")
        print(f"🌐 Server running at: http://localhost:{PORT}")
        print(f"📱 Running in offline demo mode (no backend required)")
        print(f"🚀 Opening browser automatically...")
        print(f"\n💡 Press Ctrl+C to stop the server")
        
        # Open browser in a separate thread
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n🛑 Server stopped.")