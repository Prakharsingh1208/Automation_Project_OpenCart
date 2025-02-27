import configparser
configs = configparser.RawConfigParser()
configs.read(r"C:\Users\pranj\OneDrive\Desktop\Automation_Project_OpenCart\configurations\config.ini")
class Config:
    def gethomepageurl(self):
        url = configs.get("Home_page","url")
        return url


