from decouple import config

HOST = config('POSTGRESQL_HOST')
PORT = config('POSTGRESQL_PORT')
USER = config('POSTGRESQL_USER')
PWD = config('POSTGRESQL_PWD')

print(HOST)
print(PORT)
print(USER)
print(PWD)

print('Host: {HOST2} - Puerto:{PORT2}'.format(HOST2=config('POSTGRESQL_HOST'),PORT2=config('POSTGRESQL_PORT')))
print('user: {USER2}, pwd: {PWD2}'.format(USER2= config('POSTGRESQL_USER'), PWD2= config('POSTGRESQL_PWD')))