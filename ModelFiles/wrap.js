const { spawn } = require("child_process");

// Function to execute python script
function runPythonScript(userID, num_companies) {
  // Spawn a child process
  const python = spawn("python", [
    "supply.py",
    "--userID",
    userID,
    "--num_companies",
    num_companies,
  ]);

  // Collect data from script
  python.stdout.on("data", function (data) {
    console.log("Pipe data from python script ...");
    const jsonData = JSON.parse(data);
    console.log(jsonData);
  });

  // In case of error
  python.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
  });

  // On script end
  python.on("close", (code) => {
    console.log(`child process exited with code ${code}`);
  });
}

// Call the function with parameters
runPythonScript(1, 10);
