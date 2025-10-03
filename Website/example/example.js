document.addEventListener('DOMContentLoaded', () => {
    const myBox = document.getElementById('myBox');

    myBox.addEventListener('click', () => {
       
        myBox.classList.toggle('moved');
    });
});