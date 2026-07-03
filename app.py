
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    return render_template(
        'recommendation.html',
        crop='Rice 🌾',
        confidence=94,
        yield_potential='High',
        reasons=[
            'Suitable rainfall for rice cultivation',
            'Optimal soil pH level',
            'Adequate nutrient availability',
            'Favorable temperature and humidity'
        ],
        suggestion='Continue maintaining proper irrigation practices.'
    )

@app.route('/suitability', methods=['POST'])
def suitability():
    return render_template(
        'suitability.html',
        crop=request.form['crop'],
        temp_status='Excellent ✅',
        humidity_status='Excellent ✅',
        rainfall_status='Excellent ✅',
        ph_status='Good ✅',
        score=91,
        assessment='Current environmental conditions are highly suitable for cultivation.',
        productivity='Very High',
        recommendation='Current conditions support maximum productivity.'
    )

@app.route('/research')
def research():
    dashboard={
        'total_records':2200,
        'most_recommended_crop':'Rice 🌾',
        'average_temperature':'27.3 °C',
        'average_rainfall':'178 mm',
        'average_ph':'6.4',
        'water_efficient_crop':'Maize 🌽',
        'highest_yield_crop':'Rice 🌾',
        'nitrogen_deficiency':'32%',
        'phosphorous_deficiency':'18%',
        'potassium_deficiency':'21%'
    }
    policy=[
        'Promote water-efficient irrigation methods.',
        'Encourage balanced fertilizer usage.',
        'Support farmers in regions with low rainfall.',
        'Increase awareness about soil testing.'
    ]
    return render_template('research.html', dashboard=dashboard, policy=policy)

if __name__ == '__main__':
    app.run(debug=True)
