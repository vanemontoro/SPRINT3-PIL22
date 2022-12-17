from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
options= webdriver.ChromeOptions()

driver.maximize_window()
driver.get('https://www.arredo.com.ar/')
time.sleep(4)

#Primera interacción buscar y agregar el primer producto para validar que coincida en el carrito

#Busca "almohadon" y elige uno del resultado
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div/label/div/input').send_keys('almohadon')
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div/label/div/span/div/div/button').click()
time.sleep(10)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[2]/div/div/section/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/div[5]/section/a/article/div[6]/div/div').click()
time.sleep(3)

#captura el valor para la variable que se valida al final
itemName= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[1]/div/div/div[1]/div/div/h1/span').text

#Agrega 3 unidades al carrito
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[5]/div/div/div[1]/div/div/div/div/div/div/input').send_keys(Keys.BACK_SPACE)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[5]/div/div/div[1]/div/div/div/div/div/div/input').send_keys('3')
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[5]/div/div/div[2]/div/div/button/div').click()

#Abre el carrito con el botón, se despliega la vista previa
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[3]/aside/div/div/button').click()
time.sleep(1)

#Se asignan valores a la variables para validar: nombre de item en pagina de producto y en carrito
requirement = (itemName)     
labelObtained = (driver.find_element(By.XPATH,'/html/body/div[6]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[1]/a').text)
print("*****************************\nValor de la variable: "+ itemName)


#Se define la función que compara valores en la single page de producto y en carrito
def compareLabels():
    if requirement in labelObtained:
        result= "igual al seleccionado"
    else:
        result= "distinto al seleccionado"
    return result
       
#Ejecuta la función
print("*****************************\nSe valida que el producto agregado es: "+ compareLabels())

#Cierra el carrito, y vuelve a Home
driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/button').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/a/span/img').click()
time.sleep(6)


#Segunda interacción agregar un segundo producto, para validar color elegido

#Busca el segundo producto "Cubrecama"
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div/label/div/input').send_keys('cubrecama')
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div/label/div/span/div/div/button').click()
time.sleep(10)

#Selecciona un producto del resultado
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[2]/div/div/section/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/div[2]/section/a/article/div[6]/div/div').click()
time.sleep(3)

#Selecciona color ROSA
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[3]/div/div/div/div/div/div/div[2]/div[7]').click()

#Captura la variable con el nombre del color seleccionado para validar al final
itemColor= driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[3]/div/div/div/div/div/div/div[1]/span[3]').text
print("*****************************\n Valor de la variable: "+ itemColor)

#Agrega 3 unidades al carrito
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[5]/div/div/div[1]/div/div/div/div/div/div/input').send_keys(Keys.BACK_SPACE)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[5]/div/div/div[1]/div/div/div/div/div/div/input').send_keys('3')
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[5]/div/div/div[2]/div/div/button/div').click()
time.sleep(1)

#Abre el carrito
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[3]/aside/div/div/button').click()
time.sleep(2)

#Se actualizan los valores de las variables 
requirement = (itemColor)
labelObtained = (driver.find_element(By.XPATH,'/html/body/div[6]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div/div').text)
print("*****************************\nValor de la variable de color en carrito: "+ labelObtained)

print("*****************************\nSe valida que el color agregado es: "+compareLabels())


#Tercer interacción, uso del link "vaciar carrito" para validar que realmente elimine todas las selecciones previas
#En el carrito abierto anteriormente, clic en "Vaciar carrito"
driver.find_element(By.XPATH,"//button[normalize-space()='VACIAR CARRITO']").click()
time.sleep(1)

requirement= "Tu carrito no tiene productos"
labelObtained= driver.find_element(By.XPATH,"//p[@class='lh-copy vtex-rich-text-0-x-paragraph']").text

def checkEmpty():
    if requirement == labelObtained:
        result = "se borraron todos los items"
    else:
        result= "no se vació el carrito, u ocurrio un error"
    return result

print("*****************************\nSe valida que "+ checkEmpty())
print("*****************************\nTest finalizado!")

