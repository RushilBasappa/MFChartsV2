import { Button, Input } from "../../../components";

export const SignupForm = () => {
    return (
        <form className="mt-6 flex flex-col justify-center">
            <div className="flex flex-row">
                <Input placeholder="First Name" />
                <Input placeholder="Last Name" />
            </div>
            <Input placeholder="Email" />
            <Input placeholder="Password" />
            <div className="flex justify-center">
                <Button text="Sign Up" />
            </div>
        </form>
    );
}

export default SignupForm;