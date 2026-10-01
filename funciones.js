// Funciones esenciales para Gembukai App

// Variables globales


// Entrar a la app
function enterApp() {
    console.log('Entrando a la app...');
    var splash = document.getElementById('splash-screen');
    if (splash) splash.classList.add('hidden');
    var header = document.getElementById('main-header');
    if (header) header.style.display = 'block';
    var login = document.getElementById('screen-login');
    if (login) login.classList.add('active');
}

// Mostrar pantalla
function showScreen(screenId, navItem) {
    var screens = document.querySelectorAll('.screen');
    for (var i = 0; i < screens.length; i++) screens[i].classList.remove('active');
    var target = document.getElementById(screenId);
    if (target) target.classList.add('active');
    if (navItem) {
        var navs = document.querySelectorAll('.nav-item');
        for (var i = 0; i < navs.length; i++) navs[i].classList.remove('active');
        navItem.classList.add('active');
    }
}

// Validar código
function validateCode() {
    var codeInput = document.getElementById('login-code');
    var errorDiv = document.getElementById('login-error');
    var code = codeInput.value.trim().toUpperCase();
    
    console.log('Validando código:', code);
    
    if (!code) {
        errorDiv.textContent = 'Introduce un código';
        errorDiv.style.display = 'block';
        return;
    }
    
    var user = null;
    if (usersDB.users) {
        for (var i = 0; i < usersDB.users.length; i++) {
            if (usersDB.users[i].code === code) {
                user = usersDB.users[i];
                break;
            }
        }
    }
    
    if (!user) {
        errorDiv.textContent = 'Código no válido';
        errorDiv.style.display = 'block';
        return;
    }
    
    if (!user.active) {
        errorDiv.textContent = 'Cuenta desactivada';
        errorDiv.style.display = 'block';
        return;
    }
    
    var today = new Date();
    var expires = new Date(user.expires);
    if (today > expires) {
        errorDiv.textContent = 'Cuenta caducada';
        errorDiv.style.display = 'block';
        return;
    }
    
    currentUser = user;
    localStorage.setItem('gembukai_current_user', JSON.stringify(user));
    
    console.log('Usuario válido:', user.name);
    showScreen('screen-home');
    updateWelcomeScreen();
}

// Mostrar/ocultar contraseña
function togglePasswordVisibility() {
    var input = document.getElementById('login-code');
    if (input.type === 'password') input.type = 'text';
    else input.type = 'password';
}

// Actualizar pantalla de bienvenida
function updateWelcomeScreen() {
    if (!currentUser) return;
    var title = document.getElementById('welcome-title');
    if (title) title.textContent = '¡Hola, ' + currentUser.name + '!';
    var msg = document.getElementById('welcome-msg');
    if (msg) msg.textContent = 'Vamos a entrenar';
}

// Mostrar grupo muscular
function showMuscleGroup(muscle) {
    console.log('Grupo muscular:', muscle);
    showScreen('screen-exercises');
    renderExercisesByMuscle(muscle);
}

function showMuscleGroupForDay(muscle) {
    console.log('Añadir ejercicios del grupo:', muscle);
}

// Traducciones
function translateExerciseName(name) {
    if (!name) return 'Ejercicio';
    var lower = name.toLowerCase();
    if (translationsDB.exercises && translationsDB.exercises[lower]) {
        return translationsDB.exercises[lower];
    }
    return name;
}

function translateMuscle(muscle) {
    if (translationsDB.muscles && translationsDB.muscles[muscle]) {
        return translationsDB.muscles[muscle];
    }
    return muscle;
}

function translateEquipment(equipment) {
    if (translationsDB.equipment && translationsDB.equipment[equipment]) {
        return translationsDB.equipment[equipment];
    }
    return equipment;
}

// Imagen del ejercicio
function getExerciseImage(exercise) {
    var id = String(exercise.id || '0001').padStart(4, '0');
    var mediaId = exercise.media_id || '';
    if (mediaId) return EXERCISEDB_BASE_URL + '/images/' + id + '-' + mediaId + '.jpg';
    var name = (exercise.name || 'unknown').toLowerCase().replace(/\s+/g, '-').replace(/[^\w\-]/g, '');
    return EXERCISEDB_BASE_URL + '/images/' + id + '-' + name + '.jpg';
}

// Renderizar ejercicios por músculo
function renderExercisesByMuscle(muscle) {
    var container = document.getElementById('exercises-list');
    if (!container) return;
    
    var filtered = exercisesDB.filter(function(ex) { return ex.body_part === muscle; });
    
    if (filtered.length === 0) {
        container.innerHTML = '<div class="empty-state"><p>No hay ejercicios</p></div>';
        return;
    }
    
    var html = '<div class="exercise-list">';
    for (var i = 0; i < filtered.length; i++) {
        var ex = filtered[i];
        html += '<div class="exercise-item" onclick="openExerciseDetail(' + ex.id + ')">';
        html += '<div class="exercise-image"><img src="' + getExerciseImage(ex) + '" alt="' + ex.name + '" onerror="this.style.display=\'none\'"></div>';
        html += '<div class="exercise-info"><h3>' + translateExerciseName(ex.name) + '</h3><p>' + translateEquipment(ex.equipment) + '</p></div>';
        html += '</div>';
    }
    html += '</div>';
    container.innerHTML = html;
}

