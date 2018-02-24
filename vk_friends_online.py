import vk
import getpass


APP_ID = 6385239


def get_user_login():
    return input('Enter login:\n')


def get_user_password():
    return getpass.getpass('Enter password:\n')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    all_friends_list = api.friends.get(fields='online')
    return [friend for friend in all_friends_list if friend['online'] == 1]


def output_friends_to_console(friends_online):
    print('Friends Online:')
    print('\n'.join(
        ['{} {}'.format(friend.get('first_name'),
                        friend.get('last_name')) for friend in friends_online]
    )
    )


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        print('Failed to login')
