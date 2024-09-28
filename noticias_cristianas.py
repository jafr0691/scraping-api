# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from flask import Flask, jsonify

app = Flask(__name__)

# Scraper para Noticias Cristianas
def scrape_noticias_cristianas():
    url = 'https://www.bibliatodo.com/NoticiasCristianas/rss-noticias-online/'
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")  # Ejecuta Firefox en modo headless
    firefox_options.add_argument("--disable-gpu")  # En caso de problemas con la aceleración gráfica
    firefox_options.add_argument("--no-sandbox")  # Útil en entornos de contenedor como Docker
    
    driver = webdriver.Firefox(options=firefox_options)

    try:
        driver.get(url)
        divs = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'container-news'))
        )

        noticias = []
        for div in divs:
            try:
                imagen = div.find_element(By.TAG_NAME, 'img').get_attribute('src') if div.find_elements(By.TAG_NAME, 'img') else 'No disponible'
                titulo = div.find_element(By.TAG_NAME, 'h2').text.strip() if div.find_elements(By.TAG_NAME, 'h2') else 'No disponible'
                enlace = div.find_element(By.TAG_NAME, 'a').get_attribute('href') if div.find_elements(By.TAG_NAME, 'a') else 'No disponible'
                fecha = div.find_element(By.TAG_NAME, 'h3').text.strip() if div.find_elements(By.TAG_NAME, 'h3') else 'No disponible'

                if titulo != 'No disponible' and enlace != 'No disponible':
                    noticias.append({
                        'imagen': imagen,
                        'titulo': titulo,
                        'enlace': enlace,
                        'fecha': fecha
                    })
            except Exception as e:
                print(f"Error al procesar el elemento: {str(e)}")
                continue

        return noticias if noticias else {'error': 'Error al capturar los datos scraping de las noticias cristianas'}
    except Exception as e:
        return {'error': f'Error inesperado: {str(e)}'}
    finally:
        driver.quit()

# Scraper para Predica del Día
def scrape_predica_del_dia():
    url = "https://www.bibliatodo.com/es"
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    
    driver = webdriver.Firefox(options=firefox_options)

    try:
        driver.get(url)

        img_element = driver.find_element(By.XPATH, '//div[contains(@class, "contenedor-titulos7")]//following-sibling::p//a//img')
        link_element = driver.find_element(By.XPATH, '//div[contains(@class, "contenedor-titulos7")]//following-sibling::p//a')

        img_url = img_element.get_attribute('src')
        href_url = link_element.get_attribute('href')

        return {
            'imagen_url': img_url,
            'pagina_url': href_url
        }
    except Exception as e:
        return {'error': f'Error al capturar los datos scraping de la predica del día: {str(e)}'}
    finally:
        driver.quit()

# Scraper para Imagen del Día
def scrape_imagen_del_dia():
    url = "https://www.bibliatodo.com/es"
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')  # Ejecutar en modo headless
    options.add_argument('--disable-gpu')  # Deshabilitar GPU si es aplicable
    
    driver = webdriver.Firefox(options=options)

    try:
        driver.get(url)

        img_element = driver.find_element(By.XPATH, '//div[contains(@class, "contenedor-imagenes")]//following-sibling::p//a//img')
        link_element = driver.find_element(By.XPATH, '//div[contains(@class, "contenedor-imagenes")]//following-sibling::p//a')

        img_url = img_element.get_attribute('src')
        href_url = link_element.get_attribute('href')

        return {
            'imagen_url': img_url,
            'pagina_url': href_url
        }
    except Exception as e:
        return {'error': f'Error al capturar los datos scraping de la imagen del día: {str(e)}'}
    finally:
        driver.quit()

# Scraper para Reflexion del Día
def scrape_reflexion_del_dia():
    url = "https://www.bibliatodo.com/online/reflexiondeldia"
    firefox_options = FirefoxOptions()
    firefox_options.add_argument('--headless')

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

    try:
        driver.get(url)

        img_element = driver.find_element(By.XPATH, '//span/a/img')
        link_element = driver.find_element(By.XPATH, '//span/a')

        img_url = img_element.get_attribute('src')
        href_url = link_element.get_attribute('href')

        return {
            'imagen_url': img_url,
            'pagina_url': href_url
        }
    except Exception as e:
        return {'error': f'Error al capturar los datos scraping de reflexion del día: {str(e)}'}
    finally:
        driver.quit()

# Scraper para Consejo del Día
def scrape_consejo_del_dia():
    url = "https://www.bibliatodo.com/online/consejodeldia"
    firefox_options = FirefoxOptions()
    firefox_options.add_argument('--headless')

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

    try:
        driver.get(url)
        # Esperar hasta que el elemento de imagen esté presente
        wait = WebDriverWait(driver, 10)
        img_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "orbit-container")]//a//img')))
        link_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "orbit-container")]//a')))

        img_url = img_element.get_attribute('src')
        href_url = link_element.get_attribute('href')

        return {
            'imagen_url': img_url,
            'pagina_url': href_url
        }
    except Exception as e:
        return {'error': f'Error al capturar los datos scraping del consejo del día: {str(e)}'}
    finally:
        driver.quit()

