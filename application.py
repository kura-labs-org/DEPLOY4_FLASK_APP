import helper,json
from flask import Flask,request,Response,render_template_string,jsonify
from flask_restful import Resource,Api,reqparse
import os
import werkzeug
UPLOAD_DIR='./fileupload'
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)
application = app = Flask(__name__)
api = Api(app)
class Base(Resource):
    def get(self):
        helper.start()
        return ("Init")
class Users(Resource):
    def get(self,name=None):
        if name != None:
            res_data = helper.get_user_byname(name)
        labels = helper.get_all_users()
        #return Response(json.dumps(labels),mimetype='application/json')
        return Response(render_template_string('''


        <table>
                <tr>
                    <td> ID </td> 
                    <td> Name </td>
                    <td> Team </td>
                    <td> Active </td>
                    <td> Total_Score </td>
                </tr>


        {% for user_id, user_name, team_id,is_active,total_score in labels['users'] %}

                <tr>
                    <td>{{ user_id }}</td> 
                    <td>{{ user_name }}</td>
                    <td>{{ team_id }}</td>
                    <td> {{ is_active }}</td>
                    <td> {{ total_score}} </td>
                </tr>

        {% endfor %}


        </table>
    ''', labels=labels))
    def post(self,user_name):
        res = helper.create_user(user_name)
        print (res)
        if res is None:
            return Response(f"err:{user_name} not found",mimetype='application/json')
        return Response(json.dumps(res),mimetype='application/json')
    def put(self,user_name):
        req_data = request.get_json()
        print(req_data)
        id = req_data['team_id']
        res_data = helper.add_user_to_team(user_name,id)
        if res_data is None:
            response = Response(f"err:{user_name} or {id} not found",mimetype='application/json')
            return response
        # Return response
        response = Response(json.dumps(res_data), mimetype='application/json')
        return response

    def delete(self,username):
        res = helper.delete_user(username)
        if res is None:
            return Response(f"err:{username} not found",mimetype='application/json')
        return Response(json.dumps(res),mimetype='application/json')
class Teams(Resource):
    def get(self):
        labels = helper.get_all_teams()
        return Response(render_template_string('''
        <table>
                <tr>
                    <td> ID </td> 
                    <td> Name </td>
                    <td> score </td>
                </tr>


        {% for team_id, team_name,total_score in labels['teams'] %}

                <tr>
                    <td>{{ team_id }}</td> 
                    <td>{{ team_name }}</td>
                    <td> {{total_score }} </td>
                </tr>

        {% endfor %}


        </table>
    ''', labels=labels))
    def post(self,team_name):
        res = helper.create_team(team_name)
        if res is None:
            return Response(f"err:{team_name} not found",mimetype='application/json')
        return Response(json.dumps(res),mimetype='application/json')
    def put(self):
        pass
    def delete(self,team_name):
        res = helper.delete_user(team_name)
        print (res)
        if res is None:
            return Response(f"err:{team_name} not found",mimetype='application/json')
        return Response(json.dumps(res),mimetype='application/json')
class Round(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
    def get(self):
        files = []
        for filename in os.listdir(UPLOAD_DIR):
            path = os.path.join(UPLOAD_DIR, filename)
            if os.path.isfile(path):
                files.append(filename)
        return jsonify(files)
    def post(self):
        self.parser.add_argument("userfile", type=werkzeug.datastructures.FileStorage, location='files')
        args = self.parser.parse_args()
        userfile = args.get("userfile")
        userfile.save(os.path.join(UPLOAD_DIR, userfile.filename))
        return 201
        '''curl -v -X POST -H "Content-Type: multipart/form-data" -F "userfile=@test.json" http://127.0.0.1:5000/round/upload'''
api.add_resource(Base,'/')
api.add_resource(Users,'/users/','/users/<user_name>',endpoint='users')
api.add_resource(Teams,'/teams/','/teams/<team_name>',endpoint='teams')
api.add_resource(Round,'/round/files','/round/upload')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
