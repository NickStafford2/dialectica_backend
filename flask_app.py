"""
appserver.py  
- creates an application instance and runs the dev server
"""

from app.application import create_app

app = create_app()
