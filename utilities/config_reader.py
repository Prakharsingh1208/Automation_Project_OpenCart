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

    @staticmethod
    def GetCurrencyLocattion():
        location = configs.get("Home_page","CurrencyLocation_Xpath")
        return location

    @staticmethod
    def GetDemoPriceLocation():
        location = configs.get("Home_page","DemoProductPrice_Xpath")
        return location

    @staticmethod
    def GetDollarlocation():
        location = configs.get("Home_page","DollarCurrencyLocation_Xpath")
        return location

    @staticmethod
    def GetEurolocation():
        location = configs.get("Home_page","EuroCurrencyLocation_Xpath")
        return location

    @staticmethod
    def GetPoundlocation():
        location = configs.get("Home_page","PoundCurrencyLocation_xpath")
        return location

    @staticmethod
    def GetProductAddToCartLocation_Xpath():
        location = configs.get("Home_page","ProductAddToCartLocation_Xpath")
        return location

    @staticmethod
    def GetCartLocation():
        location = configs.get("Home_page","CartLocation_Xpath")
        return location

    @staticmethod
    def GetCartInfoLocation():
        location = configs.get("Home_page","CartInfoLocation_Xpath")
        return location

    @staticmethod
    def GetEmptyCartMessage():
        Message = configs.get("Home_page","EmptyCartMessage")
        return Message
