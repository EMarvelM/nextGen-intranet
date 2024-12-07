const emailField = document.getElementById('email');
const passwordField = document.getElementById('password');

const submitBtn = document.getElementById('login-submit');

const toastBox = document.querySelector('.toast');
const toastContent = document.getElementById('toast-content');
const closeIcon = document.querySelector('.bi-background');


const toastNow = function () {
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

submitBtn.addEventListener('click', async (event) => {
    event.preventDefault()
    
    try {
        const response = await fetch('http://127.0.0.1:5000/auth/login', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                email: emailField.value,
                password: passwordField.value
            }),
        })

        const body = await response.json()
        if (!response.ok) {
            toastContent.innerHTML = `${body.error}`
            toastNow()
            console.log("Gotten response");
            console.log("Error encountered", body.error);
        } else {
            console.log(body)
        }
    } catch (error) {
        toastContent.innerHTML = `${error}`
        toastNow()
        console.log("error", error);
    }
})