import re

validation_email = re.compile(r'^[-\w.]+@([-\w]+\.)+[-\w]{2,4}$')


def email_parse(email):
    result = {'username': '', 'domain': ''}
    if validation_email.match(email):
            temp_result = re.split(r'@', email)
            result['username'] = temp_result[0]
            result['domain'] = temp_result[1]

    else:
            msg = f'wrong email: {email}'
            raise ValueError(msg)
    return result

#print(email_parse('maile_rr.rfe-ff@mail_fd.m-ailcom'))
print(email_parse(input('Введите email для проверки: ')))

#Надеюсь правильно понял с Traceback,можно было и красивее с исключением сообщение