// Detalle del ejercicio
function openExerciseDetail(exerciseId) {
    var ex = exercisesDB.find(function(e) { return e.id === exerciseId; });
    if (!ex) return;
    
    document.getElementById('detail-name').textContent = translateExerciseName(ex.name);
    document.getElementById('detail-muscle').textContent = 'Grupo: ' + translateMuscle(ex.body_part);
    document.getElementById('detail-equipment').textContent = 'Equipo: ' + translateEquipment(ex.equipment);
    
    var imgContainer = document.getElementById('detail-image');
    var img = document.createElement('img');
    img.src = getExerciseImage(ex);
    img.alt = ex.name;
    img.onerror = function() { this.style.display = 'none'; };
    imgContainer.innerHTML = '';
    imgContainer.appendChild(img);
    
    showScreen('screen-exercise-detail');
}

// Rutinas
function loadRoutine() {
    var saved = localStorage.getItem('gembukai_routine');
    if (saved) routine = JSON.parse(saved);
    else {
        routine = { days: [
            { name: 'Día 1', exercises: [], completed: false },
            { name: 'Día 2', exercises: [], completed: false },
            { name: 'Día 3', exercises: [], completed: false },
            { name: 'Día 4', exercises: [], completed: false }
        ]};
    }
}

function saveRoutine() {
    localStorage.setItem('gembukai_routine', JSON.stringify(routine));
}

function renderRoutineDays() {
    var container = document.getElementById('routine-days-container');
    if (!container) return;
    
    var html = '';
    for (var i = 0; i < routine.days.length; i++) {
        var day = routine.days[i];
        html += '<div class="day-card ' + (day.completed ? 'day-completed' : '') + '">';
        html += '<div class="day-header"><span class="day-title">' + day.name + '</span><span class="day-badge">' + day.exercises.length + ' ejercicios</span></div>';
        for (var j = 0; j < day.exercises.length; j++) {
            var ex = day.exercises[j];
            html += '<div class="day-exercise-item"><div class="routine-exercise-info"><div class="day-exercise-name">' + translateExerciseName(ex.name) + '</div></div></div>';
        }
        html += '<div class="day-actions"><button class="btn btn-small" onclick="openAddToDay(' + i + ')">Añadir</button><button class="btn btn-small" onclick="toggleDayCompleted(' + i + ')">' + (day.completed ? 'Desmarcar' : 'Completado') + '</button></div>';
        html += '</div>';
    }
    container.innerHTML = html;
}

function toggleDayCompleted(index) {
    routine.days[index].completed = !routine.days[index].completed;
    saveRoutine();
    renderRoutineDays();
}

function openAddToDay(dayIndex) {
    showScreen('screen-add-to-day');
}

function addExerciseToDay(exerciseId) {
    var ex = exercisesDB.find(function(e) { return e.id === exerciseId; });
    if (!ex) return;
    var day = routine.days[0];
    day.exercises.push({ id: ex.id, name: ex.name, body_part: ex.body_part, equipment: ex.equipment, sets: '', reps: '', weight: '' });
    saveRoutine();
    alert('Añadido');
}

function removeExerciseFromDay(dayIndex, exIndex) {
    routine.days[dayIndex].exercises.splice(exIndex, 1);
    saveRoutine();
    renderRoutineDays();
}

// Perfil
function showProfile() {
    if (!currentUser) return;
    document.getElementById('profile-name').textContent = currentUser.name;
    document.getElementById('profile-code').textContent = currentUser.code;
    showScreen('screen-profile');
}

function editProfile() { showScreen('screen-edit-profile'); }

function saveEditedProfile() {
    alert('Perfil actualizado');
    showProfile();
}

function resetProfile() {
    if (confirm('¿Borrar todos los datos?')) {
        localStorage.clear();
        location.reload();
    }
}

// Compartir/Importar
function shareRoutine() {
    if (!routine) { alert('No tienes rutina'); return; }
    var encoded = btoa(encodeURIComponent(JSON.stringify(routine)));
    navigator.clipboard.writeText(encoded).then(function() { alert('Código copiado'); }).catch(function() { prompt('Copia:', encoded); });
}

function importRoutine() {
    var code = prompt('Pega el código:');
    if (!code) return;
    try {
        var decoded = JSON.parse(decodeURIComponent(atob(code)));
        if (decoded.days) { routine = decoded; saveRoutine(); renderRoutineDays(); alert('Rutina importada'); }
    } catch (e) { alert('Código no válido'); }
}

// Carga de datos
async function loadExercises() {
    try {
        var response = await fetch(EXERCISEDB_URL);
        exercisesDB = await response.json();
        console.log('Ejercicios cargados:', exercisesDB.length);
    } catch (error) { console.error('Error cargando ejercicios:', error); }
}

async function loadTranslations() {
    try {
        var response = await fetch('translations.json');
        translationsDB = await response.json();
        console.log('Traducciones cargadas');
    } catch (error) { console.error('Error cargando traducciones:', error); }
}

async function loadUsers() {
    try {
        var response = await fetch(APPS_SCRIPT_URL + '?action=getUsers&sheetId=' + SHEET_ID);
        var data = await response.json();
        usersDB = data;
        console.log('Usuarios cargados:', usersDB.users ? usersDB.users.length : 0);
    } catch (error) { console.error('Error cargando usuarios:', error); }
}

// Inicialización
async function initApp() {
    console.log('Inicializando app...');
    await loadExercises();
    await loadTranslations();
    await loadUsers();
    loadRoutine();
    
    var savedUser = localStorage.getItem('gembukai_current_user');
    if (savedUser) {
        currentUser = JSON.parse(savedUser);
        showScreen('screen-home');
        updateWelcomeScreen();
    }
    console.log('App inicializada');
}

window.onload = function() { initApp(); };
console.log('funciones.js cargado');