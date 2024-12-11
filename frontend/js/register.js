const prevBtn = document.getElementById('prev-submit');
const nextBtn = document.getElementById('next-submit');
const submitBtn = document.getElementById('submit');

const allSec = document.querySelectorAll('.reg-sec');

const progressBar = document.querySelector('.progess');
let progressBtn = document.querySelectorAll('.progess-bar');


const toastBox = document.querySelector('.toast');
const toastContent = document.getElementById('toast-content');
const closeIcon = document.querySelector('.bi-background');



function nextPage(e) {
    e.preventDefault();

    for (let index = 0; index < allSec.length; index++) {
        const element = allSec[index];

        if (!element.classList.contains("hide-now")) {
            element.classList.add("hide-now");

            if (index + 1 < allSec.length) {
                allSec[index + 1].classList.remove("hide-now");
            }

            checkNow(allSec);
            break;
        }
    }
}

function prevPage(e) {
    e.preventDefault();

    for (let index = 0; index < allSec.length; index++) {
        const element = allSec[index];

        if (!element.classList.contains("hide-now") && index - 1 >= 0) {
            element.classList.add("hide-now");

            if (index - 1 >= 0 && index - 1 < allSec.length) {
                allSec[index - 1].classList.remove("hide-now");
            }

            checkNow(allSec);
            break;
        }
    }
}

function checkNow(all) {
    progressBar.innerHTML = ``

    all.forEach((element, index, array) => {
        if (!element.classList.contains("hide-now")) {
            if (index + 1 == array.length) {
                submitBtn.classList.remove('hide-now');
                nextBtn.classList.add('hide-now');
                prevBtn.classList.remove('hide-now');
            } else {
                submitBtn.classList.add('hide-now');
                nextBtn.classList.remove('hide-now');
                if (index === 0) {
                    if (!prevBtn.classList.contains('hide-now')) {
                        prevBtn.classList.add('hide-now');
                    }
                } else {
                    prevBtn.classList.remove('hide-now');
                }
            }

            progressBar.innerHTML += `<span class="progess-bar progress-at"></span>`
        } else {
            progressBar.innerHTML += `<span class="progess-bar progress-cannot"></span>`
        }
    })
    
    progressBtn = document.querySelectorAll('.progess-bar');
    if (progressBtn.length > 0) {
        const lastButton = progressBtn[progressBtn.length - 1];
        lastButton.title = "Submit section"; // Set the title attribute
    } else {
        console.error("No progress buttons found!");
    }

    
    console.log("adding event")
    
    // handling progress
    progressBtn.forEach((btn, idx) => {
        btn.addEventListener('click', () => {
            

            all.forEach((element) => {
                if (!element.classList.contains('hide-now')) {
                    element.classList.add('hide-now');
                }
                if (idx + 1 === all.length) {
                    if (submitBtn.classList.contains('hide-now')) {
                        submitBtn.classList.remove('hide-now');
                    }
                    if (!nextBtn.classList.contains('hide-now')) {
                        nextBtn.classList.add('hide-now');
                    } 
                    if (prevBtn.classList.contains('hide-now')) {
                        prevBtn.classList.remove('hide-now');
                    }
                } else {
                    if (!submitBtn.classList.contains('hide-now')) {
                        submitBtn.classList.add('hide-now');
                    }
                    if (nextBtn.classList.contains('hide-now')) {
                        nextBtn.classList.remove('hide-now');
                    } 
                    if (!prevBtn.classList.contains('hide-now') && idx === 0) {
                        prevBtn.classList.add('hide-now');
                    }
                }
            });
            progressBtn.forEach((b) => {
                b.classList.remove("progress-at")
                b.classList.add("progress-cannot")
            })
            btn.classList.remove('progress-cannot')
            btn.classList.add('progress-at')
            all[idx].classList.remove('hide-now');
        });
    });
}


const toastNow = function (err) {
    toastContent.innerHTML = `${err}`
    toastBox.classList.add("move-toast");

    closeIcon.addEventListener('click', (e) => {
        e.preventDefault()
        toastBox.classList.remove("move-toast");
    });

    setTimeout(() => {
        closeIcon.removeEventListener('click', () => {})
        toastBox.classList.remove("move-toast");
    }, 8000)
}


const submitNow = async (e) => {
    e.preventDefault()

    try {
        const response = await fetch('http://127.0.0.1:5000/user/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(
                getObjectFromInput()
            )
        })

        const body = await response.json()
        if (!response.ok) {
            toastNow(body.error);
            console.log("Gotten response\nError encountered", body.error);
        } else {
            // console.log(body)
            localStorage.setItem('token', body?.token)
            window.location.replace('./dashboard.html')
            // TODO: SET THE TOKEN IN THE BROWSER AND THEN REDIRECT
        }
    } catch (error) {
        toastNow(error);
        console.log("error", error);
    }
}

function getObjectFromInput() {
    try {
        const allInput = document.getElementsByTagName('input');
        const allSelect = document.getElementsByTagName('select');
        obj = {};
    
        console.log(allSelect)
        for (let element of [...allInput, ...allSelect]) {
            const elementName = element.name
            if (elementName) {
                obj[elementName] = element.value
            }
        }

        return obj;
    } catch (error) {
        
    }
}

nextBtn.addEventListener('click', nextPage);
prevBtn.addEventListener('click', prevPage);
submitBtn.addEventListener('click', submitNow)
// TODO:// ONCLICK OF SUBMIT IMPLEMENT FETCH REQUEST WITH PATCH/PUT DATA

checkNow(allSec);