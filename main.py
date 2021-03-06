from app import factory
from app.views.users.list import UserListView
from app.models import db
import os

app = factory('DevelopmentConfig')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
