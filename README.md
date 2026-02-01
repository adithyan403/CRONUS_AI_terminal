# CRONUS AI Terminal 🚀

[![Deploy to GitHub Pages](https://github.com/adithyan403/CRONUS_AI_terminal/actions/workflows/deploy.yml/badge.svg)](https://github.com/adithyan403/CRONUS_AI_terminal/actions/workflows/deploy.yml)

**Command Your Environment** - Bridge the gap between human intent and OS execution.

CRONUS AI is a powerful productivity shell that enables you to control volume, capture displays, manage processes, and optimize your workflow with simple voice or text triggers.

## ✨ Features

- **🔊 Audio Synthesis** - Granular control over system gain with mute, duck, or precise level controls
- **📸 Visual Capture** - Zero-delay screen captures with auto-save and OCR text extraction
- **⚡ Process Kill** - Instantly terminate non-responsive tasks or launch software clusters
- **📊 Neural Monitoring** - Real-time telemetry for CPU, GPU, and RAM with automatic optimization

## 🌐 Live Demo

Visit the deployed website:
- **GitHub Pages:** [https://adithyan403.github.io/CRONUS_AI_terminal/](https://adithyan403.github.io/CRONUS_AI_terminal/)

## 🚀 Quick Deploy

This project is ready to deploy to multiple platforms:

### Deploy to Render (Free)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

1. Click the button above or go to [Render.com](https://render.com)
2. Connect this GitHub repository
3. Render auto-detects configuration from `render.yaml`
4. Click **Deploy** - Done! ✅

### Deploy to Vercel (Free)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/adithyan403/CRONUS_AI_terminal)

1. Click the button above or go to [Vercel.com](https://vercel.com)
2. Import this repository
3. Vercel auto-detects configuration from `vercel.json`
4. Click **Deploy** - Done! ✅

### Deploy to GitHub Pages (Free)
Already configured! Just:
1. Go to **Settings** > **Pages**
2. Set source to **GitHub Actions**
3. Push to `main` branch triggers auto-deployment

### Other Platforms
See [DEPLOYMENT.md](DEPLOYMENT.md) for complete deployment guides including:
- Docker deployment
- Heroku
- Railway.app
- Fly.io
- Self-hosting options

## 💻 Local Development

### Prerequisites
- Python 3.9+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/adithyan403/CRONUS_AI_terminal.git
   cd CRONUS_AI_terminal
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   ```
   http://localhost:5000
   ```

### Using Docker

```bash
# Build the image
docker build -t cronus-ai-terminal .

# Run the container
docker run -p 5000:5000 cronus-ai-terminal

# Access at http://localhost:5000
```

## 📁 Project Structure

```
CRONUS_AI_terminal/
├── app.py                  # Flask application
├── index.html              # Main webpage
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── Procfile              # Heroku configuration
├── render.yaml           # Render configuration
├── vercel.json           # Vercel configuration
├── assets/               # Images and videos
│   ├── intro.mp4
│   └── logo.png
├── css/
│   └── style.css
├── js/
│   └── main.js
└── .github/
    └── workflows/
        └── deploy.yml    # GitHub Actions workflow
```

## 🛠️ Technology Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Server:** Gunicorn
- **Containerization:** Docker
- **CI/CD:** GitHub Actions

## 🎯 Performance

- **Response Latency:** 0.1s
- **Idle RAM Footprint:** 12MB
- **Local Processing:** 100%

## 📋 Requirements

### For Local Development
- Python 3.9 or higher
- Flask
- Gunicorn (for production)

### For Deployment
- See [DEPLOYMENT.md](DEPLOYMENT.md) for platform-specific requirements

## 🔒 Security

- All processing is done locally
- No data is sent to external servers
- Built with privacy in mind

## 📄 License

This software is in **DEVELOPMENT MODE** and is the exclusive property of **CRONUS PVT LTD**.

## ⚠️ Status

**ALPHA BUILD** - This software is currently in development stage. Use at your own risk.

## 🤝 Contributing

This is an alpha build. For feature requests or bug reports, please open an issue.

## 📞 Support

For deployment help or technical questions:
- Check [DEPLOYMENT.md](DEPLOYMENT.md) for detailed guides
- Open an issue on GitHub
- Contact: CRONUS PVT LTD

---

**Built with ❤️ by CRONUS PVT LTD** | **Version: 1.0.0-ALPHA**
