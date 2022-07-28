class Banner(object):
    def LoadDarkdumpBanner(self):
        try:
            from termcolor import cprint, colored
            banner = '''

            '''
            cprint(banner, 'magenta', attrs=['bold'])

        except ImportError as ie:
            print(banner)