from pyscript import document

# =========================
# CLASSMATE CLASS
# =========================

class Classmate:

    def __init__(self, name, section, hobby):

        self.name = name
        self.section = section
        self.hobby = hobby

    def introduce(self):

        return (
            f"Hi! I'm {self.name} "
            f"from {self.section} "
            f"and I like {self.hobby}."
        )


# =========================
# DEFAULT CLASSMATES
# =========================

classmates = [

    Classmate(
        "Rochel",
        "10 Emerald",
        "drawing"
    ),

    Classmate(
        "Padme",
        "10 Emerald",
        "drawing"
    ),

    Classmate(
        "Joshua",
        "10 Emerald",
        " gaming"
    ),

    Classmate(
        "Sky",
        "10 Emerald",
        "playing the violin"
    ),

    Classmate(
        "Travis",
        "10 Emerald",
        "gaming"
    )
]


# =========================
# ADD CLASSMATE
# =========================

def add_classmate(event):

    # Get input elements
    name_input = document.getElementById("classmate1")
    section_input = document.getElementById("section")
    hobby_input = document.getElementById("subject")

    # Output area
    output = document.getElementById("output")

    # Get input values
    name = name_input.value.strip()
    section = section_input.value.strip()
    hobby = hobby_input.value.strip()

    # Validation
    if name == "" or section == "" or hobby == "":

        output.innerHTML = (
            """
            <p>Please fill out all fields.</p>
            """
        )

        return

    # Create new classmate object
    new_student = Classmate(
        name,
        section,
        hobby
    )

    # Add to list
    classmates.append(new_student)

    # Success message
    output.innerHTML = (
        f"""
        <p>
            {name} added successfully!
        </p>
        """
    )

    # Clear inputs
    name_input.value = ""
    section_input.value = ""
    hobby_input.value = ""


# =========================
# SHOW CLASSMATES
# =========================

def show_classmates(event):

    output = document.getElementById("output")

    # Clear previous output
    output.innerHTML = ""

    # Display classmates
    for student in classmates:

        output.innerHTML += (
            f"""
            <div style="
                background:#e8f5e9;
                padding:12px;
                border-radius:10px;
                margin-bottom:12px;
                border-left:5px solid #0f8f3d;
            ">

                {student.introduce()}

            </div>
            """
        )