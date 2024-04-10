*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${base_url}     https://reqres.in

*** Test Cases ***
Post_User
    create session    mysession     ${base_url}
    ${body}=    create dictionary     name=John   job=SDET
    ${header}=  create dictionary    Content-Type=application/json; charset=utf-8
    ${response}=    post on session    mysession    /api/users  ${body}   ${header}
    log to console    ${response.status_code}
    log to console    ${response.content}


    #Validations
    ${status_code}=     convert to string    ${response.status_code}
    should be equal    ${status_code}   201

     ${body}=    convert to string    ${response.content}
    should contain    ${body}   John


