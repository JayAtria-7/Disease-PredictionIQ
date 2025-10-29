// ===================================
// DISEASE PREDICTIONIQ - JS
// Interactive Features & Animations
// Author: Jay Prakash
// ===================================

// ========== DOM ELEMENTS ==========
const mobileMenuToggle = document.getElementById('mobileMenuToggle');
const mobileMenuClose = document.getElementById('mobileMenuClose');
const mobileMenu = document.getElementById('mobileMenu');
const predictionForm = document.getElementById('predictionForm');
const resultsCard = document.getElementById('resultsCard');
const loadingOverlay = document.getElementById('loadingOverlay');
const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');

// ========== MOBILE MENU ==========
mobileMenuToggle.addEventListener('click', () => {
    mobileMenu.classList.add('active');
});

mobileMenuClose.addEventListener('click', () => {
    mobileMenu.classList.remove('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.mobile-nav-link').forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.remove('active');
    });
});

// ========== SMOOTH SCROLLING ==========
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        const targetSection = document.querySelector(targetId);
        
        if (targetSection) {
            targetSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
            
            // Update active link
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
        }
    });
});

// ========== ANIMATED COUNTER ==========
const animateCounter = (element) => {
    const target = parseInt(element.getAttribute('data-target'));
    const duration = 2000;
    const increment = target / (duration / 16);
    let current = 0;
    
    const updateCounter = () => {
        current += increment;
        if (current < target) {
            element.textContent = Math.floor(current);
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target;
        }
    };
    
    updateCounter();
};

// Trigger counter animation when in viewport
const observerOptions = {
    threshold: 0.5,
    rootMargin: '0px'
};

const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const counters = entry.target.querySelectorAll('.stat-number');
            counters.forEach(counter => {
                if (counter.textContent === '0') {
                    animateCounter(counter);
                }
            });
            counterObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

const statsGrid = document.querySelector('.stats-grid');
if (statsGrid) {
    counterObserver.observe(statsGrid);
}

// ========== FORM SUBMISSION ==========
predictionForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Show loading overlay
    loadingOverlay.classList.add('active');
    
    // Collect form data
    const formData = new FormData(predictionForm);
    const data = {};
    
    formData.forEach((value, key) => {
        data[key] = value;
    });
    
    try {
        // Make API request
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        // Hide loading overlay
        setTimeout(() => {
            loadingOverlay.classList.remove('active');
            
            if (result.success) {
                displayResults(result);
                
                // Scroll to results
                resultsCard.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });
            } else {
                showError(result.message || 'An error occurred during prediction');
            }
        }, 1500);
        
    } catch (error) {
        console.error('Error:', error);
        loadingOverlay.classList.remove('active');
        showError('Failed to connect to the server. Please try again.');
    }
});

// ========== DISPLAY RESULTS ==========
function displayResults(result) {
    const resultsContent = document.getElementById('resultsContent');
    
    // Determine colors based on prediction
    const bgColor = result.prediction === 1 ? 
        'linear-gradient(135deg, #ef4444 0%, #dc2626 100%)' : 
        'linear-gradient(135deg, #10b981 0%, #059669 100%)';
    
    const icon = result.prediction === 1 ? 
        '<i class="fas fa-exclamation-triangle"></i>' : 
        '<i class="fas fa-check-circle"></i>';
    
    // Build recommendations HTML
    const recommendationsHtml = result.recommendations.map(rec => 
        `<div class="recommendation-item">${rec}</div>`
    ).join('');
    
    // Create results HTML
    const resultsHtml = `
        <div class="results-content">
            <div class="result-header" style="background: ${bgColor}">
                <div class="result-icon">${icon}</div>
                <h3 class="result-diagnosis">${result.diagnosis}</h3>
                <p class="result-risk">Risk Level: <strong>${result.risk_level}</strong></p>
            </div>
            
            <div class="result-stats">
                <div class="result-stat">
                    <div class="result-stat-label">Probability</div>
                    <div class="result-stat-value" style="color: ${result.risk_color}">
                        ${result.probability}%
                    </div>
                </div>
                <div class="result-stat">
                    <div class="result-stat-label">Confidence</div>
                    <div class="result-stat-value" style="color: var(--primary-light)">
                        ${result.confidence}%
                    </div>
                </div>
            </div>
            
            <div class="recommendations">
                <h4><i class="fas fa-lightbulb"></i> Recommendations</h4>
                ${recommendationsHtml}
            </div>
            
            <div style="margin-top: 2rem; padding: 1rem; background: rgba(15, 23, 42, 0.6); border-radius: 0.5rem; text-align: center; color: var(--text-muted); font-size: 0.875rem;">
                <i class="fas fa-clock"></i> Generated at ${result.timestamp}
            </div>
        </div>
    `;
    
    resultsContent.innerHTML = resultsHtml;
    
    // Add animation class to results card
    resultsCard.classList.add('animate__animated', 'animate__pulse');
    setTimeout(() => {
        resultsCard.classList.remove('animate__pulse');
    }, 1000);
}

