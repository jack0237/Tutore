import React from 'react'
import Im1 from '../../images/1.png';
import Im3 from '../../images/3.jpg';
import Im6 from '../../images/6.png';
import './Section1.css'

const Section1 = () => {
  return (
    
    <div className="side">
            <div className="logo">
                <img src={Im1} alt="" />
                gesdoc
            </div>
            <div className="user">
                <i className="fa fa-user-circle" aria-hidden="true"></i>User name and account
            </div>
            <div className="options">
                <a href="#"><i className="fa fa-home" aria-hidden="true"></i></a>
                <a href="#"><i className="fa fa-users" aria-hidden="true"></i></a>
                <a href="#"><i className="fa fa-calendar" aria-hidden="true"></i></a>
                <a href="#"><i className="fas fa-wallet fa-xs fa-fw"></i></a>
                <a href="#"><i className="fa fa-times-circle" aria-hidden="true"></i></a>
            </div>

            <p id="espace">espace colaboratif</p>

            <li className="colaboration">
                <a href="#"><img src= {Im6} alt="docs" /> Tout les espaces</a>
                <a href="#"><img src= {Im6} alt="docs" /> Commercial</a>
                <a href="#"><img src= {Im6} alt="docs" /> Demonstration</a>
                <a href="#"><img src= {Im6} alt="docs" /> Projet</a>
                <a href="#"><img src= {Im6} alt="docs" /> Culture</a>
                <a href="#"><img src= {Im6} alt="docs" /> Projet</a>
            </li>

            <p id="compte" className=''>votre compte</p>

            <li className="comptes">
                <a href="#">Mon profile</a>
                <a href="#">Mes params</a>
                <a href="#">Administration</a>
            </li>

        </div>

  )
}

export default Section1