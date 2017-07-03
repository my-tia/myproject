
#ทีเร็คกำลังเดินทางไปต่างจังหวัด แต่ไม่รู้ว่าต้องเติมน้ำมันไปเท่าไร ถึงจะพอและไม่ต้องเติมเต็มถัง 
#เพื่อนของทีเร็คได้แนะนำเว็บนึงที่น่าสนใจ เขาจึงลองเข้าไปตามที่อยู่เว็บที่ได้รับมาจากเพื่อน

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()


    def test_can_start_a_list_and_retrieve_it_later(self):  
        #เพื่อนของทีเร็คได้แนะนำเว็บนึงที่น่าสนใจ เขาจึงลองเข้าไปตามที่อยู่เว็บที่ได้รับมาจากเพื่อน
        self.browser.get('http://localhost:8000/')

        #เขาเห็นแถบหน้าต่างเว็บนั้นเขียนไว้ว่า’calculate petrol for your car’ หัวเรื่อง ‘calculate petrol’
        self.assertIn('calculate petrol for your car', self.browser.title)  
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('คำนวณราคาน้ำมันระหว่างจังหวัดในประเทศไทย', header_text)
        self.browser.find_element_by_id('start').click()
        


    def test_signup(self):
        #เขายังไม่เคยเข้าระบบลงทะเบียน จึงคลิกไปที่ url ที่ลงทะเบียนใหม่
        self.browser.get("http://localhost:8000/signup/")
 
       #คลิกปุ่ม sign up แล้วหน้า urlจะไปที่หน้าแรกทันทีเมื่อลงเสร็จ
        self.browser.find_element_by_id('signup').click()
        self.assertIn("http://localhost:8000/", self.browser.current_url)

    def test_login(self):
        #หลังจากที่เขาได้ลงทะเบียนเสร็จ ก็ทำการlogin เข้าระบบต่อ
        self.browser.get("http://localhost:8000/login/")
        #self.driver.find_element_by_id('id_title').send_keys("test title")
        #self.driver.find_element_by_id('id_body').send_keys("test body")
       #คลิกปุ่ม login 
        self.browser.find_element_by_id('login').click()
        self.fail('Finish the test!')  

    def tearDown(self):  
        self.browser.quit()       

    def test_cal(self):
        self.browser.get("http://localhost:8000/cal/")
      #หน้าเว็บมีตัวเลือกอยู่สามอันโดยอันแรกเป็น source ,destination และ car type ตามลำดับ

        #เมื่อเขาเลือกเสร็จก็ใส่ค่าราคาน้ำมันลงไป

        #แล้วเขาก็เลือกปุ่มกด calculate
        self.browser.find_element_by_id('cal').click()

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 



