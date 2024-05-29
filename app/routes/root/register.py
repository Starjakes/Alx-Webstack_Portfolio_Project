from app import app, db
from flask import render_template, request, flash, redirect, url_for
from app.models.user.register import Registration
from app.models.admin import Event

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        admin_event = Event.query.first()
        form_data = request.form

        registration = Registration(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            email=form_data['email'],
            type_of_ticket=form_data['ticket_type'],
            num_of_ticket=form_data['number_of_tickets'],
            contact_no=form_data['contact_no'],
            country_of_residence=form_data['country_of_residence'],
            event_name=admin_event.event_name,
            event_venue=admin_event.event_venue,
            eligibility=admin_event.eligibility,
            event_date=admin_event.event_date
        )

        db.session.add(registration)
        db.session.commit()

        flash('You have successfully registered for the event. See you soon!', 'success')

        return redirect(url_for('user_inputs'))

    admin_event = Event.query.first()  # Fetch the event data to display in the form

    return render_template('root/register.html', admin_event=admin_event)


@app.route('/user_inputs')
def user_inputs():
    registrations = Registration.query.all()
    return render_template('root/user_inputs.html', registrations=registrations)

