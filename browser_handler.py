from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config import NAVER_MUSIC_CONFIG, YOUTUBE_MUSIC_CONFIG


NAVER_MUSIC_URL = 'https://music.naver.com'



class BrowserHandler:

    def __init__(self):
        self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        # if input("Go to Naver Music? [y/n] :  ") == 'y':
        self.naver_music_crawl()

    def naver_music_crawl(self):
        self.to_naver_music()
        self.naver_music_login()
        self.retreive_songs_from_list()


    def to_naver_music(self):
        self.driver.get(NAVER_MUSIC_URL)

    def naver_music_login(self):
        login_button = self.driver.find_element_by_id('gnb_login_button')
        login_button.click()  # move to login page

        id_area = self.driver.find_element_by_id('id')
        pw_area = self.driver.find_element_by_id('pw')
        login_button = self.driver.find_element_by_id('log.login')

        id_area.send_keys(NAVER_MUSIC_CONFIG['ID'])
        pw_area.send_keys(NAVER_MUSIC_CONFIG['PW'])
        login_button.click()  # login and return to page

        # captcha 때문에 잘안됨. 수동으로 로그인 할 것

        # TODO:: need to deliberatly wait for the url to change to main page.
        pass

    def mylist_names(self):
        self._get_mylist_list_li_elements()
        self.mylist_list_span = []
        for _, li_element in enumerate(self.mylist_list_li_elements):
            self.mylist_list_span.append(li_element.find_element_by_tag_name('span').text)

        return self.mylist_list_span

    def _get_mylist_list_li_elements(self):
        self.mylist_list_li_elements = self.driver.find_elements_by_class_name('_music_my_list')

    def retreive_songs_from_list(self):
        # start at logged in main page.
        self._get_mylist_list_li_elements()
        self.mylist_names()
        for list_index, li_element in enumerate(self.mylist_list_li_elements):
            print(f'Working on list no.{list_index} : {self.mylist_list_span[list_index]}...')
            li_element.click()






if __name__ == '__main__':

    bh = BrowserHandler()
    pass