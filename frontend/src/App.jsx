import { useState } from 'react'
import BookNavbar from './components/BookNavbar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <BookNavbar/>
    </>
  )
}

export default App
