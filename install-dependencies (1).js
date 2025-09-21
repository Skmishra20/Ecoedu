const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log('🌱 Installing EcoEdu Platform Dependencies...\n');

const backendDir = path.join(__dirname, 'backend');

// Check if backend directory exists
if (!fs.existsSync(backendDir)) {
    console.error('❌ Backend directory not found!');
    process.exit(1);
}

// Install backend dependencies
console.log('📦 Installing backend dependencies...');
try {
    process.chdir(backendDir);
    execSync('npm install', { stdio: 'inherit' });
    console.log('✅ Backend dependencies installed successfully!\n');
} catch (error) {
    console.error('❌ Failed to install backend dependencies:', error.message);
    process.exit(1);
}

// Go back to root directory
process.chdir(__dirname);

console.log('🎉 All dependencies installed successfully!');
console.log('\n📋 Next steps:');
console.log('1. Start the backend server: cd backend && npm start');
console.log('2. Open login.html in your browser or use: python serve.py');
console.log('3. Create an account or use demo mode');
console.log('\n🚀 Happy learning with EcoEdu Platform!');