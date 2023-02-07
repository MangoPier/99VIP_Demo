# 99 VIP 47-49
import zmail
"""
测试通过zmail模块发送HTML格式的邮件报告
"""
# 方式1：手写一份HTML格式的测试报告
content_html = """
<h1>网页测试报告邮件</h1>
<h2>本次测试的总结</h2>
<p>测试用例全部通过，没有发现问题</p>
<a href="https://www.baidu.com">查看详情，可点击</a>
"""



# 定义好发送的邮件文本和邮件的主题
# 【案例1】这里是发送文本
mail = {
    'subject':'邮件主题：文本格式的测试报告',
    'content_text':'这是一份文本格式的测试报告，用来记录这一次测试的结果详情'
}

# 【案例2】这里是发送HTML，注意第三行要改key值
mail = {
    'subject':'邮件主题：文本格式的测试报告',
    'content_html':content_html
}

# 【案例3】这里是发送HTML，加上附件，注意路径要写对
mail = {
    'subject':'邮件主题：文本格式的测试报告',
    # 'content_html':content_html,
    'content_text':'测试的总结报告，详情请看附件',
    'attachments':'../test_report46.html'
}

# 定义发送人的信息 变量名=zmail.server("qq号码","授权码")
server = zmail.server("1192549787@qq.com","pwkqsbhbcamsggcd")
# 发送邮件:server.send_mail(收件人的邮件地址，邮件的主题与文本）
server.send_mail("1192549787@qq.com",mail)


