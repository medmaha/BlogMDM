
$(document).ready(function(){
    var screenWidth = $(screen.width)
    console.log(screenWidth);
    if (screenWidth[0] < 768){
        var newPost = document.querySelectorAll('.navbar .container .collapse .lg-scr')
        console.log(newPost);
        newPost.forEach(element => {
            element.style.display = 'none'
        });
    }

    let underNav = document.createElement('div')
    underNav.classList.add('d-flex row')
    
})

