const register_div = document.querySelector('#div-form-register');
const signin_div = document.querySelector('#div-form-signin');
const overlay_div = document.querySelector('#overlay');


document.addEventListener('DOMContentLoaded', () => {
    load_menu('breakfast');
    get_user();
    document.querySelectorAll('.select-btn').forEach(link => {
        link.onclick = () => {
            load_menu(link.dataset.category);
            return false;
        };
    });

    document.querySelector('#signin').onclick = () => {

        const request = new XMLHttpRequest();
        request.open('GET', 'user/');
        request.onload = () => {
            const response = JSON.parse(request.responseText);
            if (!response.auth) {
                popup_signin_div();
            };
            if (response.auth) {
                logout();
                document.querySelector('#signin').innerHTML = "Sign In";
                location.reload();
        
            }
        };
        request.send();
        return false;
    };

    document.querySelector('#register').onclick = () => {
        signin_div.classList.remove('active');
        register_div.classList.add('active');
        return false;
    };

    document.querySelector('#login').onclick = () => {
        register_div.classList.remove('active');
        signin_div.classList.add('active');
        return false;
    };

    document.querySelector('#close1').onclick = () => {
        popdown_signin_register_div();
        return false;
    };

    document.querySelector('#close2').onclick = () => {
        popdown_signin_register_div();
        return false;
    };

    document.querySelector('#submitreg').onclick = () => {
        const username = document.querySelector('#usernamereg').value;
        const firstname = document.querySelector('#firstnamereg').value;
        const lastname = document.querySelector('#lastnamereg').value;
        const email = document.querySelector('#emailreg').value;
        const password = document.querySelector('#passwordreg').value;

        const csrf = document.querySelector("[name = csrfmiddlewaretoken]").value;

        const username_check = (username === "");
        const firstname_check = (firstname === "");
        const lastname_check = (lastname === "");
        const email_check = (email === "");
        const password_check = (password === "");

        if (username_check) {
            document.querySelector('#usernameregerror').innerHTML = "Username Required";
        } else if (firstname_check) {
            document.querySelector('#firstnameregerror').innerHTML = "First Name Required";
        } else if (lastname_check) {
            document.querySelector('#lastnameregerror').innerHTML = "Last Name Required";
        } else if (email_check) {
            document.querySelector('#emailregerror').innerHTML = "Email Required";
        } else if (password_check) {
            document.querySelector('#passwordregerror').innerHTML = "Password Required";
        }

        if (!username_check) document.querySelector('#usernameregerror').innerHTML = "";
        if (!firstname_check) document.querySelector('#firstnameregerror').innerHTML = "";
        if (!lastname_check) document.querySelector('#lastnameregerror').innerHTML = "";
        if (!email_check) document.querySelector('#emailregerror').innerHTML = "";
        if (!password_check) document.querySelector('#passwordregerror').innerHTML = "";

        if (username_check || firstname_check || lastname_check || email_check || password_check) {
            return false;
        }

        const request = new XMLHttpRequest();
        request.open('POST', 'signup/');

        request.onload = () => {
            const response = request.responseText;
            response_json = JSON.parse(response);
            if (!response_json.status) {
                document.querySelector(response_json.target).innerHTML = response_json.error;
            };
            if (response_json.status) {
                document.querySelector('#usernamereg').value = "";
                document.querySelector('#firstnamereg').value = "";
                document.querySelector('#lastnamereg').value = "";
                document.querySelector('#emailreg').value = "";
                document.querySelector('#passwordreg').value = "";

                popup_sucess_div("Registered Sucessfully !");
                popdown_signin_register_div();
                setTimeout(popdown_sucess_div, 2000);
            };
            return false;
        };

        document.querySelector("#usernameregerror").innerHTML = "";
        document.querySelector("#emailregerror").innerHTML = "";
        document.querySelector("#passwordregerror").innerHTML = "";

        const data = new FormData();
        data.append('username', username);
        data.append('firstname', firstname);
        data.append('lastname', lastname);
        data.append('email', email);
        data.append('password', password);

        request.setRequestHeader("X-CSRFToken", csrf);
        request.send(data);

        return false;
    };
    document.querySelector('#submitlog').onclick = () => {
        const username = document.querySelector("#usernamelog").value;
        const password = document.querySelector("#passwordlog").value;
        const csrf = document.querySelector("[name = csrfmiddlewaretoken]").value;

        const username_check = (username === "");
        const password_check = (password === "");

        if (username_check) {
            document.querySelector("#usernamelogerror").innerHTML = "Please enter username ";
        } else if (password_check) {
            document.querySelector("#passwordlogerror").innerHTML = "Please enter password";
        }

        if (!username_check) document.querySelector("#usernamelogerror").innerHTML = "";
        if (!password_check) document.querySelector("#passwordlogerror").innerHTML = "";


        if (username_check || password_check) {
            return false;
        }

        const request = new XMLHttpRequest();
        request.open('POST', 'signin/');

        request.onload = () => {
            const response = request.responseText;

            console.log(csrf);

            response_json = JSON.parse(response);
            if (!response_json.status) {
                document.querySelector(response_json.target).innerHTML = response_json.error;
            };
            if (response_json.status) {
                document.querySelector("#signin").innerHTML = response_json.user;
                document.querySelector("#usernamelog").value = "";
                document.querySelector("#passwordlog").value = "";
                popdown_signin_register_div();
                popup_sucess_div(`${username} Logged In Sucessfully`);
                setTimeout(popdown_sucess_div, 2000);
            }
            return false;
        };

        document.querySelector("#logerror").innerHTML = "";
        document.querySelector("#usernamelogerror").innerHTML = "";
        document.querySelector("#passwordlogerror").innerHTML = "";

        const data = new FormData();
        data.append('username', username);
        data.append('password', password);

        request.setRequestHeader("X-CSRFToken", csrf);
        request.send(data);

        return false;
    };
});

