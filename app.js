// Función para entrar a la app
function enterApp() {
    console.log('Entrando a la app...');
    const splashScreen = document.getElementById('splash-screen');
    const mainHeader = document.getElementById('main-header');
    const loginScreen = document.getElementById('screen-login');
    
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

// Función para mostrar pantallas
function showScreen(screenId, navItem) {
    console.log('Mostrando pantalla:', screenId);
    
    // Ocultar todas las pantallas
    document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.remove('active');
    });
    
    // Mostrar la pantalla seleccionada
    const targetScreen = document.getElementById(screenId);
    if (targetScreen) {
        targetScreen.classList.add('active');
    }
    
    // Actualizar navegación
    if (navItem) {
        document.querySelectorAll('.nav-item').forEach(item => {
            item.classList.remove('active');
        });
        navItem.classList.add('active');
    }
}

// Función para mostrar grupo muscular
function showMuscleGroup(muscle) {
    console.log('Mostrando grupo muscular:', muscle);
    // Aquí iría la lógica para mostrar ejercicios del grupo muscular
}

console.log('app.js cargado correctamente');