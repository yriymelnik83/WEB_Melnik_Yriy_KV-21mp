describe('chat spec', () => {
  it('passes', () => {
    cy.visit('http://localhost:8000')
    cy.get('input[id="messageText"]').type('Test')
    cy.get('button[id="chatButton"]').click()
    cy.get('textArea[id="chatArea"]').should('have.value','anonymus : Test\n')
  })
})