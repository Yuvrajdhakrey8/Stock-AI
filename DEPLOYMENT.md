# DhakreyStock AI - AWS Free-Tier Serverless Deployment Guide

This guide walks you through deploying **DhakreyStock AI** to AWS with:
- **100% Free-Tier Architecture** ($0/month, scales to zero when idle).
- **Free Automated SSL Certificate (HTTPS)** for desktop and mobile browsers.
- **Continuous Deployment (CI/CD)** on every push to your GitHub repository.

---

## Architecture Overview

```
                      ┌──────────────────────────────────────┐
                      │    User (Mobile or Desktop Browser)   │
                      └──────────────────┬───────────────────┘
                                         │ HTTPS (Free SSL)
                                         ▼
                 ┌─────────────────────────────────────────────────┐
                 │       Frontend: AWS Amplify Hosting              │
                 │   - URL: https://main.<app-id>.amplifyapp.com    │
                 │   - Auto-deploys from GitHub on push            │
                 │   - Global CDN Edge Distribution                │
                 │   - Free Tier: 1,000 build mins/mo, 15 GB served│
                 └───────────────────────┬─────────────────────────┘
                                         │ Calls /api/*
                                         ▼
                 ┌─────────────────────────────────────────────────┐
                 │      Backend: AWS HTTP API Gateway (v2)         │
                 │   - URL: https://<api-id>.execute-api.amazonaws │
                 │   - Managed AWS TLS/SSL Certificate             │
                 │   - Free Tier: 1,000,000 requests/mo forever    │
                 └───────────────────────┬─────────────────────────┘
                                         │
                                         ▼
                 ┌─────────────────────────────────────────────────┐
                 │        Compute: AWS Lambda (Container)          │
                 │   - FastAPI + Mangum Serverless                 │
                 │   - Auto-deploys via GitHub Actions             │
                 │   - Free Tier: 1M invocations & 3.2M sec compute│
                 └─────────────────────────────────────────────────┘
```

---

## Prerequisites (One-Time Setup in AWS)

1. Log into your [AWS Management Console](https://aws.amazon.com/).
2. Create an **IAM User** with permissions for deployment:
   - Search **IAM** $\to$ **Users** $\to$ **Create user** (e.g. `dhakreystock-deployer`).
   - In **Attach policies directly**, choose `AdministratorAccess` (or scoped permissions for CloudFormation, Lambda, API Gateway, and ECR).
   - In **Security credentials** tab $\to$ **Create access key** $\to$ select **Command Line Interface (CLI)**.
   - Save your:
     - `Access Key ID`
     - `Secret Access Key`

---

## Step 1: Set Up Backend CI/CD on GitHub

We have included a GitHub Actions workflow in [`.github/workflows/deploy-backend.yml`](./.github/workflows/deploy-backend.yml).

1. In your GitHub repository: [https://github.com/Yuvrajdhakrey8/Stock-AI](https://github.com/Yuvrajdhakrey8/Stock-AI)
2. Go to **Settings** $\to$ **Secrets and variables** $\to$ **Actions**.
3. Click **New repository secret** and add:
   - Name: `AWS_ACCESS_KEY_ID`, Value: *(your IAM Access Key ID)*
   - Name: `AWS_SECRET_ACCESS_KEY`, Value: *(your IAM Secret Access Key)*
   - Name: `AWS_REGION`, Value: `ap-south-1` *(Mumbai, or `us-east-1`)*
4. Go to the **Actions** tab on GitHub $\to$ select **Deploy Backend to AWS Lambda (CI/CD)** $\to$ click **Run workflow**.
5. Once complete (takes ~2 minutes), click the job logs $\to$ note down your **HTTP API Gateway URL** from the output:
   ```
   https://xxxxxxxxxx.execute-api.ap-south-1.amazonaws.com
   ```

*(Alternative: You can also deploy locally using `sam build` and `sam deploy --guided` if you have AWS CLI installed).*

---

## Step 2: Deploy Frontend on AWS Amplify Hosting (Free SSL)

AWS Amplify connects directly to your GitHub repository and automatically provisions a free, managed SSL certificate.

1. In the AWS Console, search for **AWS Amplify**.
2. Click **Create new app** (or **Host web app**).
3. Select **GitHub** as your repository provider and click **Next**.
4. Authorize AWS Amplify to access your GitHub account.
5. Select your repository: `Yuvrajdhakrey8/Stock-AI` and branch: `main`.
6. Amplify automatically detects the included [`amplify.yml`](./amplify.yml) build configuration.
7. Click **Advanced settings** $\to$ **Add environment variable**:
   - Variable: `VITE_API_BASE_URL`
   - Value: `https://xxxxxxxxxx.execute-api.ap-south-1.amazonaws.com` *(from Step 1)*
8. Click **Next** $\to$ **Save and deploy**.

Amplify will automatically:
- Pull your latest code
- Run `npm ci` and `npm run build`
- Deploy to AWS global CDN
- Provision a free SSL certificate on your dedicated URL: `https://main.<app-id>.amplifyapp.com`

---

## Step 3: Verified Testing on Mobile & Desktop

1. Open your Amplify URL on your mobile phone browser (Chrome, Safari, Firefox).
2. Look for the secure padlock 🔒 in the URL bar confirming active HTTPS.
3. Test stock search (e.g., `RELIANCE`, `TCS`, `ZOMATO`), valuation meter, technical charts, and the **IPO Research** tab.

---

## Step 4: How Automatic CI/CD Works Going Forward

Whenever you push code changes to GitHub:

```powershell
git add .
git commit -m "Your update description"
git push origin main
```

- **Frontend changes:** AWS Amplify immediately detects the push and deploys the new build within ~60 seconds.
- **Backend changes:** GitHub Actions automatically runs `sam build` and redeploys the Lambda container.
- **Zero downtime & zero manual steps required.**
