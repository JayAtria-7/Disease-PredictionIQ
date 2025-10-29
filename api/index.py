"""
Vercel Serverless Function Handler for Disease PredictionIQ
This file adapts the Flask app for Vercel's serverless environment
Author: Jay Prakash
"""

from app import app

# Vercel expects an 'app' variable for WSGI applications
# This makes the Flask app compatible with Vercel's Python runtime
application = app
