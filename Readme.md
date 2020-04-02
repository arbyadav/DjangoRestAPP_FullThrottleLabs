 ##  DJANGO REST API with CUSTOM Models & Dummy Data Generator ##
 
 #To install packages run command from your root directory-
 
 pip install -r requirements.txt
 

 ----------------------------------------------------------------------------
  
 ##  GITHUB URL
 
 https://github.com/arbyadav/DjangoRestAPP_FullThrottleLabs.git
  
 ----------------------------------------------------------------------------
 
  ##  AWS URL
 
 http://awsdjangorestapi-prod.eba-pemhpunp.ap-south-1.elasticbeanstalk.com/
 
 AWS Elastic BeanStalk uses aws ebcli that runs locally on server and then deploy it on instance using ElasticBenStalk
 
 ## Command to migrate 
 
 python manage.py migrate
 
 ## Command to makemigrations in db
 
 python manage.py makemigrations API
  
 ## Command to create superuser
 
 python manage.py createsuperuser
 
 ## Command to create dummy users in db
 
 python manage.py user --createuser 5
 
 python manage.py activity --createactivity 5
 
 ## Application URL
 
 http://awsdjangorestapi-prod.eba-pemhpunp.ap-south-1.elasticbeanstalk.com/
 
 ## Admin URL
 
 http://awsdjangorestapi-prod.eba-pemhpunp.ap-south-1.elasticbeanstalk.com/admin/
 
 ## API URL's
 
 ## Token Generation - POST Method
 
 http://awsdjangorestapi-prod.eba-pemhpunp.ap-south-1.elasticbeanstalk.com/api/auth/
 
 ## GET, POST, OPTIONS Methods Supported
 
 http://awsdjangorestapi-prod.eba-pemhpunp.ap-south-1.elasticbeanstalk.com/api/users_list/
 
 http://awsdjangorestapi-prod.eba-pemhpunp.ap-south-1.elasticbeanstalk.com/api/members_list/
 
 http://awsdjangorestapi-prod.eba-pemhpunp.ap-south-1.elasticbeanstalk.com/api/activities_list/
 
 ## GET, PUT, DELETE, OPTIONS Methods Supported
 
 http://awsdjangorestapi-prod.eba-pemhpunp.ap-south-1.elasticbeanstalk.com/api/users_list/1/
 
 
 ## GET, OPTIONS Methods Supported
 
 http://awsdjangorestapi-prod.eba-pemhpunp.ap-south-1.elasticbeanstalk.com/api/members_list/1/
 
 http://awsdjangorestapi-prod.eba-pemhpunp.ap-south-1.elasticbeanstalk.com/api/activities_list/1/
 
 
 ----------------------------------------------------------------------------
 
 ##  HEROKU HOSTED (PaaS) 
 
 https://djanorestapi-fullthrottlelabs.herokuapp.com/
 
 
 ## Command to migrate 
 
 heroku run python manage.py migrate
 
 ## Command to makemigrations in db
 
 heroku run python manage.py makemigrations API
  
 ## Command to create superuser
 
 heroku run python manage.py createsuperuser
 
 ## Command to create dummy users in db
 
 heroku run python manage.py user --createuser 5
 
 heroku run python manage.py activity --createactivity 5
 
 
 ## Application URL
 
 https://djanorestapi-fullthrottlelabs.herokuapp.com/
 
 ## Admin URL
 
 https://djanorestapi-fullthrottlelabs.herokuapp.com/admin/
 
 ## API URL's
 
 ## Token Generation - POST Method
 
 https://djanorestapi-fullthrottlelabs.herokuapp.com/api/auth/
 
 ## GET, POST, OPTIONS Methods Supported
 
 https://djanorestapi-fullthrottlelabs.herokuapp.com/api/users_list/
 
 https://djanorestapi-fullthrottlelabs.herokuapp.com/api/members_list/
 
 https://djanorestapi-fullthrottlelabs.herokuapp.com/api/activities_list/
 
 ## GET, PUT, DELETE, OPTIONS Methods Supported
 
 https://djanorestapi-fullthrottlelabs.herokuapp.com/api/users_list/1/
 
 
 ## GET, OPTIONS Methods Supported
 
 https://djanorestapi-fullthrottlelabs.herokuapp.com/api/members_list/1/
 
 https://djanorestapi-fullthrottlelabs.herokuapp.com/api/activities_list/1/
 
 ---------------------------------------------------------------------------------
 
 ## LOCAL SERVER
 
 ## Command to migrate 
 
 python manage.py migrate
 
 ## Command to makemigrations in db
 
 python manage.py makemigrations API
 
 ## Command to create superuser
 
 python manage.py createsuperuser
 
 ## Command to create dummy users in db
 
 python manage.py user --createuser 5
 
 python manage.py activity --createactivity 5
 
 
 #Application URL
 
 http://127.0.0.1:8000/
 
 ## Admin URL
 
 http://127.0.0.1:8000/admin/
 
 ## API URL's
 
 ## Token Generation  - POST
 
 http://127.0.0.1:8000/api/auth/
 
 
 ## GET, POST, OPTIONS Methods Supported
 
 http://127.0.0.1:8000/api/users_list/
 
 http://127.0.0.1:8000/api/members_list/
 
 http://127.0.0.1:8000/api/activities_list/
 
 ## GET, PUT, DELETE, OPTIONS Methods Supported
 
 http://127.0.0.1:8000/api/users_list/1/
 
 
 ## GET, OPTIONS Methods Supported
 
 http://127.0.0.1:8000/api/members_list/1/
 
 http://127.0.0.1:8000/api/activities_list/1/

