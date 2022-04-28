import { Input, Button } from "../../../components"

export const LoginForm = () => {
  return (
    <form className="max-w-sm mt-6 flex flex-col justify-center">
      <Input placeholder="Email" />
      <Input placeholder="Password" />
      <div className="flex justify-center">
        <Button text="Sign in" />
      </div>
    </form>
  )
}
