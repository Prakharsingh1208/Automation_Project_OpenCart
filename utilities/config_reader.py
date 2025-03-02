import configparser
configs = configparser.RawConfigParser()
configs.read(r"C:\Users\pranj\OneDrive\Desktop\Automation_Project_OpenCart\configurations\config.ini")
class ConfigHomePage:
    @staticmethod
    def gethomepageurl():
        url = configs.get("Home_page","url")
        return url

    @staticmethod
    def GetSearchBarLocation():
        location = configs.get("Home_page","SearchBar_Xpath")
        return location

    @staticmethod
    def GetSearchButton():
        button = configs.get("Home_page","SearchBarButton_Xpath")
        return button

    @staticmethod
    def GetInvalidQueryResponse():
        response = configs.get("Home_page","InvalidSearchQueryResponse")
        return response

    @staticmethod
    def GetValidQuery():
        query = configs.get("Home_page","ValidQuery")
        return query

    @staticmethod
    def GetInvalidQuery():
        query = configs.get("Home_page","InvalidQuery")
        return query

    @staticmethod
    def GetHomePageTitle():
        title = configs.get("Home_page","HomePageTitle")
        return title

    @staticmethod
    def GetSqlPayload():
        payload = configs.get("Home_page","SqlPayload")
        return payload
