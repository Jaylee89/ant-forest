import subprocess
from model import Operator as op
import aircv as ac



class Util(object):
    """
    to run command
    """
    def run(cmd, op = None):
        try:
            result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception as error:
            print(f"run method error is ${error}")

    def command(cmd, action = None):
        result = False
        if (action is None) or (action == op.DETECT_DEVICE_CONNECTION):
            result = self.detect_device_connection()
        if result:
            if action == op.CAPTURE_SCREENSHOTS:
                pass

    def detect_device_connection(self) -> bool:
        '''检查设备是否连接成功，如果成功返回True，否则返回False'''
        try:
            '''获取设备列表信息，并用"\r\n"拆分'''
            deviceInfo= subprocess.check_output('adb devices').split("\r\n")
            '''如果没有链接设备或者设备读取失败，第二个元素为空'''
            if deviceInfo[1] == '':
                return False
            else:
                return True
        except Exception,e:
            print(f"Device Connect Fail: ${e}")


    def screenshot(self):
        # path = PATH(os.getcwd() + "/images/captured")
        # timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        os.popen("adb wait-for-device")
        os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
        if not os.path.isdir(PATH(os.getcwd() + "/images/captured")):
            os.makedirs(path)
        os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + timestamp + ".png"))
    
    def clean_screenshot(self):
        os.popen("adb shell rm /data/local/tmp/tmp.png")

    # 对比两张图，找到坐标。
    def match_image(imgsrc, imgtpl):  # imgsrc=原始图像，imgobj=待查找的图片
        src = ac.imread(imgsrc)
        tpl = ac.imread(imgtpl)
        match_result = ac.find_all_template(src, tpl,0.9)
        # 0.9、confidence是精度，越小对比的精度就越低 {'confidence': 0.5435812473297119,
        # 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.alipay_leave0)}
        # if len(match_result) != 0:
        #     match_result['shape'] = (src.shape[1], tpl.shape[0])  # 0为高，1为宽
        return match_result
