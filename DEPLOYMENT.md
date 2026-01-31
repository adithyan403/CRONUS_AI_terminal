# CRONUS AI Terminal - Deployment Guide

This repository contains the CRONUS AI Terminal website with multiple deployment options.

## 🚀 Deployment Options

### Option 1: GitHub Pages (Static Hosting)

**Pros:** Free, simple, automatic deployments
**Best for:** Static website hosting

**Setup Steps:**
1. Go to your repository settings on GitHub
2. Navigate to **Settings** > **Pages**
3. Under "Build and deployment":
   - Source: Select **GitHub Actions**
4. The workflow will automatically deploy on push to `main` branch
5. Your site will be available at: `https://adithyan403.github.io/CRONUS_AI_terminal/`

**Note:** GitHub Pages serves static content. The Flask backend won't run, but the HTML/CSS/JS will work perfectly.

### Option 2: Render (Full Flask App)

**Pros:** Free tier available, supports Python/Flask, easy setup
**Best for:** Full-stack Flask applications

**Setup Steps:**
1. Go to [Render.com](https://render.com) and sign up/login
2. Click **New** > **Web Service**
3. Connect your GitHub repository
4. Render will automatically detect the `render.yaml` configuration
5. Click **Create Web Service**
6. Your site will be deployed automatically!

**Configuration:** The `render.yaml` file is already configured for automatic deployment.

### Option 3: Vercel (Serverless)

**Pros:** Free tier, excellent performance, global CDN
**Best for:** Serverless Flask applications

**Setup Steps:**
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel login`
3. In the project directory, run: `vercel`
4. Follow the prompts to deploy
5. Your site will be live at a Vercel URL

**Alternative (GitHub Integration):**
1. Go to [Vercel.com](https://vercel.com) and sign up/login
2. Click **Add New** > **Project**
3. Import your GitHub repository
4. Vercel will automatically detect the `vercel.json` configuration
5. Click **Deploy**

### Option 4: Docker Deployment (Any Platform)

**Pros:** Portable, works anywhere
**Best for:** Self-hosting or container platforms

**Setup Steps:**
1. Build the Docker image:
   ```bash
   docker build -t cronus-ai-terminal .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 cronus-ai-terminal
   ```

3. Access at: `http://localhost:5000`

**Deploy to Cloud Platforms:**
- **Railway.app:** Connect GitHub repo and deploy from Dockerfile
- **Fly.io:** Use `flyctl launch` to deploy
- **Google Cloud Run:** Deploy containerized apps
- **AWS ECS/Fargate:** Enterprise container hosting

### Option 5: Heroku (Traditional PaaS)

**Pros:** Simple deployment, supports Python
**Note:** Heroku no longer offers a free tier

**Setup Steps:**
1. Install Heroku CLI: `curl https://cli-assets.heroku.com/install.sh | sh`
2. Login: `heroku login`
3. Create app: `heroku create cronus-ai-terminal`
4. Deploy: `git push heroku main`
5. Open: `heroku open`

**Configuration:** The `Procfile` is already configured.

## 📋 Pre-Deployment Checklist

- [x] Flask app configured (`app.py`)
- [x] Requirements.txt present
- [x] Dockerfile available
- [x] Procfile for Heroku
- [x] render.yaml for Render
- [x] vercel.json for Vercel
- [x] GitHub Actions workflow for GitHub Pages

## 🧪 Local Development

To run the website locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py

# Access at http://localhost:5000
```

## 🌐 Recommended Deployment

For this project, we recommend:

1. **GitHub Pages** - If you just want to showcase the static website
2. **Render** - If you need the Flask backend functionality (free tier available)
3. **Vercel** - For serverless deployment with excellent performance

## 📝 Environment Variables

The app uses the following environment variable:
- `PORT` - The port to run the Flask app on (default: 5000)

Set this in your deployment platform's settings if needed.

## 🔒 Security Notes

- The app serves static files from the current directory
- Ensure sensitive files are listed in `.gitignore`
- For production, consider adding rate limiting and security headers

## 📞 Support

For issues or questions about deployment, please open an issue on GitHub.

---

**Built with Flask** | **Powered by CRONUS AI** | **Version: 1.0.0-ALPHA**
