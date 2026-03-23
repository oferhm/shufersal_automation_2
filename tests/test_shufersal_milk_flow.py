# tests/test_shufersal_milk_flow.py
import pytest
from pages.home_page import HomePage


class TestShufersalMilkFlow:

    @pytest.mark.smoke
    @pytest.mark.shufersal
    def test_search_suggestions_contain_keyword(self, home_page):
        """
        SCENARIO: User types 'חלב' into the search bar.
                  A dropdown appears with ~10 suggestions.
                  Every suggestion must contain the search keyword 'חלב'.

        STEPS:
          1. Open https://www.shufersal.co.il/online/
          2. Type 'חלב' into #js-site-search-input
          3. Wait 2 seconds for the dropdown to populate
          4. Read all items from .tt-menu .tile .text
          5. Assert each item's text contains 'חלב'
        """
        keyword = HomePage.USER_SEARCH_INPUT  # "חלב"

        # Step 1 + 2 + 3: open site, type keyword, wait for dropdown
        home_page.open()
        home_page.type_search_keyword(keyword)

        # Step 4: get all suggestion texts
        items = home_page.get_search_suggestion_items()

        # Print all items to console (visible with pytest -s)
        print(f"\nFound {len(items)} suggestions:")
        for i, text in enumerate(items, start=1):
            print(f"  {i}. {text}")

        # Step 5: verify we got results at all - we should get 10, but we test that we get more than 0
        assert len(items) > 0, (
            f"Expected search suggestions for '{keyword}' but got none"
        )

        # Step 5: verify every item contains the string that the user typed
        failing = [text for text in items if keyword not in text]
        assert len(failing) == 0, (
            f"These suggestions do not contain '{keyword}':\n"
            + "\n".join(f"  - {t}" for t in failing)
        )