from source.database import mysql
from flask import jsonify
from flask_restful import Resource,Api, reqparse
from source import app 
import pymysql

api = Api(app)



class userTable(Resource):
    def get(self):
        try:
            con=mysql.connect()
            cur=con.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT id,name,age FROM user")
            data=cur.fetchall()
            return {"users":data}
            # return jsonify(data) 
        except Exception as e:
            print(e)
        finally:
            cur.close()
            con.close()
        
     
   
            
    def post(self):
        try:
            con=mysql.connect()
            cursor=con.cursor()
            
            parser=reqparse.RequestParser()
            parser.add_argument("name")
            parser.add_argument("age")
            
            args=parser.parse_args()

            name=args.get("name")
            age=args.get("age")
            
            print (name ,age)
            query="insert into user(name,age) values (%s,%s)"
            cursor.execute(query,(name,age))
            con.commit()
            user={
                "id":cursor.lastrowid,
                "name":name,
                "age":age
            }
            response=jsonify(user)
            response.status_code = 201
        except Exception as e:
            print (e)
            response=jsonify('failed to add')
            response.status_code = 400
        finally:
            con.close()
            cursor.close()
            return response
 
 # Get a user by id, update    
class user(Resource):
    def get (self,id):
        try:
            con=mysql.connect()
            Cursor=con.cursor(pymysql.cursors.DictCursor)            
            Cursor.execute("select id, name, age from user where id=%s",id)
            user = Cursor.fetchall()              
        except Exception as e:
            print (e)
        finally:
            Cursor.close()
            con.close()
            return jsonify(user)
        
    def put(self,id):
        try:
            con=mysql.connect()
            cursor=con.cursor()
            
            parser=reqparse.RequestParser()
            parser.add_argument("name")
            parser.add_argument("age")
            parser.add_argument("id")
            
            
            
            args=parser.parse_args()

            name=args.get("name")
            age=args.get("age")            
            print(name,age)
            
            cursor.execute("UPDATE user SET name='{}',age ='{}' WHERE id='{}'".format(name,age,id))
            con.commit()
            response=jsonify("updated")
            response.status_code = 200
        except Exception as e:
            print (e)
            response=jsonify('failed to update')
            response.status_code = 400
        finally:
            con.close()
            cursor.close()
            return response            
    
    def delete(self,id):
        con =None
        cursor=None
        # response={}
        try:
            con=mysql.connect()
            cursor=con.cursor()
            cursor.execute("delete from user where id=%s",id)
            con.commit()
            response=jsonify("user deleted")
            response.status_code= 202
            
        except Exception as e:
            print(e)
            response=('delete your cars first')
            response.status_code = 204
        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.close()
            return response

class carList(Resource):
    def get(self):
        try:
            con=mysql.connect()
            cursor=con.cursor()
            cursor.execute("SELECT id,brand,colour,mileage FROM cars")
            rows=cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print (e)
        finally:
            con.close()
            cursor.close()
    
    # add car to user
    def post(self):
    
        try:
            con=mysql.connect()
            cursor=con.cursor()

            parser=reqparse.RequestParser()
            parser.add_argument("brand")
            parser.add_argument("colour")
            parser.add_argument("mileage")

            args=parser.parse_args()
            brand=args.get("brand")
            colour=args.get("colour")
            mileage=args.get("mileage")
            
            query="insert into cars (brand,colour,mileage) values (%s,%s,%s)"
            cursor.execute(query,(brand,colour,mileage))
            con.commit()
            resp=jsonify('cars')
            resp.status_code = 201
        except Exception as e:
            print (e)
            resp=jsonify('failed to add')
            resp.status_code = 400
        finally:
            con.close()
            cursor.close()
            return resp
 
    def get(self):
        try:
            con=mysql.connect()
            cur=con.cursor()
            cur.execute("SELECT id,brand,colour,mileage  from cars")
            new=cur.fetchall()
            return jsonify(new)
        except Exception as e:
            print(e)
        finally:
            con.close()
            cur.close()
            

api.add_resource(userTable, '/users',endpoint ='users')
api.add_resource(carList,'/cars',endpoint='cars')
api.add_resource(user, '/user/<int:id>', endpoint='user')

