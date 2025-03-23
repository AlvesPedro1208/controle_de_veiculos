import { useState } from "react"
import axios from "axios"

export default function Login() {
  const [form, setForm] = useState({ username: "", senha: "" })
  const [mensagem, setMensagem] = useState("")
  const [usuario, setUsuario] = useState(null)

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setMensagem("")
    setUsuario(null)
  
    try {
      const res = await axios.post(`${import.meta.env.VITE_API_URL}/api/auth/login`, form)
      setMensagem(res.data.mensagem)
      setUsuario(res.data.usuario)
      localStorage.setItem("usuario", JSON.stringify(res.data.usuario))
      window.location.href = "/dashboard"
    } catch (err) {
      console.error("Erro no login:", err)
      if (err.response) {
        console.log("Resposta da API:", err.response.data)
        setMensagem(err.response.data.erro || "Erro ao fazer login")
      } else {
        setMensagem("Erro ao conectar com o servidor")
      }
    }
  }

  return (
    <div style={{ maxWidth: "300px", margin: "100px auto", textAlign: "center" }}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Usuário"
          value={form.username}
          onChange={handleChange}
          required
        />
        <br />
        <input
          type="password"
          name="senha"
          placeholder="Senha"
          value={form.senha}
          onChange={handleChange}
          required
        />
        <br />
        <button type="submit" style={{ marginTop: "10px" }}>Entrar</button>
      </form>
      {mensagem && <p style={{ marginTop: "15px" }}>{mensagem}</p>}
      {usuario && (
        <div style={{ marginTop: "20px" }}>
          <p><strong>Usuário:</strong> {usuario.username}</p>
          <p><strong>Email:</strong> {usuario.email}</p>
          <p><strong>Status:</strong> {usuario.status}</p>
        </div>
      )}
    </div>
  )
}
