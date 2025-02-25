var close = document.getElementById('close').addEventListener('click',function(){
    var navbar =document.getElementById('navbar')
    var logo =document.getElementById('logo')
    var open =document.getElementById('open')
    var close =document.getElementById('close')
    var sidebar =document.getElementById('sidebar')
    var mainbar = document.getElementById('mainbar')
    document.querySelectorAll("ion-icon.icon").forEach(icon => {
        icon.style.display = "none"; // Hide only icons with class "hideable"
    });

    document.querySelectorAll(".dropdown").forEach(dropdown => {
        
        dropdown.style.marginLeft = "0px";
        dropdown.style.paddingLeft = "28px";
    });

    logo.style.width = "5%";
    navbar.style.width ="95%";
    open.style.display = "block";
    close.style.display = "none";
    sidebar.style.width = "5%";
    mainbar.style.width = "95%";
    mainbar.style.marginLeft = "5%";
    
})
var open = document.getElementById('open').addEventListener('click',function(){
    var navbar =document.getElementById('navbar')
    var logo =document.getElementById('logo')
    var open =document.getElementById('open')
    var close =document.getElementById('close')
    var sidebar =document.getElementById('sidebar')
    var mainbar = document.getElementById('mainbar')
    document.querySelectorAll("ion-icon.icon").forEach(icon => {
        icon.style.display = "inline-block"; // Show them again
    });
    document.querySelectorAll(".dropdown").forEach(dropdown => {
        
        dropdown.style.marginLeft = "80px";
        dropdown.style.paddingLeft = "0px";
    });

    logo.style.width = "24%";
    navbar.style.width ="76%";
    open.style.display = "none";
    close.style.display = "block";
    sidebar.style.width = "24%";
    mainbar.style.width = "76%";
    mainbar.style.marginLeft = "24%";
})


var openinput = document.getElementById('openinput').addEventListener('click',function(){
    var inputbox = document.getElementById('inputbox')
    var submitbtn = document.getElementById('submitbtn')
    var openinput = document.getElementById('openinput')
    openinput.style.display = "none"
    submitbtn.style.display = 'block'
    inputbox.style.width = "500px";
    inputbox.style.padding = "10px 20px";
    inputbox.style.border = "2pxsolid azure";
})
// var submitbtn = document.getElementById('submitbtn').addEventListener('click',function(){
//     var openinput = document.getElementById('openinput')
//     var submitbtn = document.getElementById('submitbtn')
//     var inputbox = document.getElementById('inputbox')


//     openinput.style.display = 'block'
//     submitbtn.style.display = 'none'
//     inputbox.style.width = "0";
//     inputbox.style.padding = "0";
//     inputbox.style.border = "none";
// })


var morebtn = document.getElementById('more').addEventListener('click',function(){
    var moreservices = document.getElementById('moreservices');
    moreservices.style.transform = "scale(1)";
})
var lessbtn = document.getElementById('less').addEventListener('click',function(){
    var moreservices = document.getElementById('moreservices');
    moreservices.style.transform = "scale(0)";
})