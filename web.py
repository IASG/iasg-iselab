from iselab.models import db_init
from iselab.settings import DEBUG
from web.app import app

db_init()
app.run(debug=DEBUG)
