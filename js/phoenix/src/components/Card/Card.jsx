import { Label } from "../../components"

export const Card = ({ children }) => {
    return (
        <div className="bg-slate-500 rounded-md flex flex-col justify-center items-center">
            {children}
        </div>
    )
}