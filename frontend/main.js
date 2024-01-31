window.addEventListener('DOMContentLoaded', (event) => {
    getVisitCount();
})

const functionApi = 'https://getresumecounterxx24.azurewebsites.net/api/GetResumeCounter?code=fpUB3pbxlNgUNNqv60pOV1jZF-6XzmjBp3pcNHDmE5QEAzFuKUOqwQ==';

const getVisitCount = () => {
    let count = 30;
    fetch(functionApi).then(response => {
        return response.json();
    }).then(response => {
        console.log('Website called function API');
        count = response.count;
        document.getElementById('counter').innerText = count;
    }).catch(error => {
        console.log(error);	
    });

    return count;
}