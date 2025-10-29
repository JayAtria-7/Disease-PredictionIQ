# 🌐 FREE Deployment Options for Disease PredictionIQ

**Author:** Jay Prakash Kumar  
**Project:** Disease PredictionIQ

---

## 🎯 Quick Comparison of Free Hosting Platforms

| Platform | Free Tier | Auto-Deploy | Python Support | Custom Domain | Best For |
|----------|-----------|-------------|----------------|---------------|----------|
| **Render** | 750hrs/mo | ✅ Yes | ✅ Excellent | ✅ Yes | Flask apps (EASIEST) |
| **Railway** | $5 credit/mo | ✅ Yes | ✅ Excellent | ✅ Yes | Quick deployment |
| **PythonAnywhere** | ✅ Always Free | ❌ Manual | ✅ Native | ❌ Subdomain only | Python beginners |
| **Fly.io** | 3 VMs free | ✅ Yes | ✅ Good | ✅ Yes | Docker apps |
| **Koyeb** | ✅ Free tier | ✅ Yes | ✅ Good | ✅ Yes | Microservices |
| **Cyclic** | ✅ Free | ✅ Yes | ⚠️ Node focus | ✅ Yes | Node.js (adaptable) |
| **Vercel** | ✅ Free | ✅ Yes | ⚠️ Serverless | ✅ Yes | Frontend + API |
| **Netlify** | ✅ Free | ✅ Yes | ⚠️ Functions only | ✅ Yes | Static + Functions |
| **Heroku** | ❌ No longer free | - | - | - | Not recommended |

---

## 1️⃣ **Fly.io** (Recommended for Full Apps)

### ✨ Features:
- 3 shared-cpu VMs free
- 3GB persistent storage free
- 160GB outbound data transfer
- Auto-scaling support
- Great for Docker containers

### 📋 Setup Steps:

#### Step 1: Install Fly CLI
```bash
# Windows (PowerShell)
iwr https://fly.io/install.ps1 -useb | iex

# Or download from: https://fly.io/docs/hands-on/install-flyctl/
```

#### Step 2: Sign Up & Login
```bash
fly auth signup
# Or if you have account:
fly auth login
```

#### Step 3: Initialize Fly App
```bash
cd E:\project\cap2
fly launch

# Answer the prompts:
# App name: disease-predictioniq
# Region: Select closest to you
# PostgreSQL: No
# Redis: No
```

#### Step 4: Deploy!
```bash
fly deploy
```

#### Step 5: Access Your App
```bash
fly open
# Your app: https://disease-predictioniq.fly.dev
```

### 📝 Create `fly.toml` (if needed):
```toml
app = "disease-predictioniq"

[build]
  builder = "paketobuildpacks/builder:base"

[env]
  PORT = "8080"
  FLASK_ENV = "production"

[[services]]
  http_checks = []
  internal_port = 8080
  processes = ["app"]
  protocol = "tcp"

  [[services.ports]]
    force_https = true
    handlers = ["http"]
    port = 80

  [[services.ports]]
    handlers = ["tls", "http"]
    port = 443
```

---

## 2️⃣ **Koyeb** (Great Alternative to Render)

### ✨ Features:
- Always free tier
- Global edge network
- Auto-deploy from GitHub
- Free SSL certificates
- No sleep/cold starts

### 📋 Setup Steps:

1. **Sign Up**: https://app.koyeb.com/auth/signup
   - Use GitHub account

2. **Create New App**:
   - Click "Create App"
   - Select "GitHub"
   - Choose repository: `Disease-PredictionIQ`

3. **Configure**:
   ```
   Name: disease-predictioniq
   Branch: main
   Build: Buildpack
   Run command: gunicorn app:app
   Port: 8000
   Instance: Free (Eco)
   ```

4. **Deploy**:
   - Click "Deploy"
   - Wait 3-5 minutes
   - Access: `https://disease-predictioniq-[your-name].koyeb.app`

