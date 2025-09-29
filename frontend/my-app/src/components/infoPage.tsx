import '../styles/info.css';
import { useNavigate } from 'react-router-dom';

function InfoPage() {
    const navigate = useNavigate();

    const goToMain = () => {
        navigate('/main');
    };

    return (
        <div className='container'>
            <div className="header">
                <h1>Syntax Guide</h1>
                <button className="nav-button" onClick={goToMain}>
                    Editor
                </button>
            </div>
            <div className="syntax-guide">
                <p className="intro">
                    RIMlang uses syntax inspired by LaTeX as well as mathematical language
                </p>

                <h2>Basic Operations</h2>
                <div className="syntax-section">
                    <h3>Arithmetic</h3>
                    <p>To perform simple arithmetic, simply type the expression out</p>
                    <code>display 2 + 3 * 5 -&gt; 17</code>
                </div>

                <div className="syntax-section">
                    <h3>Variables</h3>
                    <p>To assign a variable x to a number 5:</p>
                    <code>define x as 5</code>
                </div>

                <div className="syntax-section">
                    <h3>Functions</h3>
                    <p>To define a function:</p>
                    <code>func add(x,y): x + y</code>
                    <p>To call the function:</p>
                    <code>display add(3,4) -&gt; 7</code>
                </div>

                <h2>Comparisons</h2>
                <div className="syntax-section">
                    <h3>Equality</h3>
                    <p>To compare two objects (same as python ==):</p>
                    <code>display 1 equals 1 -&gt; true</code>
                    <p>In the opposite case:</p>
                    <code>display 1 nequals 1 -&gt; false</code>
                </div>

                <div className="syntax-section">
                    <h3>Magnitude Comparisons</h3>
                    <p>To compare values of magnitude (&lt;, &lt;=, &gt;, &gt;= in python), use:</p>
                    <code>lt, lte, gt, gte</code>
                    <p>Example:</p>
                    <code>display 2 gt 3 -&gt; false</code>
                </div>

                <h2>Other Operations</h2>
                <div className="syntax-section">
                    <h3>Display</h3>
                    <p>To print out values, use display keyword:</p>
                    <code>display 2 + 3 -&gt; 5</code>
                </div>

                <div className="syntax-section">
                    <h3>Unary Operators</h3>
                    <p>For unary operators on a single value or variables, ! and - exist:</p>
                    <code>display -(-5) -&gt; 5</code>
                </div>

                <div className="syntax-section">
                    <h3>Booleans</h3>
                    <p>Use <code>true</code> and <code>false</code> for boolean values</p>
                </div>
            </div>
        </div>
    );
}

export default InfoPage;