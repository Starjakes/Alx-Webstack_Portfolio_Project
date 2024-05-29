from flask import render_template
from app import app
from flask_login import login_required
from app.models.admin import Event
from app.models.user import Registration

@app.route('/dashboard')
@login_required
def dashboard():
    # Retrieve existing event from the dashboard
    existing_event = Event.query.first()

    if existing_event:
        total_tickets = existing_event.total_tickets

        # Count the number of registered users
        ticket_used = Registration.query.count()

        # Calculate the number of tickets left
        tickets_left = total_tickets - ticket_used

        # Retrieve all registered users
        registrations = Registration.query.all()

        return render_template(
            'admin/dashboard.html',
            total_tickets=total_tickets,
            ticket_used=ticket_used,
            tickets_left=tickets_left,
            existing_event=existing_event,
            registrations=registrations
        )
    else:
        # If there's no existing event, handle this case
        return render_template(
            'admin/dashboard.html',
            existing_event=None
        )

