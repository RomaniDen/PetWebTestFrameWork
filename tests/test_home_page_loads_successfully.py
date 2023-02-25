def test_home_page_loads_successfully(home_page):
    # 1. The page loaded in less than 5 seconds
    load_time = home_page.load_page()
    assert load_time < 5.0, f'Page load time: {load_time} should be less than 5.0 seconds'
    # 2. The relevant page title loaded
    assert home_page.is_title_valid, f'Loaded title should be {home_page.titles[home_page.lang_key].value}'
    # 3. The website logo is displayed
    assert home_page.header.logo.is_displayed(), 'Header logo should be displayed'
    # 4. The website header is displayed
    assert home_page.header.header_container.is_displayed(), 'Header should be displayed'
    # 5. The website footer is displayed
    assert home_page.footer.footer_container.is_displayed(), 'Footer should be displayed'
