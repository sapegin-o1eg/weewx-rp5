from setup import ExtensionInstaller


def loader():
    return RP5Installer()


class RP5Installer(ExtensionInstaller):
    def __init__(self):
        super(RP5Installer, self).__init__(
            version='0.1',
            name='rp5',
            description='Upload archive data to rp5.ru',
            author='Sapegin Oleg',
            author_email='sapegin.o@gmail.com',
            restful_services='user.rp5.StdRP5',
            config={
                'StdRESTful': {
                    'RP5': {
                        'enable': 'false',
                        'api_key': 'ENTER_RP5_API_KEY_HERE'
                    }
                }
            },
            files=[('bin/user', ['bin/user/rp5.py'])]
        )