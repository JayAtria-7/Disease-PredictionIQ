# 🚀 Vercel Deployment Guide for Disease PredictionIQ

**Author:** Jay Prakash Kumar  
**Platform:** Vercel (Free Tier)

---

## 📋 What is Vercel?

Vercel is a cloud platform optimized for frontend frameworks and serverless functions. It offers:
- ✅ **Free tier** with generous limits
- ✅ **Automatic HTTPS** and SSL
- ✅ **Global CDN** for fast content delivery
- ✅ **Auto-deploy** from GitHub
- ✅ **Custom domains** for free
- ✅ **Zero configuration** for many frameworks

---

## ⚠️ Important Notes for Flask Apps on Vercel

Vercel is primarily designed for:
- Next.js, React, Vue, Svelte (frontend frameworks)
- Node.js serverless functions
- Static sites

**Flask Compatibility:**
- ⚠️ Vercel supports Python, but it runs as **serverless functions**
- ⚠️ Each request spins up a new function (cold starts possible)
- ⚠️ Better suited for API endpoints rather than full Flask apps
- ⚠️ File uploads and persistent storage have limitations

**Recommendation:** For a full Flask app like ours, **Render.com** or **Fly.io** are better choices. But if you want to try Vercel, follow the guide below!

---

## 🎯 Deployment Methods

### Method 1: Vercel Web Dashboard (Easiest)
### Method 2: Vercel CLI (Command Line)

---

## 📦 Method 1: Deploy via Web Dashboard (RECOMMENDED)

### Step 1: Prepare Your Project

I've already created the necessary files:
- ✅ `vercel.json` - Vercel configuration
- ✅ `api/index.py` - Serverless function wrapper
- ✅ `requirements-deploy.txt` - Python dependencies

### Step 2: Push to GitHub

Your code is already on GitHub at:
```
https://github.com/JayAtria-7/Disease-PredictionIQ
```

### Step 3: Sign Up for Vercel

1. Go to: **https://vercel.com**
2. Click **"Sign Up"**
3. Choose **"Continue with GitHub"**
4. Authorize Vercel to access your GitHub account

### Step 4: Import Your Project

1. After login, click **"Add New..."** → **"Project"**
2. Find **"Disease-PredictionIQ"** in the list
3. Click **"Import"**

### Step 5: Configure Project

Vercel will auto-detect your project. Configure:

```
Project Name: disease-predictioniq
Framework Preset: Other
Root Directory: ./
Build Command: (leave empty)
Output Directory: (leave empty)
Install Command: pip install -r requirements-deploy.txt
```

### Step 6: Environment Variables (Optional)

Add if needed:
```
FLASK_ENV = production
```

### Step 7: Deploy!

1. Click **"Deploy"**
2. Wait 2-5 minutes for build
3. Your app will be live!

### Step 8: Access Your App

Vercel will provide a URL like:
```
https://disease-predictioniq.vercel.app
```

Or your custom domain:
```
https://disease-predictioniq-[random].vercel.app
```

---

## 💻 Method 2: Deploy via Vercel CLI

### Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

Or with Yarn:
```bash
yarn global add vercel
```

### Step 2: Login to Vercel

```bash
vercel login
```

This will open your browser to authenticate.

### Step 3: Navigate to Project

```bash
cd E:\project\cap2
```

### Step 4: Deploy

```bash
vercel
```

Follow the prompts:
```
? Set up and deploy "E:\project\cap2"? [Y/n] Y
? Which scope do you want to deploy to? [Your Name]
? Link to existing project? [y/N] N
? What's your project's name? disease-predictioniq
? In which directory is your code located? ./
```

### Step 5: Deploy to Production

```bash
vercel --prod
```

### Step 6: Access Your App

CLI will show the deployment URL:
```
https://disease-predictioniq.vercel.app
```

---

## 🔧 Configuration Files Created

### 1. `vercel.json`
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

**What it does:**
- Tells Vercel to build `app.py` as a Python serverless function
- Routes all requests to your Flask app

### 2. `api/index.py`
```python
from app import app
application = app
```

**What it does:**
- Creates a WSGI-compatible entry point for Vercel
- Wraps your Flask app for serverless execution

---

## ⚙️ Advanced Configuration (Optional)

### Custom Domain

1. Go to Vercel Dashboard → Your Project
2. Click **"Settings"** → **"Domains"**
3. Add your custom domain
4. Update DNS records as shown

### Environment Variables

1. Dashboard → Project → **"Settings"** → **"Environment Variables"**
2. Add variables:
   ```
   FLASK_ENV = production
   DEBUG = False
   ```

### Build Settings

