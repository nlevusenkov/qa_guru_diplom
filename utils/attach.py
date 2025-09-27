import os

import allure
from allure_commons.types import AttachmentType
from selene import browser


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='Screenshot', attachment_type=allure.attachment_type.PNG)
def add_bstack_screenshot():
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='Screenshot', attachment_type=allure.attachment_type.PNG)

def add_xml():
    xml_dump = browser.driver.page_source
    allure.attach(body=xml_dump, name='XML screen', attachment_type=allure.attachment_type.XML)


def attach_bstack_video(session_id):
    import requests
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(os.getenv('USER_NAME'), os.getenv('ACCESS_KEY')),
    ).json()
    print(bstack_session)
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )


def add_video(browser):
    video_url = f"https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')

def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')