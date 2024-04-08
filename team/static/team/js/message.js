
document.addEventListener("DOMContentLoaded", () => {
    let message = document.getElementById('toast-message');
    if (!message) return;

    setTimeout(() => {
        message.classList.replace('opacity-100', 'opacity-0');
        setTimeout(() => {
            message.style.display = 'none';
        }, 500);
    }, 1000);
});