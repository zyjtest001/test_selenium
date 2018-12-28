import requests
import unittest

class RunCase(unittest.TestCase):
    '''执行qq号查询的接口'''
    @classmethod
    def setUpClass(cls):
        #setUpClass只运行一次，setUp是每个测试案例运行的时候都会运行
        cls.s = requests.session()
    @classmethod
    def tearDownClass(cls):
        cls.s.close()
    def setUp(self):
        self.url = "http://japi.juhe.cn/qqevaluate/qq"
    def test_01(self):
        '''key和qq参数都正确，返回预期的结果success'''
        pa = {
                "key":"207cefa9b506bb40bffa1e1c478fb4bf",
                "qq":"296638238"
            }
        act_result = requests.post(self.url,params=pa).json()['reason']
        except_result = "success"
        self.assertEqual(act_result,except_result)

    def test_02(self):
        '''key的值为空，qq参数都正确，返回预期的结果KEY ERROR!'''
        pa = {
                "key":"",
                "qq":"296638238"
            }
        act_result = requests.post(self.url,params=pa).json()['reason']
        except_result = "KEY ERROR!"
        self.assertEqual(act_result,except_result)

    def test_03(self):
        '''key的值正确，qq的值为空，返回预期的结果错误的请求参数'''
        pa = {
                "key":"207cefa9b506bb40bffa1e1c478fb4bf",
                "qq":""
            }
        act_result = requests.post(self.url,params=pa).json()['reason']
        except_result = "错误的请求参数"
        self.assertEqual(act_result,except_result)
