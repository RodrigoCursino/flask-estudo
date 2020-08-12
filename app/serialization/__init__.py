from app             import api
from flask_restplus  import fields

# Posts
model_posts = api.model('Posts', {
    'id'  : fields.Integer,
    'text': fields.String,
})

# Users
model_user = api.model('User',{
    'id'       : fields.Integer,
    'username' : fields.String,
    'name'     : fields.String,
    'password' : fields.String,
    'email'    : fields.String,
    'posts'    : fields.List(fields.Nested(model_posts)),
})

# players
model_player = api.model('Player',{
    'id'          : fields.Integer,
    'name'        : fields.String,           
    'picture'     : fields.String,         
    'feature'     : fields.String,         
    'default_leg' : fields.String,    
    'birth_date'  : fields.DateTime,       
})

# teams 
model_team = api.model('Team',{
   'id'                : fields.Integer,
   'name'              : fields.String,
   'brand'             : fields.String,
   'uniform_one'       : fields.String,
   'uniform_two'       : fields.String,
   'foundation_date'   : fields.DateTime, 
})

# teams 
model_teams_players = api.model('TeamsPlayers',{
   'id'            : fields.Integer,
   'date_begin'    : fields.DateTime,
   'date_end'      : fields.DateTime,  
   'player_number' : fields.String,          
   'team'          : fields.List(fields.Nested(model_team)),  
   'player'        : fields.List(fields.Nested(model_player)),     
})