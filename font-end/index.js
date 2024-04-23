/** Once the arrow is clicked, toggle the src attribute of the image tag*/
function changeArrowColor() {
    // get all the arrow ids
    const arrowIds = document.querySelectorAll('[id^="arrow-"]')
    // loop through the arrow ids
    arrowIds.forEach(arrowId => {

    // add event listener to all the arrow ids
    arrowId.addEventListener("click", function() {
        // select img tag inside the section
        const arrowOne = arrowId.childNodes[3]
        if (arrowOne.getAttribute("src") === "./down-vector.png") {
            arrowOne.setAttribute("src", "./up-vector.png");
        } else {
            arrowOne.setAttribute("src", "./down-vector.png");
        }
    }
    )
})
}

changeArrowColor();

