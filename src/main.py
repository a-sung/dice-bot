from auth import TwitterAuth, TwitterBot

def main():
    api = TwitterAuth().get_auth()
    bot = TwitterBot(api).get_bot()
    api.update_status("dice bot test!!!")

if __name__ == "__main__":
    main()