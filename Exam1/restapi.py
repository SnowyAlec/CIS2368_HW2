import flask

from flask import jsonify
from flask import request

from sql import DBconnection
from sql import execute_read_query
from sql import execute_update_query

import cred

# set a application
# flask is a module Flask is going to pull form creds
app = flask.Flask(__name__)
app.config['DEBUG'] = True
# everything reference from class notes week4 and assignment 2



@app.route("/productpromotions/GET", methods = ["GET"]) #getting full list of productpromotion
def APP():
    #from Assignment 2
    #mycreds = cred.myCreds()
    #mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)

    #sql = "select * from productpromotions"
    #userrows = execute_read_query(mycon, sql)
    #return(finalPrice)

    #return jsonify(userrows)
    mycreds = cred.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    sql = "select * , Retailprice - (Retailprice * (Discount/100)) from productpromotions"
    userrows = execute_read_query(mycon, sql)

    return jsonify(userrows)



@app.route("/productpromotions/POST", methods = ["POST"]) #posting new items onto list
def insertProduct():
    userinput = request.get_json() # Pass new user info in JSON format within Body of the request
    newprodID = userinput['Product_id']
    newProdName = userinput['Product_name']
    newCategory = userinput['Category']
    newRP = userinput['Retailprice']
    newDiscount = userinput['Discount']

    mycreds = cred.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    sql = "insert into productpromotions( Product_id, Product_name, Category, Retailprice, Discount ) values ('%s','%s','%s', '%s', '%s')" % (newprodID, newProdName, newCategory, newRP, newDiscount)

    execute_update_query(mycon, sql)
    return 'Add Product request successful!'

@app.route("/productpromotions/DELETE", methods = ["DELETE"]) #deleting all the product info with primary key
def PPDelete():
    userinput = request.get_json() # Allows user input --> JSON format
    deletePPID = userinput['id']

    mycreds = cred.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    sql = "delete from productpromotions where id = %s " % (deletePPID)
    execute_update_query(mycon, sql)
    return "Delete request successful"



app.run()