*** Settings ***
Documentation     Basic App Testing
Library           Screenshot
Library           SeleniumLibrary
Suite Setup       Open Browser    ${URL}    ${BROWSER}
Suite Teardown    Close All Browsers


*** Variables ***
${URL}            http://127.0.0.1:9999/
${BROWSER}        Chrome
${MAIN_PAGE_PAGE_CONTAINER_LOCATOR}    class:q-page-container
${MAIN_PAGE_ADD_CONTACT_LINK}    id:add-contact-link
${ADD_CONTACT_PAGE_HEADER}    class:q-header


*** Test Cases ***
Main page test
    [Documentation]    This can open main page and go to contacts
    ...    asserts texts
    Set Window Size    1000    800
    Wait Until Element Is Enabled    ${MAIN_PAGE_PAGE_CONTAINER_LOCATOR}
    ${link_content}    Get Text   ${MAIN_PAGE_ADD_CONTACT_LINK}
    Should Be Equal As Strings    ${link_content}    add contact
    Click Link  xpath=//a[@id='add-contact-link']
    Wait Until Element Is Enabled    ${MAIN_PAGE_PAGE_CONTAINER_LOCATOR}
    Element Should Contain  ${ADD_CONTACT_PAGE_HEADER}  New contact
