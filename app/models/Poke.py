from system.core.model import Model


class Poke(Model):
    def __init__(self):
        super(Poke, self).__init__()
    
    def get_pokes_by_user(self, user_id):
        query = "select pokes.user_id as friend_id, users.alias as friend_alias from pokes join users on pokes.user_id = users.id where pokes.friend_id =:id"
        data = {'id':user_id}
        return self.db.query_db(query, data)

    def get_total_pokes(self, user_id):
        query = "select count(friend_id) as total_pokes from pokes where friend_id =:id"
        data = {'id':user_id}
        return self.db.get_one(query, data)

    def get_friends(self, user_id):
        query = "select pokes.friend_id, users.name, users.alias, users.email from users join pokes on pokes.friend_id = users.id where users.id <> :id"
        data = {'id':user_id}
        return self.db.query_db(query, data)

    def get_users(self, user_id):
        query = "select * from users where id <> :id"
        data = {'id':user_id}
        return self.db.query_db(query, data)

    def get_total_pokes_by_friend(self, user_id):
        query = "select count(friend_id) as total_pokes, users.alias from pokes join users on pokes.user_id = users.id where pokes.friend_id =:id group by users.alias order by total_pokes DESC"
        data = {'id':user_id}
        return self.db.query_db(query, data)

    def insert_poke(self, poke):
        query = "insert into pokes(user_id, friend_id, created_at) values (:user_id, :friend_id, NOW())"
        data = {'user_id':poke['user_id'], 'friend_id':poke['friend_id']}
        return self.db.query_db(query, data)