---

## 3️⃣ **PythonAnywhere** (Best for Python Learners)

### ✨ Features:
- Always free tier
- Native Python support
- Web-based IDE
- Specifically designed for Python
- Good for beginners

### 📋 Setup Steps:

#### Step 1: Create Account
- Go to: https://www.pythonanywhere.com
- Sign up for free "Beginner" account

#### Step 2: Open Bash Console
- Dashboard → "Bash" console

#### Step 3: Clone Repository
```bash
git clone https://github.com/JayAtria-7/Disease-PredictionIQ.git
cd Disease-PredictionIQ
```

#### Step 4: Create Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
pip install -r requirements-deploy.txt
```

#### Step 5: Configure Web App
- Go to "Web" tab
- Click "Add a new web app"
- Choose "Manual configuration"
- Python 3.10

#### Step 6: Set Source Code
```
Source code: /home/yourusername/Disease-PredictionIQ
Working directory: /home/yourusername/Disease-PredictionIQ
```

#### Step 7: Configure WSGI File
Click on WSGI configuration file and replace content:
```python
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/yourusername/Disease-PredictionIQ'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable
os.environ['FLASK_ENV'] = 'production'

# Import your Flask app
from app import app as application
```

#### Step 8: Set Virtual Environment
```
Virtualenv: /home/yourusername/.virtualenvs/myenv
```

#### Step 9: Reload & Access
- Click "Reload"
- Access: `http://yourusername.pythonanywhere.com`

---

## 4️⃣ **Vercel** (Best for Frontend + Serverless)

### ✨ Features:
- Unlimited free deployments
- Global CDN
- Automatic HTTPS
- Great for Next.js, but supports Python serverless

### 📋 Setup Steps:

#### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

#### Step 2: Create `vercel.json`
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

#### Step 3: Deploy
```bash
cd E:\project\cap2
vercel
```

#### Step 4: Follow Prompts
- Login with GitHub
- Link to existing project or create new
- Deploy!

**Note:** Vercel is better suited for serverless functions. Your app may need modifications.

---

## 5️⃣ **Glitch** (Community-Focused)

### ✨ Features:
- Always free
- Live code collaboration
- Instant deployment
- Great community

### 📋 Setup Steps:

1. **Sign Up**: https://glitch.com
   - Login with GitHub

2. **Import from GitHub**:
   - Click "New Project" → "Import from GitHub"
   - Paste: `https://github.com/JayAtria-7/Disease-PredictionIQ`

3. **Configure**:
   - Glitch auto-detects Python
   - Create `.glitch-assets` file if needed

4. **Access**:
   - `https://disease-predictioniq.glitch.me`

**Note:** Free tier may have limitations on always-on availability.

---

## 6️⃣ **Deta** (Micro Framework Focused)

### ✨ Features:
- Completely free
- No credit card required
- Micro services focused
- Built-in database

### 📋 Setup Steps:

1. **Install Deta CLI**:
```bash
iwr https://get.deta.dev/cli.ps1 -useb | iex
```

2. **Login**:
```bash
deta login
```

3. **Create New Micro**:
```bash
cd E:\project\cap2
deta new --python disease-predictioniq
```

4. **Deploy**:
```bash
deta deploy
```

5. **Access**:
```bash
deta details
```

---

## 7️⃣ **Back4App** (Backend as a Service)

### ✨ Features:
- Free tier available
- Built on Parse
- Auto-scaling
- Database included

### 📋 Setup Steps:

1. Sign up: https://www.back4app.com
2. Create new app
3. Deploy via GitHub integration
4. Configure environment

---

## 8️⃣ **Adaptable.io** (New Player)

### ✨ Features:
- Free tier
- One-click deploy from GitHub
- Auto-scaling

### 📋 Setup Steps:

1. Go to: https://adaptable.io
2. Connect GitHub
3. Select repository
4. Deploy!

---

