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

#testing static data
"""
householditems = [
    {
        "id": 1,
        "name": "pan",
        "category": "kitchen",  
        "quantity" : "2",
        "status" : "available"
    },
    {
        "id": 2,
        "name": "pot",
        "category": "kitchen",  
        "quantity" : "1",
        "status" : "available"  
}
]

@app.route('/HHI/test', methods = ['GET'])
def HHItest():
    return jsonify(householditems)
"""

#       ---Get---
#checking if database is showing up
@app.route('/householditems/GET', methods = ['GET'])
def allusers():
    mycreds = cred.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)

    sql = "select * from householditems"

    userrows = execute_read_query(mycon, sql)
    return jsonify(userrows)


#       ---POST--
#API request to Insert a new householditem to DB with POST method
@app.route('/householditems/POST', methods=['POST'])
def insertHHI():
    userinput = request.get_json() # Pass new user info in JSON format within Body of the request
    #newid = userinput['id']
    newname = userinput['name']
    newcategory = userinput['category']
    newquantity = userinput['quantity']
    newstatus = userinput['status']

    mycreds = cred.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    sql = "insert into householditems( name, category, quantity, status) values ('%s','%s','%s', '%s')" % ( newname, newcategory, newquantity, newstatus)

    execute_update_query(mycon, sql)
    return 'Add householditem request successful!'


#       ---Delete---       
@app.route('/householditems/DELETE', methods = ['DELETE'])    
def delete_HHI_id():                #deleting housholditem ID
    userinput = request.get_json() # Allows user input --> JSON format
    deleteHHIID = userinput['id']

    mycreds = cred.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    sql = "delete from householditems where id = %s " % (deleteHHIID)
    execute_update_query(mycon, sql)
    return "Delete request successful"


@app.route('/householditems/PUT', methods = ['PUT'])
def updateHHI():
    userinput = request.get_json()
    
    #               changing the category value
    if userinput['column'] == 'category': #checking for input to requirement to continue code to change category
        id = userinput['id']
        newcategory = userinput['category']

        mycreds = cred.myCreds()
        mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
        sql = "update householditems set category='%s' where id= '%s' " % (userinput['category'], id)
        execute_update_query(mycon, sql)
        return "Householditem(category) update successfull!"
        #return("Category has been updated!!!")
    
    #               changing the name value
    if userinput['column'] == 'name': # checking for coulnm value to change name
        id = userinput['id']
        newname = userinput['name']

        mycreds = cred.myCreds()
        mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
        sql = "update householditems set name='%s' where id= '%s' " % (newname, id)

        execute_update_query(mycon, sql)
        return "Householditem(name) update successfull!"
        #return("Name has been updated!!!")
    
    #               changing the quantity value
    if userinput['column'] == 'quantity': # checking for coulnm value to change quantity
        id = userinput['id']
        newquantity = userinput['quantity']

        mycreds = cred.myCreds()
        mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
        sql = "update householditems set quantity='%s' where id= '%s' " % (newquantity, id)

        execute_update_query(mycon, sql)
        return "Householditem(quantity) update successfull!"
        #return("Quantity has been updated!!!")
    
    #               changing the status value
    if userinput['column'] == 'status': # checking for coulnm value to change status
        id = userinput['id']
        newstatus = userinput['status']

        mycreds = cred.myCreds()
        mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
        sql = "update householditems set status='%s' where id= '%s' " % (newstatus, id)

        execute_update_query(mycon, sql)
        return "Householditem(status) update successfull!"
        #return("Status has been updated!!!")
    

    else :
        return "Please return correct column value"

        

app.run()


#original
"""
def updateHHI():
    userinput = request.get_json() # Pass user ID and email in JSON format within Body of the request
    id = userinput['id']
    newcategory = userinput['category']

    mycreds = cred.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    sql = "update householditems set category='%s' where id='%s'" % (newcategory, id)

    execute_update_query(mycon, sql)
    return 'Householditem updated successful!'
"""
#complex version
'''
def updateHHI():
    userinput = request.get_json()
    
    #               changing the category value
    if userinput['column'] == 'category': #checking for input to requirement to continue code to change category
        id = userinput['id']
        newcategory = userinput['category']

        mycreds = cred.myCreds()
        mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
        sql = "update householditems set category='%s' where id= '%s' " % (userinput['category'], id)
        execute_update_query(mycon, sql)
        return "Householditem(category) update successfull!"
        #return("Category has been updated!!!")
    
    #               changing the name value
    if userinput['column'] == 'name': # checking for coulnm value to change name
        id = userinput['id']
        newname = userinput['name']

        mycreds = cred.myCreds()
        mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
        sql = "update householditems set name='%s' where id= '%s' " % (newname, id)

        execute_update_query(mycon, sql)
        return "Householditem(name) update successfull!"
        #return("Name has been updated!!!")
    
    #               changing the quantity value
    if userinput['column'] == 'quantity': # checking for coulnm value to change quantity
        id = userinput['id']
        newquantity = userinput['quantity']

        mycreds = cred.myCreds()
        mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
        sql = "update householditems set quantity='%s' where id= '%s' " % (newquantity, id)

        execute_update_query(mycon, sql)
        return "Householditem(quantity) update successfull!"
        #return("Quantity has been updated!!!")
    
    #               changing the status value
    if userinput['column'] == 'status': # checking for coulnm value to change status
        id = userinput['id']
        newstatus = userinput['status']

        mycreds = cred.myCreds()
        mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
        sql = "update householditems set status='%s' where id= '%s' " % (newstatus, id)

        execute_update_query(mycon, sql)
        return "Householditem(status) update successfull!"
        #return("Status has been updated!!!")
    

    else :
        return "Please return correct column value"

        
'''