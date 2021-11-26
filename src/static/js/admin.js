function ready(fn) {
    if (document.readyState != 'loading'){
      fn();
    } else {
      document.addEventListener('DOMContentLoaded', fn);
    }
}

function getCookie(name) {

    var matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ))
    return matches ? decodeURIComponent(matches[1]) : undefined
};

ready(function(){

    var update_fruit_socket = new WebSocket(`ws://${window.location.host}/ws/admin/fruits/`);
    update_fruit_socket.onmessage = function(event){
        var data = JSON.parse(event.data);

        if('apples' in data){
            total_apples = document.querySelector('#id_total_apples');
            total_apples.value = `Яблок на складе: ${data.apples} штук`;
        }
        else if('bananas' in data){
            total_bananas = document.querySelector('#id_total_bananas');
            total_bananas.value = `Бананов на складе: ${data.bananas} штук`;
        }
        else if('pineapples' in data){
            total_pineapples = document.querySelector('#id_total_pineapples');
            total_pineapples.value = `Ананасов на складе: ${data.pineapples} штук`;
        }
        else if('peaches' in data){
            total_peaches = document.querySelector('#id_total_peaches');
            total_peaches.value = `Персиков на складе: ${data.peaches} штук`;
        }
        

        total_money = document.querySelector('#id_total_money');
        total_money.value = `Денег на счету: ${data.money}$`;

        history_area = document.querySelector('#id_history_area');
        document.querySelector('#id_history_area').value += data.operation;
    }

    var update_last_operations_socket = new WebSocket(`ws://${window.location.host}/ws/admin/update-last-operations/`);
    update_last_operations_socket.onmessage = function(event){
        var last_operations_data = event.data;
        console.log(last_operations_data);
        chat_area = document.querySelector('#id_last_updates');
        document.querySelector('#id_last_updates').value = last_operations_data;
    }

    
    document.getElementById('idBuyApplesModalForm').addEventListener('submit', function(e){
        e.preventDefault();
        var request = new XMLHttpRequest();
        request.open('POST', document.getElementById('idBuyApplesModalForm').getAttribute('action'), true);
        request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        data = {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            'count': document.getElementById('id_apples_count').value,
            'seconds': document.getElementById('id_apples_seconds').value,
        };
        document.getElementById('id_apples_count').value = '';
        document.getElementById('id_apples_seconds').value = '';
        request.onload = function() {
            if (this.status >= 200 && this.status < 400) {
                response = JSON.parse(this.response);
                var errorBlock = document.getElementById('id_buy_apples_errors');
                if (Object.keys(response).length == 0){
                    errorBlock.innerHTML = '<div class="alert alert-success" role="alert">Таска на покупку яблок успешно создана.</div>';
                }
                else{
                    var errorHTML = '';
                    for ([key, value] of Object.entries(response)){
                        errorHTML += '<div class="alert alert-danger" role="alert">';
                        errorHTML += `${value}`;
                        errorHTML += '</div>';
                    }
                    errorHTML += '<div class="alert alert-danger" role="alert">Таска не создана!</div>';
                    errorBlock.innerHTML = errorHTML;
                }
            }
        };

        request.onerror = function() {
            alert('Что-то пошло не так! Таска не создана!');
        };

        request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        data = JSON.stringify(data);
        request.send(data);
    });


    document.getElementById('idBuyBananasModalForm').addEventListener('submit', function(e){
        e.preventDefault();
        var request = new XMLHttpRequest();
        request.open('POST', document.getElementById('idBuyBananasModalForm').getAttribute('action'), true);
        request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        data = {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            'count': document.getElementById('id_bananas_count').value,
            'seconds': document.getElementById('id_bananas_seconds').value,
        };
        document.getElementById('id_bananas_count').value = '';
        document.getElementById('id_bananas_seconds').value = '';
        request.onload = function() {
            if (this.status >= 200 && this.status < 400) {
                response = JSON.parse(this.response);
                var errorBlock = document.getElementById('id_buy_bananas_errors');
                if (Object.keys(response).length == 0){
                    errorBlock.innerHTML = '<div class="alert alert-success" role="alert">Таска на покупку бананов успешно создана.</div>';
                }
                else{
                    var errorHTML = '';
                    for ([key, value] of Object.entries(response)){
                        errorHTML += '<div class="alert alert-danger" role="alert">';
                        errorHTML += `${value}`;
                        errorHTML += '</div>';
                    }
                    errorHTML += '<div class="alert alert-danger" role="alert">Таска не создана!</div>';
                    errorBlock.innerHTML = errorHTML;
                }
            }
        };

        request.onerror = function() {
            alert('Что-то пошло не так! Таска не создана!');
        };

        request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        data = JSON.stringify(data);
        request.send(data);
    });


    document.getElementById('idBuyPineapplesModalForm').addEventListener('submit', function(e){
        e.preventDefault();
        var request = new XMLHttpRequest();
        request.open('POST', document.getElementById('idBuyPineapplesModalForm').getAttribute('action'), true);
        request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        data = {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            'count': document.getElementById('id_pineapples_count').value,
            'seconds': document.getElementById('id_pineapples_seconds').value,
        };
        document.getElementById('id_pineapples_count').value = '';
        document.getElementById('id_pineapples_seconds').value = '';
        request.onload = function() {
            if (this.status >= 200 && this.status < 400) {
                response = JSON.parse(this.response);
                var errorBlock = document.getElementById('id_buy_pineapples_errors');
                if (Object.keys(response).length == 0){
                    errorBlock.innerHTML = '<div class="alert alert-success" role="alert">Таска на покупку ананасов успешно создана.</div>';
                }
                else{
                    var errorHTML = '';
                    for ([key, value] of Object.entries(response)){
                        errorHTML += '<div class="alert alert-danger" role="alert">';
                        errorHTML += `${value}`;
                        errorHTML += '</div>';
                    }
                    errorHTML += '<div class="alert alert-danger" role="alert">Таска не создана!</div>';
                    errorBlock.innerHTML = errorHTML;
                }
            }
        };

        request.onerror = function() {
            alert('Что-то пошло не так! Таска не создана!');
        };

        request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        data = JSON.stringify(data);
        request.send(data);
    });


    document.getElementById('idBuyPeachesModalForm').addEventListener('submit', function(e){
        e.preventDefault();
        var request = new XMLHttpRequest();
        request.open('POST', document.getElementById('idBuyPeachesModalForm').getAttribute('action'), true);
        request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        data = {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            'count': document.getElementById('id_peaches_count').value,
            'seconds': document.getElementById('id_peaches_seconds').value,
        };
        document.getElementById('id_peaches_count').value = '';
        document.getElementById('id_peaches_seconds').value = '';
        request.onload = function() {
            if (this.status >= 200 && this.status < 400) {
                response = JSON.parse(this.response);
                var errorBlock = document.getElementById('id_buy_peaches_errors');
                if (Object.keys(response).length == 0){
                    errorBlock.innerHTML = '<div class="alert alert-success" role="alert">Таска на покупку персиков успешно создана.</div>';
                }
                else{
                    var errorHTML = '';
                    for ([key, value] of Object.entries(response)){
                        errorHTML += '<div class="alert alert-danger" role="alert">';
                        errorHTML += `${value}`;
                        errorHTML += '</div>';
                    }
                    errorHTML += '<div class="alert alert-danger" role="alert">Таска не создана!</div>';
                    errorBlock.innerHTML = errorHTML;
                }
            }
        };

        request.onerror = function() {
            alert('Что-то пошло не так! Таска не создана!');
        };

        request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        data = JSON.stringify(data);
        request.send(data);
    });


    document.getElementById('idSellApplesModalForm').addEventListener('submit', function(e){
        e.preventDefault();
        var request = new XMLHttpRequest();
        request.open('POST', document.getElementById('idSellApplesModalForm').getAttribute('action'), true);
        request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        data = {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            'count': document.getElementById('id_sell_apples_count').value,
            'seconds': document.getElementById('id_sell_apples_seconds').value,
        };
        document.getElementById('id_sell_apples_count').value = '';
        document.getElementById('id_sell_apples_seconds').value = '';
        request.onload = function() {
            if (this.status >= 200 && this.status < 400) {
                response = JSON.parse(this.response);
                var errorBlock = document.getElementById('id_sell_apples_errors');
                if (Object.keys(response).length == 0){
                    errorBlock.innerHTML = '<div class="alert alert-success" role="alert">Таска на продажи яблок успешно создана.</div>';
                }
                else{
                    var errorHTML = '';
                    for ([key, value] of Object.entries(response)){
                        errorHTML += '<div class="alert alert-danger" role="alert">';
                        errorHTML += `${value}`;
                        errorHTML += '</div>';
                    }
                    errorHTML += '<div class="alert alert-danger" role="alert">Таска не создана!</div>';
                    errorBlock.innerHTML = errorHTML;
                }
            }
        };

        request.onerror = function() {
            alert('Что-то пошло не так! Таска не создана!');
        };

        request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        data = JSON.stringify(data);
        request.send(data);
    });


    document.getElementById('idSellBananasModalForm').addEventListener('submit', function(e){
        e.preventDefault();
        var request = new XMLHttpRequest();
        request.open('POST', document.getElementById('idSellBananasModalForm').getAttribute('action'), true);
        request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        data = {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            'count': document.getElementById('id_sell_bananas_count').value,
            'seconds': document.getElementById('id_sell_bananas_seconds').value,
        };
        document.getElementById('id_sell_bananas_count').value = '';
        document.getElementById('id_sell_bananas_seconds').value = '';
        request.onload = function() {
            if (this.status >= 200 && this.status < 400) {
                response = JSON.parse(this.response);
                var errorBlock = document.getElementById('id_sell_bananas_errors');
                if (Object.keys(response).length == 0){
                    errorBlock.innerHTML = '<div class="alert alert-success" role="alert">Таска на продажу бананов успешно создана.</div>';
                }
                else{
                    var errorHTML = '';
                    for ([key, value] of Object.entries(response)){
                        errorHTML += '<div class="alert alert-danger" role="alert">';
                        errorHTML += `${value}`;
                        errorHTML += '</div>';
                    }
                    errorHTML += '<div class="alert alert-danger" role="alert">Таска не создана!</div>';
                    errorBlock.innerHTML = errorHTML;
                }
            }
        };

        request.onerror = function() {
            alert('Что-то пошло не так! Таска не создана!');
        };

        request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        data = JSON.stringify(data);
        request.send(data);
    });


    document.getElementById('idSellPineapplesModalForm').addEventListener('submit', function(e){
        e.preventDefault();
        var request = new XMLHttpRequest();
        request.open('POST', document.getElementById('idSellPineapplesModalForm').getAttribute('action'), true);
        request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        data = {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            'count': document.getElementById('id_sell_pineapples_count').value,
            'seconds': document.getElementById('id_sell_pineapples_seconds').value,
        };
        document.getElementById('id_sell_pineapples_count').value = '';
        document.getElementById('id_sell_pineapples_seconds').value = '';
        request.onload = function() {
            if (this.status >= 200 && this.status < 400) {
                response = JSON.parse(this.response);
                var errorBlock = document.getElementById('id_sell_pineapples_errors');
                if (Object.keys(response).length == 0){
                    errorBlock.innerHTML = '<div class="alert alert-success" role="alert">Таска на продажу ананасов успешно создана.</div>';
                }
                else{
                    var errorHTML = '';
                    for ([key, value] of Object.entries(response)){
                        errorHTML += '<div class="alert alert-danger" role="alert">';
                        errorHTML += `${value}`;
                        errorHTML += '</div>';
                    }
                    errorHTML += '<div class="alert alert-danger" role="alert">Таска не создана!</div>';
                    errorBlock.innerHTML = errorHTML;
                }
            }
        };

        request.onerror = function() {
            alert('Что-то пошло не так! Таска не создана!');
        };

        request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        data = JSON.stringify(data);
        request.send(data);
    });


    document.getElementById('idSellPeachesModalForm').addEventListener('submit', function(e){
        e.preventDefault();
        var request = new XMLHttpRequest();
        request.open('POST', document.getElementById('idSellPeachesModalForm').getAttribute('action'), true);
        request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        data = {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            'count': document.getElementById('id_sell_peaches_count').value,
            'seconds': document.getElementById('id_sell_peaches_seconds').value,
        };
        document.getElementById('id_sell_peaches_count').value = '';
        document.getElementById('id_sell_peaches_seconds').value = '';
        request.onload = function() {
            if (this.status >= 200 && this.status < 400) {
                response = JSON.parse(this.response);
                var errorBlock = document.getElementById('id_sell_peaches_errors');
                if (Object.keys(response).length == 0){
                    errorBlock.innerHTML = '<div class="alert alert-success" role="alert">Таска на продажу персиков успешно создана.</div>';
                }
                else{
                    var errorHTML = '';
                    for ([key, value] of Object.entries(response)){
                        errorHTML += '<div class="alert alert-danger" role="alert">';
                        errorHTML += `${value}`;
                        errorHTML += '</div>';
                    }
                    errorHTML += '<div class="alert alert-danger" role="alert">Таска не создана!</div>';
                    errorBlock.innerHTML = errorHTML;
                }
            }
        };

        request.onerror = function() {
            alert('Что-то пошло не так! Таска не создана!');
        };

        request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        data = JSON.stringify(data);
        request.send(data);
    });

    var check_storage_socket = new WebSocket(`ws://${window.location.host}/ws/admin/check-storage/`);
    document.getElementById('id_check_storage_button').addEventListener('click', function(e){
        document.getElementById('id_check_storage_button').disabled = true;
        toastr.info('Проверка склада запущена!');
        check_storage_socket.send(JSON.stringify({}));
    })

    check_storage_socket.onmessage = function(event){
        var data = event.data;
        toastr.info(data);
        document.getElementById('id_check_storage_button').disabled = false;
    }
})