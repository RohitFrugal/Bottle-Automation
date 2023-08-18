import time
from Pages.Blog.BlogPage import BlogPage


def compare(actual, expected):
    print(f"\nActual : {actual}")
    print(f"Expected : {expected}")

    if actual == expected:
        return True
    else:
        return False


class BlogMethods:
    def __init__(self, driver):
        self.driver = driver
        self.blog = BlogPage(self.driver)

    # Helper
    def input_basic_blog_info(self, descriptions, Blog_type, tags):
        self.blog.click_on_Author()
        self.blog.enter_shortDescriptions(descriptions)
        self.blog.select_type(Blog_type)
        self.blog.input_tags(tags)

    def style_text_content(self, style_type, content):
        self.blog.text_style(style_type)
        self.blog.input_content(content)

    def fill_text_area(self, style_types, contents):
        style_types = style_types.split(",")
        contents = contents.split(",")
        for style_type, content in zip(style_types, contents):
            self.style_text_content(style_type, content)

    def order_items(self, content_items):
        content_items = content_items.split(",")
        print(type(content_items))

        self.blog.order_list()
        for content_item in content_items:
            self.blog.input_content(content_item)
        self.blog.order_list()

    # ************ #
    # Test Methods #
    # ************ #

    def test_landing(self):
        self.blog.navigate_to_blog()
        return compare(self.blog.get_header_text(), "Blogs")

    def create_new_blog(self, shortDescriptions, blog_type, tags, title, style_types, text_contents, list_items, imgPath, imgBlogLayout, imageArrays,  audiClip, caption):
        self.blog.navigate_to_blog()
        self.blog.click_add_new()
        # Basic Info -- Author/Descriptions/type/tags
        self.input_basic_blog_info(shortDescriptions, blog_type, tags)

        # Blog Body Title
        self.blog.input_title(title)

        # Text Blog
        self.blog.add_new_block()
        self.blog.text_blog()
        self.fill_text_area(style_types, text_contents)
        self.order_items(list_items)
        self.blog.scroll_down()

        # Image Blog
        self.blog.add_new_block()
        self.blog.click_on_type(2)
        self.blog.image_blog()
        self.blog.click_layout(imgBlogLayout)
        self.blog.upload_blog_images(imgBlogLayout, imageArrays)

        # Audio Blog
        # time.sleep(3)
        # self.blog.add_new_block()
        # self.blog.click_on_type(3)
        # self.blog.audio_blog()
        # self.blog.upload_audio(audiClip)
        # self.blog.input_caption(caption)

        time.sleep(5)

        # Submission - Button
        self.blog.upload_image(imgPath)
        self.blog.click_draft()
        self.blog.click_update()
        time.sleep(5)
        return self.blog.check_blog_created(title)
