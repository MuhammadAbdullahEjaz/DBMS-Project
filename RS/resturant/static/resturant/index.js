document.addEventListener('DOMContentLoaded', () => {
    load_menu('breakfast');

    document.querySelectorAll('.select-btn').forEach(link =>{
        link.onclick = ()=>{
            load_menu(link.dataset.category);
            return false;
        };  
    });
});

function load_menu(name) {
    const request = new XMLHttpRequest();
    request.open('GET', `/${name}`);
    request.onload = () =>{
        document.querySelector('#menu-item').innerHTML = ""
        const response = JSON.parse(request.responseText);
        Array.from(response).forEach((item) =>{
            add_item(item);
        });
    };
    request.send()
}

function add_item(item){


    const item_div = document.createElement('div');
    const img_div = document.createElement('div');
    const image = document.createElement('img')
    const name_p = document.createElement('p'); 
    const price_p = document.createElement('p'); 
    const serving_p = document.createElement('p'); 

    item_div.className = "menu-item-container";
    img_div.className = "item-image"
    name_p.className = "name"
    price_p.className = "price"
    serving_p.className = "serving"

   
    const name = item.fields.name;
    const price = item.fields.Price;
    const serving = item.fields.serving
    const img_name = name.replace(/ /g,"_");
    const img_url = imag.concat("/".concat(img_name));
    const img_url_c = img_url.concat(".jfif")

    console.log(img_url_c)

    image.setAttribute("src",img_url_c)

    console.log(image)
    name_p.innerHTML = name;
    price_p.innerHTML = price;
    serving_p.innerHTML = serving;

    img_div.appendChild(image)
    item_div.appendChild(img_div)
    item_div.appendChild(name_p)
    item_div.appendChild(price_p)
    item_div.appendChild(serving_p)

    document.querySelector('#menu-item').appendChild(item_div);
}