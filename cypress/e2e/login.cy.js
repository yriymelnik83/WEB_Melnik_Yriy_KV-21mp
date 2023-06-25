describe('login logout spec', () => {
  it('passes', () => {
    cy.visit('http://localhost:8000')
    cy.contains('Login').click()
    cy.get('input[name="username"]').type('Karton4a')
    cy.get('input[type="password"]').type('Karate2os0')
    cy.get('button[type="submit"]').click()
    cy.contains('button', 'Karton4a').should('be.visible')
    cy.contains('Karton4a').click()
    cy.contains('Log out').click()
    cy.contains('a', 'Login').should('be.visible')
  })
})