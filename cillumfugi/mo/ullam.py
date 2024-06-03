WebDriverWait(driver, wait_time).until(
    EC.presence_of_element_located((By.ID, "element_id"))
)
