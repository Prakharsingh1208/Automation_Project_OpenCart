import configparser

config=configparser.RawConfigParser()
config.read("configurations/config.ini")

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

class Cart_config:
    @staticmethod
    def get_add_to_cart_home_page_location():
        location=config.get("cart","addtocart_home_page")
        return location

    @staticmethod
    def get_add_to_cart_product_page_location():
        location = config.get("cart", "addtocart_product_page")
        return location

    @staticmethod
    def get_add_to_cart_search_page_location():
        location = config.get("cart", "addtocart_search_page")
        return location

    @staticmethod
    def get_black_cart_button():
        location = config.get("cart", "black_cart_button")
        return location

    @staticmethod
    def get_shopping_cart_button():
        location = config.get("cart", "shopping_cart_button")
        return location

    @staticmethod
    def get_empty_cart_message():
        message = config.get("cart", "empty_cart_message")
        return message

    @staticmethod
    def get_black_cart_info():
        location = config.get("cart", "black_cart_info")
        return location

    @staticmethod
    def get_success_prompt():
        location = config.get("cart", "success_prompt")
        return location

    @staticmethod
    def get_warning_prompt():
        location = config.get("cart", "warning_prompt")
        return location

    @staticmethod
    def get_product_page_location():
        location = config.get("cart","product_page_location")
        return location

    @staticmethod
    def get_addtocart_homepage_2():
        location = config.get("cart","addtocart_home_page_2")
        return location

    @staticmethod
    def get_black_cart_button_item_list():
        location = config.get("cart","black_cart_button_item_list")
        return location

    @staticmethod
    def get_delete_item_from_cart_location():
        location = config.get("cart","delete_item_from_cart_location")
        return location