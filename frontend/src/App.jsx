import { useState } from 'react'
import Login from './components/Login'
import CuratorPanel from './components/CuratorPanel'
import './App.css'

function App() {
  const [user, setUser] = useState(null)

  return (
    <div>
      {user ? (
        <CuratorPanel username={user} onLogout={() => setUser(null)} />
      ) : (
        <Login onLogin={setUser} />
      )}
    </div>
  )
}

export default App
