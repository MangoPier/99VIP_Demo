# 99 VIP P40
import logging

# 定义一个类封装自定义日志流程
class LogClass():
    def get_log(self):
        # 1、日志收集器
        logger = logging.getLogger("log_test40")

        # 2、设置日志收集器的级别
        logger.setLevel(logging.WARN)

        # 3、设置日志输出的渠道，一个是控制台输出，一个是在后台形成文件
        handle1 = logging.StreamHandler()
        handle2 = logging.FileHandler(filename="log_demo.log",encoding="utf-8")

        # 可选步骤
        # 设置输出渠道的日志级别（注意要大于前面收集器设置的级别）
        handle1.setLevel(logging.ERROR)

        # 4、设置日志输出的格式
        fmt = "%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)d %(message)s) "
        formt = logging.Formatter(fmt)

        # 5、需要让控制台输出的渠道格式为刚刚定义好的格式：formt
        handle1.setFormatter(formt)

        # 6、日志收集器添加需要的日志输出渠道
        logger.addHandler(handle1)
        logger.addHandler(handle2)

        # 测试日志生成打印
        # logger.warning("运行失败警告")
        # logger.error("运行出错")
        return logger

def sum_data(a,b):
    try:
        return a + b
    except Exception as e:
        LogClass().get_log().error("这个计算参数有问题，这是报错信息")


if __name__ == '__main__':
    # LogClass().get_log().error("报错信息")
    print(sum_data(1,2))
    print(sum_data(1,"2"))

