# 🌱 EcoEdu Platform - Gamified Environmental Education

A gamified web application designed to educate students about environmental issues through interactive challenges, quizzes, and real-world actions. Built for the Government of Punjab's Smart Education initiative.

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [API Documentation](#api-documentation)
- [Usage Guide](#usage-guide)
- [Educational Content](#educational-content)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Core Gamification Features
- **Eco Points System**: Earn points by completing environmental challenges
- **Badge System**: Unlock achievements for reaching milestones
- **Leaderboard**: Compete with other students across schools
- **Progress Tracking**: Monitor completed challenges and learning journey

### Educational Content
- **Interactive Quizzes**: Test knowledge on environmental topics
- **Action Challenges**: Hands-on activities to make real environmental impact
- **Learning Categories**: 
  - Water Conservation
  - Renewable Energy
  - Waste Management
  - Climate Action
  - Biodiversity
  - Sustainable Transportation

### User Experience
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Profile Management**: Track personal progress and achievements
- **Real-time Feedback**: Instant notifications for completed activities
- **Offline Support**: Basic functionality works without internet connection

## 🛠 Technology Stack

### Frontend
- **HTML5, CSS3, JavaScript (ES6+)**
- **Responsive Design** with CSS Grid and Flexbox
- **Progressive Web App** capabilities
- **Local Storage** for offline functionality

### Backend
- **Node.js** with Express.js framework
- **JSON file-based storage** for MVP simplicity
- **RESTful API** design
- **CORS enabled** for cross-origin requests

### Design
- **Modern UI/UX** with gradients and animations
- **Accessible design** following web standards
- **Environmental theme** with green color palette
- **Font Awesome icons** for visual elements

## 📁 Project Structure

```
eco-edu-platform/
├── frontend/           # Client-side application
│   ├── index.html     # Main HTML file
│   ├── style.css      # Styles and responsive design
│   └── app.js         # JavaScript application logic
├── backend/           # Server-side application
│   ├── package.json   # Node.js dependencies
│   └── server.js      # Express server and API
├── data/              # JSON data storage
│   ├── challenges.json # Environmental challenges and quizzes
│   └── users.json     # User profiles and progress
├── docs/              # Documentation
└── README.md          # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites
- **Node.js** (version 14 or higher)
- **npm** (comes with Node.js)
- Web browser (Chrome, Firefox, Safari, Edge)

### Quick Start

1. **Clone or Download** the project to your local machine
2. **Navigate to the project directory**:
   ```bash
   cd eco-edu-platform
   ```

3. **Install Backend Dependencies**:
   ```bash
   cd backend
   npm install
   ```

4. **Start the Backend Server**:
   ```bash
   npm start
   ```
   Server will run on `http://localhost:3000`

5. **Open the Frontend**:
   - Open `frontend/index.html` in your web browser, or
   - Use a local web server (recommended):
   ```bash
   # Using Python 3
   cd frontend
   python -m http.server 8080
   ```
   Then visit `http://localhost:8080`

### Alternative Setup (Demo Mode)
If you don't want to run the backend server, the frontend will automatically fall back to demo mode with sample data.

## 📡 API Documentation

### Base URL
```
http://localhost:3000/api
```

### Endpoints

#### Users
- `GET /api/users` - Get all users
- `POST /api/users` - Create a new user
- `GET /api/users/:id` - Get user by ID

#### Challenges
- `GET /api/challenges` - Get all challenges
- `POST /api/users/:userId/complete-challenge/:challengeId` - Complete a challenge

#### Leaderboard
- `GET /api/leaderboard` - Get top 10 users by eco-points

#### Health Check
- `GET /api/health` - Server status

### Example API Requests

#### Create User
```javascript
POST /api/users
Content-Type: application/json

{
  "name": "Priya Sharma",
  "email": "priya@example.com",
  "school": "Delhi Public School",
  "grade": "10"
}
```

#### Complete Challenge
```javascript
POST /api/users/123/complete-challenge/1
```

## 📖 Usage Guide

### Getting Started
1. **Create Profile**: Start by creating your student profile
2. **Explore Dashboard**: View your progress and quick challenge
3. **Take Challenges**: Browse available environmental challenges
4. **Earn Points**: Complete quizzes and action challenges
5. **Check Leaderboard**: See how you rank among other students

### Challenge Types

#### Quiz Challenges
- Answer multiple-choice questions
- Learn environmental facts and concepts
- Instant feedback with explanations
- Need 70% to pass and earn points

#### Action Challenges
- Real-world environmental activities
- Document your actions (photos, reports)
- Make actual environmental impact
- Higher point rewards for completion

### Badge System
- **Eco Warrior** (🌱): Earn 100+ eco-points
- **Challenger** (🎯): Complete 5+ challenges
- **Tree Planter** (🌳): Complete tree-planting challenge

### Scoring System
- Quiz challenges: 15-25 points each
- Action challenges: 30-75 points each
- Bonus points for consistency and engagement

## 📚 Educational Content

### Categories Covered

#### Water Conservation
- Learn about water scarcity and conservation methods
- Practical tips for saving water at home and school
- Understanding water cycles and environmental impact

#### Renewable Energy
- Solar, wind, and other clean energy sources
- India's renewable energy potential and policies
- Personal actions to support clean energy

#### Waste Management
- Proper waste segregation techniques
- Recycling and composting methods
- Reducing single-use plastics

#### Climate Action
- Understanding climate change and global warming
- Carbon footprint calculation and reduction
- Tree planting and forest conservation

#### Biodiversity
- India's rich ecosystem and wildlife
- Threats to biodiversity and conservation efforts
- Creating wildlife-friendly environments

#### Sustainable Transportation
- Eco-friendly transport options
- Reducing carbon emissions from travel
- Promoting cycling and public transport

### Alignment with Educational Goals
- **NEP 2020**: Supports experiential learning approach
- **SDG Goals**: Aligns with Sustainable Development Goals
- **CBSE Curriculum**: Complements environmental studies
- **Punjab Education Policy**: Supports digital learning initiatives

## 🤝 Contributing

### How to Contribute
1. **Report Issues**: Found a bug or have a suggestion? Create an issue
2. **Add Content**: Contribute new environmental challenges or quizzes
3. **Improve Code**: Submit pull requests for enhancements
4. **Documentation**: Help improve documentation and guides

### Content Guidelines
- All content should be educational and age-appropriate
- Include reliable sources for environmental facts
- Make challenges engaging and actionable
- Follow accessibility guidelines

### Code Style
- Use modern JavaScript (ES6+)
- Follow consistent naming conventions
- Add comments for complex logic
- Ensure responsive design compatibility

## 📊 Future Enhancements

### Planned Features
- **Mobile App**: Native iOS and Android applications
- **Teacher Dashboard**: Class management and progress tracking
- **Social Features**: Share achievements and challenge friends
- **Advanced Analytics**: Detailed progress and learning insights
- **Multilingual Support**: Hindi and other regional languages
- **Offline Sync**: Full offline functionality with sync
- **School Integration**: Connect with existing school systems

### Technical Improvements
- **Database Integration**: PostgreSQL or MongoDB for production
- **User Authentication**: Secure login and registration
- **File Upload**: Photo submissions for action challenges
- **Real-time Updates**: WebSocket for live leaderboard updates
- **Performance Optimization**: Lazy loading and caching

## 📄 License

This project is developed for educational purposes as part of the Government of Punjab's Smart Education initiative. 

### Usage Rights
- ✅ Educational institutions can use freely
- ✅ Modify and adapt for local requirements
- ✅ Share with other educational organizations
- ❌ Commercial use without permission

## 📞 Support & Contact

For technical support or questions about implementation:

- **Developer**: Your Name
- **Email**: your.email@example.com
- **Organization**: Government of Punjab - Department of Higher Education
- **Project Type**: Smart Education Initiative

---

## 🌟 Getting Help

### Troubleshooting

#### Backend Server Won't Start
- Ensure Node.js is installed: `node --version`
- Check if port 3000 is available
- Install dependencies: `npm install`

#### Frontend Not Loading
- Try opening `frontend/index.html` directly in browser
- Check browser console for errors
- Ensure internet connection for external resources (fonts, icons)

#### Data Not Persisting
- Check if `data/` directory exists
- Ensure backend server has write permissions
- Verify JSON files are not corrupted

### FAQ

**Q: Can this work without internet?**
A: Yes, the frontend has offline demo mode with sample data.

**Q: How do I add new challenges?**
A: Edit `data/challenges.json` and restart the backend server.

**Q: Is this suitable for different grade levels?**
A: Yes, content is designed for grades 6-12 and college students.

**Q: How secure is the user data?**
A: This MVP stores data in local JSON files. For production, implement proper database and authentication.

---

**Built with 💚 for environmental education and awareness**