function load_menu(name) {
    const request = new XMLHttpRequest();
    request.open('GET', `/${name}`);
    request.onload = () => {
        document.querySelector('#menu-item').innerHTML = ""
        console.log(request.responseText);
        const response = JSON.parse(request.responseText);
        Array.from(response).forEach((item) => {
            add_item(item);
        });
    };
    request.send()
}

function add_item(item) {


    const item_div = document.createElement('div');
    const img_div = document.createElement('div');
    const image = document.createElement('img')
    const name_div = document.createElement('div');
    const price_div = document.createElement('div');
    const serving_div = document.createElement('div');
    const name_p = document.createElement('p');
    const price_p = document.createElement('p');
    const serving_p = document.createElement('p');

    item_div.className = "menu-item-container";
    img_div.className = "item-image"
    name_div.className = "name"
    price_div.className = "price"
    serving_div.className = "serving"


    const name = item.fields.name;
    const price = item.fields.Price;
    const serving = item.fields.serving
    const img_name = name.replace(/ /g, "_");
    const img_url = imag.concat("/".concat(img_name));
    const img_url_c = img_url.concat(".jfif")

    console.log(img_url_c)

    image.setAttribute("src", img_url_c)

    console.log(image)
    name_p.innerHTML = name;
    price_p.innerHTML = `Price: ${price}`;
    serving_p.innerHTML = `Serving:  ${serving}`;

    img_div.appendChild(image);
    item_div.appendChild(img_div);

    name_div.appendChild(name_p);
    price_div.appendChild(price_p);
    serving_div.appendChild(serving_p)

    item_div.appendChild(name_div);
    item_div.appendChild(price_div);
    item_div.appendChild(serving_div);

    document.querySelector('#menu-item').appendChild(item_div);
}

function load_register() {
    signin_div.classList.remove('active');
    register_div.classList.add('active');
};

function get_user() {
    const request = new XMLHttpRequest()
    request.open('GET', 'user/');
    const csrf = document.querySelector("[name = csrfmiddlewaretoken]").value;

    request.onload = () => {
        const response = request.responseText;
        response_json = JSON.parse(response);
        if (response_json.auth) {
            document.querySelector('#signin').innerHTML = response_json.user;
        };
    };
    request.send();
};

function logout() {
    const request = new XMLHttpRequest();
    request.open('GET', 'logout_v/');
    request.onload = () => {
        const response = request.responseText;
        response_json = JSON.parse(response);
        if (response_json.status) {
            popup_error_div(`${response_json.user} Logged Out`);
            setTimeout(popdown_error_div, 2000);
        }
    };
    request.send();
};

function popup_signin_div() {
    signin_div.classList.add('active');
    overlay_div.classList.add('active');
};

function popdown_signin_div() {
    signin_div.classList.remove('active');
    overlay_div.classList.remove('active');
};
function popup_register_div() {
    register_div.classList.add('active');
    overlay_div.classList.add('active');
};

function popdown_register_div() {
    register_div.classList.remove('active');
    overlay_div.classList.remove('active');
};

function popdown_signin_register_div() {
    signin_div.classList.remove('active');
    register_div.classList.remove('active');
    overlay_div.classList.remove('active');

    document.querySelector('#usernameregerror').innerHTML = "";
    document.querySelector('#firstnameregerror').innerHTML = "";
    document.querySelector('#lastnameregerror').innerHTML = "";
    document.querySelector('#emailregerror').innerHTML = "";
    document.querySelector('#passwordregerror').innerHTML = "";

    document.querySelector("#usernamelogerror").innerHTML = "";
    document.querySelector("#passwordlogerror").innerHTML = "";

};

function popup_sucess_div(content) {
    const div = document.querySelector('#div-sucess');
    div.innerHTML = content;
    div.classList.add('active');
}

function popdown_sucess_div() {
    const div = document.querySelector('#div-sucess');
    div.classList.remove('active');
    div.innerHTML = "";
}

function popup_error_div(content) {
    const div = document.querySelector('#div-error');
    div.innerHTML = content;
    div.classList.add('active');
};

function popdown_error_div() {
    const div = document.querySelector('#div-error');
    div.classList.remove('active');
    div.innerHTML = "";
};

function get_csrf(){
    const csrf = document.querySelector("[name=csrfmiddlewaretoken]");
    return csrf;
}