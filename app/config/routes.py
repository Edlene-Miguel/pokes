from system.core.router import routes

routes ['/'] = 'Users#index'

routes ['/pokes'] = 'Pokes#main'

routes ['/logout'] = 'Users#logout'

routes ['POST'] ['/login_process'] = 'Users#login_process'

routes ['POST'] ['/registration'] = 'Users#insert_user'

routes ['POST'] ['/pokes/log'] = 'Pokes#log_poke'



