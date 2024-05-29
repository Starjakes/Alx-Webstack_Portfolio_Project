# JayHlens Event Management System

![JayHlens Logo](../../static/root/img/logo.png)

JayHlens Event Management System is a web application designed to streamline the process of organizing events, managing ticket sales, and handling attendee registrations. It provides a user-friendly interface for both event organizers and attendees, making it easy to create, promote, and attend events.

## Features

- **Event Creation**: Organizers can create new events, specifying details such as event name, date, location, and ticket types.
- **Ticket Management**: Organizers can define different types of tickets with various pricing tiers and availability.
- **User Registration**: Attendees can register for events by providing their name, email, and other required information.
- **Ticket Purchase**: Attendees can purchase tickets for events through a secure payment gateway.
- **Admin Panel**: Administrators have access to an admin panel to manage events, tickets, and user registrations.
- **Email Notifications**: Automated email notifications are sent to attendees upon successful registration and ticket purchase.

## Installation

To run the JayHlens Event Management System locally, follow these steps:

1. **Clone the repository**: `git clone https://github.com/starjakes/jayhlens.git`
2. **Navigate to the project directory**: `cd jayhlens`
3. **Install dependencies**: `pip install flask`
4. **Set up the MySQL database**: Execute the provided SQL script.
5. **Configure the database connection**: Update the `config.py` file.
6. **Run the application**: `python run.py`
7. **Access the application**: Open your web browser and go to `http://127.0.0.1:5000/`

## Usage

1. **As an organizer**:
   - Log in to the admin panel.
   - Create a new event and define ticket types.
   - Monitor ticket sales and attendee registrations.

2. **As an attendee**:
   - Browse the list of upcoming events.
   - Register for events and purchase tickets.

## Technologies Used

- Python
- Flask
- MySQL
- HTML/CSS
- Bootstrap
- JavaScript

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Owner

- **Name**: Ameh Jacob E
- **GitHub Username**: starjakes
- **Website**: [starjakes.com.ng](https://starjakes.com.ng)

