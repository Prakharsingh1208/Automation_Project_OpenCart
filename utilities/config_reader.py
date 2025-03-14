import configparser

config=configparser.RawConfigParser()
config.read("configurations\\config.ini")

class SearchBar_config:
    @staticmethod
    def get_base_url():
        url = config.get("search_bar","base_url")
        return url

    @staticmethod
    def get_search_bar_location():
        location = config.get("search_bar","search_bar_location")
        return location

    @staticmethod
    def get_search_button_location():
        location = config.get("search_bar","search_button_location")
        return location

    @staticmethod
    def get_product_catalog():
        location = config.get("search_bar","product_catalog_location")
        return location