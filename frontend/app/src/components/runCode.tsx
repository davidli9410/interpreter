async function runCode(code: string) {
    const apiUrl = 'http://127.0.0.1:5000/execute';

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: code }),
        });

        const data = await response.json();
        return data
    } catch (error) {
        console.error("API call failed:", error);
        return {"error": "An unknown network error occurred."}
    }
}

export default runCode