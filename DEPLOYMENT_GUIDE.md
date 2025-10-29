# 🚀 GitHub & Free Deployment Guide

## Disease PredictionIQ - Deployment Instructions
**Author:** Jay Prakash Kumar

---

## 📋 Prerequisites

Before deploying, ensure you have:
- ✅ Git installed on your system
- ✅ GitHub account created
- ✅ All project files ready
- ✅ Model files trained and saved

---

## 🔧 Step 1: Push to GitHub

### 1.1 Initialize Git Repository (if not already done)

Open terminal in your project directory and run:

```bash
cd E:\project\cap2
git init
```

### 1.2 Configure Git (First Time Only)

```bash
git config --global user.name "Jay Prakash Kumar"
git config --global user.email "jay.prakash7.kr@gmail.com"
```

### 1.3 Add Remote Repository

```bash
git remote add origin https://github.com/JayAtria-7/Disease-PredictionIQ.git
```

### 1.4 Stage All Files

```bash
git add .
```

### 1.5 Commit Your Changes

```bash
git commit -m "Initial commit: Disease PredictionIQ - Complete ML web application"
```

### 1.6 Push to GitHub

```bash
git branch -M main
git push -u origin main
```

**Note:** You may be prompted for GitHub credentials. Use a Personal Access Token (PAT) instead of password.

#### Generate GitHub Personal Access Token:
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scopes: `repo`, `workflow`
4. Copy the token and use it as password when pushing

---

## 🌐 Step 2: Free Deployment Options

### Option 1: Render.com (Recommended - Easiest) ⭐

**Why Render?**
- ✅ Free tier available
- ✅ Automatic deployments from GitHub
- ✅ Easy setup
- ✅ Support for Python/Flask apps
- ✅ 750 hours/month free

#### Steps:

1. **Create Account**
   - Go to: https://render.com
   - Sign up with GitHub account

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `Disease-PredictionIQ`
   - Click "Connect"

3. **Configure Service**
   ```
   Name: disease-predictioniq
   Region: Oregon (US West) or closest to you
   Branch: main
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   Instance Type: Free
   ```

4. **Add Environment Variables** (if needed)
   ```
   FLASK_ENV=production
   ```

5. **Click "Create Web Service"**
   - Deployment will start automatically
   - Wait 5-10 minutes for build

6. **Access Your App**
   - URL: `https://disease-predictioniq.onrender.com`

#### Important: Add `gunicorn` to requirements

Create `requirements-flask.txt`:
```
Flask==2.3.3
gunicorn==21.2.0
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
```

---

### Option 2: Railway.app 🚂

**Why Railway?**
- ✅ $5 free credit/month
- ✅ Very easy GitHub integration
- ✅ Fast deployments

#### Steps:

1. **Sign Up**
   - Go to: https://railway.app
   - Login with GitHub

2. **New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `Disease-PredictionIQ`

3. **Configure**
   - Railway auto-detects Python
   - Add start command: `gunicorn app:app`
   - Deploy!

4. **Generate Domain**
   - Click "Generate Domain"
   - Access your app at: `https://disease-predictioniq.up.railway.app`

---

### Option 3: PythonAnywhere 🐍

**Why PythonAnywhere?**
- ✅ Always free tier
- ✅ Specifically for Python apps
- ✅ Easy Flask deployment

#### Steps:

1. **Create Account**
   - Go to: https://www.pythonanywhere.com
   - Sign up for free account

2. **Clone Repository**
   - Open Bash console
   ```bash
   git clone https://github.com/JayAtria-7/Disease-PredictionIQ.git
   cd Disease-PredictionIQ
   ```

3. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configure Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Python 3.10

5. **Configure WSGI File**
   ```python
   import sys
   path = '/home/yourusername/Disease-PredictionIQ'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```

6. **Reload Web App**
   - Click "Reload"
   - Access at: `http://yourusername.pythonanywhere.com`

---

### Option 4: Hugging Face Spaces 🤗

**Why Hugging Face?**
- ✅ Free for public apps
- ✅ Great for ML models
- ✅ Community exposure

#### Steps:

1. **Create Space**
   - Go to: https://huggingface.co/spaces
   - Click "Create new Space"
   - Name: `disease-predictioniq`
   - SDK: Gradio or Streamlit (you'll need to adapt)

2. **Push Your Code**
   ```bash
   git remote add hf https://huggingface.co/spaces/YourUsername/disease-predictioniq
   git push hf main
   ```

**Note:** Requires conversion to Gradio/Streamlit interface

---

## 🎯 Recommended Deployment: Render.com

For your Flask app, **Render.com** is the best free option!

### Quick Render Deployment Checklist:

- [ ] Code pushed to GitHub
- [ ] Create Render account
- [ ] Connect GitHub repository
- [ ] Add `gunicorn` to requirements
- [ ] Configure build & start commands
- [ ] Deploy!

---

## 📦 Pre-Deployment Checklist

### 1. Update Requirements

Create `requirements-deploy.txt`:
```txt
Flask==2.3.3
gunicorn==21.2.0
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
werkzeug==2.3.7
```

### 2. Update app.py for Production

Add at the end of `app.py`:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

### 3. Create Procfile (for some platforms)

Create `Procfile`:
```
web: gunicorn app:app
```

### 4. Check Model Files Size

```bash
dir models
```

If `*.pkl` files are > 100MB, use Git LFS:
```bash
git lfs install
git lfs track "*.pkl"
git add .gitattributes
```

---

## 🔐 Security Considerations

1. **Remove Debug Mode** in production
2. **Add API rate limiting**
3. **Set up CORS properly**
4. **Use environment variables** for sensitive data
5. **Add HTTPS** (automatic on most platforms)

---

## 📊 Monitoring Your Deployed App

After deployment:

1. **Test All Features:**
   - Prediction form submission
   - Model info display
   - Comparison section
   - Mobile responsiveness

2. **Check Logs:**
   - Render: Dashboard → Logs
   - Railway: Deployment → Logs
   - PythonAnywhere: Files → Error log

3. **Monitor Performance:**
   - Response times
   - Error rates
   - User analytics (optional: Google Analytics)

---

## 🆘 Troubleshooting

### Common Issues:

**Issue 1: Module not found**
- Solution: Add missing package to `requirements.txt`

**Issue 2: Model file not found**
- Solution: Ensure model files are committed to Git (not in `.gitignore`)

**Issue 3: Port binding error**
- Solution: Use `port = int(os.environ.get('PORT', 5000))`

**Issue 4: Large file error (>100MB)**
- Solution: Use Git LFS or host models separately

---

## 🎉 Success!

Once deployed, your app will be live at:
- Render: `https://disease-predictioniq.onrender.com`
- Railway: `https://disease-predictioniq.up.railway.app`
- PythonAnywhere: `http://yourusername.pythonanywhere.com`

Share your live link:
- 📧 Email
- 💼 LinkedIn
- 🐙 GitHub README
- 📱 Portfolio

---

## 📞 Support

If you encounter issues:
1. Check deployment platform docs
2. Review error logs
3. Search Stack Overflow
4. GitHub Issues

---

**Made with ❤️ by Jay Prakash Kumar**

