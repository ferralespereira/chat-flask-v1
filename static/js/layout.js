var view = (window.location.pathname).split('/');
var home_navBar_link = document.getElementById('home-navBar-link');
var information_navBar_link = document.getElementById('information-navBar-link');
var contact_navBar_link = document.getElementById('contact-navBar-link');
var cars_navBar_link = document.getElementById('cars-navBar-link');
var create_car_navBar_link = document.getElementById('create_car-navBar-link');
switch (view[1]) {
    case "":
        home_navBar_link.classList.add('active');
        break;
    case "information":
        information_navBar_link.classList.add('active');
        break;
    case "contact":
        contact_navBar_link.classList.add('active');
        break;
    case "cars":
        cars_navBar_link.classList.add('active');
        break;
    case "create-car":
        create_car_navBar_link.classList.add('active');
        break;
}
