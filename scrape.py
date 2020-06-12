from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome('C:/chromedriver')

email = "cajetanrodrigues88@email.address"
password = "*m70GskgNmmTSUmVQ#BHe!A*3D0aWk5w^0QsPPviRejXCJHdZM"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/rodriguescajetan", driver=driver)
print(person)