import pytest
from pages.docs_and_series_page import DocsSeriesPage

@pytest.mark.usefixtures("setup")
class Test_DocsSeries:
    def test_01_featured_documentary_section(self):
        self.util_obj.logger.info("\n ***** test_01_featured_documentary_section *****")
        status,message=self.ds_obj.featured_documentary_section()
        assert status, message
    def test_02_featured_documentary_title(self):
        self.util_obj.logger.info("\n ***** test_02_featured_documentary_title *****")
        status,message=self.ds_obj.featured_documentary_title()
        assert status, message
    def test_03_featured_documentary_description(self):
        self.util_obj.logger.info("\n ***** test_03_featured_documentary_description  *****")
        status,message=self.ds_obj.featured_documentary_description()
        assert status,message
    def test_04_featured_documentary_play(self):
        self.util_obj.logger.info("\n ***** test_04_featured_documentary_play *****")
        status,message=self.ds_obj.featured_documentary_play()
        assert status,message
    def test_05_recently_added_list(self):
        self.util_obj.logger.info("\n ***** test_05_recently_added_list *****")
        status,message=self.ds_obj.recently_added_title_and_respective_caption()
        assert status,message
    def test_06_see_more_redirection_link (self):
        self.util_obj.logger.info("\n ***** test_06_see_more_redirection_link  *****")
        status,message=self.ds_obj.see_more_redirection_link()
        assert status,message