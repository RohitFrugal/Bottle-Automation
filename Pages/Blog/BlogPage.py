import logging
import time

from selenium import webdriver
from Utilities.utils import Utils
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BlogPage:
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.actionChain = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Blog_module", logLevel=logging.WARNING)

    # General Locators
    BLOG_TAB = (By.ID, "BlogsMenu")
    HEADER_TEXT = (By.XPATH, "//h1[contains(text(), 'Blogs')]")
    ADD_NEW_BTN = (
        By.XPATH, "//button[@class='ant-btn ant-btn-round ant-btn-primary']/span[contains(text(), 'Add New')]")

    # Post New Blog
    TITLE = (By.XPATH, "//input[@id='title']")

    #  -- Author and Basic Information -- #

    # Author Details
    AUTHOR_SELECTOR = (By.XPATH, "//span[@class='ant-select-selection-item']")
    AUTHOR_VALUE = (By.XPATH, "//div[@class='ant-select-item-option-content']")
    # Descriptions
    SHORT_DESCRIPTIONS = (By.XPATH, "//textarea[@id='shortDescription']")
    # Type Selector
    TYPE_SELECTOR = (By.XPATH, "(//span[@class='ant-select-selection-search'])[2]")
    TYPE_IMAGE = (By.XPATH, "//div[@class='rc-virtual-list-holder-inner']/div[@title='Image']")
    TYPE_VIDEO = (By.XPATH, "//div[@class='rc-virtual-list-holder-inner']/div[@title='Video']")
    TYPE_PODCAST = (By.XPATH, "//div[@class='rc-virtual-list-holder-inner']/div[@title='Podcast']")
    # TAGS
    TAGS_INPUT = (By.XPATH, "//input[@id='tags']")

    # -- Adding a new Blog -- #

    # Add new Blog Section
    ADD_BLOCK_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-default add-block-button']")
    # Blog Type
    BLOG_TYPE_DROPDOWN = (By.XPATH, "//span[@class='anticon anticon-down']")
    BLOG_TYPE_TEXT = (By.XPATH, "//span[@class='ant-dropdown-menu-title-content'][contains(text(), 'Text')]")
    BLOG_TYPE_IMAGE = (By.XPATH, "//span[@class='ant-dropdown-menu-title-content'][contains(text(), 'Image')]")
    BLOG_TYPE_AUDIO = (By.XPATH, "//span[@class='ant-dropdown-menu-title-content'][contains(text(), 'Audio')]")

    # --- Text Blog --- #

    # Text-Toolbar
    TEXT_FORMATTER_SELECTOR = (By.XPATH, "//span[@aria-controls='ql-picker-options-1']")
    # Text - Style
    BOLD_TEXT = (By.XPATH, "//button[@class='ql-bold']")
    ITALIC_TEXT = (By.XPATH, "//button[@class='ql-italic']")
    UNDERLINE_TEXT = (By.XPATH, "//button[@class='ql-underline']")
    LINK_TEXT = (By.XPATH, "//button[@class='ql-link']")
    # List
    ORDERED_LIST = (By.XPATH, "//button[@value='ordered']")
    BULLET_LIST = (By.XPATH, "//button[@value='bullet']")
    # Clear Format
    CLEAR_FORMATTING = (By.XPATH, "//button[@class='ql-clean']")
    # Text Area
    TEXT_AREA = (By.XPATH, "//div[@class='ql-editor']")

    # -- Image Blog -- #

    # Layout Selector
    LAYOUT_SELECTOR = (By.XPATH, "(//a/span[@class='ant-avatar ant-avatar-square ant-avatar-icon neumorphify'])[3]")
    IMAGE_UPLOAD = (By.XPATH, "//input[@accept='image/png, image/jpeg']")

    # -- Audio Blog -- #
    AUDIO_INPUT = (By.XPATH, "//span[contains(text(), 'Upload Audio Files')]/../../input")
    CAPTION_INPUT = (By.XPATH, "//input[@class='ant-input']")


    # -- Submit Button -- #
    PUBLISHED_RADIO = (By.XPATH, "(//span[@class='ant-radio'])[1]")
    DRAFT_RADIO = (By.XPATH, "(//span[@class='ant-radio'])[2]")
    # Upload Image
    UPLOAD_IMG = (By.XPATH, "//input[@accept='image/*']")
    OKAY = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")

    # SUBMIT_BTN
    UPDATE = (By.XPATH, "//button[@class='ant-btn ant-btn-round ant-btn-primary']")

    # Confirmation Msg
    ERROR_MSG = (By.XPATH, "//div[@class='ant-notification-notice-message']")

    # Methods

    def navigate_to_blog(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.BLOG_TAB)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find Blog Tab : {str(e)}")

    def get_header_text(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.HEADER_TEXT)).text
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Text : {str(e)}")

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, window.innerHeight);")

    # Adding new Blog
    def click_add_new(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ADD_NEW_BTN)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find Add new button : {str(e)}")

    # Input Title
    def input_title(self, title):
        try:
            self.wait.until(EC.visibility_of_element_located(self.TITLE)).send_keys(title)
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Title Input : {str(e)}")

    def add_new_block(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ADD_BLOCK_BTN)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find Add new block : {str(e)}")

    # Selecting Blog type
    def click_on_type(self, selector_No):
        try:
            BLOG_TYPE_DROPDOWN = (By.XPATH, f"(//span[@class='anticon anticon-down'])[{selector_No}]")
            self.wait.until(EC.visibility_of_element_located(BLOG_TYPE_DROPDOWN)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find click on Blog Type : {str(e)}")

    def text_blog(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.BLOG_TYPE_TEXT)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Text Blog Button : {str(e)}")

    def image_blog(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.BLOG_TYPE_IMAGE)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Image Blog Button : {str(e)}")

    def audio_blog(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.BLOG_TYPE_AUDIO)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Audio Blog Button : {str(e)}")

    # Text-Format Methods
    def text_style(self, text_flag):
        """
        :param text_flag: 1 = Heading 1, 2 = Heading 2, 3 = Heading 3
        :return: Text format
        """
        try:
            self.wait.until(EC.visibility_of_element_located(self.TEXT_FORMATTER_SELECTOR)).click()
            TEXT_FORMATTER_VALUE = (
                By.XPATH, f"//span[contains(@class, 'ql-picker-item') and contains(@data-value, '{text_flag}')]")
            self.wait.until(EC.visibility_of_element_located(TEXT_FORMATTER_VALUE)).click()
        except(NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Something went wrong while selecting the Text format : {str(e)}")

    # Bold
    def bold_text(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.BOLD_TEXT)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Bold Button : {str(e)}")

    # Italic
    def italic_text(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ITALIC_TEXT)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Italic Button : {str(e)}")

    # Underline
    def underline_text(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.UNDERLINE_TEXT)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Underline  Button : {str(e)}")

    # Link-Text

    # TODO - Complete this when you whole Text blog is complete
    def link_text(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.LINK_TEXT)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the link Button : {str(e)}")

    #  -- Incomplete Module --

    # Order list
    def order_list(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ORDERED_LIST)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Order list Button : {str(e)}")

    # Bullet list
    def bullet_list(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.BULLET_LIST)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the UnOrder list Button : {str(e)}")

    # Clear format
    def clear_format(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.CLEAR_FORMATTING)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Clear Format Button : {str(e)}")

    # TODO - Start working from Text filed

    # Textarea
    def input_content(self, content):
        try:
            self.wait.until(EC.visibility_of_element_located(self.TEXT_AREA)).send_keys(content)
            self.driver.find_element(*self.TEXT_AREA).send_keys(Keys.ENTER)
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Text area : {str(e)}")

    def click_publish(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.PUBLISHED_RADIO)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Publish button : {str(e)}")

    def click_draft(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.DRAFT_RADIO)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Draft button : {str(e)}")

    def upload_image(self, ImgPath):
        try:
            self.driver.find_element(*self.UPLOAD_IMG).send_keys(ImgPath)
            time.sleep(1)
            self.driver.find_element(*self.OKAY).click()
        except (NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find to upload image : {str(e)}")

    # Adding Author Details

    def click_on_Author(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.AUTHOR_SELECTOR)).click()
            self.driver.find_element(*self.AUTHOR_VALUE).click()
        except (NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find to Author : {str(e)}")

    def enter_shortDescriptions(self, descriptions):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SHORT_DESCRIPTIONS)).send_keys(descriptions)
        except (NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find to Short Descriptions : {str(e)}")

    def select_type(self, type_flag):
        try:
            self.driver.find_element(*self.TYPE_SELECTOR).click()
            if type_flag == 1:
                self.wait.until(EC.visibility_of_element_located(self.TYPE_IMAGE)).click()
            elif type_flag == 2:
                self.wait.until(EC.visibility_of_element_located(self.TYPE_VIDEO)).click()
            elif type_flag == 3:
                self.wait.until(EC.visibility_of_element_located(self.TYPE_PODCAST)).click()
        except (NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find to Type  : {str(e)}")

    def input_tags(self, tags):
        try:
            self.wait.until(EC.visibility_of_element_located(self.TAGS_INPUT)).send_keys(tags)
            self.wait.until(EC.visibility_of_element_located(self.TAGS_INPUT)).send_keys(Keys.ENTER)
        except (NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find to Tags : {str(e)}")

    def click_update(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.UPDATE)).click()
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Draft button : {str(e)}")

    def check_created(self, Title):
        try:
            TITLE_NAME = (By.XPATH, f"//div[@class='LinesEllipsis  '][contains(text(), '{Title}')]")
            return self.wait.until(EC.visibility_of_element_located(TITLE_NAME)).text
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Draft button : {str(e)}")

    # Adding Image Details

    def click_layout(self, layout_flag):

        """
        :param layout_flag: 1 for Layout 1 : 2 for Layout 2 : 3 for Layout 3 : 4 for Layout 4
        :return: click()
        """
        try:
            self.wait.until(EC.visibility_of_element_located(self.LAYOUT_SELECTOR)).click()
            UNIVERSAL_SELECTOR = (By.XPATH, f"(//div[@class='ant-row'])[4]/div[{layout_flag}]")
            self.wait.until(EC.visibility_of_element_located(UNIVERSAL_SELECTOR)).click()
        except(NoSuchElementException, Exception, AttributeError, TimeoutException) as e:
            self.log.error(f"Unable to find the Layout selector and Layout : {str(e)}")

    def upload_blog_images(self, layout_flag, images_array):

        """
        :param layout_flag: Flag for choosing the Layout Type
        :param images_array: List of Images depending upon the Layout
        :return: Upload images depending upon the Layout
        """
        try:
            images_array = images_array.split(",")
            if layout_flag == 1:
                indexes = [1, 2, 3, 4, 5]
                for index, image_array in zip(indexes, images_array):
                    IMAGE_PATH = (By.XPATH, f"(//input[@accept='image/png, image/jpeg'])[{index}]")
                    self.driver.find_element(*IMAGE_PATH).send_keys(image_array)
            elif layout_flag == 2:
                indexes = [1, 2, 3, 4, 5]
                for index, image_array in zip(indexes, images_array):
                    IMAGE_PATH = (By.XPATH, f"(//input[@accept='image/png, image/jpeg'])[{index}]")
                    self.driver.find_element(*IMAGE_PATH).send_keys(image_array)
            elif layout_flag == 3:
                indexes = [1, 2, 3, 4, 5, 6]
                for index, image_array in zip(indexes, images_array):
                    IMAGE_PATH = (By.XPATH, f"(//input[@accept='image/png, image/jpeg'])[{index}]")
                    self.driver.find_element(*IMAGE_PATH).send_keys(image_array)
            elif layout_flag == 4:
                indexes = [1, 2, 3]
                for index, image_array in zip(indexes, images_array):
                    IMAGE_PATH = (By.XPATH, f"(//input[@accept='image/png, image/jpeg'])[{index}]")
                    self.driver.find_element(*IMAGE_PATH).send_keys(image_array)
        except(TimeoutException, NoSuchElementException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Image Upload tab : {str(e)}")

    # Adding Audio Blog
    def upload_audio(self, audioPath):
        try:
            self.driver.find_element(*self.AUDIO_INPUT).send_keys(audioPath)
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Upload Audio button : {str(e)}")

    def input_caption(self, caption):
        try:
            self.driver.find_element(*self.CAPTION_INPUT).send_keys(caption)
        except (NoSuchElementException, TimeoutException, Exception, AttributeError) as e:
            self.log.error(f"Unable to find the Caption input box : {str(e)}")

    def check_blog_created(self, name):
        try:
            CREATED_NAME = (By.XPATH, f"//tr[@class='ant-table-row ant-table-row-level-0']/td/div[contains(text(), '{name}')]")
            print(f"RESULT : {self.wait.until(EC.visibility_of_element_located(CREATED_NAME)).is_displayed()}")
            return self.wait.until(EC.visibility_of_element_located(CREATED_NAME)).is_displayed()
        except(NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find the Created Element : {str(e)}")

