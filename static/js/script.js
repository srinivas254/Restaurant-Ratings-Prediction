document.getElementById("prediction-form").onsubmit = async function (e) {
    e.preventDefault(); 
    const formData = new FormData(this);
    const response = await fetch("/predict", {
      method: "POST",
      body: formData,
    });

    if (response.ok) {
      const data = await response.json();
      document.getElementById("result").innerText =
        "Your Rating is: " + data.prediction;
    } else {
      document.getElementById("result").innerText = "Error in prediction";
    }
  };