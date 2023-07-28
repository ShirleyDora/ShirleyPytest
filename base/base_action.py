import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
<<<<<<< HEAD
=======
import allure
from subprocess import Popen,PIPE,STDOUT
import sys
>>>>>>> 3364439 (second commit)


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=30.0, poll=1.0):
        """
        根据元组的feature在timeout时间之内每poll秒照一次，找到对应的一个元素
        :param feature: 元素的特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*feature))
        # return self.driver.find_element(*feature)

    def find_elements(self, feature, timeout=30.0, poll=1.0):
        """
        根据元组的feature在timeout时间之内每poll秒照一次，找到对应的一组元素
        :param feature: 元素的特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*feature))

    def click(self, feature, timeout=30.0, poll=1.0):
        """
        根据特征，点击元素
        :param feature: 特征
        :return:
        """
        self.find_element(feature, timeout, poll).click()

    def input(self, feature, value, timeout=30.0, poll=1.0):
        """
        :param feature: 特征
        :param value: 文字
        :return:
        """
        self.clear(feature, timeout, poll)
        self.find_element(feature, timeout, poll).send_keys(value)

    def clear(self, feature, timeout=30.0, poll=1.0):
        """
        根据特征，清空
        :param feature: 特征
        :return:
        """
        self.find_element(feature, timeout, poll).clear()

    def get_feature_text(self, feature, timeout=30.0, poll=1.0):
        """
        根据元素的特征，获取元素的文字内容
        :param feature: 元素的特征
        :return: 元素的文字内容
        """
        if self.is_feature_exist(feature, timeout, poll):
            return self.find_element(feature, timeout, poll).text
        else:
            raise Exception("没有找到，对应的feature的元素，请检查。")

    def is_feature_exist(self, feature, timeout=30.0, poll=1.0):
        """
        根据元素的特征，判断这个元素是否存在
        :param feature: 元素的特征
        :return: 是否存在
        """
        try:
            self.find_element(feature, timeout, poll)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self, message, timeout=10.0, poll=0.1):
        """
        根据toast的部分消息，获取全部的toast的文字内容
        :param message: 部分消息
        :return: 全部的toast的文字内容
        """
        toast_feature = By.XPATH, "//*[contains(@text,'%s')]" % message
        if self.is_feature_exist(toast_feature, timeout, poll):
            return self.find_element(toast_feature, timeout, poll).text
        else:
            raise Exception("没有找到，对应的toast内容，请检查。")

    def is_toast_exist(self, message, timeout=10.0, poll=0.1):
        """
        根据toast的部分消息，判断toast是否存在
        :param message: 部分消息
        :return: 是否存在
        """
        toast_feature = By.XPATH, "//*[contains(@text,'%s')]" % message
        return self.is_feature_exist(toast_feature, timeout, poll)

    def scroll_page_one_time(self, direction):
        """
        滑动一次屏幕
        :param dir: 滑动的方向
            "up"：从下往上
            "down"：从上往下
            "left"：从右往左
            "right"：从左往右
        :return:
        """
        # 滑动
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        top_x = screen_width * 0.5
        top_y = screen_height * 0.25
        bottom_x = screen_width * 0.5
        bottom_y = screen_height * 0.75
        left_x = screen_width * 0.25
        left_y = screen_height * 0.5
        right_x = screen_width * 0.75
        right_y = screen_height * 0.5

        # 根据方向参数，去滑动
        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请输入正确的滑动方向 up/down/left/right")

    def find_element_with_scroll(self, feature, direction):
        """
        按照 dir 的方向滑动，并且找到 feature 这个特征的元素
        :param dir:
            "up"：从下往上
            "down"：从上往下
            "left"：从右往左
            "right"：从左往右
        :return: 找到的元素
        """
        
        while True:
            try:
                # 如果找到元素，就点进去
                # driver.find_element_by_xpath("//*[@text='用户']").click()
                # return self.driver.find_element(*feature)
                return self.find_element(feature)
            except TimeoutException:

                # 记录一下滑动之前的page_source
                old_page_source = self.driver.page_source

                self.scroll_page_one_time(direction)

                # 判断滑动之后是不是和之前的页面一样
                if old_page_source == self.driver.page_source:
                    raise Exception("到底了！请检查传入的元素的特征")

    def is_keyword_in_page_source(self, keyword, timeout=5.0, poll=0.5):
        """
        判断 keyword 是否在当前页面的 page_source 中
        :param keyword: 需要查询的字符串
        :return: 是否在页面中
        """
        end_time = time.time() + timeout
        while True:
            res = keyword in self.driver.page_source
            if res:
                return True

            if time.time() > end_time:
                return False
            time.sleep(poll)
