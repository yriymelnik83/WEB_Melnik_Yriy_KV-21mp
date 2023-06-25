describe('links managing spec', () => {
  it('passes', () => {
    cy.visit('http://localhost:8000')
    cy.contains('Login').click()
    cy.get('input[name="username"]').type('Karton4a')
    cy.get('input[type="password"]').type('Karate2os0')
    cy.get('button[type="submit"]').click()
    cy.visit('http://localhost:8000/userPage')
    cy.contains('Add').click()
    cy.get('div.col>input').type('https://stackoverflow.com/')
    cy.contains('Login').click() // change focus
    cy.get('input[id="url"]').should('have.value','https://stackoverflow.com/')

    cy.get('input[id="url"]').clear()
    cy.get('input[id="url"]').type('https://stackoverflow.com/123')
    cy.contains('Login').click() // change focus

    cy.get('input[id="url"]').should('have.value','https://stackoverflow.com/123')

    cy.contains('X').click()
    cy.get('input[id="url"]').should('not.exist')
  })
})