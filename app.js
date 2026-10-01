// Funciones básicas de la app Gembukai

function enterApp() {
    console.log('Entrando a la app...');
    var splashScreen = document.getElementById('splash-screen');
    var mainHeader = document.getElementById('main-header');
    var loginScreen = document.getElementById('screen-login');
    
    if (splashScreen) {
        splashScreen.classList.add('hidden');
    }
    
    if (mainHeader) {
        mainHeader.style.display = 'block';
    }
    
    if (loginScreen) {
        loginScreen.classList.add('active');
    }
    
    console.log('App cargada correctamente');
}

function showScreen(screenId, navItem) {
    console.log('Mostrando pantalla:', screenId);
    
    var screens = document.querySelectorAll('.screen');
    for (var i = 0; i < screens.length; i++) {
        screens[i].classList.remove('active');
    }
    
    var targetScreen = document.getElementById(screenId);
    if (targetScreen) {
        targetScreen.classList.add('active');
    }
    
    if (navItem) {
        var navItems = document.querySelectorAll('.nav-item');
        for (var i = 0; i < navItems.length; i++) {
            navItems[i].classList.remove('active');
        }
        navItem.classList.add('active');
    }
}

function showMuscleGroup(muscle) {
    console.log('Mostrando grupo muscular:', muscle);
}

console.log('app.js cargado correctamente');