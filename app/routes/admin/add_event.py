from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime
from app.models.admin import Event

@app.route('/add_event', methods=['GET', 'POST'])
@login_required
def add_event():
    if request.method == 'POST':
        event_name = request.form.get('event_name')
        event_date_str = request.form.get('event_date')  # Retrieve date as string
        event_date = datetime.strptime(event_date_str, '%Y-%m-%d')  # Convert to datetime
        event_venue = request.form.get('event_venue')
        eligibility = request.form.get('eligibility')
        total_tickets = int(request.form.get('total_tickets'))

        # Check if an event already exists
        existing_event = Event.query.first()

        if existing_event:
            # Override existing event with new details
            existing_event.event_name = event_name
            existing_event.event_date = event_date
            existing_event.event_venue = event_venue
            existing_event.eligibility = eligibility
            existing_event.total_tickets = total_tickets
        else:
            # Create a new event in the database
            new_event = Event(
                event_name=event_name,
                event_date=event_date,
                event_venue=event_venue,
                eligibility=eligibility,
                total_tickets=total_tickets
            )

            db.session.add(new_event)
            db.session.commit()
            flash('New event added successfully', 'success')
            return redirect(url_for('dashboard'))

    return render_template('/admin/add_event.html')

