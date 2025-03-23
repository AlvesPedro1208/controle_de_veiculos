export default function Dashboard() {
    const usuario = JSON.parse(localStorage.getItem("usuario"))
  
    return (
      <div style={{ padding: 20 }}>
        <h1>Bem-vindo ao ERP de Frota</h1>
        <p>Usuário logado: <strong>{usuario?.username}</strong></p>
        <p>Email: {usuario?.email}</p>
        <p>Status: {usuario?.status}</p>
      </div>
    )
  }
  