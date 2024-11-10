from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import infoBrowser as iBrowser

infoBrowser = iBrowser.InfoBrowser()
navegador = infoBrowser.start_browser_selenium()


def busca_linkedin():
    try:
        navegador.get("https://www.google.com")

        campo_busca = WebDriverWait(navegador, 10).until( EC.presence_of_element_located((By.NAME, 'q'))) 

        campo_busca.send_keys("LinkedIn")

        botao = WebDriverWait(navegador, 10).until( EC.element_to_be_clickable((By.NAME, 'btnK')))
        botao.click()
        
        navegador.find_element(By.CLASS_NAME, 'LC20lb').click()


        
        navegador.get("https://www.linkedin.com/login/")
        
        navegador.find_element(By.ID, "username").send_keys("INSIRA_AQUI_SEU_EMAIL")
        navegador.find_element(By.ID, "password").send_keys("INSIRA_AQUI_SUA_SENHA")

        botao = WebDriverWait(navegador, 10).until( EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        botao.click()



        WebDriverWait(navegador, 20).until( EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Pesquisar"]')))
                
        campo_busca_linkedin = navegador.find_element(By.XPATH, '//input[@placeholder="Pesquisar"]')
        
        campo_busca_linkedin.send_keys('Recepcionista' + Keys.ENTER)

        botao = WebDriverWait(navegador, 40).until( EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-pill.search-reusables__filter-pill-button")))
        botao.click()
                
        elementos_nome_vaga = WebDriverWait(navegador, 30).until( EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container__link.job-card-list__title.job-card-list__title--link")))

        elemento_localizacao = WebDriverWait(navegador, 30).until( EC.visibility_of_all_elements_located((By.CLASS_NAME, 'job-card-container__metadata-item')))


        for vaga, localizacao in zip(elementos_nome_vaga, elemento_localizacao):
            print("LINKEDIN")
            print(f"Vaga: {vaga.text}")
            print(f"Localização: {localizacao.text}\n")

    finally:
        print("Busca no linkedin finalizada.")




def busca_gupy():
    try:
        navegador.get("https://www.google.com")

        campo_busca = WebDriverWait(navegador, 10).until( EC.presence_of_element_located((By.NAME, 'q')))
        
        campo_busca.send_keys("Gupy")

        WebDriverWait(navegador, 10).until( EC.element_to_be_clickable((By.NAME, 'btnK'))).click()
        
        navegador.find_element(By.CLASS_NAME, 'LC20lb').click()
        
        
        navegador.get("https://login.gupy.io/candidates/signin")

        try:
            consent_banner = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.cc-btn.cc-deny')))
            
            consent_banner.click()
        except Exception as e:
            print("Banner de consentimento não encontrado ou já foi fechado.")

        username_input = WebDriverWait(navegador, 20).until( EC.element_to_be_clickable((By.ID, "username")))

        username_input.send_keys("INSIRA_AQUI_SEU_EMAIL")
        navegador.find_element(By.NAME, "password").send_keys("INSIRA_AQUI_SUA_SENHA")

        navegador.find_element(By.ID, 'button-signin').click()
        
        
        try:
            fechar_banner = WebDriverWait(navegador, 20).until( EC.element_to_be_clickable((By.ID, "pushActionRefuse")))
            fechar_banner.click() 

        except Exception as e:
            print("Banner de consentimento não encontrado ou já foi fechado.")


        try:
            fechar_banner = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dp-bar-button[title="Rejeitar"]')))
            fechar_banner.click()
        except Exception as e:
            print("Banner de consentimento não encontrado ou já foi fechado.")




        avatar_elemento = WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'avatar') and contains(@class, 'avatar__default')]")))
        avatar_elemento.click()

    
        avatar_elemento = WebDriverWait(navegador, 20).until( EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='access-portal-button']")))
        avatar_elemento.click()


    
        campo_busca = WebDriverWait(navegador, 30).until( EC.element_to_be_clickable((By.NAME, 'searchTerm')))
        
        campo_busca.send_keys("Desenvolvedor Front-end")
        
        WebDriverWait(navegador, 30).until( EC.element_to_be_clickable((By.ID, 'undefined-button'))).click()
        
        elementos_nome_vaga = WebDriverWait(navegador, 30).until( EC.visibility_of_all_elements_located((By.TAG_NAME, 'h3')))
    
        elemento_localizacao = WebDriverWait(navegador, 30).until( EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="job-location"]')))


        for vaga, localizacao in zip(elementos_nome_vaga, elemento_localizacao):
            print("GUPY.IO")
            print(f"Vaga: {vaga.text}")
            print(f"Localização: {localizacao.text}\n")
    
    finally:
        print("Busca na Gupy finalizada.")

if not navegador:
    print("Seu navegador padrão não é suportado para essa aplicação")
    print("Navegadores suportados: Chrome, Firefox, Microsoft Edge, Internet Explorer e Safari.")
else:
    print("Iniciando busca na Gupy...")
    busca_gupy()
    print("Iniciando busca no Linkedin...")
    busca_linkedin()
    navegador.quit()
