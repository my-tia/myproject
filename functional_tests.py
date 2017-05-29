
#ทีเร็คกำลังเดินทางไปต่างจังหวัด แต่ไม่รู้ว่าต้องเติมน้ำมันไปเท่าไร ถึงจะพอและไม่ต้องเติมเต็มถัง 
#เพื่อนของทีเร็คได้แนะนำเว็บนึงที่น่าสนใจ เขาจึงลองเข้าไปตามที่อยู่เว็บที่ได้รับมาจากเพื่อน

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        #เพื่อนของทีเร็คได้แนะนำเว็บนึงที่น่าสนใจ เขาจึงลองเข้าไปตามที่อยู่เว็บที่ได้รับมาจากเพื่อน
        self.browser.get('http://localhost:8000/calpetrol')

        #เขาเห็นแถบหน้าต่างเว็บนั้นเขียนไว้ว่า’calculate petrol for your car’ หัวเรื่อง ‘calculate petrol’
        self.assertIn('calculate petrol for your car', self.browser.title)  
        self.fail('Finish the test!')  

        #หน้าเว็บมีตัวเลือกอยู่สามอันโดยอันแรกเป็น source ,destination และ car type ตามลำดับ

        #เมื่อเขาเลือกเสร็จก็ใส่ค่าราคาน้ำมันลงไป

        #แล้วเขาก็เลือกปุ่มกด calculate

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 



