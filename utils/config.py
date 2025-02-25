# =============== GENERAL SETTINGS ===============
TIMEOUT = 90  # 无日期后刷新间隔

# =============== VISA CENTER SELECTION ===============
CENTER_MAN = ('England', 'Manchester', 'Normal', 'Tourism')
CENTER_EDN = ('Scotland', 'Edinburgh', 'Normal', 'Tourism')
CENTER_LON = ('Bristol', 'London', 'Normal', 'Tourist')

# ======================= MODE =========================
# 日期选择页面的4个勾勾，从上到下的顺序，可以自己选择
# 不使用加急
MODE_NORMAL = ('Yes', 'Yes', 'No', 'Yes')
# 使用加急
MODE_FAST = ('Yes', 'Yes', 'Yes', 'Yes')

# =============== PERSONAL CONFIG FOR VISA ===============
FIXED = 'https://uk.blsspainvisa.com/visa4spain/book-appointment/'

# ======================= USER LIST =======================
# 这里添加客户
# 账号参数: Email, 密码, 链接地址, 中心地点(CENTER_MAN, CENTER_EDN, CENTER_LON), 是否优先(MODE_NORMAL, MODE_FAST), None是启动线程池的默认参数
No1 = (['zhuyue0806@gmail.com', 'ADnnnn0931!@', 'X6uqpJaiiQ', CENTER_EDN, MODE_FAST], None)
No2 = (['secondPersonEmail@xxx.com', '@password@', 'X6Wnq5ms5f', CENTER_EDN, MODE_NORMAL], None)
# 加入线程池
USERS = [No1, No2]
