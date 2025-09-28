import { useNavigate } from "react-router-dom";
import { useState } from "react";
import '../styles/main.css';
import runCode from "./runCode";


function MainPage () {
    const [inputText, setInputText] = useState('')
    const [outputText, setOutputText] = useState('')
    const navigate = useNavigate()

    const handleRunCode = async () => {
        setOutputText("Executing...")
        const result = await runCode(inputText)

        setOutputText(result.result || 'No output');

    }

    
    
    return (
        <div className="editor-container">
            <div className="header">
                <h1>RIMLang Editor</h1>
                <button 
                    className="back-button" 
                    onClick={() => navigate('/')}
                >
                    Home
                </button>
            </div>
            
            <div>
                <textarea 
                    className="code-editor"
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                    placeholder="Enter your RIMLang code here..."
                />
            </div>
            
            <div className="output-container">
                <div className="output">
                    <pre className="output-text">
                        {outputText || "Output will appear here..."}
                    </pre>
                </div>
                <button
                    className="run-button"
                    onClick={handleRunCode}
                >
                    Run Code
                </button>
            </div>
        </div>
    )
}

export default MainPage;