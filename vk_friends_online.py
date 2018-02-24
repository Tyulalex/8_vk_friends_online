import vk
import getpass


APP_ID = -1


def get_user_login():
    return input('Enter login:\n')


def get_user_password():
    return getpass.getpass('Enter password:\n')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_online = api.friends.getOnline()
    return api.users.get(user_ids=friends_online)


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