<<<<<<< HEAD
=======
    # def get_screenshot_as_file(self):
    #     """
    #     截屏保存
    #     :return:返回路径
    #     """
    #     pic_name = str.split(str(time.time()), '.')[0] + str.split(str(time.time()), '.')[1] + '.png'
    #     screent_path = os.path.join(SCREENSHOTDIR, pic_name)
    #     self.driver.get_screenshot_as_file(screent_path)
    #     return screent_pathe
    def screen(self,s):
        if s is not None:
            allure.attach(self.driver.get_screenshot_as_png(), s, allure.attachment_type.PNG)
    def video(self,s):
        if s is not None:
            allure.attach.file("***.mp4",name="{s}",attachment_type=allure.attachment_type.MP4,extension="mp4")
    # 调起cmd命令
    def run_cmd(self,cmd):
        p = Popen(self.cmd,shell=True,stdin=PIPE,stdout=PIPE,stderr=STDOUT)
        stdout,stderr = p.communicate()
        return p.returncode,stdout.strip()
    # 前置条件
    def initlog(self):
        cmd1 = 'echo "start1:开启相关权限,by Shirley"'
        cmd2 = 'adb root'
        cmd3 = 'adb remount'
        cmd4 = 'echo "start2:开始初始化抓取蓝牙电话log,by Shirley"'
        cmd5 = 'adb shell "msg_center_test -t "misc_service/command/qxdm_ondevice_log_request" "{\"command\":\"22\", \"operation\":\"set\", \"id\":\"qxdm_ondevice_log_set\"}""'
        cmd6 = 'adb shell "ls -l /qlog/ondevice_logging"'
        cmd7 = 'adb shell "msg_center_test -t "misc_service/command/qxdm_ondevice_log_request" "{\"command\":\"23\", \"operation\":\"set\", \"id\":\"qxdm_ondevice_log_set\"}""'
        cmd8 = 'echo "start3:开始初始化抓取音频,by Shirley"'
        cmd9 = 'adb shell setprop vendor.audio.hal.dump_rx true'
        cmd10 = 'adb shell setprop sys.audio.fw.dump_rx true'
        cmd11 = 'adb shell setprop sys.audio.fw.dump_tx true'
        cmd12 = 'echo "start4:删除之前的log,by Shirley'
        cmd13 = 'adb shell rm /log/android/logcat.log.0*'
        cmd14 = 'adb shell rm /log/anr/*'
        cmd15 = 'adb shell rm /log/dropbox/*'
        cmd16 = 'adb shell rm /log/tombstones/*'
        self.run_cmd(cmd1 and cmd2 and cmd3 and cmd4 and cmd5 and cmd6 and cmd7 and cmd8
        and cmd9 and cmd10 and cmd11 and cmd12 and cmd13 and cmd14 and cmd15 and cmd16)
    
    def finishedlog(self):
        cmd1 = 'echo "创建本地存储文件,by Shirley"'
        cmd2 = 'mkdir "D:/CarLog/"'
        cmd3 = 'echo "(5)开始导出蓝牙电话log,by Shirley"'
        cmd4 = 'adb pull /qlog/ondevice_logging D:/CarLog/'
        cmd5 = 'echo "(6)开始导出音频文件,by Shirley"'
        cmd6 = 'adb pull /data/vendor/audio D:/CarLog/'
        cmd7 = 'adb pull /data/misc/audioserver D:/CarLog/'
        cmd8 = 'echo "(1)开始导出普通log,by Shirley"'
        cmd9 = 'adb pull /log/android D:/'
        cmd10 = 'echo "(2)开始导出蓝牙log,by Shirley"'
        cmd11 = 'adb pull /log/btsnoop D:/CarLog/'
        cmd12 = 'echo "(3)开始导出卡顿log,by Shirley"'
        cmd13 = 'adb pull /log/tombstones D:/CarLog/'
        cmd14 = 'adb pull /log/dropbox D:/CarLog/'
        cmd15 = 'adb pull /log/anr D:/CarLog/'
        cmd16 = 'echo "(7)结束音频导出,还原初始态,by Shirley"'
        cmd17 = 'adb shell setprop vendor.audio.hal.dump_rx false' 
        cmd18 = 'adb shell setprop sys.audio.fw.dump_rx false'
        cmd19 = 'adb shell setprop sys.audio.fw.dump_tx false'   
        self.run_cmd(cmd1 and cmd2 and cmd3 and cmd4 and cmd5 and cmd6 and cmd7 and cmd8
        and cmd9 and cmd10 and cmd11 and cmd12 and cmd13 and cmd14 and cmd15 and cmd16 
        and cmd17 and cmd18 and cmd19)
        
    def killallapp(self):
        cmd1 = 'killall com.voyah.car'
        self.run_cmd(cmd1)







    




>>>>>>> 3364439 (second commit)
