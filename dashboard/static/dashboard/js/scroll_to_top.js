function scrollToTop() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
}

// Call scrollToTop function when the page is loaded
window.onload = function() {
    scrollToTop();
};