import unittest
from bill100 import Billboard100Parser

b = Billboard100Parser()

class Bill100Test(unittest.TestCase):

    def url_test(self):
        """url must been set"""
        self.assertTrue(b.url)

    def get_html_test(self):
        """should get html"""
        self.assertTrue(b.get_html)

    def get_test(self):
        """get video titles"""
        self.assertTrue(b.get_titles)

    def title_len_test(self):
        """make sure the titles consists of more than 100 titles"""
        self.assertEqual(len(b.get_titles()), 199)

    def ids_len_test(self):
        """make sure the ids is 199 in length"""
        self.assertEqual(len(b.get_videos()), 199)

    def get_first_video_test(self):
        """makesure that the first video have id==0"""
        self.assertIn('index=1', b.get_videos()[0])

    def get_last_video_test(self):
        """makesure that the last video have id==199"""
        self.assertIn('index=199', b.get_videos()[-1])

    def get_200_video_test(self):
        """must be false, since we only have 199 videos"""
        self.assertNotIn('index=200', b.get_videos()[-1])

    def get_ids_test(self):
        """return video ids with total length == 199"""
        self.assertEqual(len(b.get_ids()), 199)

    def check_len_test(self):
        """make sure that the len of titles and video ids are the same"""
        len_titles = len(b.get_titles())
        len_ids = len(b.get_ids())
        self.assertEqual(len_titles, len_ids)


if __name__ == '__main__':
    unittest.main()
