
import './index.css'

import LandingPage from './components/landingPage.tsx'
import MainPage from './components/mainPage.tsx'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
function App () {


    return (
        <Router>
            <Routes>
                <Route path='/main' element={<MainPage/>}/>
                <Route path='/' element={<LandingPage/>}/>

            </Routes>    
        </Router>


        
    );
}

export default App;