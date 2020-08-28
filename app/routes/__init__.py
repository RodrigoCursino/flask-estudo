from app import api

#login route
login_route    = api.namespace('login', description='User Authentication')
#register route
register_route = api.namespace('register', description='User Register')
# users route
users_route    = api.namespace('users', description='User CRUD')
# posts route
posts_route    = api.namespace('posts', description='Posts CRUD')
# player route
players_route  = api.namespace('players', description='Player CRUD')
# teams route
teams_route    = api.namespace('teams', description='Team CRUD')
# teams_players route
teams_players_route  = api.namespace('teams-players', description='Teams and Players CRUD')