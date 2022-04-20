export const Input = ({ placeholder }) => {
  const inputClassNames = [
    "bg-gray-200",
    "appearance-none",
    "border-2",
    "border-gray-200",
    "rounded-full",
    "w-full",
    "py-2",
    "px-4",
    "text-gray-700",
    "leading-tight",
    "focus:outline-none",
    "focus:bg-white",
    "focus:border-bgColor",
    "mb-6"
  ].join(" ")
  return(
    <input className={inputClassNames} type="text" placeholder={placeholder} />
  )
}
