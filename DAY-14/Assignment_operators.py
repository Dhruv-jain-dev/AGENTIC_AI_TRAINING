from Session12E import DBHelper

def main():
    
    db = DBHelper()
    db.select_collection()
    students = [
        {
        "name": "Dhruv",
        "age": 20,
        "marks": 90,
        "city": "Ludhiana",
        "skills": ["C++", "Python"]
        },
        {
        "name": "Rahul",
        "age": 19,
        "marks": 75,
        "city": "Delhi",
        "skills": ["Java"]
        },
        {
        "name": "Aman",
        "age": 22,
        "marks": 85,
        "city": "Mumbai",
        "skills": ["Python", "Java"]
        },
        {
        "name": "Simran",
        "age": 18,
        "marks": 65,
        "city": "Delhi",
        "skills": ["C"]
        }
        ]

    # db.delete(students)

        # -------------------------------
        # Comparison Operators
        # -------------------------------
    # equal to
    print("\n$eq")
    for doc in db.find({"age": {"$eq": 20}}):
        print(doc)
    # not equal to
        print("\n$ne")
    for doc in db.find({"city": {"$ne": "Delhi"}}):
        print(doc)
    # greater than
        print("\n$gt")
    for doc in db.find({"marks": {"$gt": 80}}):
        print(doc)
    # greater than equal to
        print("\n$gte")
    for doc in db.find({"marks": {"$gte": 85}}):
        print(doc)
    # less than
        print("\n$lt")
    for doc in db.find({"age": {"$lt": 20}}):
        print(doc)
    # less than equal to
        print("\n$lte")
    for doc in db.find({"age": {"$lte": 20}}):
        print(doc)
    # in operator
        print("\n$in")
    for doc in db.find({"city": {"$in": ["Delhi", "Mumbai"]}}):
        print(doc)
    # not in operator
        print("\n$nin")
    for doc in db.find({"city": {"$nin": ["Delhi", "Mumbai"]}}):
        print(doc)


if __name__ == '__main__':
    main()