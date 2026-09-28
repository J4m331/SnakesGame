#Imports go here
from .user import user_views
from .index import index_views
from .auth import auth_views
from .host import host_views

views = [user_views, index_views, auth_views, host_views] 
# Blueprints must be added to this list