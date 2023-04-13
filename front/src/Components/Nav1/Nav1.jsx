import React from 'react'
import Im2 from '../../images/2.png';
import './Nav1.css'

const Nav1 = props => {
    return (
        <nav className="nav_1">
            <div className="logo2">
                <img src={Im2} alt="logo2" /> demonstration
            </div>
            <li>
                <a href="#" onclick="openForm()">+Ajouter des fichiers</a>
                <a href="#">+Cree un repertoire</a>
                <a href="#">i</a>
                <a href="#">?</a>
            </li>
        </nav>
    )
}


export default Nav1