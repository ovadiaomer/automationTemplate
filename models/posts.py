import json


class Post:
    def __init__(self, user_id, id, title, body):
        self.user_id = user_id
        self.id = id
        self.title = title
        self.body = body

    def __repr__(self):
        return f"Post({self.user_id}, {self.id}, {self.title}, {self.body})"

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "id": self.id,
            "title": self.title,
            "body": self.body
        }


    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
