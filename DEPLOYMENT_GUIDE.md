# 🚀 DIU FAQ Chatbot — Deployment Guide

## Recommended deployment

For this Streamlit project, the recommended deployment is **Streamlit Community Cloud**.

Architecture:

```text
GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
Public URL
       ↓
DIU FAQ Chatbot
```

The deployed app reads the code and FAQ dataset directly from the GitHub repository.

## 1. Create a GitHub repository

Recommended repository name:

```text
DIU-FAQ-Chatbot
```

Keep these files in the **root** of the repository:

```text
DIU-FAQ-Chatbot/
├── .streamlit/
│   └── config.toml
├── data/
│   └── faqs.json
├── app.py
├── chatbot.py
├── preprocess.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 2. Push the project

From the project root:

```powershell
git init
git add .
git commit -m "Initial DIU FAQ Chatbot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/DIU-FAQ-Chatbot.git
git push -u origin main
```

If the repository already has a remote, use:

```powershell
git remote -v
```

and push normally:

```powershell
git add .
git commit -m "Update DIU FAQ Chatbot"
git push
```

## 3. Deploy

Open:

https://share.streamlit.io/

Sign in with GitHub and create a new app.

Choose:

```text
Repository: YOUR_USERNAME/DIU-FAQ-Chatbot
Branch: main
Main file path: app.py
```

Choose an app subdomain such as:

```text
diu-faq-chatbot
```

Then deploy.

The live address will look similar to:

```text
https://diu-faq-chatbot.streamlit.app
```

The exact URL depends on availability.

## 4. Future code changes

This is the important part.

After deployment, **do not edit the deployed server manually**.

Instead:

```text
VS Code
   ↓
Change code
   ↓
Test locally
   ↓
git add .
   ↓
git commit
   ↓
git push
   ↓
GitHub
   ↓
Streamlit Community Cloud
   ↓
Live app updates
```

For example:

```powershell
git add .
git commit -m "Improve FAQ matching"
git push
```

Streamlit Community Cloud monitors the connected GitHub repository and automatically updates the deployed app after committed changes.

## 5. If FAQ data changes

Edit:

```text
data/faqs.json
```

Then:

```powershell
git add data/faqs.json
git commit -m "Update DIU FAQ dataset"
git push
```

The live chatbot will receive the updated dataset.

## 6. If Python code changes

For example, after changing `chatbot.py`:

```powershell
git add chatbot.py
git commit -m "Improve chatbot matching"
git push
```

The app will redeploy/update automatically.

## 7. If dependencies change

Update:

```text
requirements.txt
```

Then:

```powershell
git add requirements.txt
git commit -m "Update dependencies"
git push
```

Community Cloud detects dependency changes and reinstalls the environment.

## 8. Important deployment rules

- Keep `app.py` in the repository root.
- Keep `requirements.txt` in the repository root.
- Use forward-slash paths in Python code.
- Keep `data/faqs.json` inside the GitHub repository.
- Do not put passwords, API keys, or private credentials in GitHub.
- Test locally before pushing.
- Important DIU information should be verified against current official DIU sources.

## 9. Local development

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

## 10. Development workflow

Use this cycle for the whole project:

```text
1. Edit
2. Run locally
3. Test
4. Fix
5. git add .
6. git commit -m "..."
7. git push
8. Check live Streamlit app
```

This means you can continue improving the chatbot after it is live without redeploying it manually every time.
