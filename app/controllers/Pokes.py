from system.core.controller import *

class Pokes(Controller):
    def __init__(self, action):
        super(Pokes, self).__init__(action)
        self.load_model('User')
        self.load_model('Poke')
        self.db = self._app.db

   
    def main(self):
        #get welcome info
        user = self.models['User'].get_user_by_id(session['user_id'])
        
        #get total pokes by friend
        total_pokes = self.models['Poke'].get_total_pokes(session['user_id'])
        
        #get all pokes from all friends that poked logged user
        pokes = self.models['Poke'].get_total_pokes_by_friend(session['user_id'])
          
        #display each friend logged user can poke
        friends_list = self.models['Poke'].get_users(session['user_id'])
        cur_id = -1
        friends = []
        for friend in friends_list:
            if friend['id'] != cur_id:
                friend = {'friend_id':friend['id'], 'name':friend['name'], 'alias':friend['alias'], 'email':friend['email'], 'pokes':0}
                cur_id = friend['friend_id']
                friend['poke'] = self.models['Poke'].get_total_pokes(friend['friend_id'])
                friends.append(friend)
     
        return self.load_view('main.html', user=user, pokes=pokes, friends=friends, total_pokes=total_pokes)

    def log_poke(self):
        poke ={'user_id':session['user_id'], 'friend_id':request.form['friend_id']}
        new_poke = self.models['Poke'].insert_poke(poke)
        return redirect('/pokes')

    