If you need custom build settings:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python",
      "config": {
        "maxLambdaSize": "15mb"
      }
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "env": {
    "FLASK_ENV": "production"
  }
}
```

---

## 📊 Vercel Free Tier Limits

- ✅ **Bandwidth:** 100 GB/month
- ✅ **Builds:** Unlimited
- ✅ **Serverless Functions:** 100 GB-hours/month
- ✅ **Function Duration:** 10 seconds max
- ✅ **Function Size:** 50 MB max
- ✅ **Deployments:** Unlimited

---

## 🐛 Troubleshooting

### Issue 1: "Module not found" Error

**Solution:** Ensure all dependencies are in `requirements-deploy.txt`

```bash
# Update requirements
pip freeze > requirements-deploy.txt
```

### Issue 2: "Function timeout"

**Problem:** Vercel functions have 10-second timeout
**Solution:** Optimize your code or use a different platform (Render, Fly.io)

### Issue 3: Static files not loading

**Solution:** Update `vercel.json`:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    },
    {
      "src": "static/**",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

### Issue 4: Model files not found

**Problem:** Serverless functions may have storage limitations
**Solution:** 
- Ensure `models/` directory is committed to Git
- Check model file sizes (should be < 50MB)
- Consider hosting models separately (AWS S3, etc.)

### Issue 5: Cold starts (slow first load)

**Problem:** Serverless functions sleep when not in use
**Solution:** 
- Accept cold starts (free tier limitation)
- Upgrade to paid tier for warmer instances
- Or use Render/Fly.io for always-on apps

---

## 🔍 Checking Deployment Status

### Via CLI:
```bash
vercel ls
```

### Via Dashboard:
1. Go to https://vercel.com/dashboard
2. Click on your project
3. View deployments and logs

### View Logs:
```bash
vercel logs [deployment-url]
```

---

## 🎯 Post-Deployment Checklist

After deploying, test:

- [ ] Home page loads
- [ ] Navigation works
- [ ] Prediction form submits
- [ ] Results display correctly
- [ ] Model comparison section loads
- [ ] Static files (CSS, JS) load
- [ ] Mobile responsiveness works
- [ ] No console errors

---

## 📈 Monitoring & Analytics

### Vercel Analytics (Free)

1. Dashboard → Project → **"Analytics"**
2. View:
   - Page views
   - Top pages
   - Unique visitors
   - Performance metrics

### Add Custom Analytics

Update `templates/index.html` to add:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-ID');
</script>
```

---

## 🔄 Auto-Deployment

Once connected to GitHub, Vercel automatically:
- ✅ Deploys on every push to `main` branch
- ✅ Creates preview deployments for pull requests
- ✅ Shows deployment status in GitHub

### Disable Auto-Deploy (Optional):

1. Dashboard → Project → **"Settings"** → **"Git"**
2. Configure deployment branches

---

## 🚀 Continuous Deployment Workflow

```bash
# Make changes locally
code app.py

# Test locally
python app.py

# Commit changes
git add .
git commit -m "Update feature"

# Push to GitHub
git push

# Vercel automatically deploys! 🎉
# Check: https://disease-predictioniq.vercel.app
```

---

## ⚡ Quick Command Reference

```bash
# Login
vercel login

# Deploy
vercel

# Deploy to production
vercel --prod

# List deployments
vercel ls

# View logs
vercel logs

# Remove deployment
vercel rm [deployment-id]

# Open project in browser
vercel open

# Link local project to Vercel
vercel link
```

---

## 🎨 Custom Domain Setup

### Step 1: Add Domain in Vercel

1. Dashboard → Project → **"Settings"** → **"Domains"**
2. Click **"Add"**
3. Enter your domain: `yourdomain.com`

### Step 2: Configure DNS

Add these records in your domain registrar:

**For Root Domain:**
```
Type: A
Name: @
Value: 76.76.21.21
```

**For www Subdomain:**
```
Type: CNAME
Name: www
Value: cname.vercel-dns.com
```

### Step 3: Verify

Vercel will automatically verify and issue SSL certificate.

---

## 💡 Vercel vs Other Platforms

| Feature | Vercel | Render | Fly.io |
|---------|--------|--------|--------|
| **Best For** | Frontend + API | Full Flask apps | Always-on apps |
| **Cold Starts** | Yes | Yes (free tier) | No |
| **Setup** | Very Easy | Easy | Medium |
| **Free Tier** | Generous | 750hrs/mo | 3 VMs |
| **Python Support** | Serverless only | Native | Docker |
| **Recommendation** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## ⚠️ When NOT to Use Vercel for This Project

- ❌ If you need long-running processes
- ❌ If you have heavy ML model loading (>10s startup)
- ❌ If you need persistent storage
- ❌ If you want no cold starts

**Better Alternatives:**
- **Render.com** - Best for Flask apps
- **Fly.io** - Best for always-on apps
- **Railway** - Quick deployment

---

## ✅ Deployment Steps Summary

1. **Commit Changes:**
   ```bash
   git add vercel.json api/index.py
   git commit -m "Add Vercel deployment configuration"
   git push
   ```

2. **Go to Vercel:**
   - Visit: https://vercel.com
   - Sign up with GitHub

3. **Import Project:**
   - Click "Add New" → "Project"
   - Select "Disease-PredictionIQ"
   - Click "Import"

4. **Deploy:**
   - Click "Deploy"
   - Wait 3-5 minutes

5. **Access:**
   - Visit: `https://disease-predictioniq.vercel.app`

---

## 🆘 Need Help?

- **Vercel Docs:** https://vercel.com/docs
- **Vercel Community:** https://github.com/vercel/vercel/discussions
- **Support:** support@vercel.com

---

## 📝 Next Steps After Deployment

1. **Test thoroughly** - Check all features work
2. **Add custom domain** (optional)
3. **Enable analytics**
4. **Share your link** on LinkedIn, GitHub
5. **Monitor performance**

---

## 🎯 Final Notes

**Vercel is great for:**
- ✅ Quick deployments
- ✅ Frontend-heavy apps
- ✅ API endpoints
- ✅ Preview deployments

**For this full Flask ML app, consider:**
- ⭐ **Render.com** (easiest, best for Flask)
- ⭐ **Fly.io** (no cold starts, always-on)

But Vercel will work if you accept serverless limitations!

---

**Made with ❤️ by Jay Prakash Kumar**

**Ready to deploy? Go to https://vercel.com and import your GitHub repo! 🚀**
