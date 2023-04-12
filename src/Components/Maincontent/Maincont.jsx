import React from 'react'
import './Maincont.css'
import Im6 from '../../images/6.png';

const Maintcont = ({image, title}) => {
  return (

    <div className="filescont">
        <img src={image} alt="" />
        <div>{title}</div>
    </div>
    
  )
}

export default Maintcont