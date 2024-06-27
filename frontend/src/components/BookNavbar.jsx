const { Container } = require("react-bootstrap")

const BookNavbar = ()=>{
  return (
    <Navbar className="bg-body-tertiary">
      <h1>My book navbar here!</h1>
    <Container>
      <Navbar.Brand href="#home">
        React Bootstrap
      </Navbar.Brand>
    </Container>
  </Navbar>
  )
}

export default BookNavbar;