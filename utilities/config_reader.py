import configparser
configs = configparser.RawConfigParser()
configs.read(r"C:\Users\pranj\OneDrive\Desktop\Automation_Project_OpenCart\configurations\config.ini")
class Config:
    @staticmethod
    def gethomepageurl():
        url = configs.get("Home_page","url")
        return url

    @staticmethod
    def GetSearchBarLocation():
        location = configs.get("Home_page","SearchBar_Xpath")
        return location