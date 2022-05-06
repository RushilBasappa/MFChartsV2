import { Button } from "../components"
import { useAuth } from "../../src/context/AuthContext"

const Home = () => {
  const { logout } = useAuth()

  const handleLogout = (e) => {
    e.preventDefault()

    logout().then(authUser => {
    }).catch(error => {
      console.log(error.message)
      alert("Logout Not successfull")
    });
  }

  const handleChangePassword = (e) => {
    e.preventDefault()

    logout().then(authUser => {
    }).catch(error => {
      console.log(error.message)
      alert("Logout Not successfull")
    });
  }

  return (
    <div className="flex justify-center items-center text-2xl">
      <Button text="Logout" handleClick={handleLogout} />
      <Button text="Change Password" handleClick={handleChangePassword} />
    </div>
  )
}

export default Home