// ========== ERROR HANDLING ==========
function showError(message) {
    const resultsContent = document.getElementById('resultsContent');
    
    resultsContent.innerHTML = `
        <div class="no-results" style="color: var(--danger-color);">
            <i class="fas fa-exclamation-circle"></i>
            <p><strong>Error:</strong> ${message}</p>
            <button class="btn btn-primary" onclick="location.reload()" style="margin-top: 1rem;">
                <i class="fas fa-redo"></i> Try Again
            </button>
        </div>
    `;
}

// ========== LOAD MODEL INFO ==========
async function loadModelInfo() {
    const modelInfoContent = document.getElementById('modelInfoContent');
    
    try {
        const response = await fetch('/api/model-info');
        const data = await response.json();
        
        if (data.success) {
            const metrics = data.metrics;
            
            const modelInfoHtml = `
                <div class="model-info-card animate__animated animate__fadeInUp" style="animation-delay: 0.1s">
                    <h3><i class="fas fa-robot"></i> Model Details</h3>
                    <div class="metric-grid">
                        <div class="metric-item">
                            <span class="metric-label">Model Name</span>
                            <span class="metric-value">${data.model_name}</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">Algorithm</span>
                            <span class="metric-value">${data.model_type}</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">Training Date</span>
                            <span class="metric-value">${data.training_date}</span>
                        </div>
                    </div>
                </div>
                
                <div class="model-info-card animate__animated animate__fadeInUp" style="animation-delay: 0.2s">
                    <h3><i class="fas fa-chart-bar"></i> Performance Metrics</h3>
                    <div class="metric-grid">
                        <div class="metric-item">
                            <span class="metric-label">Accuracy</span>
                            <span class="metric-value" style="color: var(--success-color)">
                                ${(metrics.accuracy * 100).toFixed(2)}%
                            </span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">Precision</span>
                            <span class="metric-value" style="color: var(--primary-light)">
                                ${(metrics.precision * 100).toFixed(2)}%
                            </span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">Recall</span>
                            <span class="metric-value" style="color: var(--warning-color)">
                                ${(metrics.recall * 100).toFixed(2)}%
                            </span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">F1 Score</span>
                            <span class="metric-value" style="color: var(--accent-color)">
                                ${(metrics.f1_score * 100).toFixed(2)}%
                            </span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">ROC-AUC</span>
                            <span class="metric-value" style="color: var(--primary-color)">
                                ${(metrics.roc_auc * 100).toFixed(2)}%
                            </span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">Overall Score</span>
                            <span class="metric-value" style="color: var(--secondary-color)">
                                ${(metrics.overall_score * 100).toFixed(2)}%
                            </span>
                        </div>
                    </div>
                </div>
                
                <div class="model-info-card animate__animated animate__fadeInUp" style="animation-delay: 0.3s">
                    <h3><i class="fas fa-list"></i> Input Features</h3>
                    <div class="metric-grid">
                        ${data.features.slice(0, 6).map((feature, index) => `
                            <div class="metric-item">
                                <span class="metric-label">${index + 1}. ${feature}</span>
                            </div>
                        `).join('')}
                    </div>
                    <div style="margin-top: 1rem; text-align: center; color: var(--text-muted); font-size: 0.875rem;">
                        Total Features: ${data.features.length}
                    </div>
                </div>
            `;
            
            modelInfoContent.innerHTML = modelInfoHtml;
        } else {
            modelInfoContent.innerHTML = `
                <div class="no-results" style="color: var(--danger-color);">
                    <i class="fas fa-exclamation-circle"></i>
                    <p>Failed to load model information</p>
                </div>
            `;
        }
    } catch (error) {
        console.error('Error loading model info:', error);
        modelInfoContent.innerHTML = `
            <div class="no-results" style="color: var(--danger-color);">
                <i class="fas fa-exclamation-circle"></i>
                <p>Error connecting to server</p>
            </div>
        `;
    }
}

