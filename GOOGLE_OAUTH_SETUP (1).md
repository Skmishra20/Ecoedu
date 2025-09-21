# Google OAuth Setup Instructions

This guide will help you configure Google Sign-In for your EcoEdu Platform.

## Step 1: Create Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Make note of your project ID

## Step 2: Enable Google+ API

1. In the Google Cloud Console, go to "APIs & Services" > "Library"
2. Search for "Google+ API" and enable it
3. Alternatively, you can enable "Google Identity" API

## Step 3: Configure OAuth Consent Screen

1. Go to "APIs & Services" > "OAuth consent screen"
2. Choose "External" user type (unless you have a Google Workspace account)
3. Fill in the required information:
   - **App name**: EcoEdu Platform
   - **User support email**: Your email address
   - **Developer contact information**: Your email address
4. Add your domain to "Authorized domains" if you have one
5. Save and continue through the scopes and test users sections

## Step 4: Create OAuth 2.0 Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth 2.0 Client IDs"
3. Choose "Web application"
4. Set the name to "EcoEdu Platform Web Client"
5. Add Authorized JavaScript origins:
   - `http://localhost:5500` (if using Live Server)
   - `http://127.0.0.1:5500`
   - `http://localhost:3000`
   - Add your production domain when ready
6. Add Authorized redirect URIs (optional for this implementation):
   - `http://localhost:5500/frontend/login.html`
   - Add your production URLs when ready
7. Click "Create"

## Step 5: Configure Your Application

1. Copy the **Client ID** from the credentials page
2. Open `frontend/auth.js` and replace `YOUR_GOOGLE_CLIENT_ID.apps.googleusercontent.com` with your actual Client ID:
   ```javascript
   const GOOGLE_CLIENT_ID = 'your-actual-client-id.apps.googleusercontent.com';
   ```

3. For production, set the environment variable in your server:
   ```bash
   export GOOGLE_CLIENT_ID="your-actual-client-id.apps.googleusercontent.com"
   ```

## Step 6: Install Dependencies

Run the following command in your backend directory:

```bash
npm install
```

This will install the `google-auth-library` package that was added to your `package.json`.

## Step 7: Test the Integration

1. Start your backend server:
   ```bash
   cd backend
   npm run dev
   ```

2. Open your frontend (using Live Server or similar)

3. Navigate to the login page and test the "Continue with Google" button

## Important Security Notes

- **Never commit your Google Client ID to version control if it contains sensitive information**
- For production, always use environment variables for configuration
- Make sure to add your production domain to the authorized origins in Google Cloud Console
- Consider implementing additional security measures like CSRF protection

## Troubleshooting

### Common Issues:

1. **"Invalid origin" error**: Make sure your current URL is added to "Authorized JavaScript origins"

2. **"Token verification failed"**: Ensure your Client ID matches exactly between frontend and backend

3. **"Popup blocked"**: Make sure popups are enabled for your site, or implement the redirect flow instead

4. **Network errors**: Check that your backend server is running and accessible

### Development vs Production

- **Development**: Use `http://localhost` origins
- **Production**: Use your actual domain with HTTPS

## Next Steps

Once Google Sign-In is working:

1. Consider adding profile completion flow for users who sign in with Google
2. Implement account linking for users who want to add Google sign-in to existing accounts
3. Add other OAuth providers (Facebook, GitHub, etc.) using similar patterns
4. Implement proper user session management