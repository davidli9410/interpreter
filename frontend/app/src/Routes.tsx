
import './index.css'

import LandingPage from './components/landingPage.tsx'
import MainPage from './components/mainPage.tsx'
import InfoPage from './components/infoPage.tsx'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
function RouterModule () {


    return (
        <Router>
            <Routes>
                <Route path='/main' element={<MainPage/>}/>
                <Route path='/' element={<LandingPage/>}/>
                <Route path='/info' element={<InfoPage/>}/>

            </Routes>    
        </Router>


        
    );
}

export default RouterModule ;