// Listen for the scroll event
window.addEventListener('scroll', function() {
    var nav = document.querySelector('header nav');

    // Define the scroll position where you want to keep the navigation at the top
    var scrollThreshold = 100; // Adjust the value as needed

    if (window.scrollY > scrollThreshold) {
        nav.classList.add('fixed-nav'); // Add a class to keep the navigation at the top
    } else {
        nav.classList.remove('fixed-nav'); // Remove the class when scrolling back up
    }
});