// ========== SCROLL ANIMATIONS ==========
const animateOnScroll = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate__animated', 'animate__fadeInUp');
        }
    });
}, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
});

// Observe all feature cards and model info cards
document.querySelectorAll('.feature-card').forEach(card => {
    animateOnScroll.observe(card);
});

// ========== ACTIVE NAV LINK ON SCROLL ==========
window.addEventListener('scroll', () => {
    let current = '';
    const sections = document.querySelectorAll('section');
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        
        if (window.pageYOffset >= sectionTop - 100) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// ========== FORM VALIDATION ==========
const formInputs = predictionForm.querySelectorAll('input, select');

formInputs.forEach(input => {
    input.addEventListener('blur', () => {
        if (input.checkValidity()) {
            input.style.borderColor = 'var(--success-color)';
        } else {
            input.style.borderColor = 'var(--danger-color)';
        }
    });
    
    input.addEventListener('focus', () => {
        input.style.borderColor = 'var(--primary-color)';
    });
});

// ========== SAMPLE DATA BUTTON ==========
function fillSampleData() {
    document.getElementById('age').value = 63;
    document.getElementById('sex').value = 1;
    document.getElementById('chest_pain_type').value = 3;
    document.getElementById('resting_blood_pressure').value = 145;
    document.getElementById('cholesterol').value = 233;
    document.getElementById('fasting_blood_sugar').value = 1;
    document.getElementById('resting_ecg').value = 0;
    document.getElementById('max_heart_rate').value = 150;
    document.getElementById('exercise_induced_angina').value = 0;
    document.getElementById('st_depression').value = 2.3;
    document.getElementById('st_slope').value = 0;
    document.getElementById('num_major_vessels').value = 0;
    document.getElementById('thalassemia').value = 1;
}

// Add sample data button to form
const formActions = document.querySelector('.form-actions');
const sampleBtn = document.createElement('button');
sampleBtn.type = 'button';
sampleBtn.className = 'btn btn-secondary';
sampleBtn.innerHTML = '<i class="fas fa-flask"></i> Fill Sample Data';
sampleBtn.onclick = fillSampleData;
formActions.insertBefore(sampleBtn, formActions.firstChild);

// ========== MODEL COMPARISON ==========
async function loadModelsComparison() {
    try {
        const response = await fetch('/api/models-comparison');
        const data = await response.json();
        
        if (data.success) {
            displayModelsComparison(data);
        } else {
            throw new Error(data.message || 'Failed to load comparison data');
        }
    } catch (error) {
        console.error('Error loading comparison:', error);
        const comparisonContent = document.getElementById('comparisonContent');
        if (comparisonContent) {
            comparisonContent.innerHTML = `
                <div class="error-message">
                    <i class="fas fa-exclamation-circle"></i>
                    <p>Failed to load comparison data</p>
                </div>
            `;
        }
    }
}

function displayModelsComparison(data) {
    const comparisonContent = document.getElementById('comparisonContent');
    if (!comparisonContent) return;
    
    const bestModel = data.best_model;
    const avgAccuracy = (data.models.reduce((sum, m) => sum + m.accuracy, 0) / data.models.length * 100).toFixed(2);
    const avgROC = (data.models.reduce((sum, m) => sum + m.roc_auc, 0) / data.models.length * 100).toFixed(2);
    
    comparisonContent.innerHTML = `
        <!-- Stats Overview -->
        <div class="comparison-stats animate__animated animate__fadeInUp">
            <div class="stat-card">
                <div class="stat-icon"><i class="fas fa-brain"></i></div>
                <div class="stat-value">${data.total_models}</div>
                <div class="stat-label">Models Trained</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon"><i class="fas fa-trophy"></i></div>
                <div class="stat-value">${(bestModel.roc_auc * 100).toFixed(2)}%</div>
                <div class="stat-label">Best ROC-AUC</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon"><i class="fas fa-chart-line"></i></div>
                <div class="stat-value">${avgAccuracy}%</div>
                <div class="stat-label">Avg Accuracy</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon"><i class="fas fa-award"></i></div>
                <div class="stat-value">${bestModel.name.split(' ')[0]}</div>
                <div class="stat-label">Best Model</div>
            </div>
        </div>
        
        <!-- Models Table -->
        <div class="models-table-container animate__animated animate__fadeInUp" style="animation-delay: 0.2s">
            <h3><i class="fas fa-table"></i> Complete Model Performance</h3>
            <div style="overflow-x: auto;">
                <table class="models-table">
                    <thead>
                        <tr>
                            <th>Rank</th>
                            <th>Model Name</th>
                            <th>Category</th>
                            <th>Accuracy</th>
                            <th>Precision</th>
                            <th>Recall</th>
                            <th>F1-Score</th>
                            <th>ROC-AUC</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${data.models.map((model, index) => `
                            <tr class="${model.is_best ? 'best-model' : ''}">
                                <td><strong>#${index + 1}</strong></td>
                                <td>
                                    <div class="model-name">
                                        ${model.name}
                                        ${model.is_best ? '<span class="best-badge"><i class="fas fa-star"></i> Best</span>' : ''}
                                    </div>
                                </td>
                                <td>
                                    <span class="model-category category-${model.category.toLowerCase().replace(/[- ]/g, '-')}">
                                        ${model.category}
                                    </span>
                                </td>
                                <td>
                                    <div class="metric-bar">
                                        <div class="metric-progress">
                                            <div class="metric-fill" style="width: ${model.accuracy * 100}%"></div>
                                        </div>
                                        <span class="metric-value">${(model.accuracy * 100).toFixed(2)}%</span>
                                    </div>
                                </td>
                                <td>${(model.precision * 100).toFixed(2)}%</td>
                                <td>${(model.recall * 100).toFixed(2)}%</td>
                                <td>${(model.f1_score * 100).toFixed(2)}%</td>
                                <td><strong style="color: var(--accent-color)">${(model.roc_auc * 100).toFixed(2)}%</strong></td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
        </div>
        
        <!-- Visualizations -->
        <div class="charts-container">
            <!-- Accuracy Bar Chart -->
            <div class="chart-card animate__animated animate__fadeInUp" style="animation-delay: 0.3s">
                <div class="chart-title">
                    <i class="fas fa-chart-bar"></i>
                    ROC-AUC Comparison
                </div>
                <div class="bar-chart">
                    ${data.models.slice(0, 8).map(model => `
                        <div class="bar-item">
                            <div class="bar-label">${model.name}</div>
                            <div class="bar-visual">
                                <div class="bar-fill" style="width: ${model.roc_auc * 100}%">
                                    ${(model.roc_auc * 100).toFixed(1)}%
                                </div>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
            
            <!-- Best Model Metrics Radar -->
            <div class="chart-card animate__animated animate__fadeInUp" style="animation-delay: 0.4s">
                <div class="chart-title">
                    <i class="fas fa-star"></i>
                    Best Model: ${bestModel.name}
                </div>
                <div class="radar-container">
                    <div class="radar-item">
                        <span class="radar-metric">Accuracy</span>
                        <span class="radar-score">${(bestModel.accuracy * 100).toFixed(2)}%</span>
                    </div>
                    <div class="radar-item">
                        <span class="radar-metric">Precision</span>
                        <span class="radar-score">${(bestModel.precision * 100).toFixed(2)}%</span>
                    </div>
                    <div class="radar-item">
                        <span class="radar-metric">Recall</span>
                        <span class="radar-score">${(bestModel.recall * 100).toFixed(2)}%</span>
                    </div>
                    <div class="radar-item">
                        <span class="radar-metric">F1-Score</span>
                        <span class="radar-score">${(bestModel.f1_score * 100).toFixed(2)}%</span>
                    </div>
                    <div class="radar-item">
                        <span class="radar-metric">ROC-AUC</span>
                        <span class="radar-score">${(bestModel.roc_auc * 100).toFixed(2)}%</span>
                    </div>
                </div>
            </div>
            
            <!-- Category Performance -->
            <div class="chart-card animate__animated animate__fadeInUp" style="animation-delay: 0.5s">
                <div class="chart-title">
                    <i class="fas fa-layer-group"></i>
                    Performance by Category
                </div>
                <div class="bar-chart">
                    ${Object.entries(
                        data.models.reduce((acc, model) => {
                            if (!acc[model.category]) acc[model.category] = [];
                            acc[model.category].push(model.roc_auc);
                            return acc;
                        }, {})
                    ).map(([category, scores]) => {
                        const avgScore = scores.reduce((a, b) => a + b, 0) / scores.length;
                        return `
                            <div class="bar-item">
                                <div class="bar-label">${category}</div>
                                <div class="bar-visual">
                                    <div class="bar-fill" style="width: ${avgScore * 100}%">
                                        ${(avgScore * 100).toFixed(1)}%
                                    </div>
                                </div>
                            </div>
                        `;
                    }).join('')}
                </div>
            </div>
            
            <!-- Top 5 Models -->
            <div class="chart-card animate__animated animate__fadeInUp" style="animation-delay: 0.6s">
                <div class="chart-title">
                    <i class="fas fa-medal"></i>
                    Top 5 Models by ROC-AUC
                </div>
                <div class="radar-container">
                    ${data.models.slice(0, 5).map((model, index) => `
                        <div class="radar-item">
                            <span class="radar-metric">
                                <i class="fas fa-trophy" style="color: ${
                                    index === 0 ? '#FFD700' : 
                                    index === 1 ? '#C0C0C0' : 
                                    index === 2 ? '#CD7F32' : 
                                    'var(--text-secondary)'
                                }"></i>
                                ${model.name}
                            </span>
                            <span class="radar-score">${(model.roc_auc * 100).toFixed(2)}%</span>
                        </div>
                    `).join('')}
                </div>
            </div>
        </div>
    `;
}

// ========== INITIALIZE ==========
document.addEventListener('DOMContentLoaded', () => {
    // Load model info
    loadModelInfo();
    
    // Load models comparison
    loadModelsComparison();
    
    // Add smooth appearance to elements
    const observeElements = document.querySelectorAll('.stat-card, .feature-card');
    observeElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            el.style.transition = 'all 0.5s ease';
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, index * 100);
    });
    
    console.log('Disease PredictionIQ App Initialized ✓');
});

// ========== TOOLTIPS ==========
const inputHints = document.querySelectorAll('.input-hint');
inputHints.forEach(hint => {
    hint.style.transition = 'all 0.3s ease';
});

// ========== NAVBAR SCROLL EFFECT ==========
let lastScroll = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        navbar.style.background = 'rgba(15, 23, 42, 0.95)';
        navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
    } else {
        navbar.style.background = 'rgba(15, 23, 42, 0.9)';
        navbar.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
    }
    
    lastScroll = currentScroll;
});

// ========== ACCESSIBILITY ==========
document.addEventListener('keydown', (e) => {
    // Close mobile menu on Escape
    if (e.key === 'Escape' && mobileMenu.classList.contains('active')) {
        mobileMenu.classList.remove('active');
    }
});

// ========== PERFORMANCE MONITORING ==========
window.addEventListener('load', () => {
    const loadTime = performance.now();
    console.log(`Page loaded in ${loadTime.toFixed(2)}ms`);
});
