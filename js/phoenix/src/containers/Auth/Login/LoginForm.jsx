import react from "react"
import { Input, Button } from "../../../components"
import { useState } from "react"
import { useAuth } from "../../../components/"
import { useRouter } from 'next/router'

export const LoginForm = () => {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const router=useRouter()
  const { login } = useAuth()
  const handleLogin=(e)=>{
    e.preventDefault()
    console.log(email,password)
    login(email,password).then(authUser=>{
      console.log(authUser)
      router.push("/")
    }).catch(error => {
      console.log(error.message)
      alert("Invalid Credentials")
    });
  }
  return(
    <form className="w-full max-w-sm mt-6 flex flex-col justify-center" onSubmit={handleLogin}>
      <Input placeholder="Email" setFunction={setEmail} type="email"/>
      <Input placeholder="Password" setFunction={setPassword} type="password"/>
      <div className="flex justify-center">
        <Button text="Sign in" type="submit"/>
      </div>
    </form>
  )
}
