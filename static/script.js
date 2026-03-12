let history = [];
function selectOp(op){
    let inputArea = document.getElementById("input-area");
    //inputArea is the text box where the user inputs their calculations. I want to clear it after every calculation, so I set its innerHTML to an empty string.
    inputArea.innerHTML = "";
    //Below, the code checks if the operation selected is "log". If it is, we only need one input field for the number. If it's not, we need two input fields for the two numbers.
    if (op === "clear"){
        document.getElementById("history").innerHTML = "";
        document.getElementById("result").innerHTML = "";
        return;
    } else if(op === "log"){
        inputArea.innerHTML = '<input type="number" id="num1" placeholder="Enter first number">';
    } else if(op === "graph"){
        inputArea.innerHTML = '<input type="text" id="num1" placeholder="Enter function of x, e.g. sin(x)">';
    inputArea.innerHTML = `
        <input type="text" id="num1" placeholder="Enter function e.g. 2*x+3">
        <input type="number" id="xmin" placeholder="X min (default -10)">
        <input type="number" id="xmax" placeholder="X max (default 10)">
    `; 
    } else{
    inputArea.innerHTML = '<input type="number" id="num1" placeholder="Enter first number"><input type="number" id="num2" placeholder="Enter second number">';
    }
    //Below, I added a button to the input area that will call the calculate function when clicked. Notice how I put in '${op}'. This is a template literal that allows us to insert the value of the op variable into the string. This way, when the button is clicked, it will call the calculate function with the correct operation, all autonomously without me having to write separate code for each operation.
    inputArea.innerHTML += `<button onclick="calculate('${op}')">Calculate</button>`;

}
function calculate(op){
    //Here, I get the values of the input fields. I use document.getElementById to get the elements by their IDs, and then I use .value to get the values that the user has entered. For num2, I check if the element exists (since it won't exist for the "log" operation) and if it does, I get its value; otherwise, I set it to null(I can't set it to zero otherwise potential bugs may occur, despite the unlikelihood)
    let num1 = document.getElementById("num1").value;
    let num2 = document.getElementById("num2") ? document.getElementById("num2").value : null;
    let result;
    if (op === "graph") {
    //So that the graph starts at the correct position.
        let xmin = document.getElementById("xmin").value || -10;
        let xmax = document.getElementById("xmax").value || 10;
    fetch("/graph", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ func: num1, xmin, xmax })
    })
    .then(response => response.json())
    .then(data => {
        if (data.image) {
            document.getElementById("result").innerHTML = `<img src="data:image/png;base64,${data.image}" alt="Graph">`;
        } else {
            document.getElementById("result").innerHTML = data.result;
        }
    });
    return;
}
    
    //Fetch is really complicated, but essentially it allows the code to send a request to the server (in this case the /calculate(it's a calculator)) Here are some notes of mine:
    //1. fetch("/calculate," this is saying to go to the /calculate endpoint on my server and do something there. Fetch is what it seems - you're asking your code to fetch something.
    //2. method: "POST" - this is saying that I want to send data to the server. In this case, we want to send the operation and the numbers that the user has entered. POST means you're getting something, and GET means you're asking to recieve something.
    //3. headers: {"Content-Type": "application/json"}, this is saying to Flask that the data I'm sending is in JSON, and without this, Flask doesn't know what to expect, so the program just won't run.
    //4. body: JSON.stringify({ op, num1, num2 }) so this is just telling Flask what data I'm actually sending. Before we were telling it what type of data, and now I'm giving exactly what the data is.
    //5. then. - this whole thing is really simple, just read it out loud. "Then." just means "after you do the fetch, do this". So after I send the data to the server, I want to wait for a response. The response will be in JSON format, so I use response.json() to parse it. Then, I take the data that we got back from the server and set the innerHTML of the result element to the result that I got back from the server.
    //Overall, this is how the frontend and backend communicate. The frontend sends a request to the backend with the data that the user has entered, and then the backend processes that data and sends back a response, which the frontend then displays to the user. Please tell me you know what front end and back end are.
            
        
    fetch("/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ operation:op, num1, num2 })
    })
    .then(response => response.json())
    .then(data => {
    if (data.image) {
        document.getElementById("result").innerHTML = `<img src="data:image/png;base64,${data.image}" alt="Graph" style="max-width:100%;">`;
    } else {
        document.getElementById("result").innerHTML = data.result;
    }
    });
}