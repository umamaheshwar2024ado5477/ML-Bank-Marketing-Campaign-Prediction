# Deployment Guide for Streamlit Community Cloud

## Step-by-Step Deployment Instructions

### Prerequisites
1. GitHub account
2. Streamlit Community Cloud account (free - sign up at https://share.streamlit.io)

### Step 1: Prepare Your Repository

1. **Create a new GitHub repository**:
   - Go to https://github.com/new
   - Repository name: `bank-marketing-ml-prediction` (or your choice)
   - Description: "Bank Marketing Campaign Prediction using ML"
   - Make it **Public** (required for free Streamlit hosting)
   - Click "Create repository"

### Step 2: Upload Files to GitHub

**Option A: Using Git Command Line**
```bash
cd c:\UmaMahesh\ML_Assignment_2
git init
git add .
git commit -m "Initial commit: Bank Marketing ML project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

**Option B: Using GitHub Desktop or Web Interface**
- Use GitHub Desktop to add and commit files
- Or upload files directly through GitHub web interface

**Important**: Make sure to include:
- ✅ `app.py`
- ✅ `train_model.py`
- ✅ `requirements.txt`
- ✅ `README.md`
- ✅ `bank-full.csv`
- ✅ `models/` folder with all `.pkl` files
- ✅ `.gitignore`
- ❌ Do NOT upload `venv/` folder (excluded by .gitignore)

### Step 3: Deploy on Streamlit Community Cloud

1. **Go to Streamlit Cloud**:
   - Visit https://share.streamlit.io
   - Click "Sign in" and authorize with GitHub

2. **Create New App**:
   - Click "New app" button
   - Select your repository: `YOUR_USERNAME/YOUR_REPO_NAME`
   - Branch: `main`
   - Main file path: `app.py`
   - App URL (optional): Choose a custom subdomain or use auto-generated

3. **Advanced Settings** (Optional):
   - Python version: 3.9+ (default is usually fine)
   - Secrets: Not needed for this project

4. **Deploy**:
   - Click "Deploy!" button
   - Wait for deployment (usually 2-5 minutes)
   - Streamlit will install dependencies from `requirements.txt` and start your app

### Step 4: Verify Deployment

1. Once deployment is complete, you'll get a URL like:
   ```
   https://your-app-name.streamlit.app
   ```

2. Test the app:
   - Open the URL in a browser
   - Select a model from the sidebar
   - Fill in the form with sample data
   - Click "Predict Subscription"
   - Verify the prediction works

### Step 5: Share Your Links

For assignment submission, you'll need:

1. **GitHub Repository Link**:
   ```
   https://github.com/YOUR_USERNAME/YOUR_REPO_NAME
   ```

2. **Live Streamlit App Link**:
   ```
   https://your-app-name.streamlit.app
   ```

## Troubleshooting Common Issues

### Issue 1: App Won't Start
**Solution**: Check the logs in Streamlit Cloud dashboard. Common causes:
- Missing files in repository
- Incorrect file paths in `app.py`
- Missing dependencies in `requirements.txt`

### Issue 2: Models Not Found
**Solution**: Ensure the `models/` folder with all `.pkl` files is committed to GitHub

### Issue 3: Import Errors
**Solution**: 
- Verify all packages in `requirements.txt` are correct
- Check Python version compatibility
- Try redeploying the app

### Issue 4: Large File Size Warning
**Solution**: The dataset `bank-full.csv` is about 4.6MB, which is fine. But if you get warnings:
- Ensure you're not uploading the `venv/` folder
- GitHub has a 100MB file limit (we're well under that)

## Updating Your Deployed App

After deployment, any changes you push to GitHub will automatically trigger a redeployment:

```bash
git add .
git commit -m "Update message"
git push
```

Streamlit Cloud will detect the changes and redeploy within a few minutes.

## App Management

- **View Logs**: Click on your app in Streamlit Cloud dashboard → "Manage app" → "Logs"
- **Restart App**: "Reboot app" button in the dashboard
- **Delete App**: "Delete app" option (be careful!)
- **Change Settings**: Edit advanced settings from the app management page

## Best Practices

1. **Keep repository public** for free hosting
2. **Don't commit sensitive data** (use Streamlit secrets for API keys if needed)
3. **Test locally first** before pushing to GitHub
4. **Monitor app usage** through Streamlit Cloud analytics
5. **Keep dependencies minimal** for faster deployment

## Resource Limits (Free Tier)

- **Memory**: 1 GB RAM
- **CPU**: Shared
- **Apps**: Up to 3 public apps
- **Sleep**: Apps sleep after inactivity (wake up when accessed)

Our app should work fine within these limits!

## Need Help?

- Streamlit Docs: https://docs.streamlit.io/streamlit-community-cloud
- Streamlit Forum: https://discuss.streamlit.io
- GitHub Issues: Use your repository's Issues tab

---

Good luck with your deployment! 🚀
