export const Button = ({ text, type }) => {
  return (
    <button className="shadow bg-bgColor  focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded-full mb-6 w-40" type={type}>
      {text}
    </button>
  )
}
