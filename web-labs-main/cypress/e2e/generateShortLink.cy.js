describe('generate short link spec', () => {
  it('passes', () => {
    cy.visit('http://localhost:8000')
    cy.get('input[id = "shortLink"]').type('https://twitter.com/')
    cy.get('button[id = "shortenButton"]').click()
    cy.get('h2[id="resultLink]"').should("not.eq","")
    //h2 id="resultLink"
  })
})