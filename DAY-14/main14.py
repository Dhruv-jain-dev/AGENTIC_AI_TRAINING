from Session12E import DBHelper

def main():
    
    db = DBHelper()
    db.select_collection()
    
    condition = {
        'name' : 'Vanshika',
        'email' : 'vp@gmail.com'}
    

    # db.retrieve(condition)

    condition = {'email' : ''}
    document_to_update = {
        'email' : 'dhruv@gmail.com'
    }

    db.update(condition=condition, document_to_update=document_to_update)

# for deleting a document in database, following will be used
    
    # condition = {'name':'VP', 'email' : 'vp@gmail.com'}
    # db.delete(condition=condition)

if __name__ == '__main__':
    main()