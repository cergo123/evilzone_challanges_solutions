import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import hashlib


def hash_md5(string):
    return hashlib.md5(string.encode()).hexdigest()


driver = uc.Chrome()

driver.get('https://evilzone.org/challenges/fast_hasher/')

# click button with text 'Get 100 random hashes' and type submit
driver.find_element(By.XPATH, '//button[text()="Get 100 random hashes"]').click()

# copy textarea content with xpath /html/body/textarea
textarea = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/textarea')))
hashes = textarea.text.splitlines()

md5_hases = []
for hash in hashes:
    md5_hases.append(hash_md5(hash.strip()))

con = ''.join(md5_hases).strip()
result = hash_md5(con)

# fill input with name 'hash' with result
driver.find_element(By.NAME, 'hash').send_keys(result)

# click button with text 'Check answer' and type submit
driver.find_element(By.XPATH, '//button[text()="Check answer"]').click()

input('Press Enter to continue...')
