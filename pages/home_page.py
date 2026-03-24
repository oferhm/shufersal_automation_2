# pages/home_page.py
from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.constants import URLs


class HomePage(BasePage):

    # ── Selectors ─────────────────────────────────────────────────────────────
    SEARCH_BAR            = "#js-site-search-input"
    ITEMS_SEARCH_RESULT_LIST     = ".tt-menu .tile button.text"
    ADD_TO_CART_BUTTON_LIST = ".tt-menu .tile .addToCart .js-add-to-cart"
    ITEM_NAME_IN_CART_LIST       = ".miglog-prod-body .miglog-text3"


    
    
    items_full_name_result_list = ""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def open(self) -> "HomePage":
        """Navigate to the Shufersal home page."""
        self.navigate(URLs.HOME)
        return self

    def type_user_requested_item_to_search_bar(self, item_to_search: str) -> "HomePage":
        """
        Type a string of item requested into the search input
        No Enter needed — dropdown appears automatically.
        """
        self.fill(self.SEARCH_BAR, item_to_search)
        self.page.wait_for_timeout(2000)
        return self

    def get_search_result_items_list(self) -> list[str]:
        """
        Return the full name of every suggestion item in the dropdown after search request.
        (expected: 10 items)
        """
        print("\n--- get_search_result_items_list ---")
        locators = self.page.locator(self.ITEMS_SEARCH_RESULT_LIST).all()
        return [locator.inner_text() for locator in locators]
    

    def print_all_item_names_after_search(self) -> None:
        
        print("\n--- All items full names ***** ---")

        self.items_full_name_result_list = self.page.locator(self.ITEMS_SEARCH_RESULT_LIST)
        self.firstItem = self.items_full_name_result_list.first()
        print(self.items_full_name_result_list)
        print(f"first time: {self.firstItem}")

    def get_add_to_cart_buttons(self):
        """
        Return a list of all 'Add to cart' button locators from the dropdown.
        Selector: .tt-menu .tile .addToCart .js-add-to-cart
        """
        return self.page.locator(self.ADD_TO_CART_BUTTON_LIST).all()

    def click_first_add_to_cart(self) -> "HomePage":
        """
        Click the first 'Add to cart' button in the dropdown suggestion list.
        Waits for the button to be visible before clicking.
        """
        buttons = self.get_add_to_cart_buttons()
        assert len(buttons) > 0, "No 'Add to cart' buttons found in dropdown"
        buttons[0].wait_for(state="visible")
        buttons[0].click()
        return self

    def get_cart_item_name(self) -> str:
        """
        Return the name of the item shown in the cart panel after adding.
        Selector: .miglog-prod-body .miglog-text3
        """
        self.page.locator(self.ITEM_NAME_IN_CART_LIST).first.wait_for(state="visible")
        return self.page.locator(self.ITEM_NAME_IN_CART_LIST).first.inner_text()

    def print_cart_item_name(self) -> None:
        """Print the cart item name to console."""
        name = self.get_cart_item_name()
        print(f"\nItem added to cart: {name}")