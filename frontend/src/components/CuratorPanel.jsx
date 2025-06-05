import { useEffect, useState } from 'react'

export default function CuratorPanel({ username, onLogout }) {
  const [employees, setEmployees] = useState([])

  useEffect(() => {
    fetch('/api/employees').then(res => res.json()).then(setEmployees)
  }, [])

  return (
    <div style={{ padding: '1rem' }}>
      <h2>Панель куратора – {username}</h2>
      <button onClick={onLogout}>Выход</button>
      <ul>
        {employees.map(emp => (
          <li key={emp.id}>{emp.nickname} – {emp.city} – {emp.deposit}р – {emp.mk}</li>
        ))}
      </ul>
    </div>
  )
}
