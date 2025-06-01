document.addEventListener('DOMContentLoaded', () => {
    console.log('🕷️ Aethero Spider-Man Dashboard Loaded');

    // Spider-Man corner image interactions
    const spiderManCorner = document.querySelector('.spiderman-corner');
    if (spiderManCorner) {
        // Add click effect
        spiderManCorner.addEventListener('click', () => {
            spiderManCorner.style.transform = 'scale(1.2) rotate(360deg)';
            setTimeout(() => {
                spiderManCorner.style.transform = 'scale(1)';
            }, 500);
            
            // Add web shooting effect
            createWebEffect();
        });
        
        // Hover sound effect simulation
        spiderManCorner.addEventListener('mouseenter', () => {
            console.log('🕸️ Web sense activated!');
        });
    }

    // Create web shooting effect
    function createWebEffect() {
        const web = document.createElement('div');
        web.style.cssText = `
            position: fixed;
            top: 85px;
            left: 85px;
            width: 200px;
            height: 2px;
            background: linear-gradient(90deg, #fff, transparent);
            z-index: 999;
            pointer-events: none;
            animation: shootWeb 1s ease-out forwards;
        `;
        
        // Add CSS animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes shootWeb {
                0% { width: 0; opacity: 1; }
                100% { width: 300px; opacity: 0; }
            }
        `;
        document.head.appendChild(style);
        document.body.appendChild(web);
        
        setTimeout(() => {
            document.body.removeChild(web);
            document.head.removeChild(style);
        }, 1000);
    }

    // Enhanced header animation
    const header = document.querySelector('header h1');
    if (header) {
        header.addEventListener('click', () => {
            header.style.animation = 'pulse 0.5s ease-in-out';
            setTimeout(() => {
                header.style.animation = '';
            }, 500);
        });
    }

    // Add CSS for pulse animation
    const pulseStyle = document.createElement('style');
    pulseStyle.textContent = `
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
    `;
    document.head.appendChild(pulseStyle);

    // Simulate loading parser logs
    const logsContainer = document.getElementById('logs-container');
    logsContainer.textContent = 'Parser logs will be displayed here.';

    // Simulate radar chart for test results
    const radarChart = document.getElementById('radar-chart');
    if (radarChart) {
        const ctx = radarChart.getContext('2d');
        new Chart(ctx, {
            type: 'radar',
            data: {
                labels: ['Stability', 'Performance', 'Coverage', 'Accuracy', 'Introspection'],
                datasets: [{
                    label: 'Test Metrics',
                    data: [80, 90, 70, 85, 95],
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    r: {
                        angleLines: {
                            display: false
                        },
                        suggestedMin: 50,
                        suggestedMax: 100
                    }
                }
            }
        });
    }

    // Simulate loading feedback
    const feedbackContainer = document.getElementById('feedback-container');
    feedbackContainer.textContent = 'Feedback data will be displayed here.';

    // Example interaction logic
    const introspectiveSpace = document.getElementById('introspective-space');
    introspectiveSpace.addEventListener('click', () => {
        alert('Welcome to the introspective space!');
    });
});
