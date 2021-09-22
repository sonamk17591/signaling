from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver


#SIGNAL FOR USER LOGIN

@receiver (user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print('-------')
    print('This is login success signal,Run Intro....')
    print('Sender',sender)
    print('Request',request)
    print('User',user)
    print('User',user.password)
    print(f'Kwargs:{kwargs}')
#user_logged_in.connect(login_success,sender=User) 

#SIGNAL FOR USER LOG OUT AND LOGIN FAILED

@receiver (user_logged_out,sender=User)
def logout_success(sender,request,user,**kwargs):
    print('-------')
    print('introduction of signal')

    print('This is logout success signal')
    print('Sender',sender)
    print('Request',request)
    print('User',user)
    print(f'Kwargs:{kwargs}')
    
#user_logged_out.connect(logout_success,sender=User)

#SIGNAL FOR USER LOGIN FAILED 


@receiver (user_login_failed)
def login_fail(sender,request,credentials,**kwargs):
    print('-------')
    print('This is login failed signal')
    print('Sender',sender)
    print('Request',request)
    print('credentials',credentials)
    print(f'Kwargs:{kwargs}')
#user_logged_out.connect(logout_success,sender=User)    





