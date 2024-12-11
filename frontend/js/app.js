const eyeIcon = document.querySelectorAll('.open-eye');
const pswd = document.getElementById('password');

function switchEye() {
    pswd.type = (pswd.type === 'password') ? 'text' : 'password'
    eyeIcon.forEach((e) => {
        if (e.classList.contains('hide-now')) {
            e.classList.remove('hide-now');
        } else {
            e.classList.add('hide-now');
        }
    })
}

eyeIcon.forEach((e) => {
    e.addEventListener('click', switchEye)
})