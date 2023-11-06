def to_persian(form):
    persian_errors = {'A user with that username already exists': 'این نام کاربری قبلا استفاده شده است',
                      'This password is too short': 'رمز عبور خیلی کوتاه است',
                      ' It must contain at least 8 characters': 'رمز عبور باید حداقل شامل 8 کاراکتر باشد',
                      'This password is too common': 'رمز عبور خیلی ساده است',
                      'The two password fields didn’t match': 'پسورد ها یکسان نیستند',
                      'This password is entirely numeric': 'رمز عبور تنها از اعداد تشکیل شده است. باید شامل اعداد و حروف باشد', }

    form_errors = list(form.errors.values())
    form_errors = [''.join(i) for i in form_errors]
    form_errors = ''.join(form_errors)
    form_errors = form_errors.split('.')
    form_errors = [i for i in form_errors if len(i) != 0]
    form_errors = [persian_errors.get(i, 'اطلاعات ورودی صحیح نیستند') for i in form_errors]

    return form_errors
