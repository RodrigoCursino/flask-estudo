from app             import api
from flask_restplus  import fields

# Posts
model_posts = api.model('Posts', {
    'id'  : fields.Integer,
    'text': fields.String,
})

# Users

model_login = api.model('Login',{
    'username' : fields.String(required=True),
    'password' : fields.String(required=True),
    'email'    : fields.String(required=True),
})

model_user = api.model('User',{
    'id'       : fields.Integer,
    'username' : fields.String,
    'name'     : fields.String,
    'password' : fields.String,
    'email'    : fields.String,
    'posts'    : fields.List(fields.Nested(model_posts),default=[]),
})

# players
model_player = api.model('Player',{
    'id'            : fields.Integer,
    'team_id'       : fields.Integer,
    'name'          : fields.String, 
    'country'       : fields.String, 
    'position'      : fields.String, 
    'player_number' : fields.String, 
    'height'        : fields.Float, 
    'weight'        : fields.Integer,          
    'picture'       : fields.String,         
    'feature'       : fields.String,         
    'default_leg'   : fields.String,    
    'birth_date'    : fields.DateTime,       
    'date_begin'    : fields.DateTime,       
    'date_end'      : fields.DateTime,       
})

model_player_list = api.model('Player',{
    'id'            : fields.Integer,
    'name'          : fields.String, 
    'country'       : fields.String, 
    'position'      : fields.String, 
    'height'        : fields.Float, 
    'weight'        : fields.Integer,          
    'picture'       : fields.String,         
    'feature'       : fields.String,         
    'default_leg'   : fields.String,    
    'birth_date'    : fields.DateTime,       
    'date_begin'    : fields.DateTime,       
    'date_end'      : fields.DateTime,        
})

# teams 
model_team = api.model('Team',{
   'id'                : fields.Integer,
   'name'              : fields.String,
   'brand'             : fields.String,
   'color'             : fields.String,
   'country'           : fields.String,
   'alternateColor'    : fields.String,
   'abbreviation'      : fields.String,
   'uniform_one'       : fields.String(default=None),
   'uniform_two'       : fields.String(default=None),
   'foundation_date'   : fields.DateTime(default=None),
#    'players'           : fields.List(fields.Nested(model_player),default=[]),   
})

# teams 
model_teams_players = api.model('TeamsPlayers',{
   'date_begin'    : fields.DateTime,
   'date_end'      : fields.DateTime,  
   'player_number' : fields.String,          
   'team'          : fields.Nested(model_team),  
   'player'        : fields.Nested(model_player_list),     
})

