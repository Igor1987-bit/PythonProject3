def send_email(message, recipient, sender='university.help@gmail.com'):
    character_email = ('@', '.com', '.ru', '.net')
    if recipient.endswith(character_email) or sender.endswith(character_email):
        print(message)
        print('   Невозможно отправить письмо с адреса {0} на адрес {1}'.format(sender,
                                                                                recipient))
    elif recipient == sender:
        print(message)
        print('   Нельзя отправить письмо самому себе! с адреса {0} на адрес {1}'.format(
            sender,
            recipient))
    elif sender == 'university.help@gmail.com':
        print(message)
        print('   отправлено с адреса {0} на адрес {1}.'.format(sender,
                                                                recipient))
    else:
        print(message)
        print(
            '   НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {0} на адрес {1}.'.format(
                sender,
                recipient))


send_email('Это сообщение для проверки связи: ', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!: ',
           'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание: ',
           'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре: ',
           'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
send_email('Письмо самому себе: ', 'university.help@gmail.com')
send_email('Сообщение с ошибкой в адресе: ', 'vasyok1337gmail.com')

# consol
#Это сообщение для проверки связи: 
#    отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com.
# Вы видите это сообщение как лучший студент курса!: 
#    НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru.
# Пожалуйста, исправьте задание: 
#    Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Напоминаю самому себе о вебинаре: 
#    Нельзя отправить письмо самому себе! с адреса urban.teacher@mail.ru на адрес urban.teacher@mail.ru
# Письмо самому себе: 
#    Нельзя отправить письмо самому себе! с адреса university.help@gmail.com на адрес university.help@gmail.com
# Сообщение с ошибкой в адресе: 
#    Невозможно отправить письмо с адреса university.help@gmail.com на адрес vasyok1337gmail.com

