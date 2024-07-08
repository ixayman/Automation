import unittest

from sel.POM.youtube import BrowserWrapper
from sel.POM.youtube import ConfigProvider
from sel.POM.youtube import VideoPage
from sel.POM.youtube import check_if_array_in_descending_order


class TestDeviceTheme(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("adele")
        # cls.home_page = HomePage(cls.driver)
        cls.config = ConfigProvider()
        # cls.home_page.insert_in_search_field(cls.config.get_value(cls,"search_query"))
        # cls.home_page.search_field_enter()
        cls.driver.execute_script("window.scrollTo(0, 600)")

        cls.video_page = VideoPage(cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.close()

    def test_sort_comments_by_news_first(self):
        self.video_page.click_sort_by_newest_first()
        comments = self.video_page.get_first_5_comments()
        comment_timestamps = [self.video_page.get_comment_timestamp(self, comment) for comment in comments]
        self.assertTrue(check_if_array_in_descending_order(comment_timestamps))

    def test_sort_comments_by_top_comments(self):
        self.video_page.click_sort_by_top_comments()
        comments = self.video_page.get_first_5_comments()
        comment_likes = [self.video_page.get_comment_likes(self, comment) for comment in comments]
        for likes in comment_likes:
            self.assertGreaterEqual(likes, self.config.get_value(self, "adele-hello-minimum-likes"))


if __name__ == "__main__":
    unittest.main()
