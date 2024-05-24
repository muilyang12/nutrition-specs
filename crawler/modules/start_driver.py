from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.edge.service import Service


def start_driver():
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)

    return driver
