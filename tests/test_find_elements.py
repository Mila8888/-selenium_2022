import time


def test_title(driver):
    driver.save_screenshot("test.png")
    assert driver.title == "Your Store", "Проверить заголовок"

# def test_main_page_menu(driver):
#     time.sleep(1)  # Пауза для демонстрации
#     menu_items = driver.find_elements_by_css_selector("ul.navbar-nav > li")
#     assert len(menu_items) == 8, "Неверное количество элементов меню"
#
#
# def test_main_page_fetured_items(driver):
#     time.sleep(1)  # Пауза для демонстрации
#     fetured_items = driver.find_elements_by_class_name("product-thumb")
#     assert len(fetured_items) == 4, "Неверное количество продуктов в блоке featured"
#
#
# def test_main_page_footer_blocks(driver):
#     time.sleep(1)  # Пауза для демонстрации
#     footer_blocks = driver.find_elements_by_xpath("//footer//ul")
#     result = footer_blocks[0].location_once_scrolled_into_view
#     time.sleep(1)  # Пауза для демонстрации
#     assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"
#
#
# def test_main_page_open_product(driver):
#     fetured_items = driver.find_elements_by_class_name("product-thumb")
#     fetured_items[2].location_once_scrolled_into_view
#     fetured_items[2].click()
#     driver.find_elements_by_link_text("Apple Cinema")
#     time.sleep(1)  # Пауза для демонстрации
