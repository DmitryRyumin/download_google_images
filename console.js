// Имитация щелчка правой кнопкой мыши на изображении, которое отображается в браузере
function simulateRightClick(element) {
    var event1 = new MouseEvent('mousedown', {
        bubbles: true, cancelable: false, view: window, button: 2, buttons: 2,
        clientX: element.getBoundingClientRect().x,
        clientY: element.getBoundingClientRect().y
    });
    element.dispatchEvent(event1);
    var event2 = new MouseEvent('mouseup', {
        bubbles: true, cancelable: false, view: window, button: 2, buttons: 0,
        clientX: element.getBoundingClientRect().x,
        clientY: element.getBoundingClientRect().y
    });
    element.dispatchEvent(event2);
    var event3 = new MouseEvent('contextmenu', {
        bubbles: true, cancelable: false,
        view: window, button: 2, buttons: 0,
        clientX: element.getBoundingClientRect().x,
        clientY: element.getBoundingClientRect().y
    });
    element.dispatchEvent(event3);
}

// Извлечение URL
function getURLParam(queryString, key) {
    var vars = queryString.replace(/^\?/, '').split('&');
    for (let i = 0; i < vars.length; i++) {
        let pair = vars[i].split('=');
        if (pair[0] == key) { return pair[1]; }
    }
    return false;
}

// Сбор всех URL в текстовый файл
function createDownload(contents) {
    var hiddenElement = document.createElement('a');
    hiddenElement.href = 'data:attachment/text,' + encodeURI(contents);
    hiddenElement.target = '_blank'; hiddenElement.download = 'urls.txt'; hiddenElement.click();
}

// Захват всех URL
function grabUrls() {
    var urls = [];
    return new Promise(function (resolve, reject) {
        var count = document.querySelectorAll('.isv-r a:first-of-type').length, index = 0;
        Array.prototype.forEach.call(document.querySelectorAll(
            '.isv-r a:first-of-type'), function (element) {
                simulateRightClick(element.querySelector(':scope img'));
                var interval = setInterval(function () {
                    if (element.href.trim() !== '') {
                        clearInterval(interval);
                        let googleUrl = element.href.replace(/.*(\?)/, '$1'),
                            fullImageUrl = decodeURIComponent(getURLParam(googleUrl, 'imgurl'));
                        if (fullImageUrl !== 'false') { urls.push(fullImageUrl); }
                        index++;
                        if (index == (count - 1)) { resolve(urls); }
                    }
                }, 10);
            });
    });
}

// Старт загрузки
grabUrls().then(function (urls) { urls = urls.join('\n'); createDownload(urls); });