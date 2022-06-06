import json, os

def load_db():
    if os.path.exists('flashcards.json'):
        with open('flashcards.json', encoding='utf-8') as infile:
            data = json.load(infile)
        return data

def save_db():
    if os.path.exists('flashcards.json'):
        with open('flashcards.json', 'w') as outfile:
            return json.dump(db, outfile)

db = load_db()

if __name__ == '__main__':
    db = load_db()
    print(db)




"""
https://app.pluralsight.com/library/courses/flask-getting-started/table-of-contents
https://app.pluralsight.com/course-player?clipId=27d1dcb2-d672-42cb-80d1-6ed7ad7a3cbf

https://bobbyhadz.com/blog/python-typeerror-the-json-object-must-be-str-bytes-or-bytearray-not-textiowrapper
https://www.tldevtech.com/json-example/

def loadUsers(self):
    # Dosya var?
    if os.path.exists("AccInformation.json"):  # True ise......
        with open("AccInformation.json", encoding="utf-8") as infile:
            users = json.load(infile)
        # return indent here as we've already loaded the file

        for user in users:
            newUser = Account(
                user_id=user["user_id"],
                firstName=user["first_name"],
                lastName=user["last_name"],
                email=user["email"],
                username=user["username"],
                password=user["password"],
                accountKEY=user["AccountKEY"],
            )

            self.users.append(newUser)
        print(self.users)
    else:
        print('AccInformation Wayneı.')

"""