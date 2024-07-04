import os
import random
import pickle
import logging
from time import sleep
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
USER_AGENT = {'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

options = webdriver.ChromeOptions()
# options.add_argument("--windows-size = 1000,1000") 
options.add_argument(f'USER-AGENT={USER_AGENT}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--start-maximized') #sirve para iniciar chrome maximizado 
options.add_argument('--disable-web-security') #desabilita la politica d l mismo origen
options.add_argument('--disable-extensions') # sirve para que no cargue extensiones de chrome
options.add_argument('--ignore-certifficate-errors') #ignora el aviso de 'su conexion no es privada'
options.add_argument('--no-sandbox') #deshabilita el modo sanbox
options.add_argument('--long-level=3') #para tener  una terminal limpia
options.add_argument('--allow-running-unsecure-content') #desactiva el aviso de contenido no seguro
options.add_argument('--no-default-browswer-check') #evita el aviso de que chrome no es el navegador por defecto
options.add_argument('--no-first-run') #evita la ejecucion de tareas que se realizan cuando se es nuevo en chrome
options.add_argument('--no-proxy-server') #para no usar proxy
options.add_argument('--disable-blink-features=AutomationControlled') #evita que selenium sea detectado como un bot

#PARAMETROS A OMITIR EN EL INICIO DE CHROMEDRIVER:
exp_opt = [
        'enable-automation', #para que no muestre el mensaje de 'software automatizado'
        'ignore-cerificate-errors' #para ignorar errores de certificados
        'enable-logging' # para que no muestre 'devtools listening' en la terminal
        ]
options.add_experimental_option('excludeSwitches', exp_opt)
    
    # PARAMETROS DE PREFERENCIAS WN CHROMEDRIVER:
prefs={
        'profile.defaut_content_setting_values.notifications': 2, #notificaciones: 0=preguntar|1=permitir|2=no permitir notificaciones
        'intl.accept_languages': ['en-EN', 'en'], #preferencia de idiomas
        'credentials_enable_service': False #sirve para evitar que chrome pregunte si queremos guardar las contrasenias.
        }

options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=options)
driver.get('https://www.youtube.com/')

wait=WebDriverWait(driver, 40)

def sing_in():
    if os.path.isfile('youtube.cookies'):
        log_cookies()
    acceder  = wait.until(EC.visibility_of_element_located((By.XPATH, '//ytd-button-renderer[@id="sign-in-button"]')))
    pause()
    acceder.click()

    pause()
    input_email = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@type="email"]')))
    pause()
    input_email.send_keys('adoniscabrera240@gmail.com')
    logging.warning('Email Ingresado')

    pause()
    next_button =  wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="identifierNext"]/div/button')))
    pause()
    next_button.click()
    

    pause()
    input_password = next_button =  wait.until(EC.visibility_of_element_located((By.XPATH, '//div/input[@type="password"]')))
    pause()
    input_password.send_keys('AdonisEduardo2000')
    logging.warning('contrasenia Ingresadoa')
    next_button_pass = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button/span')))
    pause()
    next_button_pass.click()
    save_cookies()
    sleep(20)

    
    pause()
    not_now_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//div/div[1]/button[1]')))
    pause()
    not_now_button.click()




def save_cookies():
    cookies = driver.get_cookies()
    pickle.dump(cookies, open('youtube.cookies', 'wb'))
    # driver.get('https://www.youtube.com/robots.txt')
    # for cookie in cookies:
    #     driver.add_cookie(cookie)
    driver.get('https://www.youtube.com/')
def log_cookies():
   pickle.load(open('youtube.cookies', 'rb'))


# --PAUSE--->
def pause():
   stop=random.uniform(5,10)
   sleep(stop)

def run():
    sing_in()



if __name__ == '__main__':
    run()
    print('Fin')
    while True:
      pass
