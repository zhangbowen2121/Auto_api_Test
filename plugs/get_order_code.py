# 生成订单号
import time


def get_order_code():
    #order_no = str('T'+time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))+ str(time.time()).replace('.', '')[-7:]
    order_no = str(time.strftime('%d', time.localtime(time.time()))) + str(time.time()).replace('.',
                                                                                                                '')[-7:]
    return order_no