# Scraper para Versiculo del Día
def scrape_versiculo_del_dia():
    url = "https://www.bibliatodo.com/es/online/versiculo-del-dia"
    firefox_options = FirefoxOptions()
    firefox_options.add_argument('--headless')

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

    try:
        driver.get(url)
        # Esperar hasta que el elemento de imagen esté presente
        wait = WebDriverWait(driver, 10)
        img_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "imagenversobt")]//img')))

        img_url = img_element.get_attribute('src')

        return {
            'imagen_url': img_url,
        }
    except Exception as e:
        return {'error': f'Error al capturar los datos scraping del versiculo del día: {str(e)}'}
    finally:
        driver.quit()

# Scraper para Testimonio del Día
def scrape_testimonio_del_dia():
    url = "https://www.bibliatodo.com/es"
    firefox_options = FirefoxOptions()
    firefox_options.add_argument('--headless')

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

    try:
        driver.get(url)
        # Esperar hasta que el elemento de imagen esté presente
        wait = WebDriverWait(driver, 10)

        # Obtener la imagen del primer enlace dentro del div especificado
        img_element = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//div[contains(@class, "large-4") and contains(@class, "medium-12") and contains(@class, "small-12")]/p/a/img'))
        )

        # Obtener el enlace del primer elemento dentro del div especificado
        link_element = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//div[contains(@class, "large-4") and contains(@class, "medium-12") and contains(@class, "small-12")]/p/a'))
        )

        img_url = img_element[1].get_attribute('src')
        href_url = link_element[1].get_attribute('href')

        return {
            'imagen_url': img_url,
            'pagina_url': href_url
        }
    except Exception as e:
        return {'error': f'Error al capturar los datos scraping del Testimonio del día: {str(e)}'}
    finally:
        driver.quit()

@app.route('/noticias-cristianas', methods=['GET'])
def get_noticias_cristianas():
    try:
        noticias = scrape_noticias_cristianas()
        return jsonify(noticias)
    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al realizar el scraping a las noticias cristianas: {str(e)}'}), 500
    

@app.route('/predica-del-dia', methods=['GET'])
def get_predica():
    try:
        predica = scrape_predica_del_dia()
        return jsonify(predica)
    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al realizar el scraping a la predica del dia: {str(e)}'}), 500
    
@app.route('/imagen-del-dia', methods=['GET'])
def get_imagen():
    try:
        imagen = scrape_imagen_del_dia()
        return jsonify(imagen)
    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al realizar el scraping a la imagen del dia: {str(e)}'}), 500

@app.route('/reflexion-del-dia', methods=['GET'])
def get_reflexion():
    try:
        reflexion = scrape_reflexion_del_dia()
        return jsonify(reflexion)
    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al realizar el scraping a la reflexion del dia: {str(e)}'}), 500

@app.route('/consejo-del-dia', methods=['GET'])
def get_consejo():
    try:
        consejo = scrape_consejo_del_dia()
        return jsonify(consejo)
    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al realizar el scraping al consejo del dia: {str(e)}'}), 500
    
@app.route('/versiculo-del-dia', methods=['GET'])
def get_versiculo():
    try:
        versiculo = scrape_versiculo_del_dia()
        return jsonify(versiculo)
    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al realizar el scraping al versiculo del dia: {str(e)}'}), 500
    
@app.route('/testimonio-del-dia', methods=['GET'])
def get_testimonio():
    try:
        testimonio = scrape_testimonio_del_dia()
        return jsonify(testimonio)
    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al realizar el scraping al testimonio del dia: {str(e)}'}), 500

@app.route('/', methods=['GET'])
def get_testimonio():
    try:
        testimonio = {
            'info':'Esta web es un servicio api sobre informacion Cristiana.',
            'Urls':{
                    os.path.join(os.path.dirname(__file__), '/noticias-cristiana'),
                    os.path.join(os.path.dirname(__file__), '/predica-del-dia'),
                    os.path.join(os.path.dirname(__file__), '/imagen-del-dia'),
                    os.path.join(os.path.dirname(__file__), '/reflexion-del-dia'),
                    os.path.join(os.path.dirname(__file__), '/testimonio-del-dia'),
                    os.path.join(os.path.dirname(__file__), '/consejo-del-dia'),
                    os.path.join(os.path.dirname(__file__), '/versiculo-del-dia')
                }
            }
        return jsonify(testimonio)
    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al realizar el scraping al testimonio del dia: {str(e)}'}), 500
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
