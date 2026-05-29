from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class Checkout_Page_Class:
    playstation4_xpath="//h3[normalize-space()='Playstation 4']"
    addtocart_xpath="//input[@value='Add to Cart']"
    continueshopping_xpath="//a[@class='btn btn-primary btn-lg']"
    applemacbk_xpath="//h3[normalize-space()='Apple Macbook Pro']"
    proceedtockout_xpath="//a[@class='btn btn-success btn-lg']"

    first_name_id="first_name"
    last_name_id="last_name"
    phone_id="phone"
    address_id="address"
    zip_id="zip"
    state_id="state"

    owner_id="owner"
    cvv_id="cvv"
    cardno_id="cardNumber"
    ###expiration date
    expirymon_id="exp_month"
    expiryyr_id="exp_year"
    continutochkout_xpath="//button[@id='confirm-purchase']"

    def __init__(self, driver):  ##CONSTRUCTOR
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5, 0.25)

    def Click_playstation4(self):
        self.driver.find_element(By.XPATH, self.playstation4_xpath).click()
    def Click_addtocart(self):
        self.driver.find_element(By.XPATH, self.addtocart_xpath).click()
    def Click_continueshopping(self):
        self.driver.find_element(By.XPATH, self.continueshopping_xpath).click()
    def Click_applemacbk(self):
        self.driver.find_element(By.XPATH, self.applemacbk_xpath).click()
    def Click_proceedtockout(self):
        self.driver.find_element(By.XPATH, self.proceedtockout_xpath).click()

    def Enterfirstname(self,first_name):
        self.driver.find_element(By.ID, self.first_name_id).send_keys(first_name)
    def Enterlastname(self,last_name):
        self.driver.find_element(By.ID, self.last_name_id).send_keys(last_name)
    def Enterphoneno(self,phone_no):
        self.driver.find_element(By.ID, self.phone_id).send_keys(phone_no)
    def Enteraddress(self,address):
        self.driver.find_element(By.ID, self.address_id).send_keys(address)
    def Enterzip(self,zip):
        self.driver.find_element(By.ID, self.zip_id).send_keys(zip)

    def Enterowner(self,owner):
        self.driver.find_element(By.ID, self.owner_id).send_keys(owner)
    def Entercvv(self,cvv):
        self.driver.find_element(By.ID, self.cvv_id).send_keys(cvv)
    def Entercardno(self,cardno):
        self.driver.find_element(By.ID, self.cardno_id).send_keys(cardno)
    def Select_expirymon(self,mon):
        dropdown=Select(self.driver.find_element(By.ID, self.expirymon_id))
        dropdown.select_by_visible_text(mon)

    def Select_expiryyr(self,year):
        dropdown=Select(self.driver.find_element(By.ID, self.expiryyr_id))
        dropdown.select_by_visible_text(year)

    def Click_conticheckout(self):
        self.driver.find_element(By.XPATH, self.continutochkout_xpath).click()

