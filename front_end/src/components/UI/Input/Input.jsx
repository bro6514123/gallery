import cl from "./Input.module.css"

const Input = ({className = null, placeholder="", value, setValue}) => {   
    return (
        <input value={value} onChange={e => {setValue(e.target.value)}} className={[cl.Input, className].join(" ")} placeholder={placeholder} />
    )
}

export default Input;
