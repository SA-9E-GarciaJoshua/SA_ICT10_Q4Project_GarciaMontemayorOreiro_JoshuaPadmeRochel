from pyscript import document
import numpy as np
import matplotlib.pyplot as plt

days = []
absences = []


def displaying(event):

    day = document.getElementById("dayOfTheWeek").value

    absence_input = document.getElementById("absences")

    output = document.getElementById(
        "attendance-output"
    )

    if absence_input.value == "":

        output.innerHTML = (
            "<p>Please enter absences.</p>"
        )

        return

    absence = int(absence_input.value)

    days.append(day)
    absences.append(absence)

    output.innerHTML = (
        f"<p>Added {absence} absence(s) for {day}.</p>"
    )

    plt.clf()

    x = np.array(days)
    y = np.array(absences)

    plt.plot(x, y, marker="o")

    plt.title("Weekly Attendance")
    plt.xlabel("Day")
    plt.ylabel("Absences")

    plt.grid(True)

    plt.show()