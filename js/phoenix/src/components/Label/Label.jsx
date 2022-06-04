export const Label = ({ text, classes = [] }) => {
    const inputClassNames = [
        "block",
        "font-medium",
        ...classes
    ].join(" ")
    return (
        <span className={inputClassNames}>{text}</span>
    );
}