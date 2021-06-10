import react, { useState } from 'react'
import Input from "./input"

function Echo(props) {
    const [txt, setTxt] = useState("")
    const inpKeyDown = (event) => {  // 匿名函數
        console.log(event.target.value)
        setTxt(event.target.value)
    }
    return (
    <> 
        <div> {txt} </div>
        <Input onChange={inpKeyDown} />
    </>
    )
}
export default Echo
