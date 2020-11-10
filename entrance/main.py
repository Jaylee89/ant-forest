
class Main(object):
    pass

if __name__ == '__main__':
    
    #1 check adb connection
    """
    获取手机名称
    adb shell getprop ro.product.model
    获取手机版本
    adb shell getprop ro.build.version.release
    获取手机厂商
    adb shell getprop ro.product.brand
    获取整个相关手机信息
    adb shell getprop | grep product
    """

    #2 capture images
    """
    adb wait-for-device
    adb shell screencap -p /sdcard/download/
    """

    #3 compare exiting file to captured image and return match points

    # 4 return match points

    #5 execute touch point
    """
    adb shell input tap <x> <y>
    """

    #6 page scroll down
    """
    adb shell input swipe <x1> <y1> <x2> <y2> [duration(ms)]
    """

    #7 go back #2

