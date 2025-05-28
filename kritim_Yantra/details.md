https://www.youtube.com/watch?v=xA24wu3z4q0
# Create a Simple Rest-api with Flask

to create a flask rest-api we have to import some lib
```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
```

we have to define the flask app and api 
```python
app = Flask(__name__)
api = Api(app)
```

for write the route we have to call the api 
```python
api.add_resource(PeopleResource,'/people')  #PeopleResource is a class name
api.add_resource(PersonResource,'/people/<int:person_id>')#PersonResource is a class name
```
https://github.com/rahuljawale30/Flask_rest_api/blob/master/kritim_Yantra/Screenshot%20(348).png
