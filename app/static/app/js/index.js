function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function onClick(event) {
    if (event.target.nodeName == 'SPAN') {
        parentElement = event.target.parentElement.parentElement.id
    }
    else {
        parentElement = event.target.id
    }

    if (parentElement == "experience-name-one") {
        hiddenElement = document.getElementById('exp-details-one')
        if (hiddenElement.style.display == 'none' || hiddenElement.style.display == '') {
            hiddenElement.style.display = 'block';
            iconElement = document.getElementById("job-con-one")
            iconElement.textContent = "Content Engineering -"
        }
        else {
            hiddenElement.style.display = 'none';
            iconElement = document.getElementById("job-con-one")
            iconElement.textContent = "Content Engineering +"
        }

    }
    if (parentElement == "experience-name-two") {
        hiddenElement = document.getElementById('exp-details-two')
        if (hiddenElement.style.display == 'none' || hiddenElement.style.display == '') {
            hiddenElement.style.display = 'block';
            iconElement = document.getElementById("job-con-two")
            iconElement.textContent = "Software Engineering -"
        }
        else {
            hiddenElement.style.display = 'none';
            iconElement = document.getElementById("job-con-two")
            iconElement.textContent = "Software Engineering +"
        }

    }
}