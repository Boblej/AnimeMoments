// ожидание пока весь HTML документ прогрузиться
document.addEventListener("DOMContentLoaded", function() {
    // функция для получения имени куки
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // проверка соответствии имени куки
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
                return cookieValue;
        }
            // получаем значение из dom
            const usernameSpan = document.getElementById('username');
            const signinLink = document.getElementById('signin');
            // получаем куки
            const authCookie = getCookie('login_success');
            // если куки найден отображаем имя пользователя
            if (authCookie) {
                usernameSpan.style.display = 'inline';
                // если куки не найден отображается ссылка
            } else {
                signinLink.style.display = 'inline';
            }
});