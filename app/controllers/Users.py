from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Poke')
        self.db = self._app.db

   
    def index(self):
        return self.load_view('index.html')

    def logout(self):
        session.pop('user_id')
        return redirect('/')

    def insert_user(self):
        dob = str(request.form['year']+ '-' + request.form['month'] + '-' + request.form['day'])
        new_user = {'name':request.form['name'],'alias':request.form['alias'],
        'email':request.form['email'],'password':request.form['password'],'pwd_conf':request.form['pwd_conf'], 'dob':dob}
        print dob
        print new_user
        validation = self.models['User'].user_validation(new_user)
        
        if validation['status']:
            user_id = self.models['User'].insert_user(new_user)
            session['user_id'] = user_id
            return redirect('/pokes')
        else:
            for error in validation['errors']:
                flash(error, 'validation')
            return redirect('/')

    def login_process(self):
        user_info = {'email': request.form['email'],'password': request.form['password']}
        
        user = self.models['User'].get_user_by_email(user_info['email'])
        if not user:
            flash("E-mail and/or Password invalid!", 'login')
            return redirect('/')
        
        if not self.models['User'].pwd_validation(user['password'], user_info['password']):
            flash("E-mail and/or Password invalid!", 'login')
            return redirect('/')
            
        session['user_id'] = user['id']
        return redirect('/pokes')




