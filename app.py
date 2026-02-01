
from flask import Flask, send_from_directory, send_file
import os

# Initialize Flask app
# static_url_path='' ensures files are served from root (e.g. /css/style.css)
# static_folder='.' sets the current directory as the source for static files
app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def home():
    """Serve the main index.html"""
    return send_file('index.html')

@app.route('/download')
def download_zip():
    """Specific endpoint for downloading the zip (optional, direct link works too)"""
    try:
        return send_file('CronusAI_Beta.zip', as_attachment=True)
    except Exception as e:
        return str(e), 404

@app.route('/health')
def health():
    """Health check endpoint for monitoring"""
    return {'status': 'healthy', 'version': '1.0.0-ALPHA'}, 200

if __name__ == '__main__':
    # Determine port for local vs production
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