## 🎯 **MY TOP 3 RECOMMENDATIONS FOR YOUR PROJECT:**

### 🥇 **#1: Render.com**
**Why?** 
- ✅ Easiest to use
- ✅ Great for Flask
- ✅ 750 hours free/month (enough for personal projects)
- ✅ Auto-deploy from GitHub
- ✅ Free SSL

**Setup Time:** 5 minutes

---

### 🥈 **#2: Fly.io**
**Why?**
- ✅ More powerful free tier
- ✅ 3 VMs free (better than Render's sleep policy)
- ✅ Great performance
- ✅ Docker support

**Setup Time:** 10 minutes (need to install CLI)

---

### 🥉 **#3: Koyeb**
**Why?**
- ✅ No sleep/cold starts
- ✅ Global edge network
- ✅ Similar to Render but newer
- ✅ Good free tier

**Setup Time:** 5 minutes

---

## 💡 **Special Use Cases:**

### For Learning/Testing:
→ **PythonAnywhere** (Native Python environment)

### For Portfolio Projects:
→ **Render** or **Fly.io** (Professional URLs)

### For Quick Demos:
→ **Glitch** (Instant sharing)

### For Production-Ready Free:
→ **Fly.io** (No sleep, better resources)

---

## 📊 **Cost After Free Tier:**

| Platform | Paid Starting At |
|----------|-----------------|
| Render | $7/month |
| Fly.io | $1.94/month (paid as you go) |
| Railway | $5/month (usage-based) |
| PythonAnywhere | $5/month |
| Koyeb | €5.42/month |

---

## 🚀 **Quick Start Command Summary:**

### Render (Easiest):
```bash
# No CLI needed - use web interface
# 1. Go to render.com
# 2. Connect GitHub
# 3. Deploy!
```

### Fly.io (Powerful):
```bash
iwr https://fly.io/install.ps1 -useb | iex
fly auth signup
cd E:\project\cap2
fly launch
fly deploy
```

### Railway:
```bash
npm install -g @railway/cli
railway login
railway link
railway up
```

### Koyeb:
```bash
# Use web interface - no CLI needed
# 1. Go to koyeb.com
# 2. Connect GitHub
# 3. Deploy!
```

---

## 🎯 **DECISION HELPER:**

**Choose Render if:**
- You want the easiest setup
- You're okay with sleep after inactivity
- You want GitHub auto-deploy

**Choose Fly.io if:**
- You want always-on free apps
- You're comfortable with CLI
- You want better performance

**Choose PythonAnywhere if:**
- You're learning Python
- You want web-based IDE
- You want simple Python-focused hosting

**Choose Koyeb if:**
- You want no cold starts
- You want global edge deployment
- Render alternative

---

## 📝 **Additional Files Needed for Some Platforms:**

### For Fly.io - Add `runtime.txt`:
```
python-3.11
```

### For all platforms - Ensure `requirements-deploy.txt` has:
```txt
Flask>=2.3.0
gunicorn>=21.2.0
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=1.0.0
Werkzeug>=2.3.0
```

---

## ✅ **Action Plan:**

1. **Try Render first** (5 min setup)
   - If satisfied → Done!
   
2. **If Render sleeps too much** → Try Fly.io
   - Install CLI
   - Deploy with `fly launch`
   
3. **If you want simplest** → Try Koyeb
   - Web interface only
   - Similar to Render

---

## 🆘 **Troubleshooting:**

### App crashes on deployment?
- Check logs in platform dashboard
- Ensure `requirements-deploy.txt` has all dependencies
- Check `PORT` environment variable support

### Model file errors?
- Verify models/ directory is in Git
- Check `.gitignore` doesn't exclude models
- Models are small (220KB) - should work everywhere

### Import errors?
- Add missing package to requirements
- Check Python version compatibility

---

**🎉 You have 10+ free deployment options! Start with Render.com for the easiest experience! 🚀**

**Made with ❤️ by Jay Prakash Kumar**
