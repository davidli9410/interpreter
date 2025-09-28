import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import '../styles/landing.css'

function LandingPage() {
    const [displayText, setDisplayText] = useState('')
    const [displaySubText, setDisplaySubText] = useState('')
    const [showButton, setShowButton] = useState(false)
    const [buttonVisible, setButtonVisible] = useState(false)
    const navigate = useNavigate()

    const [isTitleComplete, setIsTitleComplete] = useState(false)
    const [isSubTextComplete, setIsSubTextComplete] = useState(false)
    const fullText = 'RIMLang'
    const subText = 'A readable, interpreted, mathematical language'
    
    useEffect(() => {
        let currentIndex = 0
        const typingSpeed = 150 
        
        const typingInterval = setInterval(() => {
            if (currentIndex < fullText.length) {
                setDisplayText(fullText.slice(0, currentIndex + 1))
                currentIndex++
            } else {
                clearInterval(typingInterval)
                setIsTitleComplete(true)
                setTimeout(() => {
                    let subIndex = 0
                    const subTypingInterval = setInterval(() => {
                        if (subIndex < subText.length) {
                            setDisplaySubText(subText.slice(0, subIndex + 1))
                            subIndex++
                        } else {
                            clearInterval(subTypingInterval)
                            setIsSubTextComplete(true)
                            setTimeout(() => {
                                setShowButton(true)
                                setTimeout(() => setButtonVisible(true), 50)
                            }, 1000) 
                        }
                    }, 50) 
                }, 250) 
            }
        }, typingSpeed)
        
        return () => clearInterval(typingInterval)
    }, [])
    
    return (
        <div className="page">
            <div>
            <h1 className={`typing-text ${isTitleComplete ? 'no-cursor' : ''}`}>{displayText}</h1>
            </div>
            <div>
            <h2 className={`typing-subtext ${isSubTextComplete ? 'no-cursor' : ''}`}>{displaySubText}</h2>
            </div>
            <div className="button-container">
                {showButton && (
                    <button className={`main-button ${buttonVisible ? 'button-visible' : ''}`} onClick={() => navigate('/main')}>
                        Try it out
                    </button>
                )}
            </div>
        </div>
    )
}

export default LandingPage;