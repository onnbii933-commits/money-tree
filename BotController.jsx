function BotController() {

  const startBot = () => {

    fetch(
      "http://localhost:8000/bots/start",
      {
        method: "POST"
      }
    );
  };

  const stopBot = () => {

    fetch(
      "http://localhost:8000/bots/stop",
      {
        method: "POST"
      }
    );
  };

  return (

    <div className="card">

      <h2>
        Robot Control
      </h2>

      <button
        onClick={startBot}
      >
        Start Robot
      </button>

      <button
        onClick={stopBot}
      >
        Stop Robot
      </button>

    </div>

  );
}

export default BotController;
