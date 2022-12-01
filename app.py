from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

	res = ''
	if request.method == "POST":
		Edad = request.form.get('age')
		Tipo_Trabajo = request.form.get('job')
		Estado_Civil = request.form.get('marital-status')
		Educacion = request.form.get('education')
		Incumplimiento = request.form.get('has-credit')
		Vivienda = request.form.get('has-loan')
		Consumo = request.form.get('has-persone-loan')
		Contacto = request.form.get('contact-type')
		Mes = request.form.get('last-contact-month')
		Dia = request.form.get('last-contact-day')
		Campana = request.form.get('number-of-contacts')
		Dias_Ultima_Cam = request.form.get('number-of-days-passed')
		No_Contactos = request.form.get('number-of-contacts-before')
		Resultado_Anterior = request.form.get('outcome-of-the-previous')
		emp_var_rate = request.form.get('employment-variation-rate')
		cons_price_idx = request.form.get('consumer-price-index')
		cons_conf_idx = request.form.get('consumer-confidence-index')
		euribor3m = request.form.get('euribor')
		nr_employed = request.form.get('number-of-employees')

		columnds = ['Edad']

	return render_template('home.html')