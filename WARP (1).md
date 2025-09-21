# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Architecture Overview

The EcoEdu Platform is a gamified environmental education web application built for the Government of Punjab's Smart Education initiative. It features a **two-tier architecture** with offline capabilities:

### Backend (Node.js/Express)
- **Entry Point**: `backend/server.js` - Express server with RESTful API endpoints
- **Data Storage**: JSON files in `data/` directory (users.json, challenges.json)
- **Key Dependencies**: express, cors, body-parser, uuid
- **Port**: 3000 by default (configurable via PORT environment variable)

### Frontend (Vanilla JavaScript SPA)
- **Entry Point**: `frontend/index.html` with `frontend/app.js` as main application logic
- **State Management**: Global `appState` object with currentUser, challenges, leaderboard
- **Offline Capability**: Falls back to demo data when backend is unavailable
- **Local Storage**: Persists user data for offline functionality

### Data Layer
- **User Profiles**: UUID-based users with ecoPoints, badges, completedChallenges
- **Challenges**: Quiz and action types with points, difficulty levels, and categories
- **Gamification**: Points system, badge rewards, and leaderboard rankings

## Common Development Commands

### Backend Operations
```bash
# Install backend dependencies
cd backend && npm install

# Start development server with auto-reload
npm run dev

# Start production server
npm start

# Check server health
curl http://localhost:3000/api/health
```

### Frontend Development
```bash
# Serve frontend with Python (from frontend/ directory)
cd frontend && python -m http.server 8080

# Or simply open index.html in browser for basic testing
# Note: Backend API calls will fail gracefully to demo mode
```

### Full Stack Testing
```bash
# Start backend in one terminal
cd backend && npm start

# Serve frontend in another terminal (recommended for full functionality)
cd frontend && python -m http.server 8080
```

## Key Application Flow

### User Journey
1. **Profile Creation**: Users register with name, email, school, grade
2. **Challenge Selection**: Browse available environmental challenges (quiz/action types)
3. **Challenge Completion**: 
   - Quiz challenges require 70% score to pass
   - Action challenges are self-reported completions
4. **Gamification**: Earn eco-points, unlock badges, compete on leaderboards

### API Integration Pattern
The frontend implements a resilient API pattern:
```javascript
// Try API first, fallback to local data
const makeApiCall = async (endpoint, method = 'GET', data = null) => {
    // API call with error handling
    // Returns null on failure, enabling demo mode fallback
};
```

### State Management
- **appState** object holds current user, challenges, leaderboard
- **localStorage** persists user data across sessions
- **Modal system** for challenge interactions with quiz logic

## Challenge System Architecture

### Challenge Types
- **Quiz Challenges**: Multiple-choice questions with explanations and scoring
- **Action Challenges**: Real-world environmental activities with instructions

### Scoring & Badges
- **Points**: 15-75 points per challenge based on difficulty
- **Badge System**: 'eco-warrior' (100+ points), 'challenger' (5+ challenges)
- **Difficulty Levels**: 1-5 dots indicating complexity

### Content Categories
- water-conservation, renewable-energy, waste-management
- climate-action, biodiversity, sustainable-transport, plastic-reduction

## Database Schema (JSON Structure)

### User Object
```javascript
{
  id: "uuid",
  name: "string",
  email: "string", 
  school: "string",
  grade: "string",
  ecoPoints: number,
  badges: ["badge-id"],
  completedChallenges: ["challenge-id"],
  createdAt: "ISO string"
}
```

### Challenge Object
```javascript
{
  id: "string",
  title: "string",
  description: "string", 
  type: "quiz" | "action",
  points: number,
  difficulty: 1-5,
  category: "string",
  estimatedTime: "string",
  questions: [...] | instructions: [...]
}
```

## Development Patterns

### Frontend Module Organization
- **Tab Navigation**: Single-page app with tab-based navigation
- **Modal System**: Reusable modal for challenge interactions
- **API Resilience**: Graceful degradation when backend unavailable
- **Local Storage**: User data persistence for offline mode

### Backend API Design
- **RESTful endpoints** following `/api/resource` pattern
- **File-based storage** with atomic read/write operations
- **CORS enabled** for cross-origin frontend requests
- **UUID generation** for user identification

### Error Handling Strategy
- Frontend shows user-friendly notifications for all operations
- Backend returns appropriate HTTP status codes with error messages
- Fallback to demo data when API calls fail
- Local storage backup for user data persistence

## Testing Single Components

### Test Individual Challenge
```javascript
// In browser console, load specific challenge
openChallengeModal('1'); // For plant-a-tree challenge
openChallengeModal('2'); // For water conservation quiz
```

### Test API Endpoints
```bash
# Test user creation
curl -X POST http://localhost:3000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","school":"Test School","grade":"10"}'

# Test challenge completion
curl -X POST http://localhost:3000/api/users/{userId}/complete-challenge/1

# View leaderboard
curl http://localhost:3000/api/leaderboard
```

## Educational Content Guidelines

### Challenge Creation
- Include clear instructions and learning objectives
- Provide explanations for quiz answers
- Align with SDG goals and NEP 2020 guidelines
- Use age-appropriate content for grades 6-12

### Localization Considerations
- Content focuses on Indian environmental issues
- References local policies and environmental challenges
- Uses familiar contexts (schools in Punjab, local environmental problems)

## Deployment Notes

### MVP Limitations
- JSON file storage (not suitable for production scale)
- No user authentication or session management
- Basic error handling and logging
- No rate limiting or security measures

### Production Readiness Path
- Migrate to PostgreSQL/MongoDB for data persistence
- Implement OAuth authentication system  
- Add comprehensive logging and monitoring
- Implement proper validation and sanitization
- Add WebSocket support for real-time leaderboard updates

This architecture prioritizes simplicity and educational value while maintaining offline capability and smooth user experience. The modular design allows for incremental enhancement toward a full production system.
