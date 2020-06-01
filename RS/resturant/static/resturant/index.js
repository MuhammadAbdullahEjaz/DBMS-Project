const regist = document.querySelector('#div-form');
const model = document.querySelector('#div-form-signin');
const overlay = document.querySelector('#overlay');


document.addEventListener('DOMContentLoaded', () => {
    load_menu('breakfast');

    document.querySelectorAll('.select-btn').forEach(link => {
        link.onclick = () => {
            load_menu(link.dataset.category);
            return false;
        };
    });

    document.querySelector('#signin').onclick = () => {
        model.classList.add('active');
        overlay.classList.add('active');

        const request = new XMLHttpRequest();
        request.open('GET', 'user');
        request.onload = () => {
            const response = JSON.parse(request.responseText);
            if (!response.auth) {
                model.classList.add('active');
                overlay.classList.add('active');
            };
        };
        request.send();
        return false;
    };

    document.querySelector('#register').onclick = ()=>{
        model.classList.remove('active');
        regist.classList.add('active');
        return false;
    };

    document.querySelector('#login').onclick = ()=>{
        regist.classList.remove('active');
        model.classList.add('active');
        return false;
    };

    document.querySelector('#close1').onclick = ()=>{
        regist.classList.remove('active');
        model.classList.remove('active');
        overlay.classList.remove('active');
        return false;
    };

    document.querySelector('#close2').onclick = ()=>{
        regist.classList.remove('active');
        model.classList.remove('active');
        overlay.classList.remove('active');
        return false;
    };

    document.querySelector('#submitreg').onclick = ()=>{
        return false;
    };
    document.querySelector('#submitlog').onclick = ()=>{
        return false;
    };
});

function load_menu(name) {
    const request = new XMLHttpRequest();
    request.open('GET', `/${name}`);
    request.onload = () => {
        document.querySelector('#menu-item').innerHTML = ""
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
    model.classList.remove('active');
    regist.classList.add('active');
};