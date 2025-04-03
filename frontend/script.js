document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("taskForm")
    .addEventListener("submit", async function (event) {
      event.preventDefault();
      const description = document.getElementById("description").value;

      const taskData = {
        description: description,
        isComplete: false,
      };

      try {
        const response = await fetch("http://localhost:8000/task", {
          method: "POST",
          headers: {
            "Content-type": "application/json",
          },
          body: JSON.stringify(taskData),
        });
        await response.json();
        document.getElementById("responseStatus").textContent =
          "Task Created Successfully";
      } catch (error) {
        document.getElementById(responseStatus).textContent = error.textContent;
      }
    });
});

document
  .getElementById("deleteTaskForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();
    const taskId = document.getElementById("taskId").value;

    try {
      const response = await fetch(
        `http://localhost:8000/task/delete/${taskId}`,
        {
          method: "DELETE",
        }
      );

      if (response.ok) {
        document.getElementById("responseStatus").textContent =
          "Task Deleted Successfully";
      } else {
        document.getElementById("responseStatus").textContent =
          "Error deleting task";
      }
    } catch (error) {
      document.getElementById("responseStatus").textContent =
        "Error deleting task";
    }
  });

document
  .getElementById("getTaskForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    try {
      const response = await fetch("http://localhost:8000/tasks/all", {
        method: "GET",
      });

      if (response.ok) {
        const tasks = await response.json();

        if (tasks.length === 0) {
          document.getElementById("responseStatus").textContent =
            "No tasks found.";
        } else {
          let result = "Tasks:\n";
          tasks.forEach((task) => {
            result += `ID: ${task.id}, Description: ${task.description}, Completed: ${task.isComplete}\n`;
          });
          document.getElementById("responseStatus").textContent = result;
        }
      } else {
        document.getElementById("responseStatus").textContent =
          "Error fetching tasks.";
      }
    } catch (error) {
      document.getElementById("responseStatus").textContent =
        "Error fetching tasks.";
    }
  });
